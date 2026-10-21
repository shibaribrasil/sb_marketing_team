#!/usr/bin/env python3
"""Sincroniza a fila prioritária do Instagram (planejamento do Hugo) com a pauta do marketing.

Fonte da verdade: sb_admin_team/planejamento/sequencia-instagram-plano.json (somente leitura).
Efeitos:
  1. regrava o bloco FILA-PRIORITARIA em contexto/pauta.md;
  2. compara com o último snapshot (contexto/fila-snapshot.json) e destaca o que mudou;
  3. cruza a fila com as linhas da pauta: peças sem linha, produção fora da fila, substituições, atrasos;
  4. registra as mudanças em contexto/fila-historico.md.

Uso:  python scripts/sincronizar_fila.py [--plano CAMINHO] [--check] [--resumo]
  --check   não grava nada, só imprime o resumo
  --resumo  imprime só o que exige atenção (usado pelo hook de início de sessão)
Vinculo manual: coloque [fila:P4] no título da linha da pauta para ligá-la ao slot P4 da fila.
Linhas com PAUSADA, ARQUIVADA ou [pausada] no título são ignoradas na checagem.
"""
import argparse
import json
import os
import re
import sys
from datetime import date, datetime

sys.stdout.reconfigure(encoding="utf-8")

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLANO_PADRAO = os.environ.get(
    "SB_PLANO_JSON",
    r"C:\Users\HTK1562\Documents\GitHub\sb_admin_team\planejamento\sequencia-instagram-plano.json",
)
PAUTA = os.path.join(RAIZ, "contexto", "pauta.md")
SNAPSHOT = os.path.join(RAIZ, "contexto", "fila-snapshot.json")
HISTORICO = os.path.join(RAIZ, "contexto", "fila-historico.md")
STATUS_IG = os.path.join(RAIZ, "contexto", "status-instagram.json")  # gerado por scripts/status_instagram.py
INI = "<!-- FILA-PRIORITARIA:INICIO (gerado por scripts/sincronizar_fila.py, não editar à mão) -->"
FIM = "<!-- FILA-PRIORITARIA:FIM -->"

# seções da pauta que representam peças em produção, da mais atrasada para a mais avançada
SECOES = [
    ("Briefing", "Briefing"),
    ("Em Produção", "Em Produção"),
    ("Design em Produção", "Design em Produção"),
    ("Aguardando Revisão", "Aguardando Revisão"),
    ("Pendente de Alteração no Canva", "Pendente no Canva"),
    ("Pronto - Aguardando Publicação", "Pronto, aguardando publicação"),
    ("Pronto - Agendado", "Agendado"),
    ("Pronto - Publicado", "Publicado"),
]
RANK = {nome: i for i, (_, nome) in enumerate(SECOES)}
PRONTOS = {"Pronto, aguardando publicação", "Agendado", "Publicado"}
COD = re.compile(r"C-\d{3}")
TAG = re.compile(r"\[fila:([A-Z]\d+)\]")


def dmy(iso):
    try:
        return datetime.strptime(iso, "%Y-%m-%d").strftime("%d/%m")
    except Exception:
        return iso or "—"


def ler_pauta():
    """Retorna lista de dicts {secao, titulo, linha} das linhas de tabela das seções de produção."""
    linhas = open(PAUTA, encoding="utf-8").read().split("\n")
    secao, achados = None, []
    for ln in linhas:
        if ln.startswith("## "):
            secao = None
            for chave, nome in SECOES:
                if chave in ln:
                    secao = nome
            continue
        if secao and ln.startswith("| ") and not ln.startswith("| Título") and not ln.startswith("|---"):
            titulo = ln.split("|")[1].strip()
            if titulo:
                achados.append({"secao": secao, "titulo": titulo, "linha": ln})
    return achados


def ignorada(titulo, codigos_reserva):
    t = titulo.upper()
    if "PAUSADA" in t or "ARQUIVADA" in t or "[PAUSADA]" in t:
        return True
    cods = COD.findall(titulo)
    return bool(cods) and all(c in codigos_reserva for c in cods)


