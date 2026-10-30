# Formatos de Conteúdo da Shibari Brasil

Este arquivo é o índice dos formatos cadastrados. Cada formato tem seu próprio arquivo em `contexto/formatos/`.

## Regra geral: tema legível no grid (Hugo, 30/10/2026)

Vale para **todo formato temático** (que trata de uma prática, material ou fetiche específico): Post de 5 motivos, Por Trás do Desejo, Carrossel Livre, Desatando Mitos, Post de Produto, Post de Foto com texto. Quem passa pelo perfil precisa identificar o assunto **pela miniatura do grid, sem abrir o post**.

- O **nome do tema** aparece escrito no post único ou na **capa** do carrossel, como as pessoas o chamam e buscam ("wax play"). Metáfora, foto ou ilustração reforçam, mas não substituem o nome.
- **Corpo de título** (110–150px no canvas 1080, nunca abaixo de 96px). Nunca só no subtítulo, num rótulo, num texto vertical, no rodapé ou na legenda.
- **Contraste alto**; sobre foto, só em área calma. Dentro da margem de 80px (o grid corta as laterais em 3:4).
- **Teste da miniatura:** reduzir a peça a ~130px de largura. Se o tema não se lê, volta para a Julia (texto da capa) ou para a Bia (arte).

Regra completa: `sb_cerebro/03_visual/gramatica-visual.md`, seção "Tema legível no grid".

## Regra geral: composição do post único (Hugo, 30/10/2026)

Vale para todo post, e pesa mais nos densos (lista, 5 motivos). Regra completa: `sb_cerebro/03_visual/gramatica-visual.md`, seção "Composição do post único".

- **Ordem de leitura única:** tema (título) → gancho (subtítulo) → conteúdo → fecho → assinatura, de cima para baixo. O tema é o maior elemento.
- **Respiro:** margem de **108px nos quatro lados** para todo texto, rótulo, contador e assinatura (medida nos posts do Canva). Fundo de card ou pílula pode ir até 80px, com o texto dentro voltando para ~124–132px. 64px livres antes da assinatura. Só decoração sangra; texto nunca.
- **Legibilidade:** título 110px, título de item 38px, apoio 32px (explicação curta de item 28px), rodapé 26px. Item = título de até três palavras + uma linha. Se não cabe, corta texto (Julia), não corpo nem margem (Bia).

## Como Adicionar um Novo Formato

Quando o usuário solicitar um tipo de conteúdo ainda não registrado:
1. Perguntar ao usuário: objetivo do formato, plataforma, tamanho ideal e CTA esperado.
2. Criar um novo arquivo em `contexto/formatos/[slug-do-formato].md` com as especificações levantadas.
3. Adicionar o novo tipo à lista abaixo e à lista de `diretrizes.md`.
4. Só então gerar o conteúdo.

## Modelo de Arquivo (usar como base ao criar um novo formato)

```markdown
# [Nome do Formato]

**Objetivo:** [Para que serve este formato e qual resultado ele deve gerar]

**Plataforma:** [Onde será publicado]

**Regras de escrita:** [Skills e capítulos obrigatórios]

---

### Estrutura obrigatória de entrega

**1. [Elemento 1]**
[Descrição]

**2. [Elemento 2]**
[Descrição]

---

### Direção visual (referência para a Bia)

- **Template no Canva:** [nome e ID]
- **Fundo recomendado:** [cor]
- **Dimensões:** [px]

---

### Checklist de entrega

- [ ] [Item 1]
- [ ] [Item 2]
```

---

## Formatos Cadastrados

1. [Post para Blog](formatos/post-para-blog.md)
2. [Post de Frase](formatos/post-de-frase.md) — layout "tarja e etiqueta" desde 30/10/2026; modelo no Canva "Post Frase - Modelo 2"
3. [Post Por Trás do Desejo](formatos/post-por-tras-do-desejo.md)
4. [Post Inspiração de Amarração](formatos/post-inspiracao-de-amarracao.md)
5. [Carrossel Livre](formatos/carrossel-livre.md)
6 e 7. (Os formatos de descrição de produto saíram do marketing em 27/10/2026: são do cadastrador, no `sb_admin_team`. A numeração dos demais formatos não muda.)
8. [Post Desatando Mitos](formatos/post-desatando-mitos.md)
9. [Post de Foto (Instagram)](formatos/post-de-foto.md)
10. [Post de Produto (Instagram)](formatos/post-de-produto.md)
11. [Instagram Vídeo](formatos/instagram-video.md)
12. [Post de Bingo (Instagram)](formatos/post-de-bingo.md) — post casual de identificação: cartela 3×3 com 9 situações; eventual, sob demanda
13. [Post de Duelo (Instagram)](formatos/post-de-duelo.md) — post casual de identificação: duas colunas "time A × time B" com 4 itens paralelos; eventual, em teste
14. [Post de 5 Motivos (Instagram)](formatos/post-5-motivos.md) — post único: tema grande no topo, cinco motivos de uma linha com explicação e foto lateral; limites de caracteres por campo e tabela de cores por fundo; modelo no Canva `DAHZf-__wsg`
