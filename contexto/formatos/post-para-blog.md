# Post para Blog

**Objetivo:** responder a dúvida de quem busca, com fonte e experiência, e levar o leitor ao passo seguinte dentro do domínio (outro post, a loja, o e-mail). O blog existe para trazer acesso e venda por meio de conteúdo que resolve a dúvida do leitor; o leitor vem primeiro, e o produto entra onde ele precisaria dele. Conteúdo permanente.

**Plataforma:** Site da Shibari Brasil (`shibaribrasil.com.br/blog`).

**Fonte única das orientações:** `sb_cerebro/04_formatos/blog.md` (estrutura do post, produto no texto, voz, rastreio, medição). Posições que o sustentam: P93 (produto no texto) e P94 (estrutura e voz do blog). **Em caso de conflito entre este arquivo, a skill `hab-produtor-textual` e o `blog.md`, o `blog.md` vence.** Este arquivo só diz o que entregar e como conferir.

**Regras de escrita:** carregar `voz-shibari` (voz do blog: **"nós"**, primeira pessoa do plural, o Hugo fala pela equipe; **sem "eu"**; **sem emoji**), seguir o capítulo 3.1 da skill `hab-produtor-textual` (técnica de blog) e os capítulos 1 e 2.

**HTML e publicação (padrão de 04/11/2026, P98):** o post publicado segue o modelo `contexto/formatos/modelos/post-para-blog-modelo.html` (estilo em linha do design system, página em fundo branco, caixas em plum, grade de 3 posts no "Leia a seguir"), e o passo a passo, as lições e o que ainda não foi testado estão em `contexto/formatos/post-para-blog-html.md`. A Julia entrega, além dos campos abaixo, as **imagens previstas** (com contexto, legenda neutra e texto alternativo; imagem de terceiros com crédito e link) e os **3 posts do "Leia a seguir"**; o SEO (título, descrição, resumo e endereço) faz parte da entrega e da publicação.

**Papel do post:** todo post declara um papel no cabeçalho, e o papel decide quais blocos entram e quanto produto cabe:

| Papel | Objetivo | Produto |
|---|---|---|
| **Pilar educativo** | Ser achado e citado | 1 a 2 menções em prosa, sem bloco |
| **Decisão** (escolher, cuidar, comparar) | Ajudar a decidir | Até 4 menções em prosa e o bloco "Na loja" |
| **Verbete ou FAQ** | Ser citado por IA | Nenhuma (só links para os pilares) |
| **Série ligada ao Instagram** (Desatando mitos e afins) | Dar destino permanente ao conteúdo da rede | Nenhuma ou 1 |

Briefing de blog **deriva do briefing de Instagram** e não entra na fila antes dele (P86).

---

### Estrutura obrigatória de entrega

O arquivo `texto.md` de um post para blog tem o cabeçalho da Julia (ver `agente-escritor`, com o carimbo `**Voz carregada:**`) mais os campos de blog abaixo, na ordem.

**Cabeçalho (além do padrão do `texto.md`)**

- **Papel do post** (tabela acima) e **intenção de busca** (informacional, comparativa ou de decisão).
- **Palavra-chave principal.** Se não estiver no briefing, perguntar ao Hugo antes de escrever.
- **Fontes** com `S-###` e página, vindas do `bibliotecario` (só para registro da equipe; ver "Regra de referências" abaixo).
- **Quem confere o fato de segurança** (Hugo ou praticante experiente; a IA não preenche fato de segurança, P86).
- **Produtos permitidos**: nome e dado do Notion (Catálogo — Produtos), **com a data em que o estoque foi conferido**.
- **Post de Instagram de origem.**
- **Aviso de segurança:** sim ou não (componente opcional; o briefing decide conforme o risco do tema).

**Campos, na ordem**

1. **Título do post** (promessa verificável, sem "guia completo"; claro e direto, com a palavra-chave).
2. **Resposta rápida:** 40 a 60 palavras que respondem a pergunta do post, em caixa destacada logo abaixo do título. Obrigatória em todos os papéis (no verbete, a definição em uma frase).
3. **Corpo do post**, nos blocos definidos em `sb_cerebro/04_formatos/blog.md`, seção 3. O tema já mostra o título como H1, então **o corpo começa em H2**, em forma de pergunta, cada um abrindo com a frase-resposta:
   - **Índice** se o post tem 3 seções ou mais, ou passa de 800 palavras;
   - componentes quando couberem: lista ou passos numerados, tabela comparativa, aviso de segurança (sempre com fonte), "Na prática da casa" (relato da equipe, em "nós", nunca simulado) e imagem com legenda e texto alternativo;
   - **extensão pela pergunta, sem mínimo fixo.**
