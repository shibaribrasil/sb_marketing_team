"""Produzido x Postado: cruza a pauta do time de marketing (sb_marketing_team) com o que está NO AR no Instagram (BigQuery).

Somente leitura: não altera pauta, histórico nem nenhuma pasta do marketing, e não escreve no banco.

O que faz
  1. Lê `contexto/pauta.md` (status de cada peça) e `contexto/historico-conteudos.md` (peças prontas que a pauta não lista).
  2. Para cada peça do Instagram, extrai a LEGENDA planejada do `texto.md` (seção "Legenda").
  3. Compara a legenda com a legenda postada de cada peça em `dbt_dw_az.tb_instagram_midia` (similaridade de texto, com data
     como desempate e conferência). A pauta NÃO é a fonte de verdade de "postou": o perfil é.
  4. Entrega: o que foi produzido e NÃO foi postado; o que já está no ar mas a pauta ainda mostra como pendente; o que a pauta
     diz que foi publicado e não aparece no perfil; divergências de data; peças em produção (informativo).

Uso (venv do sb_relatorios, que tem pandas e o cliente do BigQuery):
  /c/Users/HTK1562/venvs/sb_relatorios/Scripts/python.exe produzido_x_postado.py            # relatório em Markdown
  ... produzido_x_postado.py --debug                                                        # mostra os 2 melhores candidatos de cada peça
  ... produzido_x_postado.py --out C:/caminho/relatorio.md                                  # também grava em arquivo

Limites (também impressos no relatório): legenda editada no mLabs/Instagram pode baixar a similaridade (aparece como "provável");
peça sem legenda (foto, vídeo, produto sem texto) é cruzada só por título e data; Stories não entram (a API só os vê por 24 h);
a extração do Instagram roda 3x por dia, então uma peça postada há poucas horas pode ainda não aparecer.
"""
import argparse
import io
import re
import sys
import unicodedata
from datetime import date, datetime, timedelta
from difflib import SequenceMatcher
from pathlib import Path

import pandas as pd

MKT = Path(__file__).resolve().parents[4]   # raiz do sb_marketing_team
# desde 21/10/2026 a produção de cada conteúdo (texto, legenda, imagens) mora no Drive; nos registros do marketing
# o caminho continua escrito `conteudos/<tipo>/<pasta>` e equivale a `03_CONTEUDO/<tipo>/<pasta>` lá
CONTEUDOS = Path(r"G:\Meu Drive\SB Audiovisual\03_CONTEUDO")


def pasta_do_conteudo(pasta):
    """`conteudos/<tipo>/<pasta>` dos registros -> pasta real no Drive. Outros caminhos seguem relativos ao repo do marketing."""
    p = str(pasta).replace("\\", "/")
    return CONTEUDOS / p[len("conteudos/"):] if p.startswith("conteudos/") else MKT / pasta
BQ_SCRIPTS = Path(r"C:\Users\HTK1562\Documents\GitHub\sb_admin_team\.claude\skills\analista-de-dados\scripts")
sys.path.insert(0, str(BQ_SCRIPTS))
sys.stdout.reconfigure(encoding="utf-8")

LIMIAR_CERTO = 0.88      # similaridade a partir da qual consideramos "postada"
LIMIAR_PROVAVEL = 0.62   # entre este e o anterior: "provável" (legenda editada); abaixo disso: não casou
INICIO_PIPELINE = date(2026, 6, 1)   # primeiras peças da pauta atual (antes disso o perfil não tinha este fluxo)
JANELA_DIAS = 2          # tolerância entre a data da pauta e a data real do post