def casar(plano_itens, linhas, codigos_reserva):
    """Liga cada slot às linhas da pauta (por tag [fila:ID] ou por código C-XXX do título)."""
    ligacao = {it["id"]: [] for it in plano_itens}
    usadas = set()
    for i, ln in enumerate(linhas):
        if ignorada(ln["titulo"], codigos_reserva):
            usadas.add(i)
            continue
        tag = TAG.search(ln["titulo"])
        if tag and tag.group(1) in ligacao:
            ligacao[tag.group(1)].append(ln)
            usadas.add(i)
    for i, ln in enumerate(linhas):
        if i in usadas:
            continue
        cods = COD.findall(ln["titulo"])
        for it in plano_itens:
            if cods and any(c in COD.findall(it["titulo"]) for c in cods) and not ligacao[it["id"]]:
                ligacao[it["id"]].append(ln)
                usadas.add(i)
                break
    return ligacao, usadas


def palavras_em_comum(a, b):
    def pal(t):
        t = re.sub(r"\[fila:[A-Z]\d+\]", "", t.split(" (")[0].lower())
        return {w for w in re.findall(r"[a-zà-ú]{5,}", t)}
    return pal(a) & pal(b)


def diff_snapshot(velho, novo):
    msgs = []
    for k, n in novo.items():
        v = velho.get(k)
        if v is None:
            msgs.append(f"entrou na fila: {n['titulo']} ({dmy(n['data'])})")
            continue
        if v["data"] != n["data"]:
            msgs.append(f"{n['titulo']}: data de postagem {dmy(v['data'])} -> {dmy(n['data'])}")
        if v["titulo"] != n["titulo"]:
            msgs.append(f"slot {k}: '{v['titulo']}' virou '{n['titulo']}'")
        if v.get("prazo") != n.get("prazo"):
            msgs.append(f"{n['titulo']}: prazo de entrega {dmy(v.get('prazo'))} -> {dmy(n.get('prazo'))}")
        if v.get("responsavel") != n.get("responsavel"):
            msgs.append(f"{n['titulo']}: responsável {v.get('responsavel')} -> {n.get('responsavel')}")
    for k, v in velho.items():
        if k not in novo:
            msgs.append(f"saiu da fila: {v['titulo']} ({dmy(v['data'])})")
    return msgs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plano", default=PLANO_PADRAO)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--resumo", action="store_true")
    args = ap.parse_args()

    if not os.path.exists(args.plano):
        print(f"[fila] plano não encontrado: {args.plano}. A fila da pauta não foi atualizada.")
        return 0
    plano = json.load(open(args.plano, encoding="utf-8"))
    itens = sorted(plano["plano"], key=lambda x: (x["data"], x["id"]))
    reserva = {r["codigo"] for r in plano.get("reserva", [])} | {r["codigo"] for r in plano.get("em_espera", [])}
    hoje = date.today()

    novo_snap = {
        it["id"]: {k: it.get(k) for k in ("data", "titulo", "formato", "prazo", "responsavel", "assunto", "arco")}
        for it in itens
    }
    velho = {}
    ultimas = []
    if os.path.exists(SNAPSHOT):
        s = json.load(open(SNAPSHOT, encoding="utf-8"))
        velho, ultimas = s.get("itens", {}), s.get("ultimas_mudancas", [])
    mudancas = diff_snapshot(velho, novo_snap) if velho else []
    if mudancas:
        ultimas = {"quando": datetime.now().strftime("%d/%m/%Y %H:%M"), "itens": mudancas}
    elif isinstance(ultimas, list):
        ultimas = {}

    linhas = ler_pauta()
    ligacao, usadas = casar(itens, linhas, reserva)
    ig = {"fila": {}, "posts": []}
    if os.path.exists(STATUS_IG):
        ig_raw = json.load(open(STATUS_IG, encoding="utf-8"))
        ig["fila"] = {f["id"]: f for f in ig_raw.get("fila", [])}
        ig["posts"] = ig_raw.get("posts", [])
        ig["gerado_em"] = ig_raw.get("gerado_em")

    alertas, tabela = [], []
    for it in itens:
        rows = ligacao[it["id"]]
        status = "sem linha na pauta"
        obs = []
        if it.get("reservado"):
            status = "reservado (Black Friday)"
        elif rows:
            melhor = max(rows, key=lambda r: RANK[r["secao"]])
            status = melhor["secao"]
            cods_fila = set(COD.findall(it["titulo"]))
            cods_pauta = set(c for r in rows for c in COD.findall(r["titulo"].split(" (")[0]))
            if cods_fila and cods_pauta and not (cods_fila & cods_pauta):
                obs.append(f"pauta tem {', '.join(sorted(cods_pauta))}; a fila ainda diz {', '.join(sorted(cods_fila))}")
                alertas.append(f"{dmy(it['data'])}: substituição não registrada na fila (fila {sorted(cods_fila)}, pauta {sorted(cods_pauta)})")
            elif not (cods_fila & cods_pauta) and not palavras_em_comum(it["titulo"], melhor["titulo"]):
                obs.append("a peça da pauta não bate com a da fila")
                alertas.append(f"{dmy(it['data'])}: a pauta tem '{melhor['titulo'].split(' (')[0][:60]}' no slot de '{it['titulo'].split(' (')[0][:55]}'; registrar a troca na fila")
        ag = ig["fila"].get(it["id"])
        if ag and ag["status"] != "cancelado":
            rotulo = {"agendado": "AGENDADO", "publicado": "NO AR", "aprovado": "aprovado, falta agendar", "rascunho": "na fila, sem aprovação",
                      "falhou": "FALHOU", "atrasado": "ATRASOU", "incerto": "conferir no perfil"}.get(ag["status"], ag["status"])
            obs.append(f"Instagram: {rotulo} {dmy(ag['data'])} {ag['hora']}")
            if ag["status"] in ("falhou", "atrasado", "incerto"):
                alertas.append(f"{dmy(it['data'])} {it['titulo'][:50]}: fila de publicação {ag['status']}")
            if ag["status"] in ("agendado", "publicado") and status not in ("Agendado", "Publicado"):
                alertas.append(f"{dmy(it['data'])} {it['titulo'][:50]}: está {rotulo.lower()} no Instagram ({dmy(ag['data'])} {ag['hora']}), mas a pauta mostra '{status}'; mover para {'Pronto - Agendado' if ag['status'] == 'agendado' else 'Pronto - Publicado'}")
                status = status + " (Instagram: " + rotulo.lower() + ")"
            else:
                status = status + f" (Instagram: {rotulo.lower()})"
        elif ig["posts"] and not it.get("reservado") and not it.get("extra"):
            no_ar = [p for p in ig["posts"] if p["data"] == it["data"]]
            if no_ar and status not in ("Publicado",):
                alertas.append(f"{dmy(it['data'])} {it['titulo'][:50]}: há post no ar nesse dia ({no_ar[0]['link']}); confirmar a postagem na pauta")
                obs.append("post no ar nesse dia")
        prazo = it.get("prazo")
        if prazo and not it.get("reservado") and status not in PRONTOS and "Instagram:" not in status:
            try:
                if datetime.strptime(prazo, "%Y-%m-%d").date() < hoje:
                    obs.append("ENTREGA ATRASADA")
                    alertas.append(f"{dmy(it['data'])} {it['titulo'][:60]}: entrega de {dmy(prazo)} atrasada ({status})")
            except ValueError:
                pass
        if status == "sem linha na pauta" and not it.get("reservado"):
            try:
                if (datetime.strptime(it["data"], "%Y-%m-%d").date() - hoje).days <= 14:
                    obs.append("abrir linha na pauta")
            except ValueError:
                pass
        tabela.append((it, status, "; ".join(obs)))

    fora = []
    for i, ln in enumerate(linhas):
        if i in usadas or ln["secao"] in PRONTOS:
            continue
        low = ln["linha"].lower()
        if "blog" in low:  # a fila cobre o Instagram
            continue
        fora.append(ln)
        alertas.append(f"produção fora da fila ({ln['secao']}): {ln['titulo'][:70]}")

    md = [INI, ""]
    md.append("## 🎯 Fila prioritária (sequência do Instagram)")
    md.append("")
    md.append(f"> **Regra:** esta fila tem prioridade sobre qualquer outra produção de Instagram. Fonte: sequência do Hugo, versão **{plano.get('versao', '?')}**, atualizada em **{plano.get('atualizado_em', '?')}**. Sincronizada em {datetime.now().strftime('%d/%m/%Y %H:%M')} por `scripts/sincronizar_fila.py`. Produção fora da fila só com autorização do Hugo. Arco só vale para peças de produto.")
    md.append("")
    if ultimas and ultimas.get("itens"):
        md.append(f"**Mudanças na fila ({ultimas['quando']}):**")
        for m in ultimas["itens"]:
            md.append(f"- {m}")
        md.append("")
    if alertas:
        md.append("**Atenção:**")
        for a in alertas:
            md.append(f"- {a}")
        md.append("")
    if ig.get("gerado_em"):
        md.append(f"> Status do Instagram (no ar e agendado) lido de `contexto/status-instagram.json`, gerado em {ig['gerado_em']}. Atualizar: `python scripts/status_instagram.py`.")
    else:
        md.append("> Status do Instagram (no ar e agendado) ainda não carregado: rodar `python scripts/status_instagram.py`.")
    md.append("")
    md.append("| Posta em | Peça | Formato | Assunto | Arco | Entrega | Quem | Status na pauta | Alerta |")
    md.append("|---|---|---|---|---|---|---|---|---|")
    for it, status, obs in tabela:
        extra = " (extra)" if it.get("extra") else ""
        md.append(
            f"| {dmy(it['data'])}{extra} | {it['titulo']} | {it.get('formato', '')} | {it.get('assunto', '')} | {it.get('arco') or '—'} | {dmy(it.get('prazo'))} | {it.get('responsavel', '')} | {status} | {obs} |"
        )
    md.append("")
    md.append("**Ordens de produção por pessoa:**")
    for o in plano.get("ordens_producao", []):
        md.append(f"- **{o['para']}** ({o.get('prazo', '')}): {o['o_que']}")
    md.append("")
    md.append(FIM)
    bloco = "\n".join(md)

    if args.resumo:
        print(f"[fila {plano.get('versao', '?')} de {plano.get('atualizado_em', '?')}] próximos posts:")
        proximos = [t for t in tabela if t[0]["data"] >= hoje.isoformat()][:4]
        for it, status, obs in proximos:
            print(f"  {dmy(it['data'])} {it['titulo'][:70]} [{status}] {obs}")
        if mudancas:
            print("MUDANÇAS NA FILA desde a última sincronização:")
            for m in mudancas:
                print(f"  - {m}")
        for a in alertas:
            print(f"  ! {a}")
        print("A produção segue a fila de contexto/pauta.md (bloco FILA-PRIORITARIA). Mudança de fila: avisar o Hugo e atualizar a pauta.")
    else:
        print(bloco)

    if args.check:
        return 0

    pauta = open(PAUTA, encoding="utf-8").read()
    if INI in pauta and FIM in pauta:
        a, b = pauta.index(INI), pauta.index(FIM) + len(FIM)
        pauta = pauta[:a] + bloco + pauta[b:]
    else:
        alvo = "## Pipeline de Produção de Conteúdo Orgânico"
        pauta = pauta.replace(alvo, bloco + "\n\n---\n\n" + alvo, 1)
    open(PAUTA, "w", encoding="utf-8").write(pauta)

    json.dump({"versao": plano.get("versao"), "atualizado_em": plano.get("atualizado_em"), "itens": novo_snap, "ultimas_mudancas": ultimas},
              open(SNAPSHOT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if mudancas:
        novo = not os.path.exists(HISTORICO)
        with open(HISTORICO, "a", encoding="utf-8") as f:
            if novo:
                f.write("# Histórico de mudanças na fila prioritária\n\n> Registro automático de `scripts/sincronizar_fila.py`.\n\n")
            f.write(f"## {datetime.now().strftime('%d/%m/%Y %H:%M')} (fila v{plano.get('versao', '?')})\n")
            for m in mudancas:
                f.write(f"- {m}\n")
            f.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
