"""Gera o artefato visual da Sequência de Conteúdo Instagram (HTML único, somente leitura).

Junta o HISTÓRICO real (BigQuery `tb_instagram_midia` + casamento com as peças do marketing) ao PLANO vigente
(`estrategia/sequencia-instagram-plano.json`) e grava `estrategia/sequencia-instagram.html` a partir do template
`sequencia_artefato.template.html`. Depois, publicar/atualizar com a ferramenta Artifact (mesmo caminho de arquivo).

Uso (venv do sb_relatorios):
  /c/Users/HTK1562/venvs/sb_relatorios/Scripts/python.exe gerar_artefato_sequencia.py [--desde 2025-10-01] [--out caminho.html]

Não altera pauta, histórico nem plano; não escreve no banco.
"""
import argparse
import base64
import io
import json
import os
import re
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

from datetime import date, timedelta

import pandas as pd
import requests
from PIL import Image

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import insumos_sequencia as ins  # noqa: E402
import produzido_x_postado as pxp  # noqa: E402

RAIZ = AQUI.parents[3]
PLANO = RAIZ / "estrategia" / "sequencia-instagram-plano.json"
TEMPLATE = AQUI / "sequencia_artefato.template.html"
SAIDA = RAIZ / "estrategia" / "sequencia-instagram.html"
CAPAS = RAIZ / "estrategia" / "capas"     # cache local das capas (a URL da Meta expira)
GRAPH = "https://graph.facebook.com/v26.0"
LARGURA_CAPA = 420                                  # px; basta para a grade e mantém o HTML leve


def primeira_linha(legenda, n=90):
    t = (legenda or "").strip().splitlines()[0] if (legenda or "").strip() else ""
    t = re.sub(r"#\w+", "", t).strip()
    return (t[: n - 1] + "…") if len(t) > n else t


def historico(desde):
    from bq_client import get_client
    cli = get_client("us-east4")
    df = cli.query(f"""
        SELECT cd_midia, ds_formato, qt_slides, dt_publicacao, qt_views, pct_envio, pct_salvamento, qt_seguidores_por_mil_views AS seg_mil,
               qt_seguidores_ganhos, qt_visitas_perfil, qt_reposts, qt_comentarios, fg_impulsionada, ds_permalink, ds_legenda, ts_extracao
          FROM `igneous-sandbox-381622.dbt_dw_az.tb_instagram_midia`
         WHERE NOT fg_story AND dt_publicacao >= DATE '{desde}'
         ORDER BY dt_publicacao
    """).to_dataframe()
    df["dt_publicacao"] = pd.to_datetime(df["dt_publicacao"]).dt.date
    return df


STATUS_FILA = {"rascunho": "Na fila, sem aprovação", "aprovado": "Aprovado, falta agendar", "agendado": "Agendado", "publicando": "Publicando agora",
               "publicado": "Publicado", "falhou": "Falhou: nada foi ao ar", "atrasado": "Atrasou: não publicou", "incerto": "Conferir no perfil", "cancelado": "Cancelado"}
DIA_PT = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
BUCKET_PUBLICADOR = "sb-instagram-midia-igneous-sandbox-381622"   # imagens aprovadas do publicador (sb_data_pipeline)