4. **Bloco "Na loja"** (papel "decisão"; ver P93): 2 a 3 itens por situação, com nome, uma linha de "para quem faz sentido" e link. **Rótulo "Na loja" visível. Sem preço e sem promoção.**
5. **Perguntas frequentes:** de 3 a 5 perguntas reais do atendimento, **sempre visíveis** (nunca recolhidas).
6. **Fontes:** lista com link e, quando for livro, página. Fonte original, nunca o extrato da biblioteca.
7. **"Leia a seguir":** **3 posts do blog em grade de cartões** (foto de capa, título e subtítulo de cada um; Hugo, 04/11/2026), e o convite ao e-mail, com o Instagram como link secundário. **Substitui o bloco fixo antigo** (siga no Instagram, com emoji).
8. **Assinatura e linha de uso:** "Escrito por Hugo Barcellos (The Priest), da Shibari Brasil. Reprodução proibida sem autorização." Dentro do limite de exposição do P46.
9. **Resumo** (para a listagem do blog): 2 a 3 frases, máximo 300 caracteres; convite à leitura, não resumo técnico.
10. **Título SEO:** máximo 65 caracteres, com a palavra-chave.
11. **Descrição SEO (meta description):** 120 a 160 caracteres, com a palavra-chave, como convite ao clique.
12. **Endereço (slug) desejado:** o nome certo do post, em minúsculas, sem acento, com hífens e a palavra-chave, **sem ano nem número que envelhece** (exemplo: `historia-do-shibari`). A Nuvemshop acrescenta sozinha ao final do endereço 12 caracteres fixos do identificador do post, e isso não dá para tirar; **o nome é corrigido à mão na publicação** (ver "Publicação do post" abaixo).
13. **Imagem principal:** a Bia produz separadamente; o briefing informa o tema ou conceito visual. PNG, 1024 × 630 px, comprimida para web (peso-alvo abaixo de 200 KB). Foto própria do acervo, sem banner de promoção.

**Linha de uso do texto (decisão do Hugo, 03/11/2026):** continua **"Reprodução proibida sem autorização"**, na mesma linha da assinatura. Não trocar por "pode citar".

---

### Regras de produto no texto (P93)

- O teste: **se a menção sumisse, o leitor perderia alguma coisa?** Se não perderia, é propaganda e sai.
- **Nunca preço nem promoção** dentro do texto (desconto, frete grátis, contagem regressiva, "garanta já").
- **Só linkar produto publicado e em estoque**, conferido antes de publicar. Produto inexistente, despublicado ou esgotado não entra.
- **Fato de produto vem do Notion** (Catálogo — Produtos), nunca de memória. O marketing não define produto.
- **Equipamento de risco (suspensão)** só entra depois do trecho de segurança e com revisão do Hugo ou de praticante experiente. Produto nunca fica dentro de trecho de segurança.
- Sem anúncio de terceiros e sem link de afiliado de outra loja.

### Regras de redação do blog (P97, Hugo e Ana, 04/11/2026)

- **Gancho com fato:** cada seção termina dizendo o que vem a seguir, com fato; a seguinte o retoma. Nunca máxima genérica nem "X pede Y".
- **Abertura que responde:** a primeira frase de cada seção responde ao H2, também nas seções narrativas (sem começar por "Porque" nem por negação).
- **Variedade:** variar os verbos de atribuição (diz, escreve, aponta, conta, registra, lembra, observa, segundo) e as expressões; hojojutsu, kinbaku, shibari e bakushi não têm sinônimo e ficam.
- **Sem fórmula mecânica:** nada de "pelo que lemos", "nas fontes que lemos", "não há consenso", "conforme a fonte", "voltando à pergunta do começo". A leitura da casa se marca pelo rótulo "Na nossa leitura" e pela razão que a sustenta.

### Regra de referências

**Como a fonte aparece no corpo (P96, Hugo, 04/11/2026):** só como citação direta de **livro**, com autor e título (e página só na afirmação central ou contestada; nas demais menções o nome do autor basta, porque a bibliografia é completa; ajuste do Hugo, 04/11/2026) ("Shin Nawakiri escreve, no livro *Essence of Shibari*, que... (p. 20)"). Artigo só se o tema for muito específico e o autor estiver claro, nunca o nome do site ou da página. O conteúdo de sites, artigos e verbetes pode ser usado, **sem menção no texto corrido**, e fica só em "Fontes" (livros primeiro, depois artigos, ensaios e verbetes consultados). **Título de referência sempre no original, sem tradução.** O texto é da casa ("nós"): a fonte sustenta a afirmação, não conduz o parágrafo. Livro da biblioteca só entra com a amostra de leitura do Hugo; resumo não literal precisa da leitura dele antes de publicar.

