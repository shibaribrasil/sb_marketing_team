#!/usr/bin/env python3
"""Ponte entre a Mari (marketing) e a skill de Instagram (sb_admin_team): o que está NO AR e o que está AGENDADO.

Somente leitura. Usa o Python do venv `sb_relatorios` (que tem o cliente do BigQuery) para consultar:
  - `dbt_dw_az.tb_instagram_midia`        -> posts publicados nos últimos 45 dias (data, formato, link, views, envio)
  - `raw_instagram.fila_publicacao`        -> posts agendados/aprovados/falhos na fila de publicação (id do slot P1, P2...)
Grava `contexto/status-instagram.json` e `contexto/status-instagram.md`, que o `sincronizar_fila.py` lê para marcar
cada slot da fila como no ar, agendado ou pendente. Se o BigQuery estiver indisponível, mantém o último arquivo e avisa.

Uso:  python scripts/status_instagram.py [--resumo]
"""
import argparse
import json
import os
import subprocess
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = os.environ.get("SB_VENV_PYTHON", r"C:\Users\HTK1562\venvs\sb_relatorios\Scripts\python.exe")
OUT_JSON = os.path.join(RAIZ, "contexto", "status-instagram.json")
OUT_MD = os.path.join(RAIZ, "contexto", "status-instagram.md")

CODIGO = r'''
import json, sys, warnings
sys.path.insert(0, "C:/Users/HTK1562/Documents/GitHub/sb_admin_team/.claude/skills/analista-de-dados/scripts")
warnings.filterwarnings("ignore")
from zoneinfo import ZoneInfo
import pandas as pd
from bq_client import get_client
cli = get_client("us-east4")
saida = {"posts": [], "fila": [], "avisos": []}
df = cli.query("""
  SELECT cd_midia, ds_formato, dt_publicacao, qt_views, pct_envio, qt_reposts, ds_permalink, ds_legenda, ts_extracao
    FROM `igneous-sandbox-381622.dbt_dw_az.tb_instagram_midia`
   WHERE NOT fg_story AND dt_publicacao >= DATE_SUB(CURRENT_DATE('America/Sao_Paulo'), INTERVAL 45 DAY)
   ORDER BY dt_publicacao DESC""").to_dataframe()
for r in df.itertuples():
    leg = (r.ds_legenda or "").strip().splitlines()
    saida["posts"].append({"data": str(r.dt_publicacao)[:10], "formato": r.ds_formato, "views": None if pd.isna(r.qt_views) else int(r.qt_views),
                           "envio": None if pd.isna(r.pct_envio) else float(r.pct_envio), "reposts": None if pd.isna(r.qt_reposts) else int(r.qt_reposts),
                           "link": r.ds_permalink, "primeira_linha": (leg[0][:110] if leg else "")})
saida["ultima_extracao"] = str(df["ts_extracao"].max()) if len(df) else None
try:
    f = cli.query("""SELECT id, status, data_hora, permalink, erro FROM `igneous-sandbox-381622.raw_instagram.fila_publicacao`
                      WHERE status != 'cancelado' ORDER BY data_hora""").to_dataframe()
    for r in f.itertuples():
        q = pd.Timestamp(r.data_hora).tz_convert(ZoneInfo("America/Sao_Paulo"))
        saida["fila"].append({"id": r.id, "status": r.status, "data": q.date().isoformat(), "hora": q.strftime("%H:%M"),
                              "permalink": None if pd.isna(r.permalink) else r.permalink, "erro": None if pd.isna(r.erro) else r.erro})
except Exception as exc:
    saida["avisos"].append("fila de publicação indisponível: " + exc.__class__.__name__)
print("@@JSON@@" + json.dumps(saida, ensure_ascii=False))
'''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--resumo", action="store_true")
    args = ap.parse_args()
    if not os.path.exists(PY):
        print("[status-instagram] venv do BigQuery não encontrado; mantendo o último status.")
        return 0
    try:
        r = subprocess.run([PY, "-c", CODIGO], capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120,
                           env={**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"})
    except Exception as exc:
        print(f"[status-instagram] falha ao consultar: {exc.__class__.__name__}; mantendo o último status.")
        return 0
    marca = "@@JSON@@"
    if r.returncode != 0 or not r.stdout or marca not in r.stdout:
        print("[status-instagram] consulta ao BigQuery falhou; mantendo o último status.")
        print((r.stderr or "")[-400:])
        return 0
    dados = json.loads(r.stdout.split(marca, 1)[1])
    dados["gerado_em"] = datetime.now().strftime("%d/%m/%Y %H:%M")
    json.dump(dados, open(OUT_JSON, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    md = [f"# Status do Instagram (gerado em {dados['gerado_em']} por scripts/status_instagram.py)", "",
          "> Somente leitura, vindo da skill de Instagram (BigQuery). A pauta NÃO é a fonte de verdade de \"postou\": o perfil é.",
          f"> Última extração do perfil: {dados.get('ultima_extracao')}. A extração roda 3x por dia; um post de poucas horas pode não aparecer ainda.", ""]
    if dados.get("avisos"):
        md += [f"> Aviso: {a}" for a in dados["avisos"]] + [""]
    md += ["## Agendados e na fila de publicação", ""]
    fila = [f for f in dados["fila"] if f["status"] != "publicado"]
    md += (["| Slot | Status | Dia | Hora | Obs |", "|---|---|---|---|---|"] +
           [f"| {f['id']} | {f['status']} | {f['data']} | {f['hora']} | {f['erro'] or ''} |" for f in fila]) if fila else ["Nenhum post agendado na fila."]
    md += ["", "## No ar nos últimos 45 dias", "", "| Data | Formato | Views | Envio | Repostagens | Primeira linha |", "|---|---|---|---|---|---|"]
    for p in dados["posts"]:
        envio = f"{p['envio'] * 100:.1f}%" if p["envio"] is not None else "—"
        md.append(f"| {p['data']} | {p['formato']} | {p['views'] if p['views'] is not None else '—'} | {envio} | {p['reposts'] if p['reposts'] is not None else '—'} | {p['primeira_linha']} |")
    open(OUT_MD, "w", encoding="utf-8").write("\n".join(md) + "\n")
    if args.resumo:
        print(f"[status-instagram] {len(dados['posts'])} posts no ar (45 dias), {len(fila)} na fila de publicação.")
    else:
        print("\n".join(md))
    return 0


if __name__ == "__main__":
    sys.exit(main())
