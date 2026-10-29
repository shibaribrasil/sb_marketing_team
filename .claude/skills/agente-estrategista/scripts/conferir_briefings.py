"""Confere se os briefings (Drive) mostram o mesmo que o plano da sequência: data da postagem e fundo.

Liga cada slot do plano ao briefing pela pauta (`[fila:Pn]` + caminho `conteudos/.../briefing.md`). Somente leitura.
Uso: python conferir_briefings.py   (imprime `BRIEFING:` por divergência; sai com código 0).
"""
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]
DRIVE = Path(r"G:\Meu Drive\SB Audiovisual\03_CONTEUDO")


def divergencias():
    plano = json.loads((RAIZ / "estrategia" / "sequencia-instagram-plano.json").read_text(encoding="utf-8"))
    slots = {s["id"]: s for s in plano["plano"]}
    saida = []
    if not DRIVE.exists():
        return ["BRIEFING: pasta do Drive não abre (G:); conferência não feita"]
    for linha in (RAIZ / "contexto" / "pauta.md").read_text(encoding="utf-8").splitlines():
        m_id = re.search(r"\[fila:((?:P|X)\d+)\]", linha)
        m_arq = re.search(r"`conteudos/([^`]+?/briefing\.md)`", linha)
        if not (m_id and m_arq) or m_id.group(1) not in slots:
            continue
        s, arq = slots[m_id.group(1)], DRIVE / m_arq.group(1)
        if not arq.exists():
            continue
        t = arq.read_text(encoding="utf-8")
        m_data = re.search(r"\*\*Posta em:\*\*\s*(\d{2})/(\d{2})/(\d{4})", t)
        if m_data:
            d = f"{m_data.group(3)}-{m_data.group(2)}-{m_data.group(1)}"
            if d != s["data"]:
                saida.append(f"BRIEFING: {s['titulo'][:40]}: briefing posta em {d}, plano diz {s['data']} ({arq.parent.name})")
        m_f = re.search(r"\*\*Fundo(?: sugerido)?:\*\*\s*([A-Za-z ]+?)\s*(?:`|\(|$)", t, re.M)
        if m_f and s.get("fundo") and m_f.group(1).strip() != s["fundo"]:
            saida.append(f"BRIEFING: {s['titulo'][:40]}: briefing sugere fundo {m_f.group(1).strip()}, plano diz {s['fundo']} ({arq.parent.name})")
    return saida


if __name__ == "__main__":
    out = divergencias()
    print("\n".join(out) if out else "BRIEFING: briefings e plano mostram a mesma data e o mesmo fundo")
