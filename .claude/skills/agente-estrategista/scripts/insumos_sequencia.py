"""Insumos para o Planejador de Sequência do Instagram (somente leitura).

Junta, num único dossiê em Markdown, tudo que o planejador precisa para propor a sequência de conteúdos:
  1. Cadência real (posts por semana, dias desde o último, Reels em 90 dias).
  2. Grade recente: últimos posts de feed, com a peça do marketing (C-XXX), tipo, fundo (cor), views e taxas,
     e as verificações da marca (cor repetida em sequência, Scarlet nos últimos 9, claro/escuro, mix do ciclo de 9).
  3. Estoque: peças prontas, em produção e em espera (da pauta do `sb_marketing_team`).
  4. Banco legado de briefings (antigo Caio, congelado) que ainda não foi produzido.
  5. Desempenho por formato e por tipo de peça (orgânico separado do impulsionado) e os melhores posts.
  6. Produtos em foco (vendas, margem e estoque) para escolher o produto de cada arco temático.
  7. Banco de mídia próprio (fotos e vídeos disponíveis) para saber o que precisa ser captado.
  8. Calendário dos próximos dias de postagem (seg/qua/sex).

Uso (venv do sb_relatorios):
  /c/Users/HTK1562/venvs/sb_relatorios/Scripts/python.exe insumos_sequencia.py [--dias 21] [--out arquivo.md]

Não altera pauta, histórico nem briefings do marketing e não escreve no banco. As leituras do perfil vêm do BigQuery
(`dbt_dw_az.tb_instagram_midia`, extração 3x por dia). Fundo da peça = campo "Fundo" do briefing/visual-spec/histórico.
"""
import argparse
import re
import sys
from datetime import date, timedelta
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import produzido_x_postado as pxp  # noqa: E402  (reaproveita leitura da pauta e casamento por legenda)

MKT = pxp.MKT
CLARO, ESCURO = {"warm light", "skin nude"}, {"deep plum", "carbon black"}
DIAS_POST = (0, 2, 4)  # seg, qua, sex (Organização Semanal: feed seg/qua/sex)
DIAS_PT = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
EM_ESPERA = {"C-090": "descartada pelo Hugo (28/10); frase parecida com post de terceiro (@kyntv101)",
             "C-079": "mesmo conteúdo da C-057, no ar em 18/09 (confirmado em 28/10)"}
# Datas que mexem na pauta (confirmar com o Hugo; não é calendário oficial)
DATAS = {date(2026, 10, 31): "Halloween (sáb)", date(2026, 11, 27): "Black Friday (sex)"}


def categoria_ciclo(tipo, pasta=""):
    """Categoria do ciclo de 9 posts (design-system §7) a partir do tipo da peça do marketing."""
    t = f"{tipo} {pasta}".lower()
    if "frase" in t:
        return "Conceitual"
    if "foto de produto" in t or ("foto" in t and "produto" in t):
        return "Foto de produto"
    if "produto" in t:
        return "Produto"
    if "inspira" in t or "amarra" in t and "foto" in t:
        return "Foto de prática"
    if "foto" in t:
        return "Foto de prática"
    if "video" in t or "vídeo" in t or "reel" in t:
        return "Vídeo"
    if "bingo" in t:
        return "Identificação (bingo)"
    if "mitos" in t or "desejo" in t or "carrossel" in t:
        return "Educativo"
    return "Outro"


def fundo_da_peca(pasta, fundo_historico=None):
    """Fundo (cor) da peça: briefing.md → visual-spec.md → coluna Fundo do histórico."""
    for nome in ("briefing.md", "visual-spec.md"):
        f = pxp.pasta_do_conteudo(pasta) / nome
        if f.exists():
            m = re.search(r"\*\*Fundo:?\*\*:?\s*([A-Za-zÀ-ú ]+?)\s*(?:`|\(|—|-|$)", f.read_text(encoding="utf-8"), re.M)
            if m and m.group(1).strip():
                return m.group(1).strip()
    if fundo_historico:
        m = re.match(r"([A-Za-z ]+?)\s*(?:`|$)", fundo_historico.strip())
        return m.group(1).strip() if m else None
    return None


def luz(fundo):
    f = (fundo or "").lower()
    if f in CLARO:
        return "claro"
    if f in ESCURO:
        return "escuro"
    if "scarlet" in f:
        return "scarlet"
    return "?"