STATUS_POR_SECAO = [
    ("Aguardando Publica", "PRONTO_AGUARDANDO"), ("Agendado", "PRONTO_AGENDADO"), ("Publicado", "PRONTO_PUBLICADO"),
    ("Design em Produ", "DESIGN"), ("Pendente de Altera", "CANVA"), ("Aguardando Revis", "REVISAO"),
    ("Em Produ", "PRODUCAO"), ("Briefing", "BRIEFING"),
]
ROTULO_STATUS = {
    "PRONTO_AGUARDANDO": "Pronto - Aguardando Publicação", "PRONTO_AGENDADO": "Pronto - Agendado", "PRONTO_PUBLICADO": "Pronto - Publicado",
    "DESIGN": "Design em Produção (Bia)", "CANVA": "Pendente de ajuste no Canva", "REVISAO": "Aguardando aprovação do Hugo",
    "PRODUCAO": "Em produção (Julia)", "BRIEFING": "Slot aprovado (aguarda a Julia)", "SO_HISTORICO": "Só no histórico (fora da pauta)",
}


# ── leitura do marketing ───────────────────────────────────────────────────────────────────────────────────────
def _limpa(c):
    return c.strip().strip("`").strip()


def _tabelas(md):
    """[(titulo_da_secao, [dict linha])] de todas as tabelas markdown do arquivo."""
    saida, secao, cab, linhas = [], "", None, []   # "" (não None): arquivos sem seção ## (histórico) também têm tabela
    for raw in md.splitlines() + ["## fim"]:
        if raw.startswith("## "):
            if secao is not None and linhas:
                saida.append((secao, linhas))
            secao, cab, linhas = raw[3:].strip(), None, []
            continue
        if not raw.startswith("|"):
            continue
        cels = [_limpa(c) for c in raw.strip().strip("|").split("|")]
        if cab is None:
            cab = cels
        elif all(re.fullmatch(r":?-{2,}:?", c.replace(" ", "")) for c in cels if c):
            continue
        elif len(cels) == len(cab):
            linhas.append(dict(zip(cab, cels)))
    return saida


def _dir(arquivo):
    a = arquivo.replace("\\", "/").strip()
    return a.rsplit("/", 1)[0] if a.endswith(".md") else a.rstrip("/")


def _codigo(titulo):
    m = re.match(r"\s*(C-\d+)\s*[—-]\s*(.*)", titulo)
    return (m.group(1), m.group(2).strip()) if m else (None, titulo.strip())


def _data(txt):
    m = re.search(r"(\d{2})/(\d{2})/(\d{4})", txt or "")
    return date(int(m.group(3)), int(m.group(2)), int(m.group(1))) if m else None


def legenda_planejada(pasta):
    """Legenda planejada da peça (None se não houver). O texto.md aparece em três formatos:
    `## 2. Legenda`, `**9. Legenda**` e (vídeo) só a legenda com hashtags, sem títulos."""
    # desde 21/10/2026 a legenda aprovada vive em `legenda.txt` (é o arquivo que o publicador envia ao Instagram);
    # peças antigas ainda trazem a legenda dentro do texto.md
    arq_legenda = pasta_do_conteudo(pasta) / "legenda.txt"
    if arq_legenda.exists() and arq_legenda.read_text(encoding="utf-8").strip():
        return arq_legenda.read_text(encoding="utf-8").strip()
    f = pasta_do_conteudo(pasta) / "texto.md"
    if not f.exists():
        return None
    md = f.read_text(encoding="utf-8")
    m = re.search(r"^(?:#{1,3}\s*|\*\*\s*)\d*\.?\s*Legenda[^\n]*\n(.*?)(?=^#{1,3}\s|^\*\*\s*\d+\.|^\s*---\s*$|\Z)", md, re.S | re.M | re.I)
    if m and m.group(1).strip():
        return m.group(1).strip()
    tem_secao = re.search(r"^#{1,3}\s|^\*\*\s*\d+\.", md, re.M)
    if not tem_secao and re.search(r"#\w+", md):      # vídeo/foto: o arquivo inteiro é a legenda
        return md.strip()
    return None