Documentos do acervo interno (glossários, guias, extrações da biblioteca, `S-###`) **nunca aparecem como link no corpo do artigo**, porque o leitor público não tem acesso a eles e porque o repositório guarda texto de terceiros. Eles entram só no cabeçalho do `texto.md`, para registro da equipe. No corpo e na seção "Fontes", citar a **fonte original** com link. Referências a conteúdo da marca apontam só para páginas públicas (site, Instagram, outros posts do blog).

---

### Checklist de entrega (a Julia preenche antes de chamar a Ana)

- [ ] Cabeçalho completo, com o carimbo `**Voz carregada:**` e o **papel do post**
- [ ] Título definido; **resposta rápida** de 40 a 60 palavras logo abaixo
- [ ] Corpo começa em H2, em forma de pergunta; **sem H1 no corpo**
- [ ] Índice, se o post tem 3 seções ou mais, ou passa de 800 palavras
- [ ] Voz "nós", sem "eu" e sem emoji; nenhuma afirmação sem fonte ou sem dono (segurança: Hugo ou praticante)
- [ ] Produto: dentro do limite do papel; sem preço nem promoção; só item publicado e em estoque (estoque conferido em ____); fato de produto do Notion; equipamento de risco só depois do trecho de segurança
- [ ] Bloco "Na loja" com o rótulo visível (papel "decisão")
- [ ] FAQ sempre visível, de 3 a 5 perguntas reais
- [ ] Fontes com link e página; nenhuma `S-###` no corpo
- [ ] "Leia a seguir" com 3 posts em grade (foto, título e subtítulo) e convite ao e-mail; **nenhum bloco fixo antigo** (Instagram com emoji)
- [ ] Assinatura "Escrito por Hugo Barcellos (The Priest), da Shibari Brasil. Reprodução proibida sem autorização."
- [ ] Resumo (até 300), título SEO (até 65), descrição SEO (120 a 160) e **nome do endereço desejado** (limpo; o final fixo da Nuvemshop não conta) escritos
- [ ] Plano de publicação registrado no cabeçalho: endereço a ajustar à mão em rascunho e pedido de indexação depois de publicar (seção "Publicação do post")
- [ ] Especificação da imagem principal informada para a Bia; a imagem principal não se repete no corpo
- [ ] Imagens do corpo: com contexto na seção, legenda neutra, texto alternativo e, se de terceiros, crédito com link; nenhuma foto aleatória ou de estoque; foto própria sem rosto
- [ ] "Leia a seguir" com 3 posts (título, endereço, capa e subtítulo) e posts de destino conferidos (SEO e endereço certos)
- [ ] Título SEO (até 65), descrição SEO (120 a 160), resumo e endereço entregues e conferidos depois de salvar
- [ ] Autorrevisão em 4 camadas executada (capítulo 4 da skill de produção)

### Publicação do post (parte obrigatória; P95, Hugo, 03/11/2026)

Detalhe e checklist completo em `sb_cerebro/04_formatos/blog.md`, seção 7. Publicar de verdade é sempre do Hugo. Duas etapas fazem parte da publicação de todo post:

1. **Endereço limpo.** A Nuvemshop gera o nome do endereço a partir do título e acrescenta um final fixo de 12 caracteres (não sai). Corrigir à mão o nome, no campo "URL do post" (Tags e SEO), **com o post ainda em rascunho, antes de publicar**. Post já publicado e indexado só muda de nome com redirecionamento 301 criado logo depois (Configurações > Redirecionamentos 301, caminho antigo para caminho novo; passo a passo em `sb_cerebro/04_formatos/blog.md`, seção 7). Conferir o endereço final aberto no navegador, com a barra final.
2. **Pedido de indexação no Search Console**, logo depois de publicar e conferir: Inspeção de URL com o endereço final, "Testar o URL publicado" e "Solicitar indexação" (propriedade de domínio `shibaribrasil.com.br`). Em revisão de post já indexado, novo pedido. Uma vez só: enviar o `sitemap_blog.xml` em Sitemaps. Conferir a indexação em 7 dias.

Quem faz: quem tem o login (Hugo ou Robson), ou o agente pelo Chrome do Hugo quando ele avisar o endereço final (autorização dada só para esse passo). Registrar na pauta o endereço final e a data do pedido.

**Pendente (não bloqueia a escrita):** o modelo visual em HTML dos posts (a ser montado com o Claude Design; estilo em linha, blocos marcados por `data-sb`, ver `sb_cerebro/04_formatos/blog.md`, seções 2 e 3) e o rastreio do clique do blog para a loja (já publicado no GTM; a posição do link depende do modelo).
