"""Hook PreToolUse (Write): bloqueia briefing.md ou texto.md sem o carimbo de voz.

Regra do Hugo (03/11/2026): todo briefing e todo texto nascem com a voz carregada
(skill voz-shibari). O carimbo "**Voz carregada:**" no topo do arquivo registra o que
foi lido e o teste das quatro perguntas. Sem ele, a gravação é recusada.
"""
import json
import sys
from pathlib import PurePath

ARQUIVOS = {"briefing.md", "texto.md"}
CARIMBO = "Voz carregada:"

MENSAGEM = (
    "Gravação recusada: {nome} sem o carimbo de voz.\n"
    "Todo briefing e todo texto nascem com a voz (Hugo, 03/11/2026). Antes de gravar:\n"
    "1. Invocar a skill do agente que está escrevendo (agente-estrategista para briefing, "
    "agente-escritor para texto), com a ferramenta Skill, não de memória.\n"
    "2. Invocar a skill voz-shibari e ler sb_cerebro/02_voz/voz.md, tom.md, "
    "ajustes-recorrentes.md e as posições (P#) do tema em posicoes.md.\n"
    "3. Rodar o teste das quatro perguntas do voz.md no título, no ângulo e no gancho.\n"
    "4. Pôr no topo do arquivo a linha: **Voz carregada:** <arquivos e P# lidos> em "
    "DD/MM/AAAA; teste das 4 perguntas em <título, gancho...>: <passou / o que mudou>."
)


def main() -> int:
    try:
        dados = json.loads(sys.stdin.buffer.read().decode("utf-8", "replace"))
    except ValueError:
        return 0
    sys.stderr.reconfigure(encoding="utf-8")
    entrada = dados.get("tool_input") or {}
    nome = PurePath(str(entrada.get("file_path", ""))).name.lower()
    if nome not in ARQUIVOS:
        return 0
    if CARIMBO in str(entrada.get("content", "")):
        return 0
    sys.stderr.write(MENSAGEM.format(nome=nome))
    return 2


if __name__ == "__main__":
    sys.exit(main())