def itens_do_marketing():
    pauta = (MKT / "contexto" / "pauta.md").read_text(encoding="utf-8")
    itens, vistos = [], set()
    for secao, linhas in _tabelas(pauta):
        status = next((s for k, s in STATUS_POR_SECAO if k in secao), None)
        if status is None:
            continue
        for r in linhas:
            titulo, arquivo = r.get("Título", ""), r.get("Arquivo", "")
            if not titulo or not arquivo:
                continue
            cod, nome = _codigo(titulo)
            pasta = _dir(arquivo)
            itens.append({
                "codigo": cod, "titulo": nome, "tipo": r.get("Tipo de Conteúdo", ""), "pasta": pasta, "status": status,
                "aprovado_em": _data(r.get("Aprovado em", "")), "publicado_em": _data(r.get("Publicado em", "")),
                "agendado_em": _data(r.get("Publicação agendada", "")), "origem": "pauta",
                "etapa_desde": _data(r.get("Texto entregue em", "") or r.get("Entrou em revisão", "")),
            })
            vistos.add(pasta)
    hist = (MKT / "contexto" / "historico-conteudos.md").read_text(encoding="utf-8")
    for _, linhas in _tabelas(hist):
        for r in linhas:
            pasta = _dir(r.get("Arquivo", ""))
            if not pasta or pasta in vistos:
                continue
            cod = r.get("Código", "").strip()
            itens.append({
                "codigo": cod if cod.startswith("C-") else None, "titulo": r.get("Título", "").strip(), "tipo": r.get("Tipo", ""),
                "pasta": pasta, "status": "SO_HISTORICO", "aprovado_em": _data(r.get("Aprovado em", "")),
                "publicado_em": _data(r.get("Publicado em", "")), "agendado_em": None, "origem": "historico", "etapa_desde": None,
            })
            vistos.add(pasta)
    for it in itens:
        it["instagram"] = "instagram" in it["pasta"].lower() or "instagram" in (it["tipo"] or "").lower()
        it["legenda"] = legenda_planejada(it["pasta"]) if it["instagram"] else None
        it["tem_pasta"] = pasta_do_conteudo(it["pasta"]).exists()
    return itens


