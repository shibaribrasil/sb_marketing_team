# Post de Frase `instagram-post-de-frase`

> **Formato novo desde 30/10/2026 (layout "tarja e etiqueta").** Mistura das ideias L (Tarja lateral) e R (Palavra em etiqueta) do artefato "Post de Frase" (https://claude.ai/artifact/F2Q8MnGXaVi3cC24D1NtYZ, aba Post v2), pedida pelo Hugo em 30/10/2026 para dar ao post uma identidade reconhecível no grid. Substitui o layout antigo (frase dominante em Deep Plum ou Carbon, template "Post Frase Efeito", ID EAHMvTf7Hkk) e o uso de foto de fundo (a C-096, de 19/09, foi o último nesse modelo). **Layout aprovado pelo Hugo em 30/10/2026 (Post v2).** O modelo no Canva ("Post Frase - Modelo 2") foi criado no mesmo dia (ver "Template no Canva"). Pontos marcados **(confirmar)** ainda aguardam o Hugo.

**Objetivo:** Gerar identificação e repostagem a partir de uma frase com posição clara, sobre o universo do shibari, do BDSM ou da prática consciente. A frase se sustenta sozinha na imagem e a legenda desenvolve de onde ela parou. O visual existe para o post ser reconhecido no grid antes de ser lido.

**Plataforma:** Instagram (feed, imagem única, 1080 × 1350)

**Pasta de conteúdos:** `conteudos/instagram-post-de-frase/[slug-da-frase]/` (= `03_CONTEUDO\instagram-post-de-frase\` no Drive)

**Fluxo de produção:** Leo (slot na fila, com o **fundo**) → Julia (`texto.md`: frase, palavra marcada e legenda) → Ana (revisão) → Bia (arte no template) → Mari (publicação). A frase e a legenda passam pelo teste do praticante com a `voz-shibari` carregada.

**Quando não é este formato:** frase sobre uma foto continua sendo o Post de Foto (`post-de-foto.md`). Este formato não leva foto.

---

## Conceito

O post é uma **frase em que uma palavra foi marcada**, como o trecho que alguém grifaria para guardar. O conceito aparece na forma, não no texto:

- uma **faixa de cor na borda esquerda**, da altura toda da página, assina o post: no grid, a coluna de cor se repete de um post para outro e a frase é reconhecida antes de ser lida;
- **uma palavra** da frase vai sobre um bloco da mesma cor, e é nela que o olho pousa;
- a frase em si é grande, sozinha e sem enfeite.

**As palavras "tarja" e "etiqueta" não aparecem em nenhum texto do post nem na legenda.** São nomes de trabalho do layout, não recurso de linguagem. A tarja e o bloco repetem a mesma cor de propósito: um corte só (gramática visual).

Nenhum elemento vem de outro formato (sem índice de letras, sem marcação à mão, sem rótulo de quadro, sem cabeçalho corrente). A linha vertical fina em Scarlet, que o formato antigo evitava, **não é usada**: a tarja ocupa o lugar dela.

Dados que orientam a escolha da frase: as frases de posição clara e vocabulário da prática renderam de 21 a 64 repostagens ("controle sem consentimento não é bdsm", "a marca passa, mas a vontade de repetir continua"); as frases suaves renderam de 1 a 7.

---

## Estrutura fixa: 1 página

```
1. Imagem: tarja + frase com uma palavra marcada + assinatura
2. Legenda
```

---

## Conteúdo

### 1. Imagem

- **Frase:** a frase do post, autossuficiente (funciona sem a legenda).
  - Até **15 palavras** e até **5 linhas**, quebradas à mão. Minúsculas. **Sem ponto final**. Sem hashtag, sem @, sem elemento extra.
  - Toma posição em vez de montar contraste: antítese "não é X, é Y" só quando defende uma posição clara e falável (P81). Não sentencia a conduta nem o pensamento dos outros (P51, P85). Sem palavra de clique (P82), sem regra única para o que depende da pessoa (P84).
  - Termo do meio (inglês ou japonês) fica como o meio usa, e se explica na legenda se a frase precisar dele.
- **Palavra marcada:** **uma** por post (nunca duas). É a palavra que carrega a posição ou a ideia (na C-107, "limite"). A Julia indica a palavra entre `**` no `texto.md`; o Hugo confirma. Máximo de 13 letras. Se for a primeira da linha, o bloco avança 18px para a esquerda (ver Layout).
- **Assinatura:** "shibari brasil", fixa; a arte escreve, a Julia não.

### 2. Legenda (`legenda.txt`)

- Continuação do raciocínio da frase, não um resumo. Pode explicar a polêmica por trás dela ou o que ela quer dizer para quem pratica.
- **80 a 200 palavras**, minúsculas, parágrafos curtos, sem emoji.
- Sem pergunta obrigatória. Termina em afirmação ou deixa o pensamento em aberto.
- Se levar CTA de envio, **convida em vez de prescrever** (P91): "manda pra quem vai gostar de ler", e não "manda pra quem precisa ler".
- Até **5 hashtags** ao final, depois de uma linha em branco **(confirmar: os formatos novos usam até 3)**.
- Sem produto e sem linha de cashback, salvo se o briefing disser o contrário.
- **Abertura:** não repetir a frase palavra por palavra. Fecho de efeito curto ("a corda passa. o desejo de repetir fica") só quando conversa com uma foto (P59); como este formato não tem foto, evitar.

---

## Estrutura obrigatória do `texto.md`

O briefing é o cabeçalho do `texto.md` (frase, persona, objetivo, ângulo, **fundo do slot**, data). Depois, na ordem:

| Campo | Exemplo (C-107, 04/11/2026) | Limite |
|---|---|---|
| **1. Frase** | o **limite** de alguém não é um desafio pra você vencer | até 15 palavras, até 5 linhas, sem ponto final |
| **2. Palavra marcada** | limite | 1 palavra, até 13 letras |
| **3. Quebra de linhas** | o limite / de alguém / não é um / desafio pra / você vencer | até 5 linhas |
| **4. Legenda** | ver a legenda da C-107 | 80 a 200 palavras |

---

## Layout (referência para a Bia)

Medidas no canvas 1080 × 1350. Peça de referência: aba Post v2 do artefato citado no topo.

### Elementos
- **Margem de 108px** (`post-margem`) nos quatro lados para texto e assinatura. Só a tarja encosta na borda.
- **Tarja:** borda esquerda, altura toda (0 a 1350), **48px de largura**, sem raio. Cor conforme o fundo (tabela). **(confirmar a largura de 48px)**
- **Frase:** Playfair Display Bold, minúscula, alinhada à esquerda em x = 108, largura máxima de 864px, espaçamento −0,02em (−3px a 150px), entrelinha 0,98.
  - O corpo depende da maior linha: até **11 letras → 150px**; **12 a 13 letras → 130px**; **14 a 15 letras → 110px** (mínimo do sistema). Em 150px a entrelinha é 147px.
  - O bloco da frase **termina a 96px acima da assinatura** (base a y = 1106) e cresce para cima. Com 5 linhas a 150px, ocupa 735px.
  - Testar a peça reduzida a ~130px de largura: a frase se lê e a palavra marcada aparece.
- **Palavra marcada:** retângulo reto (sem raio) na cor da tarja, com **18px de folga** de cada lado do texto e a **altura da linha** (147px a 150px). O bloco avança 18px para a esquerda, para o texto da palavra alinhar com o das outras linhas, e não encosta na tarja (sobram 42px). A cor do texto da palavra vem da tabela.
- **Assinatura:** Cormorant Garamond Bold 40px, espaçamento 0,015, **60% de opacidade**, x = 108, base a 108px da borda inferior. Cor conforme o fundo.

---

## Cores conforme o fundo

O **fundo vem do slot do Leo** (campo Fundo do briefing), seguindo o ritmo do feed (`sb_cerebro/03_visual/gramatica-visual.md`). Valores de `sb_cerebro/03_visual/tokens.json`. Contraste calculado na proposta.

| Fundo | Frase | Tarja e bloco da palavra | Texto da palavra | Assinatura (60%) |
|---|---|---|---|---|
| **Warm Light** `#f4ece7` | Carbon `#141419` (15,7:1) | Scarlet `#d10f2f` | Warm Light `#f4ece7` (4,7:1) | Smoke Taupe `#8c6f68` |
| **Skin Nude** `#e6cfc3` | Carbon `#141419` (12,3:1) | Scarlet `#d10f2f` | Warm Light `#f4ece7` (4,7:1) | Smoke Taupe `#8c6f68` |
| **Carbon** `#141419` | Warm Light `#f4ece7` (15,7:1) | Scarlet `#d10f2f` | Warm Light `#f4ece7` (4,7:1) | Skin Nude `#e6cfc3` |
| **Deep Plum** `#5b1e4b` | Warm Light `#f4ece7` (10,4:1) | Scarlet 200 `#e89fa7` | Deep Plum `#5b1e4b` (5,7:1) | Skin Nude `#e6cfc3` |
| **Wine Knot** `#7e1a2e` | Warm Light `#f4ece7` (8,7:1) | Skin Nude `#e6cfc3` | Wine Knot `#7e1a2e` (6,8:1) | Skin Nude `#e6cfc3` |

### Regras de cor
- **Scarlet nunca sobre Deep Plum ou Wine Knot**: a tabela já troca por Scarlet 200 e Skin Nude.
- **Scarlet sobre Carbon** vale porque o bloco é grande (a palavra tem 150px); a tarja é forma, não texto.
- **Wine Knot:** no máximo 1 a cada 9 posts e nunca ao lado de Scarlet nem de Plum no grid (gramática visual).
- **Jute Gold, Plum 900 e fundo totalmente Scarlet não se usam neste formato.** Se o slot vier com um deles, o Leo troca com o Hugo.
- **Assinatura em fundo claro** tem 2,1:1 (Warm Light) e 1,9:1 (Skin Nude) a 60% de opacidade. É o padrão fixo da casa (Hugo, 30/10/2026), não uma escolha deste formato **(confirmar se vale revisar nos fundos claros)**.
- A tarja e a palavra marcada têm sempre a **mesma cor**; nunca duas cores de destaque na peça.

---

## Template no Canva

- **Modelo a usar: "Post Frase - Modelo 2"**, https://canva.link/i0ob25omxn429a4 (design `DAHZg2-dicc`, página `PB40sXr7DDf9n4R8`). Fundo Carbon, com a frase da C-107 ("o limite de alguém não é um desafio pra você vencer"). É a referência visual e a base de todo Post de Frase novo: duplicar (no Canva, ou com `copy-design` pelo MCP) e só trocar texto, bloco da palavra e cores. **Nunca editar o original.**
- **Dimensões:** 1080 × 1350px.
- **Elementos do modelo (IDs de edição pelo MCP; a cópia gera IDs novos, então ler a cópia com `read-design`):**

| Elemento | ID | Posição e tamanho no modelo |
|---|---|---|
| Fundo (retângulo `#141419`) | `LBbkFZqgQySMl4JS` | 0, 0 · 1080 × 1350, no fundo da pilha |
| Bloco da palavra (`#d10f2f`) | `LBLNDJHHwTmB0ms5` | x = 210, y = 385 · 441 × 147, atrás do texto |
| Frase | `LBJF9dBq0KV919SJ` | x = 108, y = 371 · 864 de largura; Playfair Bold 150px, entrelinha 0,98 |
| Assinatura | `LBHBFv1YSYTv0tyd` | esperado: x = 108, topo 1202; Bold 40px, 60% de opacidade |
| Tarja (`#d10f2f`) | `LBkFnrVXQWSJ3s1n` | 0, 0 · 48 × 1350 |

- **Como gerar um post novo:**
  1. Copiar o modelo.
  2. Trocar o texto da frase com as linhas já quebradas (`replace_text`) e ajustar o corpo (150, 130 ou 110px) pela maior linha.
  3. Reposicionar e redimensionar o bloco da palavra: largura = largura da palavra + 36px; altura = a entrelinha (147px a 150px); x = início da palavra − 18px; y = topo da frase + 147 × (linha − 1) + 14px.
  4. Aplicar as cores da tabela do fundo (tarja, bloco, texto da palavra, frase, assinatura).
  5. Registrar o link da cópia no `visual-spec.md` e mandar ao Hugo para aprovação visual antes de exportar.
- **Deslocamento de 14px:** no Canva a fonte assenta cerca de 14px mais abaixo na linha do que no navegador; por isso o bloco da palavra fica 14px abaixo do topo da caixa de texto.
- **Trocar o fundo e as cores pelo MCP:** o fundo gerado do Canva é uma imagem que o MCP não recolore. O modelo traz um retângulo vetorial `#141419` no fundo, a tarja e o bloco também são formas vetoriais. Para trocar a cor, usar `recolor_element` nessas formas (ainda não testado em uma cópia); se não aceitar, inserir uma forma nova com `insert_shape` na cor certa e mandar para a posição certa com `layer_element`. Retângulos preenchidos por imagem não aceitam recolorir.
- **Limites do MCP:** não troca fonte nem espaçamento entre letras. Por isso o modelo é sempre copiado (as fontes vêm dele). Pendências conhecidas do próprio modelo, a ajustar à mão no Canva **(confirmar se o Hugo já ajustou)**: a assinatura saiu em Playfair e deve ser Cormorant Garamond Bold com espaçamento 0,015; o espaçamento da frase está em 0 e o manual pede −0,02em.
- O template antigo "Post Frase Efeito" (ID EAHMvTf7Hkk) fica só para consulta dos posts anteriores a 30/10/2026. O design `DAHZg1P8-ZA` (1080 × 1440) é descarte de teste: não usar.

---

## Checklist de entrega (Julia preenche antes de passar para a Ana)

- [ ] Frase com até 15 palavras e até 5 linhas, minúsculas, sem ponto final
- [ ] Frase toma posição e se diria em voz alta; sem sentenciar a conduta dos outros (P51, P85), sem antítese só de efeito (P81), sem palavra de clique (P82)
- [ ] Uma palavra marcada entre `**`, com até 13 letras
- [ ] Quebra de linhas indicada e corpo da frase conferido pela maior linha
- [ ] "tarja" e "etiqueta" não aparecem na frase nem na legenda
- [ ] Legenda de 80 a 200 palavras, sem emoji, com ângulo que continua a frase
- [ ] CTA, se houver, convida em vez de prescrever (P91)
- [ ] Até 5 hashtags ao final, depois de uma linha em branco
- [ ] Fundo do slot anotado no cabeçalho, para a Bia aplicar a tabela de cores
- [ ] Nenhuma palavra da lista negra da `hab-produtor-textual`; autorrevisão em 4 camadas feita
- [ ] Voz conferida com a `voz-shibari`