def fundos_do_historico():
    hist = (MKT / "contexto" / "historico-conteudos.md").read_text(encoding="utf-8")
    saida = {}
    for _, linhas in pxp._tabelas(hist):
        for r in linhas:
            if r.get("Código", "").startswith("C-"):
                saida[r["Código"].strip()] = r.get("Fundo", "")
    return saida


def metricas(dias=365):
    from bq_client import get_client
    cli = get_client("us-east4")
    df = cli.query(f"""
        SELECT cd_midia, ds_formato, dt_publicacao, qt_views, qt_alcance, qt_slides, fg_impulsionada, pct_envio, pct_salvamento,
               qt_seguidores_por_mil_views AS seg_mil, qt_seguidores_ganhos, qt_visitas_perfil, ds_permalink
          FROM `igneous-sandbox-381622.dbt_dw_az.tb_instagram_midia`
         WHERE NOT fg_story AND dt_publicacao >= DATE_SUB(CURRENT_DATE('America/Sao_Paulo'), INTERVAL {dias} DAY)
    """).to_dataframe()
    df["dt_publicacao"] = pd.to_datetime(df["dt_publicacao"]).dt.date
    return df


def ler_banco_briefings():
    md = (MKT / "contexto" / "briefings.md").read_text(encoding="utf-8")
    linhas = []
    for secao, tab in pxp._tabelas(md):
        if not secao.startswith("Território"):
            continue
        territorio = secao.split(":", 1)[1].strip()
        for r in tab:
            status = r.get("Status", "")
            if any(k in status for k in ("Publicado", "Arquivado", "Agendado")):
                continue
            linhas.append({"codigo": r.get("#", ""), "titulo": r.get("Título provisório", ""), "formato": r.get("Formato", ""),
                           "persona": r.get("Persona", ""), "status": status, "territorio": territorio})
    return linhas


def produtos_em_foco(n=14):
    """Produtos que mais vendem (90 dias) com margem e estoque, para escolher o produto de cada arco."""
    from bq_client import get_client
    cli = get_client("us-east4")
    return cli.query(f"""
        WITH v AS (SELECT nm_produto, ANY_VALUE(ds_frente) frente, SUM(qt_item) un, SUM(vl_receita_liquida_produto) receita, SUM(vl_margem_contribuicao) mc
                     FROM `igneous-sandbox-381622.dbt_dw_az.tb_pedido`
                    WHERE fg_pedido_valido AND NOT fg_brinde AND dt_pedido >= DATE_SUB(CURRENT_DATE('America/Sao_Paulo'), INTERVAL 90 DAY) GROUP BY 1),
        e AS (SELECT nm_produto, SUM(qt_estoque_atual) estoque, MIN(qt_cobertura_atual) cobertura_min, STRING_AGG(DISTINCT ds_classificacao_risco) risco
                FROM `igneous-sandbox-381622.dbt_dw_az.tb_estoque_analitico` GROUP BY 1)
        SELECT v.*, e.estoque, e.cobertura_min, e.risco FROM v LEFT JOIN e USING (nm_produto) ORDER BY receita DESC LIMIT {n}
    """).to_dataframe()


def banco_de_midia():
    """Quantos arquivos de foto/vídeo próprios existem (não abre nem classifica o conteúdo)."""
    pastas = [("Fotos próprias (raiz)", "assets/fotos-proprias", False), ("Fotos 'Single Column Tie' (ebook)", "assets/fotos-proprias/ebook-1", True),
              ("Vídeos próprios", "assets/videos", True), ("Fotos 'A publicar' (arquivo)", "assets/arquivo/Post de Fotos - A Publicar", True),
              ("Produtos 'A publicar' (arquivo)", "assets/arquivo/Post de Produtos - A Publicar", True), ("Material de Stories de produto", "conteudos/instagram-story-produtos", True)]
    ext = {".jpg", ".jpeg", ".png", ".mp4", ".mov", ".heic"}
    saida = []
    for rotulo, rel, recursivo in pastas:
        d = pxp.pasta_do_conteudo(rel)
        arq = [f for f in (d.rglob("*") if recursivo else d.glob("*")) if f.is_file() and f.suffix.lower() in ext]
        saida.append((rotulo, rel, len(arq), sum(f.suffix.lower() in {".mp4", ".mov"} for f in arq)))
    return saida


def tabela(df, cols, fmt=None):
    fmt = fmt or {}
    cab = "| " + " | ".join(cols) + " |\n|" + "---|" * len(cols) + "\n"
    corpo = ""
    for _, r in df.iterrows():
        corpo += "| " + " | ".join(fmt.get(c, str)(r[c]) if pd.notna(r[c]) else "—" for c in cols) + " |\n"
    return cab + corpo


