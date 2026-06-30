---
name: hab-criador-produto
description: Use esta skill SEMPRE que for criar um produto novo do zero ou atualizar informações de um produto existente na Shibari Brasil. Cobre boas práticas de descrição para e-commerce, SEO de produto, formatação própria da SB, criação de código interno, EAN-13 e checklist de publicação. Deve ser carregada em paralelo com a skill hab-produtor-textual ao redigir qualquer texto de produto.
---

# Manual de Criação de Produtos — Shibari Brasil

Este manual define as regras de criação, estruturação e publicação de produtos da Shibari Brasil. Ele é dividido em capítulos: os fundamentos gerais de e-commerce e SEO, o formato de descrição próprio da marca, as regras técnicas de cadastro (código interno, EAN-13) e o checklist de entrega.

Ao criar ou atualizar um produto, carregar este manual **em conjunto com a skill `hab-produtor-textual`**. As regras de linguagem, lista negra de vocabulário e antirrobô da hab-produtor-textual se aplicam integralmente ao texto de produto.

---

## Capítulo 1 — Boas Práticas de Descrição para E-commerce

> Regras de produção aplicadas a todos os produtos da SB. Camada base — as regras do Capítulo 2 complementam com o formato próprio da marca.

---

### 1.1 Estrutura obrigatória

Toda descrição deve ter, nessa ordem:

1. Título
2. Subtítulo / frase de destaque
3. Parágrafo de abertura
4. Lista de benefícios (bullets)
5. Especificações técnicas
6. CTA final
7. Informações de envio, garantia e suporte

---

### 1.2 Título

**Fazer:**
- Nome do produto + variação relevante (espessura, comprimento, modelo)
- Palavra-chave principal no início ou muito próxima ao começo
- Destacar diferenciais quando couber: exclusivo, artesanal, tratado, vegano
- Manter entre 50 e 70 caracteres (evita corte nos resultados do Google)

**Não fazer:**
- Títulos vagos ou genéricos ("Corda Especial", "Kit Completo")
- Criatividade que prejudique clareza — o título deve informar, não encantar

---

### 1.3 Parágrafo de Abertura

**Fazer:**
- Palavra-chave principal na primeira ou segunda frase
- Começar com tom emocional ou sensorial — coloca o cliente dentro da experiência
- 2 a 4 frases

**Não fazer:**
- Começar com lista de características técnicas
- Abrir com contexto histórico ou explicação genérica do produto

---

### 1.4 Benefícios vs. Características

Para cada característica técnica, perguntar: *"e daí? o que isso significa para quem usa?"* — essa resposta é o benefício.

| ✗ Característica (fraco) | ✓ Benefício (forte) |
|---|---|
| Material: 100% juta natural | Toque natural que aquece e amacia com o uso |
| Finalização com óleo vegetal | Chega pronta pra usar, sem tratamento extra |
| Ponta com nó de overhand | Não desfia, não machuca, não precisa de acabamento |

**Fazer:**
- 3 a 6 bullets
- Benefícios antes das especificações técnicas
- Máximo 1 frase por bullet

**Não fazer:**
- Listar apenas características sem traduzir em benefício

---

### 1.5 Especificações Técnicas

**Fazer:**
- Lista ou tabela — nunca parágrafo corrido
- Incluir: dimensões, material, peso, acabamento, padrão de fabricação, certificações relevantes
- Unidades padronizadas (mm, m, g, cm)
- Ser exaustivo — o cliente não pode ficar com dúvida não respondida na página

---

### 1.6 SEO — Palavras-chave

**Fazer:**
- Densidade entre 0,5% e 1,5% da keyword principal no texto total
- Keyword presente em: título, primeiro parágrafo, pelo menos um subtítulo, alt text de imagem, meta title e meta description
- Usar palavras-chave de cauda longa além da principal (ex: "corda de juta tratada para shibari", "corda para bondage asanawa")
- Extensão mínima: 250 palavras; produtos complexos ou alto valor: 400 a 800 palavras

**Não fazer:**
- Keyword stuffing — repetição forçada que prejudica leitura e pode penalizar no Google
- Copiar descrição do fornecedor ou de concorrente — conteúdo duplicado é penalizado

---

### 1.7 Meta Title e Meta Description

**Meta Title:**
- Keyword principal + nome da loja quando couber
- Máximo **65 caracteres**

**Meta Description:**
- Keyword + benefício principal + convite ao clique
- Escrever como CTA, não como resumo técnico
- Entre **140 e 160 caracteres**

---

### 1.8 Imagens

**Fazer:**
- Nomear o arquivo com keyword (ex: `corda-juta-6mm-shibari-brasil.webp`)
- Formato preferencial: WebP; PNG aceito
- Peso máximo: **< 200KB** — comprimir antes de publicar (TinyPNG ou equivalente)
- Alt text com keyword secundária (ex: `corda de juta tratada 6mm shibari brasil asanawa`)

**Não fazer:**
- Deixar alt text vazio
- Publicar imagens acima de 200KB sem compressão

