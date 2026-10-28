"""Confere se o grafo (graphify-out/) está defasado em relação aos documentos .md.

Somente leitura, local, sem modelo. Compara a data de cada .md (respeitando o
.graphifyignore) com a registrada em graphify-out/manifest.json.

Saída: uma linha de status e, se houver diferença, a lista de arquivos.
Código de saída: 0 = em dia, 1 = defasado ou sem documentos no grafo, 2 = sem grafo.
"""
import fnmatch
import json
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
MANIFESTO = RAIZ / "graphify-out" / "manifest.json"
IGNORE = RAIZ / ".graphifyignore"


def padroes_ignorados():
    if not IGNORE.exists():
        return []
    linhas = IGNORE.read_text(encoding="utf-8").splitlines()
    return [l.strip() for l in linhas if l.strip() and not l.lstrip().startswith("#")]


def ignorado(caminho, padroes):
    for p in padroes:
        if p.endswith("/"):
            if caminho.startswith(p):
                return True
        elif fnmatch.fnmatch(caminho, p):
            return True
    return False


def documentos():
    saida = subprocess.run(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard", "*.md"],
        cwd=RAIZ, capture_output=True, check=True,
    ).stdout.decode("utf-8")
    padroes = padroes_ignorados() + ["graphify-out/"]
    nomes = [n for n in saida.split("\0") if n]
    return sorted(n for n in nomes if not ignorado(n, padroes))


def main():
    if not MANIFESTO.exists():
        print("GRAFO AUSENTE: graphify-out/manifest.json não existe. Rodar /graphify .")
        return 2
    manifesto = json.loads(MANIFESTO.read_text(encoding="utf-8"))
    docs = documentos()
    if not any(k.endswith(".md") for k in manifesto):
        print(f"GRAFO SEM DOCUMENTOS: o grafo só tem código; {len(docs)} .md ainda não entraram. Rodar /graphify .")
        return 1
    novos, mudados = [], []
    for d in docs:
        reg = manifesto.get(d)
        if reg is None:
            novos.append(d)
        elif (RAIZ / d).stat().st_mtime > reg["mtime"] + 1:
            mudados.append(d)
    if not novos and not mudados:
        print(f"GRAFO EM DIA: {len(docs)} documentos conferidos.")
        return 0
    print(f"GRAFO DEFASADO: {len(novos)} novo(s), {len(mudados)} alterado(s). Rodar /graphify . --update")
    for d in novos:
        print(f"  novo: {d}")
    for d in mudados:
        print(f"  alterado: {d}")
    return 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
