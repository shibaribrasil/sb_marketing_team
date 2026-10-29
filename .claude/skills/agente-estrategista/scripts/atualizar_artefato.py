"""Regenera o artefato da sequência e diz se ele MUDOU desde a última publicação (para a tarefa agendada do Leo).

Roda o gerador (`gerar_artefato_sequencia.py`), calcula um hash do HTML sem os campos que mudam todo dia (data de hoje
e hora da extração) e compara com `estrategia/.hash-artefato`. Não publica nada e não altera plano, pauta nem banco.

Uso (interpretador do sb_relatorios):
  python atualizar_artefato.py                 # gera e imprime MUDOU ou IGUAL (exit 0 nos dois casos)
  python atualizar_artefato.py --gravar-hash   # depois de PUBLICAR, grava o hash como "última versão publicada"

Saída da primeira linha: `MUDOU` ou `IGUAL`. Depois de `MUDOU`, publicar `estrategia/sequencia-instagram.html` com a
ferramenta Artifact no mesmo link (https://claude.ai/artifact/DR9doaKArQHDPQPfJQFRj4) e rodar de novo com `--gravar-hash`.
"""
import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[3]
HTML = RAIZ / "estrategia" / "sequencia-instagram.html"
HASH = RAIZ / "estrategia" / ".hash-artefato"


def hash_normalizado():
    t = HTML.read_text(encoding="utf-8")
    t = re.sub(r'"hoje": "[^"]*"', '"hoje": ""', t)
    t = re.sub(r'"extracao": "[^"]*"', '"extracao": ""', t)
    return hashlib.sha256(t.encode("utf-8")).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gravar-hash", action="store_true", help="grava o hash atual (use depois de publicar)")
    args = ap.parse_args()
    if args.gravar_hash:
        HASH.write_text(hash_normalizado(), encoding="utf-8")
        print("hash gravado")
        return
    r = subprocess.run([sys.executable, str(AQUI / "gerar_artefato_sequencia.py")], capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0 or not HTML.exists():
        print("ERRO ao gerar o artefato")
        print((r.stderr or r.stdout)[-1500:])
        sys.exit(1)
    atual = hash_normalizado()
    anterior = HASH.read_text(encoding="utf-8").strip() if HASH.exists() else ""
    print("MUDOU" if atual != anterior else "IGUAL")
    print([l for l in r.stdout.splitlines() if l.startswith("gravado")][-1:] or "")
    linhas = r.stdout.splitlines()
    for l in linhas:
        if l.startswith("COR:"):
            print(l)
    import conferir_briefings
    print(chr(10).join(conferir_briefings.divergencias()) or "BRIEFING: briefings e plano mostram a mesma data e o mesmo fundo")
    if any(l.startswith("REPROGRAMAR") for l in linhas):
        i = [n for n, l in enumerate(linhas) if l.startswith("REPROGRAMAR")][0]
        print(chr(10).join(linhas[i:i + 12]))


if __name__ == "__main__":
    main()
