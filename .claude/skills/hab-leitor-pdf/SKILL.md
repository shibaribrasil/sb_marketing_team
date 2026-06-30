---
name: hab-leitor-pdf
description: Habilidade de leitura e extração de texto de arquivos PDF. Carregar esta skill quando precisar ler o conteúdo de um PDF para usar como fonte de dados em qualquer tarefa do projeto. Verifica automaticamente se já existe um markdown espelho — se sim, usa ele; se não, extrai do PDF, formata com hierarquia de seções e cria o markdown.
---

# Habilidade — Leitor de PDF

Esta habilidade permite extrair texto de qualquer arquivo PDF do projeto com formatação estruturada. Sempre que um PDF precisar ser consultado, este protocolo é executado primeiro — nunca acessar o PDF diretamente sem verificar se já existe um markdown espelho.

## Protocolo de Leitura (Executar Sempre)

### Passo 1 — Verificar se o markdown espelho existe

O markdown espelho de um PDF tem o mesmo nome do arquivo, com extensão `.md`, na mesma pasta.

Exemplo:
```
assets/docs/Guia da marca - Shibari Brasil.pdf
assets/docs/Guia da marca - Shibari Brasil.md   ← espelho
```

Se o arquivo `.md` existir → **usar o markdown, não tocar no PDF**.
Se não existir → seguir para o Passo 2.

### Passo 2 — Garantir o pdfplumber

```bash
python -c "import pdfplumber; print('ok')" 2>/dev/null || python -m pip install pdfplumber -q
```

### Passo 3 — Extrair texto com informações de fonte

Usar o script abaixo para extrair o texto página por página com tamanho de fonte de cada linha. Isso permite identificar títulos, subtítulos e corpo de texto:

```bash
python -c "
import pdfplumber, sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

path = r'CAMINHO_DO_PDF'

with pdfplumber.open(path) as pdf:
    total = len(pdf.pages)
    for i, page in enumerate(pdf.pages):
        print(f'##PAGE## {i+1} of {total}')
        words = page.extract_words(extra_attrs=['fontname','size'])
        if not words:
            print('[pagina sem texto extraivel]')
            continue
        # Agrupar palavras em linhas por posição vertical (tolerância de 3px)
        lines = []
        current_line = []
        current_top = None
        for w in words:
            top = round(w['top'])
            if current_top is None or abs(top - current_top) <= 3:
                current_line.append(w)
                current_top = top
            else:
                if current_line:
                    lines.append(current_line)
                current_line = [w]
                current_top = top
        if current_line:
            lines.append(current_line)
        for line in lines:
            text = ' '.join(w['text'] for w in line)
            size = round(max(w['size'] for w in line), 1)
            print(f'##SIZE:{size}## {text}')
"
```

### Passo 4 — Aplicar formatação markdown

Com base nos tamanhos de fonte extraídos, aplicar hierarquia:

1. **Identificar os tamanhos distintos** presentes no documento e classificá-los:
   - Tamanho maior (títulos de seção) → `#`
   - Tamanho intermediário (subtítulos) → `##` ou `###`
   - Tamanho padrão/corpo → parágrafo normal

2. **Anotar o número de página em cada título** — todo heading (`#`, `##`, `###`) deve terminar com `*(p. N)*` indicando a página do PDF onde a seção começa. Exemplo: `### tom de voz *(p. 3)*`. Isso permite que qualquer consulta ao markdown referencie a página exata sem reabrir o PDF.

3. **Filtrar repetições de cabeçalho de página** — linhas que se repetem identicamente em múltiplas páginas (ex: nome da marca + nome do documento) devem ser removidas do corpo do texto. Capítulos que continuam em páginas seguintes com o mesmo título não devem ter o título repetido.

4. **Identificar listas** — quando linhas consecutivas de corpo de texto forem curtas e paralelas (3+ itens), formatar como lista markdown (`-`).

5. **Separar páginas** com `---` apenas quando houver mudança de capítulo ou seção relevante. Não colocar `---` entre cada página se o conteúdo for contínuo.

### Passo 5 — Salvar o markdown espelho

Salvar o arquivo `.md` com o mesmo nome do PDF, na mesma pasta, com este cabeçalho:

```markdown
# [Nome do PDF sem extensão]

> Arquivo gerado automaticamente a partir de [nome-do-arquivo.pdf]. Não editar manualmente — use `Reler PDF: [nome]` para regerá-lo.

---
```

Seguido do conteúdo formatado com hierarquia de títulos, subtítulos, listas e separadores de seção.

### Passo 6 — Tratar problemas de extração

- Se o texto vier vazio ou ilegível em todas as páginas → avisar o usuário que o PDF pode ser baseado em imagem (escaneado) e precisaria de OCR.
- Se o texto vier com quebras de linha estranhas ou espaçamento irregular → normalizar ao interpretar, comum em PDFs exportados de ferramentas de design.
- Usar o conteúdo como fonte de dados para a tarefa em andamento — não apresentar o texto bruto ao usuário a menos que ele peça.
- Sempre indicar de qual seção/página cada informação foi extraída quando isso for relevante.

## Quando Reler o PDF

O markdown espelho só deve ser regerado se o usuário pedir explicitamente:
```
Reler PDF: [nome do arquivo]
```
Nesse caso, repetir o protocolo do zero e sobrescrever o markdown existente.

## Regras

- Nunca inventar ou completar informações que não estejam no PDF.
- Se uma seção estiver incompleta ou cortada, perguntar ao usuário antes de interpretar.
- O markdown espelho é fonte de dados neutra e navegável — fiel ao conteúdo, estruturada para consulta.
- Nunca editar o markdown espelho manualmente — ele é sempre gerado ou regerado pela skill.