def milhar(n):
    return f"{int(n or 0):,}".replace(",", ".")


def pct(x):
    return f"{x * 100:.2f}%".replace(".", ",")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", type=int, default=21, help="horizonte do calendário")
    ap.add_argument("--out")
    args = ap.parse_args()
    hoje = date.today()

    itens = pxp.itens_do_marketing()
    perfil = pxp.carregar_perfil()
    ig = [i for i in itens if i["instagram"]]
    for it in ig:
        pxp.classificar(it, perfil)
    pxp.resolver_conflitos(ig)
    met = metricas()
    hist_fundo = fundos_do_historico()
    por_post = {i["match"].cd_midia: i for i in ig if i["match"] is not None}
    for it in ig:
        it["fundo"] = fundo_da_peca(it["pasta"], hist_fundo.get(it["codigo"] or ""))
        it["categoria"] = categoria_ciclo(it["tipo"], it["pasta"])

    out = [f"# Insumos do Planejador de Sequência — Instagram @shibari.brasil\n",
           f"_Gerado em {hoje.strftime('%d/%m/%Y')}. Perfil: BigQuery (extração 3x/dia); pauta, histórico e briefings: `sb_marketing_team`, somente leitura._\n"]

    # 1. cadência -------------------------------------------------------------------------------------------------
    feed = met.sort_values("dt_publicacao", ascending=False).copy()
    feed["semana"] = feed["dt_publicacao"].map(lambda d: d - timedelta(days=d.weekday()))
    sem = feed.groupby("semana").agg(posts=("cd_midia", "count"), reels=("ds_formato", lambda s: (s == "reel").sum())).sort_index(ascending=False).head(10)
    ultimo = feed["dt_publicacao"].max()
    reels90 = int(((feed["ds_formato"] == "reel") & (feed["dt_publicacao"] >= hoje - timedelta(days=90))).sum())
    out.append("## 1. Cadência real\n")
    out.append(f"- Último post de feed: **{ultimo.strftime('%d/%m/%Y')}** (há {(hoje - ultimo).days} dias). Reels em 90 dias: **{reels90}**. Meta do projeto: 3 posts/semana (seg/qua/sex).\n")
    out.append("| Semana (seg) | Posts de feed | Reels |\n|---|---|---|\n" + "".join(f"| {s.strftime('%d/%m')} | {int(r.posts)} | {int(r.reels)} |\n" for s, r in sem.iterrows()))

    # 2. grade recente ---------------------------------------------------------------------------------------------
    ult = feed.head(12)
    linhas, seq_cor = [], []
    for _, r in ult.iterrows():
        it = por_post.get(r.cd_midia)
        fundo, cat = (it["fundo"], it["categoria"]) if it else (None, "sem peça (" + r.ds_formato + ")")
        titulo = (f"{it['codigo'] or ''} {it['titulo']}".strip() if it else "—")[:60]
        linhas.append((r.dt_publicacao, r.ds_formato, titulo, cat, fundo or "?", int(r.qt_views or 0), r.pct_envio, r.pct_salvamento, bool(r.fg_impulsionada)))
        seq_cor.append(fundo)
    out.append("\n## 2. Grade recente (mais novo primeiro) e verificações da marca\n")
    out.append("| Data | Formato | Peça | Categoria do ciclo | Fundo | Views | Envio | Salv. | Imp. |\n|---|---|---|---|---|---|---|---|---|\n")
    for d, f, t, c, fu, v, e, s, im in linhas:
        out.append(f"| {d.strftime('%d/%m')} | {f} | {t} | {c} | {fu} | {milhar(v)} | {pct(e) if pd.notna(e) else '—'} | {pct(s) if pd.notna(s) else '—'} | {'sim' if im else ''} |\n")
    out.append("\n**Verificações (fundo desconhecido = post sem peça no marketing ou fundo não registrado):**\n")
    cronologico = list(reversed(seq_cor))
    reps = [(cronologico[i], cronologico[i + 1]) for i in range(len(cronologico) - 1) if cronologico[i] and cronologico[i] == cronologico[i + 1]]
    out.append(f"- Mesma cor em posts seguidos (regra do Hugo: não repetir): " + (", ".join(f"{a} → {b}" for a, b in reps) if reps else "nenhum caso nos últimos 12 com fundo conhecido") + ".\n")
    ultimos9 = [f for f in seq_cor[:9] if f]
    out.append(f"- Scarlet nos últimos 9 (máx. 1): {sum('scarlet' in f.lower() for f in ultimos9)}. Claro × escuro nos últimos 9 conhecidos: {sum(luz(f) == 'claro' for f in ultimos9)} claros / {sum(luz(f) == 'escuro' for f in ultimos9)} escuros.\n")
    cats = pd.Series([l[3] for l in linhas[:9]]).value_counts()
    out.append("- Mix dos últimos 9 por categoria (alvo do ciclo: 3 educativo, 2 conceitual, 1 minimalista, 1–2 produto, 1 foto de prática, 1 foto de produto): " + "; ".join(f"{k} {v}" for k, v in cats.items()) + ".\n")

    # 3. estoque ---------------------------------------------------------------------------------------------------
    out.append("\n## 3. Estoque de peças do marketing (Instagram)\n")
    prontas = [i for i in ig if i["match"] is None and i["status"] in ("PRONTO_AGUARDANDO", "PRONTO_AGENDADO", "SO_HISTORICO")]
    prod = [i for i in ig if i["match"] is None and i["status"] in ("DESIGN", "CANVA", "REVISAO", "PRODUCAO", "BRIEFING")]
    out.append(f"**Prontas e não postadas: {len(prontas)}.**\n\n| Peça | Tipo | Categoria | Fundo | Parada há | Observação |\n|---|---|---|---|---|---|\n")
    for i in prontas:
        parada = (hoje - i["aprovado_em"]).days if i["aprovado_em"] else None
        out.append(f"| {pxp._nome(i)[:70]} | {i['tipo']} | {i['categoria']} | {i['fundo'] or '?'} | {parada if parada is not None else '—'} dias | {EM_ESPERA.get(i['codigo'] or '', '')} |\n")
    out.append(f"\n**Em produção: {len(prod)}** (texto pronto ou em revisão; não é entrega).\n\n| Peça | Etapa | Categoria | Fundo | Na etapa há |\n|---|---|---|---|---|\n")
    for i in prod:
        dias = (hoje - i["etapa_desde"]).days if i["etapa_desde"] else None
        out.append(f"| {pxp._nome(i)[:70]} | {pxp.ROTULO_STATUS.get(i['status'], i['status'])} | {i['categoria']} | {i['fundo'] or '?'} | {dias if dias is not None else '—'} dias |\n")

    # 4. banco de briefings ----------------------------------------------------------------------------------------
    banco = ler_banco_briefings()
    em_pauta = {i["codigo"] for i in itens if i["codigo"]}
    livres = [b for b in banco if b["codigo"] not in em_pauta and ("Backlog" in b["status"] or "Briefing criado" in b["status"])]
    insta = [b for b in livres if "instagram" in b["formato"].lower()]
    out.append(f"\n## 4. Banco legado de briefings (congelado) ainda não produzido: {len(insta)} ideias de Instagram\n")
    out.append("| Código | Título provisório | Formato | Persona | Status | Território |\n|---|---|---|---|---|---|\n")
    for b in insta:
        out.append(f"| {b['codigo']} | {b['titulo'][:80]} | {b['formato']} | {b['persona']} | {b['status']} | {b['territorio'][:45]} |\n")

    # 5. desempenho ------------------------------------------------------------------------------------------------
    org = met[~met["fg_impulsionada"].astype(bool)].copy()
    org["tipo_peca"] = org["cd_midia"].map(lambda c: por_post[c]["categoria"] if c in por_post else None)
    ult180 = org[org["dt_publicacao"] >= hoje - timedelta(days=180)]
    def agrega(df, chave):
        g = df.groupby(chave).agg(n=("cd_midia", "count"), views_mediana=("qt_views", "median"), envio_mediana=("pct_envio", "median"),
                                  salvamento_mediano=("pct_salvamento", "median"), seg_mil_mediano=("seg_mil", "median")).reset_index()
        return g.sort_values("envio_mediana", ascending=False)
    fmt = {"views_mediana": lambda x: f"{x:,.0f}".replace(",", "."), "envio_mediana": pct, "salvamento_mediano": pct, "seg_mil_mediano": lambda x: f"{x:.1f}".replace(".", ","), "n": lambda x: str(int(x))}
    out.append("\n## 5. Desempenho (somente posts orgânicos, 180 dias; medianas; n pequeno é hipótese)\n\n**Por formato do Instagram**\n\n")
    out.append(tabela(agrega(ult180, "ds_formato"), ["ds_formato", "n", "views_mediana", "envio_mediana", "salvamento_mediano", "seg_mil_mediano"], fmt))
    com_peca = ult180.dropna(subset=["tipo_peca"])
    if len(com_peca):
        out.append("\n**Por categoria da peça do marketing (só posts com peça casada)**\n\n")
        out.append(tabela(agrega(com_peca, "tipo_peca"), ["tipo_peca", "n", "views_mediana", "envio_mediana", "salvamento_mediano", "seg_mil_mediano"], fmt))
    top = ult180.sort_values("seg_mil", ascending=False).head(8)
    out.append("\n**Top 8 em seguidores por mil views (orgânicos, 180 dias)**\n\n| Data | Formato | Peça | Views | Envio | Seg./mil | Link |\n|---|---|---|---|---|---|---|\n")
    for _, r in top.iterrows():
        it = por_post.get(r.cd_midia)
        out.append(f"| {r.dt_publicacao.strftime('%d/%m')} | {r.ds_formato} | {(pxp._nome(it) if it else 'sem peça')[:55]} | {milhar(r.qt_views)} | {pct(r.pct_envio) if pd.notna(r.pct_envio) else '—'} | {str(round(r.seg_mil, 1)).replace('.', ',')} | [abrir]({r.ds_permalink}) |\n")
    out.append("\n_Impulsionados ficam fora das medianas (views e alcance incluem o pago). Separar sempre o pago do orgânico antes de tirar lição._\n")

    # 6. produtos em foco -------------------------------------------------------------------------------------------
    prod_df = produtos_em_foco()
    out.append("\n## 6. Produtos em foco (90 dias; margem de contribuição e estoque) — para escolher o produto de cada arco\n\n")
    out.append("| Produto | Frente | Un. | Receita | MC % | Estoque (soma) | Cobertura mín. (dias) | Risco de estoque |\n|---|---|---|---|---|---|---|---|\n")
    for _, r in prod_df.iterrows():
        mcp = (r.mc / r.receita) if r.receita else None
        kit = pd.isna(r.estoque)
        estoque_txt = "kit/composição: ver componentes" if kit else str(int(r.estoque))
        cob_txt = "—" if pd.isna(r.cobertura_min) else str(int(r.cobertura_min))
        risco_txt = "—" if kit else (r.risco or "—")[:60]
        out.append(f"| {r.nm_produto} | {r.frente} | {int(r.un)} | R$ {milhar(r.receita)} | {pct(mcp) if mcp is not None else '—'} | {estoque_txt} | {cob_txt} | {risco_txt} |\n")
    out.append("\n_Kits herdam o estoque dos componentes (a corda de juta 8m está em cobertura curta; ver `dados/analises/previsao-ruptura-juta-8m-*.md`). **Não montar arco comercial em produto que vai romper**; confirmar reposição com o Hugo._\n")

    # 7. banco de mídia --------------------------------------------------------------------------------------------
    out.append("\n## 7. Banco de mídia próprio (o que existe para foto de prática, foto de produto e vídeo)\n\n| Pasta | Caminho (no marketing) | Arquivos | Vídeos |\n|---|---|---|---|\n")
    for rotulo, rel, n, v in banco_de_midia():
        out.append(f"| {rotulo} | `{rel}` | {n} | {v} |\n")
    out.append("\n_Não há subpastas pratica/produto/lifestyle: classificar antes de planejar. Se o arco precisa de foto ou vídeo que não existe, entra na **lista de captação** (shot list) da sequência._\n")

    # 8. calendário -----------------------------------------------------------------------------------------------
    out.append(f"\n## 8. Calendário dos próximos {args.dias} dias (slots seg/qua/sex)\n\n| Data | Dia | Slot | Observação |\n|---|---|---|---|\n")
    d = hoje
    while d <= hoje + timedelta(days=args.dias):
        if d.weekday() in DIAS_POST or d in DATAS:
            out.append(f"| {d.strftime('%d/%m')} | {DIAS_PT[d.weekday()]} | {'feed' if d.weekday() in DIAS_POST else '—'} | {DATAS.get(d, '')} |\n")
        d += timedelta(days=1)
    out.append("\n_Agendamento da semana seguinte é na sexta (mLabs, ~2 h). Datas especiais: confirmar com o Hugo._\n")

    texto = "".join(out)
    if args.out:
        Path(args.out).write_text(texto, encoding="utf-8")
        print(f"gravado em {args.out}")
    else:
        print(texto)


if __name__ == "__main__":
    main()