# ── casamento com o que está no ar ─────────────────────────────────────────────────────────────────────────────
def _norm(txt, n=320):
    if not txt:
        return ""
    t = unicodedata.normalize("NFKD", txt).encode("ascii", "ignore").decode().lower()
    t = re.sub(r"#\w+", " ", t)
    t = re.sub(r"[^a-z0-9 ]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()[:n]


def carregar_perfil():
    from bq_client import get_client
    cli = get_client("us-east4")
    df = cli.query("""
        SELECT cd_midia, ds_formato, dt_publicacao, ts_publicacao, ds_legenda, ds_permalink, qt_views, qt_alcance, fg_impulsionada, ts_extracao
          FROM `igneous-sandbox-381622.dbt_dw_az.tb_instagram_midia`
         WHERE NOT fg_story ORDER BY ts_publicacao DESC
    """).to_dataframe()
    df["dt_publicacao"] = pd.to_datetime(df["dt_publicacao"]).dt.date
    df["norm"] = df["ds_legenda"].map(_norm)
    return df


def melhores(item, perfil, k=6):
    """Candidatos do perfil ordenados por similaridade de legenda (e por título quando não há legenda)."""
    alvo = _norm(item["legenda"]) if item["legenda"] else ""
    por_titulo = False
    if not alvo:
        alvo, por_titulo = _norm(item["titulo"]), True
    saida = []
    for r in perfil.itertuples():
        if not r.norm or not alvo:
            continue
        if por_titulo:
            # título curto está CONTIDO na legenda postada: usa fração de palavras do título presentes na legenda
            palavras = [w for w in alvo.split() if len(w) > 3]
            sim = (sum(w in r.norm.split() for w in palavras) / len(palavras)) if palavras else 0.0
            sim *= 0.9    # sem legenda planejada a evidência é mais fraca
        else:
            sim = SequenceMatcher(None, alvo, r.norm, autojunk=False).ratio()
        saida.append((sim, r))
    return sorted(saida, key=lambda x: x[0], reverse=True)[:k], por_titulo


def classificar(item, perfil):
    cand, por_titulo = melhores(item, perfil)
    item["metodo"] = "título (sem legenda planejada)" if por_titulo else ("legenda" if item["legenda"] else "sem texto para cruzar")
    item["cand"] = cand
    item["match"], item["confianca"], item["sim"] = None, None, 0.0
    if not cand:
        return item
    sim, r = cand[0]
    item["sim"] = sim
    if item["metodo"].startswith("título"):
        # evidência fraca: no máximo "provável", e só se a data (quando a pauta a tem) bater com o post
        data_ref = item["publicado_em"] or item["agendado_em"]
        data_ok = data_ref is None or abs((r.dt_publicacao - data_ref).days) <= 3
        if sim >= 0.8 and data_ok:
            item["match"], item["confianca"] = r, "provável (título)"
        return item
    # por legenda: entre os candidatos plausíveis, o post NÃO pode ser anterior à aprovação da peça; empate de similaridade
    # (mesma legenda repetida em dois posts) vai para o mais próximo da data da pauta, ou o mais recente se não houver data.
    plausiveis = [(sm, rr) for sm, rr in cand if sm >= LIMIAR_PROVAVEL]
    if item["aprovado_em"]:
        depois = [(sm, rr) for sm, rr in plausiveis if rr.dt_publicacao >= item["aprovado_em"] - timedelta(days=1)]
        item["so_anterior"] = bool(plausiveis) and not depois      # só existe post parecido ANTERIOR à aprovação
        plausiveis = depois
    if not plausiveis:
        return item
    topo = max(sm for sm, _ in plausiveis)
    empate = [(sm, rr) for sm, rr in plausiveis if sm >= topo - 0.03]
    ref = item["publicado_em"] or item["agendado_em"]
    sim, r = (min(empate, key=lambda c: abs((c[1].dt_publicacao - ref).days)) if ref
              else max(empate, key=lambda c: c[1].dt_publicacao))
    item["sim"] = sim
    item["match"], item["confianca"] = r, ("alta" if sim >= LIMIAR_CERTO else "provável")
    return item


def resolver_conflitos(itens):
    """Se duas peças do marketing disputam o mesmo post, fica quem tem a maior similaridade."""
    por_post = {}
    for it in itens:
        if it["match"] is not None:
            por_post.setdefault(it["match"].cd_midia, []).append(it)
    for _, disputa in por_post.items():
        if len(disputa) > 1:
            disputa.sort(key=lambda i: i["sim"], reverse=True)
            for perdedor in disputa[1:]:
                perdedor["conflito"] = disputa[0]["codigo"] or disputa[0]["titulo"]
                perdedor["match"], perdedor["confianca"] = None, None


# ── relatório ──────────────────────────────────────────────────────────────────────────────────────────────────
def _fmt(d):
    return d.strftime("%d/%m/%Y") if d else "—"


def _nome(it):
    return (f"{it['codigo']} — " if it["codigo"] else "") + it["titulo"]


def _formato(it):
    return it["tipo"] or it["pasta"].split("/")[1].replace("instagram-", "") if "/" in it["pasta"] else it["tipo"]


def relatorio(itens, perfil, hoje):
    ig = [i for i in itens if i["instagram"]]
    prontos = [i for i in ig if i["status"] in ("PRONTO_AGUARDANDO", "PRONTO_AGENDADO", "SO_HISTORICO")]
    no_ar = [i for i in ig if i["match"] is not None]
    nao_postados = [i for i in prontos if i["match"] is None and i["status"] != "PRONTO_PUBLICADO"]
    so_hist_sem_data = [i for i in nao_postados if i["status"] == "SO_HISTORICO" and not i["publicado_em"]]
    ja_no_ar_pauta_pendente = [i for i in prontos if i["match"] is not None and i["status"] in ("PRONTO_AGUARDANDO", "PRONTO_AGENDADO")]
    publicado_nao_achado = [i for i in ig if i["status"] == "PRONTO_PUBLICADO" and i["match"] is None]
    diverg = [i for i in no_ar if i["publicado_em"] and abs((i["publicado_em"] - i["match"].dt_publicacao).days) > JANELA_DIAS]
    repetidas = [i for i in ig if i["match"] is not None and sum(1 for sm, _ in i["cand"] if sm >= LIMIAR_CERTO) > 1]
    em_producao = [i for i in ig if i["status"] in ("DESIGN", "CANVA", "REVISAO", "PRODUCAO", "BRIEFING")]
    blog = [i for i in itens if not i["instagram"]]
    ult = pd.to_datetime(perfil["ts_extracao"]).max()
    dono = {i["match"].cd_midia: (i["codigo"] or i["titulo"][:30]) for i in no_ar}

    L = [f"# Produzido x Postado — Instagram @shibari.brasil", "",
         f"_Gerado em {hoje:%d/%m/%Y}. Perfil lido do BigQuery (última extração: {ult:%d/%m %H:%M} UTC; a extração roda 3x por dia). "
         f"Pauta e histórico do `sb_marketing_team` em somente leitura._", ""]

    L += ["## 1. Produzido e AINDA NÃO postado", ""]
    if not nao_postados:
        L += ["Nada: toda peça pronta já está no ar.", ""]
    else:
        L += [f"**{len(nao_postados)} peça(s) pronta(s) que não aparece(m) no perfil:**", "",
              "| Peça | Formato | Status na pauta | Aprovada em | Parada há | Melhor candidato no perfil (similaridade) |", "|---|---|---|---|---|---|"]
        for i in sorted(nao_postados, key=lambda x: x["aprovado_em"] or date.min):
            dias = (hoje - i["aprovado_em"]).days if i["aprovado_em"] else None
            c = "—"
            if i["cand"]:
                sm, rr = i["cand"][0]
                c = f"{_fmt(rr.dt_publicacao)} ({sm:.0%})" + (f", mas esse post é da {dono[rr.cd_midia]}" if rr.cd_midia in dono else ", parecido, não é a mesma peça")
            L.append(f"| {_nome(i)} | {_formato(i)} | {ROTULO_STATUS[i['status']]}{' (agendada p/ ' + _fmt(i['agendado_em']) + ')' if i['agendado_em'] else ''} | {_fmt(i['aprovado_em'])} | "
                     f"{str(dias) + ' dias' if dias is not None else '—'} | {c} |")
        L += ["", "Peça **parada há mais de 14 dias** é alcance perdido (a conta ganha com constância): decidir se entra na semana ou se é descartada. Texto e imagens ficam no Drive, em `03_CONTEUDO/<tipo>/<pasta>/`.", ""]

    L += ["## 2. Já está no ar, mas a pauta ainda mostra como pendente (pedir à Mari para confirmar a postagem)", ""]
    if not ja_no_ar_pauta_pendente:
        L += ["Nenhuma.", ""]
    else:
        L += ["| Peça | Status na pauta | Postada em | Link | Similaridade | Views |", "|---|---|---|---|---|---|"]
        for i in sorted(ja_no_ar_pauta_pendente, key=lambda x: x["match"].dt_publicacao):
            m = i["match"]
            L.append(f"| {_nome(i)} | {ROTULO_STATUS[i['status']]} | **{_fmt(m.dt_publicacao)}** | [abrir]({m.ds_permalink}) | {i['sim']:.0%} ({i['confianca']}) | {int(m.qt_views) if pd.notna(m.qt_views) else '—'} |")
        L += ["", "Sugestão: dizer à Mari `Confirmar postagem: <título>` com a data real acima (não mexo na pauta do marketing).", ""]

    L += ["## 3. A pauta diz \"publicado\", mas não achei no perfil", ""]
    if not publicado_nao_achado:
        L += ["Nenhuma.", ""]
    else:
        L += ["| Peça | Publicado em (pauta) | Melhor candidato (similaridade) | Possível causa |", "|---|---|---|---|"]
        for i in publicado_nao_achado:
            c = f"{_fmt(i['cand'][0][1].dt_publicacao)} — [{i['cand'][0][1].ds_permalink[-14:]}]({i['cand'][0][1].ds_permalink}) ({i['cand'][0][0]:.0%})" if i["cand"] else "—"
            causa = "legenda editada ao postar" if i["cand"] and i["cand"][0][0] >= 0.45 else ("sem legenda planejada para cruzar" if not i["legenda"] else "post apagado, ainda não extraído ou legenda muito diferente")
            L.append(f"| {_nome(i)} | {_fmt(i['publicado_em'])} | {c} | {causa} |")
        L.append("")

    L += ["## 4. Data da pauta diferente da data real do post", ""]
    if not diverg:
        L += ["Nenhuma divergência acima de 2 dias.", ""]
    else:
        L += ["| Peça | Pauta diz | Post real | Diferença |", "|---|---|---|---|"]
        for i in sorted(diverg, key=lambda x: abs((x["publicado_em"] - x["match"].dt_publicacao).days), reverse=True):
            d = (i["match"].dt_publicacao - i["publicado_em"]).days
            L.append(f"| {_nome(i)} | {_fmt(i['publicado_em'])} | {_fmt(i['match'].dt_publicacao)} ([abrir]({i['match'].ds_permalink})) | {d:+d} dias |")
        L += ["", "A data da pauta é a da confirmação/agendamento, nem sempre a do post (quando a data real é ANTERIOR, a confirmação foi feita depois). Para análise de desempenho vale sempre a data real.", ""]

    L += ["## 4b. Mesma legenda em mais de um post (repostagem do próprio conteúdo)", ""]
    if not repetidas:
        L += ["Nenhuma.", ""]
    else:
        L += ["| Peça | Posts com a mesma legenda |", "|---|---|"]
        for i in repetidas:
            posts = ", ".join(f"[{_fmt(r.dt_publicacao)}]({r.ds_permalink})" for sm, r in sorted(i["cand"], key=lambda c: c[1].dt_publicacao) if sm >= LIMIAR_CERTO)
            L.append(f"| {_nome(i)} | {posts} |")
        L += ["", "Repostar conteúdo **próprio** é permitido, mas se a peça nova da pauta (ex.: C-079) não foi ao ar, o que subiu foi a antiga. "
                  "Confira se a arte também foi a antiga e, se for repostar mais, lembre que o Instagram não recomenda conta que repete conteúdo demais (regra de originalidade).", ""]

    L += ["## 5. Em produção (texto pronto, arte em andamento; ainda não é entrega)", ""]
    if not em_producao:
        L += ["Nada em produção.", ""]
    else:
        L += ["| Peça | Etapa | Formato | Na etapa desde | Parada há |", "|---|---|---|---|---|"]
        for i in sorted(em_producao, key=lambda x: x["etapa_desde"] or date.max):
            dias = (hoje - i["etapa_desde"]).days if i["etapa_desde"] else None
            L.append(f"| {_nome(i)} | {ROTULO_STATUS[i['status']]} | {_formato(i)} | {_fmt(i['etapa_desde'])} | {str(dias) + ' dias' if dias is not None else '—'} |")
        L.append("")

    casados = {i["match"].cd_midia for i in no_ar}
    avulsos = perfil[(~perfil["cd_midia"].isin(casados)) & (perfil["dt_publicacao"] >= INICIO_PIPELINE)].sort_values("ts_publicacao", ascending=False)
    L += [f"## 5b. Posts no ar SEM peça correspondente no marketing (desde {INICIO_PIPELINE:%d/%m/%Y})", ""]
    if avulsos.empty:
        L += ["Nenhum: tudo que subiu veio da pauta.", ""]
    else:
        L += ["| Data | Formato | Começa com | Views | Obs. | Link |", "|---|---|---|---|---|---|"]
        for r in avulsos.head(25).itertuples():
            # legenda igual à de uma peça da pauta = repostagem de peça que já tinha ido ao ar
            igual = next((_nome(i) for i in ig if i["legenda"] and SequenceMatcher(None, _norm(i["legenda"]), r.norm, autojunk=False).ratio() >= LIMIAR_CERTO), None)
            obs = f"legenda igual à de {igual[:40]} (repostagem)" if igual else ""
            L.append(f"| {_fmt(r.dt_publicacao)} | {r.ds_formato} | {(r.ds_legenda or '').strip().replace(chr(10), ' ')[:60]} | {int(r.qt_views) if pd.notna(r.qt_views) else '—'} | {obs} | [abrir]({r.ds_permalink}) |")
        L += ["", "São posts fora do fluxo da pauta (Reels, fotos, produtos, anúncios impulsionados ou conteúdo feito direto no app). Não é erro; serve para ver o que a pauta não enxerga.", ""]

    L += ["## 6. Resumo", "",
          f"- Peças do Instagram acompanhadas: **{len(ig)}** ({len(no_ar)} no ar, {len(nao_postados)} prontas e não postadas, {len(em_producao)} em produção).",
          f"- Posts do perfil sem peça no marketing: **{len(avulsos)}** desde {INICIO_PIPELINE:%d/%m/%Y} (início do fluxo atual); os {len(perfil) - len(casados) - len(avulsos)} mais antigos são de antes da pauta e não entram.",
          f"- Fora do escopo (blog): {len(blog)}.", ""]
    L += ["## Como o cruzamento foi feito (e seus limites)", "",
          f"- Compara a **legenda planejada** (`texto.md`, seção Legenda) com a legenda postada, ignorando acento, pontuação, emoji e hashtag. Similaridade ≥ {LIMIAR_CERTO:.0%} = no ar (alta); {LIMIAR_PROVAVEL:.0%} a {LIMIAR_CERTO:.0%} = provável (legenda editada); abaixo = não casou.",
          "- Peça sem legenda planejada é cruzada só por palavras do título (evidência fraca, marcada na coluna de similaridade).",
          "- Duas peças que disputam o mesmo post ficam com a de maior similaridade. Stories e blog não entram.",
          "- Uma peça postada nas últimas horas pode ainda não ter sido extraída (3 extrações por dia)."]
    return "\n".join(L), {"nao_postados": nao_postados, "no_ar": no_ar, "debug": itens}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--debug", action="store_true", help="mostra os 2 melhores candidatos de cada peça")
    ap.add_argument("--out", help="grava o relatório neste arquivo (além de imprimir)")
    a = ap.parse_args()
    hoje = datetime.now().date()
    itens = itens_do_marketing()
    perfil = carregar_perfil()
    for it in itens:
        if it["instagram"]:
            classificar(it, perfil)
        else:
            it["match"], it["cand"], it["sim"], it["confianca"] = None, [], 0.0, None
    resolver_conflitos([i for i in itens if i["instagram"]])
    if a.debug:
        for it in itens:
            if not it["instagram"]:
                continue
            c = " | ".join(f"{s:.2f} {r.dt_publicacao} {(r.ds_legenda or '')[:38]!r}" for s, r in it["cand"][:2])
            print(f"[{it['status']:<18}] {_nome(it)[:58]:<58} legenda={'sim' if it['legenda'] else 'NÃO'} -> {it['confianca'] or '—':<8} {c}")
        return 0
    texto, _ = relatorio(itens, perfil, hoje)
    print(texto)
    if a.out:
        Path(a.out).parent.mkdir(parents=True, exist_ok=True)
        io.open(a.out, "w", encoding="utf-8", newline="").write(texto + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