---

### 1.9 Linguagem e Tom

**Fazer:**
- Voz ativa e verbos diretos (use, experimente, descubra, garanta)
- Frases curtas — especialmente para mobile
- Palavras emocionais com moderação para conectar características a benefícios: conforto, exclusividade, segurança, durabilidade
- Adaptar o tom ao produto: sensorial/emocional para produtos de experiência; objetivo/técnico para produtos com specs complexas

**Não fazer:**
- Voz passiva
- Frases longas e cheias de subordinadas
- Palavras da lista negra da `hab-produtor-textual`

---

### 1.10 CTA

**Fazer:**
- Verbos no imperativo com foco no benefício: "Garanta a sua", "Adicione ao carrinho"
- Reforçar com informação de suporte: prazo, frete, garantia de troca
- Na SB: o bloco fixo `📦 💌 🤝` cumpre essa função — sempre ao final

**Não fazer:**
- Terminar a descrição sem direcionar o cliente para a próxima ação

---

## Capítulo 2 — Formato de Descrição Padrão da Shibari Brasil

> O formato ativo é o `site-descricao-produto` (formato 7), registrado em `contexto/formatos-conteudo.md`. Consultar esse arquivo para a estrutura completa e o checklist antes de redigir qualquer descrição.

**Estrutura vigente (desde 19/06/2026):**
1. Título (H1) — keyword no início, 50–70 chars, sem emoji
2. Linha de posicionamento — factual, sem apelativo, sem emoji
3. Parágrafo de abertura — sensorial/funcional, 2–3 frases curtas
4. Parágrafo técnico — material, processo, padrão, 2–3 frases curtas
5. H2 de benefícios (com keyword) — 4–6 bullets, característica → benefício
6. H2 especificações técnicas — lista objetiva
7. H2 cuidados com o produto — 3–5 bullets
8. H2 por que comprar na Shibari Brasil — diferenciais da loja
9. CTA — 1 frase com verbo de ação
10. Bloco operacional — emoji ao final da linha, não no início
11. Meta Title (máx. 65 chars)
12. Meta Description (140–160 chars)

**Formato anterior (arquivado):** `site-descricao-produto-old` (formato 6) — referência em `assets/docs/Padrão de Descrição de Produtos - SB.md`

---

## Capítulo 3 — Código Interno do Produto

> ⏳ **A ser definido com Hugo.** Este capítulo cobrirá as regras de criação e formatação do código interno de identificação de cada produto no catálogo da Shibari Brasil.

Pontos a definir:
- Estrutura do código (prefixo de categoria, número sequencial, variações)
- Onde o código aparece (sistema, planilha, página do produto)
- Regras para kits e variações de um mesmo produto
- Como atualizar sem quebrar referências existentes

---

## Capítulo 4 — EAN-13

> ⏳ **A ser definido com Hugo.** Este capítulo cobrirá as regras de uso, geração e registro de códigos EAN-13 nos produtos da Shibari Brasil.

Pontos a definir:
- Quando o EAN-13 é obrigatório vs. opcional
- Processo de geração ou obtenção do código
- Como registrar no sistema da loja
- Regras para variações (cor, tamanho) do mesmo produto

---

## Capítulo 5 — Checklist de Criação e Publicação

### Para produtos novos (do zero):

- [ ] Nome do produto definido e aprovado pelo Hugo
- [ ] Palavra-chave principal pesquisada e definida
- [ ] Código interno criado (Capítulo 3)
- [ ] EAN-13 obtido ou registrado (Capítulo 4)
- [ ] Formato de descrição consultado (`contexto/formatos-conteudo.md`)
- [ ] Texto redigido com `hab-produtor-textual` ativa
- [ ] Título com palavra-chave (máx. 65 caracteres para SEO)
- [ ] Parágrafo de abertura com benefício + keyword na primeira frase
- [ ] Benefícios em bullets (mínimo 3)
- [ ] Especificações técnicas completas (dimensões, material, acabamento)
- [ ] Recomendações de cuidado
- [ ] Bloco "Por que comprar com a Shibari Brasil?"
- [ ] 3 destaques fixos de operação ao final
- [ ] Meta title escrito (máx. 65 caracteres)
- [ ] Meta description escrita (140–160 caracteres, com CTA)
- [ ] Imagens: nomeadas com keyword, peso < 200KB, alt text preenchido
- [ ] Nenhuma palavra da lista negra da `hab-produtor-textual`
- [ ] Revisão mobile (frases curtas, bullets visíveis)

### Para atualização de produto existente:

- [ ] Identificar o produto pelo código interno
- [ ] Verificar qual informação está desatualizada (preço, material, dimensão, descrição)
- [ ] Atualizar apenas os campos afetados — não reescrever do zero sem necessidade
- [ ] Conferir se a palavra-chave principal permanece presente após a edição
- [ ] Atualizar meta title e meta description se o título mudou
- [ ] Registrar a atualização no histórico de produto (quando houver)