def capa_do_agendado(item_id, midias_hash, primeira):
    """Capa (1ª página) do post AGENDADO, lida do bucket do publicador: é a cópia exata que o Hugo aprovou (nome do objeto
    leva o hash). Devolve os bytes JPEG redimensionados ou None. Guarda cópia local para não baixar de novo."""
    if not midias_hash or not primeira:
        return None
    arq = CAPAS / f"ag-{item_id.lower()}-{midias_hash[:10]}.jpg"
    if arq.exists():
        return arq.read_bytes()
    objeto = f"gs://{BUCKET_PUBLICADOR}/{item_id.lower()}/01-{midias_hash[:10]}-{primeira}"
    env = {**os.environ, "CLOUDSDK_CORE_ACCOUNT": "lojashibaribrasil@gmail.com"}
    r = subprocess.run(["gcloud", "storage", "cat", objeto, "--project=igneous-sandbox-381622"], capture_output=True, env=env, shell=(os.name == "nt"))
    if r.returncode != 0 or not r.stdout:
        print(f"aviso: não consegui baixar a capa do agendado {item_id} ({objeto.split('/')[-1]})")
        return None
    im = Image.open(io.BytesIO(r.stdout)).convert("RGB")
    if im.width > LARGURA_CAPA:
        im = im.resize((LARGURA_CAPA, round(im.height * LARGURA_CAPA / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=72, optimize=True)
    CAPAS.mkdir(parents=True, exist_ok=True)
    arq.write_bytes(buf.getvalue())
    return buf.getvalue()


def agendamentos():
    """Itens da fila de publicação do sb_data_pipeline (`raw_instagram.fila_publicacao`), por id do plano (P1, P2...).
    Somente leitura. Sem a tabela (ainda não criada) ou sem acesso: devolve {} e o artefato sai como antes."""
    from zoneinfo import ZoneInfo
    from bq_client import get_client
    try:
        df = get_client("us-east4").query("""
            SELECT id, status, data_hora, media_id, permalink, liberado_real_em, erro, midias_hash, midias_json
              FROM `igneous-sandbox-381622.raw_instagram.fila_publicacao` WHERE status != 'cancelado'""").to_dataframe()
    except Exception as exc:  # tabela inexistente ou sem permissão: não derruba a geração do artefato
        print(f"aviso: fila de publicação indisponível ({exc.__class__.__name__}); artefato sem agendados")
        return {}
    out = {}
    for r in df.itertuples():
        quando = pd.Timestamp(r.data_hora).tz_convert(ZoneInfo("America/Sao_Paulo"))
        midias = json.loads(r.midias_json) if pd.notna(r.midias_json) and r.midias_json else []
        jpg = capa_do_agendado(r.id, r.midias_hash if pd.notna(r.midias_hash) else None, midias[0] if midias else None)
        out[r.id] = {"status": r.status, "status_txt": STATUS_FILA.get(r.status, r.status), "data": quando.date().isoformat(),
                     "dia_semana": DIA_PT[quando.weekday()], "hora": quando.strftime("%H:%M"),
                     "media_id": r.media_id if pd.notna(r.media_id) else None, "permalink": r.permalink if pd.notna(r.permalink) else None,
                     "liberado": pd.notna(r.liberado_real_em), "erro": r.erro if pd.notna(r.erro) else None,
                     "capa": ("data:image/jpeg;base64," + base64.b64encode(jpg).decode()) if jpg else None}
    return out


_TOK = {}   # token da Meta guardado uma vez por execução (capa_em_cache)


def aplicar_agendamentos(plano_slots, posts, fila_ag):
    """Cruza o plano com a fila. Slot com item na fila ganha `agendamento` (a moldura do artefato). Se o post JÁ foi
    publicado e já consta no extrato do perfil (`posts`), o slot SAI do plano: o post aparece como os demais publicados."""
    no_ar = {p["id"] for p in posts}
    restantes, virou_post = [], []
    for sl in plano_slots:
        # item da fila do publicador; sem ele, vale o `agendamento` lançado à mão no JSON (post agendado por outro canal, ex.: mLabs)
        ag = fila_ag.get(sl.get("id")) or sl.get("agendamento")
        if ag and ag.get("media_id") and not ag.get("capa"):   # já no ar: capa real (Reel = thumbnail), a mesma do cache das capas
            jpg = capa_em_cache(ag["media_id"], _TOK)
            if jpg:
                ag["capa"] = "data:image/jpeg;base64," + base64.b64encode(jpg).decode()
        if ag and ag["status"] == "publicado" and ag["media_id"] in no_ar:
            virou_post.append(sl["id"])
            continue
        if ag and ag["status"] != "rascunho":
            sl["agendamento"] = ag
        elif ag:
            sl["na_fila"] = ag["status_txt"]
        restantes.append(sl)
    return restantes, virou_post


def _token():
    """Token do Instagram no Secret Manager (nunca impresso nem gravado; vai só no cabeçalho Authorization)."""
    env = {**os.environ, "CLOUDSDK_CORE_ACCOUNT": "lojashibaribrasil@gmail.com"}
    r = subprocess.run(["gcloud", "secrets", "versions", "access", "latest", "--secret=meta_instagram_token", "--project=igneous-sandbox-381622"],
                       capture_output=True, text=True, env=env, shell=(os.name == "nt"))
    if r.returncode != 0:
        raise SystemExit("não consegui ler o token do Secret Manager (gcloud autenticado?)")
    return r.stdout.strip()


def capa_em_cache(cd_midia, tok_holder):
    """Devolve os bytes JPEG da capa (carrossel/imagem: media_url; Reel: thumbnail_url). Baixa uma vez e guarda em estrategia/capas/."""
    arq = CAPAS / f"{cd_midia}.jpg"
    if arq.exists():
        return arq.read_bytes()
    if "t" not in tok_holder:
        tok_holder["t"] = _token()
    r = requests.get(f"{GRAPH}/{cd_midia}", params={"fields": "media_type,media_url,thumbnail_url"},
                     headers={"Authorization": f"Bearer {tok_holder['t']}"}, timeout=30)
    if r.status_code != 200:
        return None
    j = r.json()
    url = j.get("thumbnail_url") if j.get("media_type") == "VIDEO" else j.get("media_url")
    url = url or j.get("media_url") or j.get("thumbnail_url")
    if not url:
        return None
    img = requests.get(url, timeout=60)
    if img.status_code != 200:
        return None
    im = Image.open(io.BytesIO(img.content)).convert("RGB")
    if im.width > LARGURA_CAPA:
        im = im.resize((LARGURA_CAPA, round(im.height * LARGURA_CAPA / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=72, optimize=True)
    CAPAS.mkdir(parents=True, exist_ok=True)
    arq.write_bytes(buf.getvalue())
    return buf.getvalue()


ETAPAS = [("BRIEFING", "Slot aprovado (Julia)"), ("PRODUCAO", "Em produção (Julia)"), ("REVISAO", "Aguardando aprovação do Hugo"), ("DESIGN", "Design em produção (Bia)"),
          ("CANVA", "Ajuste no Canva (Hugo)"), ("PRONTO_AGUARDANDO", "Pronto, aguardando publicação"), ("PRONTO_AGENDADO", "Pronto, agendado"), ("SO_HISTORICO", "Pronto (só no histórico)")]
EM_ESPERA = {"C-090": "descartada (decisão do Hugo, 28/10)"}


def _dias(d):
    return (date.today() - d).days if d else None


def pipeline_e_backlog(ig, itens):
    """Fila do marketing hoje (peças de Instagram ainda não postadas) e backlog mapeado (banco de briefings + território do Leo)."""
    rotulo = dict(ETAPAS)
    fila = []
    for it in ig:
        if it["match"] is not None or it["status"] == "PRONTO_PUBLICADO":
            continue
        desde = it.get("etapa_desde") or it.get("aprovado_em")
        fila.append({"codigo": it["codigo"], "titulo": it["titulo"], "tipo": it["tipo"], "etapa": it["status"], "etapa_txt": rotulo.get(it["status"], it["status"]),
                     "desde": desde.isoformat() if desde else None, "dias": _dias(desde), "fundo": it.get("fundo"), "espera": EM_ESPERA.get(it["codigo"] or "")})
    em_pauta = {i["codigo"] for i in itens if i["codigo"]}
    banco = ins.ler_banco_briefings()
    backlog = [b for b in banco if b["codigo"] not in em_pauta and ("Backlog" in b["status"] or "Briefing criado" in b["status"])]
    for b in backlog:
        f = b["formato"].lower()
        b["familia"] = "Blog" if "blog" in f else ("Instagram" if "instagram" in f or "rapidinha" in f else "Outros")
        b["status_txt"] = "Briefing criado" if "Briefing criado" in b["status"] else "Backlog"
        del b["status"]
    # territórios do Leo sem nenhum briefing no banco
    pauta = (pxp.MKT / "contexto" / "pauta.md").read_text(encoding="utf-8")
    territorios_banco = {b["territorio"].lower() for b in banco} | {t.lower() for _, tab in pxp._tabelas((pxp.MKT / "contexto" / "briefings.md").read_text(encoding="utf-8")) for t in []}
    leo = []
    for secao, linhas in pxp._tabelas(pauta):
        if "Backlog" in secao and "Leo" in secao:
            for r in linhas:
                nome = re.sub(r"\*+", "", r.get("Território", "")).split("—")[0].strip()
                if nome and not any(nome.lower() in t or t in nome.lower() for t in territorios_banco):
                    leo.append({"territorio": re.sub(r"\*+", "", r.get("Território", "")).strip(), "persona": r.get("Persona", ""), "gancho": (r.get("Gancho de Produto", "") or "")[:140]})
    return fila, backlog, leo


def checar_cores(posts, slots):
    """Confere a cor de fundo de cada slot PLANEJADO contra o post imediatamente anterior (real ou planejado):
    1) não repete a mesma cor em posts seguidos; 2) alternar claro e escuro. Sai um aviso por slot em `alerta_cor`.
    Slot atrasado e reservado ficam fora; foto e vídeo (sem fundo) não geram aviso."""
    claro, escuro = {"Warm Light", "Skin Nude"}, {"Deep Plum", "Carbon Black"}
    def tom(f):
        if not f:
            return None
        if "×" in f:
            return "escuro" if "Carbon Black" in f else None
        return "claro" if f in claro else ("escuro" if f in escuro else None)
    hoje = date.today().isoformat()
    seq = [(p["data"], 0, p.get("peca") or p["titulo"][:30], p.get("fundo"), None) for p in posts if p["data"] >= (date.today() - timedelta(days=21)).isoformat()]
    seq += [(s["data"], 1, s["titulo"][:48], s.get("fundo"), s) for s in slots if not s.get("reservado") and s["data"] >= hoje]
    seq.sort(key=lambda x: (x[0], x[1]))
    avisos = []
    for a, b in zip(seq, seq[1:]):
        if b[4] is None or not a[3] or not b[3]:
            continue
        msg = None
        if a[3] == b[3]:
            msg = f"mesma cor do anterior ({a[3]})"
        elif tom(a[3]) and tom(a[3]) == tom(b[3]):
            msg = f"{tom(b[3])} depois de {tom(a[3])} ({a[3]} → {b[3]}): alternar"
        if msg:
            b[4]["alerta_cor"] = msg
            avisos.append(f"{b[0][8:]}/{b[0][5:7]} {b[2]}: {msg}; anterior: {a[2]}")
    return avisos


def chave_tipo(tipo):
    """Normaliza o tipo da peça do marketing para a chave de formato da marca."""
    t = (tipo or "").lower()
    for k, chave in (("carrossel livre", "carrossel_livre"), ("por trás", "por_tras"), ("desatando", "mitos"), ("frase", "frase"),
                     ("bingo", "bingo"), ("produto", "produto"), ("vídeo", "video"), ("video", "video"), ("inspira", "inspiracao")):
        if k in t:
            return chave
    return None


def estatistica_por_formato(posts, desde="2026-06-01"):
    """Medianas por formato, só posts orgânicos desde o início do fluxo atual (n pequeno é hipótese)."""
    df = pd.DataFrame([p for p in posts if p["tipo_marca"] and not p["pago"] and p["data"] >= desde])
    saida = {}
    if df.empty:
        return saida
    for chave, g in df.groupby("tipo_marca"):
        saida[chave] = {"n": int(len(g)), "views": num(g["views"].median()), "envio": num(g["envio"].median(), 4),
                        "salvamento": num(g["salvamento"].median(), 4), "reposts": num(g["reposts"].median()), "seg_mil": num(g["seg_mil"].median(), 1)}
    return saida


def num(x, nd=None):
    if x is None or pd.isna(x):
        return None
    return round(float(x), nd) if nd is not None else int(x)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", default="2025-10-01")
    ap.add_argument("--out", default=str(SAIDA))
    args = ap.parse_args()

    plano = json.loads(PLANO.read_text(encoding="utf-8"))
    manual = plano.pop("classificacao_manual", {})

    # peças do marketing casadas com o perfil
    itens = pxp.itens_do_marketing()
    perfil = pxp.carregar_perfil()
    ig = [i for i in itens if i["instagram"]]
    for it in ig:
        pxp.classificar(it, perfil)
    pxp.resolver_conflitos(ig)
    hist_fundo = ins.fundos_do_historico()
    por_post = {}
    for it in ig:
        if it["match"] is not None:
            it["fundo"] = ins.fundo_da_peca(it["pasta"], hist_fundo.get(it["codigo"] or ""))
            it["categoria"] = ins.categoria_ciclo(it["tipo"], it["pasta"])
            por_post[it["match"].cd_midia] = it

    df = historico(args.desde)
    posts, tok, sem_capa = [], {}, 0
    for r in df.itertuples():
        codigo_url = r.ds_permalink.rstrip("/").split("/")[-1]
        it = por_post.get(r.cd_midia)
        tipo_marca = None
        if it:
            titulo = (f"{it['codigo']} · " if it["codigo"] else "") + it["titulo"]
            categoria, fundo, peca = it["categoria"], it["fundo"], it["codigo"] or "sem código"
            tipo_marca = chave_tipo(it["tipo"])
        elif codigo_url in manual:
            m = manual[codigo_url]
            titulo, categoria, fundo, peca = m["titulo"], m["categoria"], m.get("fundo"), "fora da pauta"
            tipo_marca = m.get("tipo_marca")
        else:
            titulo = primeira_linha(r.ds_legenda) or "(sem legenda)"
            categoria = "Vídeo" if r.ds_formato == "reel" else "Sem classificação"
            fundo, peca = None, "sem peça no marketing"
        jpg = capa_em_cache(r.cd_midia, tok)
        sem_capa += jpg is None
        posts.append({
            "capa": ("data:image/jpeg;base64," + base64.b64encode(jpg).decode()) if jpg else None,
            "tipo_marca": tipo_marca, "reposts": num(r.qt_reposts), "comentarios": num(r.qt_comentarios),
            "id": r.cd_midia, "data": r.dt_publicacao.isoformat(), "formato": r.ds_formato, "slides": num(r.qt_slides),
            "titulo": titulo, "categoria": categoria, "fundo": fundo, "peca": peca,
            "views": num(r.qt_views), "envio": num(r.pct_envio, 4), "salvamento": num(r.pct_salvamento, 4), "seg_mil": num(r.seg_mil, 1),
            "seguidores": num(r.qt_seguidores_ganhos), "visitas": num(r.qt_visitas_perfil),
            "pago": bool(r.fg_impulsionada), "link": r.ds_permalink,
        })

    # posts agendados na fila de publicação: moldura no slot; o que já foi ao ar e já foi extraído vira post real
    plano["plano"], virou_post = aplicar_agendamentos(plano["plano"], posts, agendamentos())
    # post publicado FORA do publicador (ex.: mLabs): o slot sai do plano se o código da peça já está num post real,
    # ou se há um post real exatamente no dia do slot (cadência de um post por slot)
    hoje_iso = date.today().isoformat()
    cod_no_ar = {p["peca"] for p in posts if str(p.get("peca", "")).startswith("C-")}
    datas_no_ar = {p["data"] for p in posts}
    restam, fora = [], []
    for s in plano["plano"]:
        m = re.match(r"(C-\d+)", s["titulo"])
        if s["data"] <= hoje_iso and ((m and m.group(1) in cod_no_ar) or s["data"] in datas_no_ar):
            fora.append(s["id"])
        else:
            restam.append(s)
    plano["plano"] = restam
    virou_post = list(virou_post) + fora
    n_ag = sum(1 for s in plano["plano"] if s.get("agendamento"))

    fila, backlog, leo = pipeline_e_backlog(ig, itens)
    by_code = {f["codigo"]: f for f in fila if f["codigo"]}
    for sl in plano["plano"]:
        m = re.match(r"(C-\d+)", sl["titulo"])
        sl["etapa_real"] = by_code.get(m.group(1)) if m else None
    alertas_cor = checar_cores(posts, plano["plano"])
    extracao = df["ts_extracao"].max()
    dados = {
        "meta": {"hoje": date.today().isoformat(), "extracao": extracao.strftime("%d/%m/%Y %H:%M UTC") if pd.notna(extracao) else "",
                 "versao": plano["versao"], "atualizado_em": plano["atualizado_em"], "desde": args.desde},
        "cores_alerta": alertas_cor, "posts": posts, "formatos_stats": estatistica_por_formato(posts), "fila": fila, "backlog": backlog, "leo_sem_briefing": leo, "etapas": [{"id": i, "nome": n} for i, n in ETAPAS],
        **{k: v for k, v in plano.items() if k not in ("nota",)},
    }
    html = TEMPLATE.read_text(encoding="utf-8")
    blob = json.dumps(dados, ensure_ascii=False).replace("</", "<\\/")
    assert "/*__DADOS__*/null" in html
    html = html.replace("/*__DADOS__*/null", blob, 1)
    Path(args.out).write_text(html, encoding="utf-8")
    atrasados = [f"{s['id']} ({s['data']}) {s['titulo'][:60]}" for s in plano["plano"]
                 if s["data"] < date.today().isoformat() and not (s.get("agendamento") and s["agendamento"].get("status") == "publicado")]
    if atrasados:
        print("REPROGRAMAR: slot(s) com data vencida e sem post no ar (saem da grade e vão para o bloco Atrasados):")
        for a in atrasados:
            print("  - " + a)
    for a in alertas_cor:
        print("COR: " + a)
    print(f"gravado em {args.out} ({len(posts)} posts reais, {sem_capa} sem capa, {len(plano['plano'])} slots planejados, "
          f"{n_ag} agendados na fila, {len(virou_post)} já no ar e tirados do plano {virou_post}, {len(html) // 1024} KB)")


if __name__ == "__main__":
    main()
