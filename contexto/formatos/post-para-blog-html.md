# Post para Blog: HTML, publicação e lições (padrão de 04/11/2026)

**Para que serve:** o primeiro post publicado nesse padrão foi "Breve História do Shibari: de onde vem e quem moldou a prática" (pasta no Drive: `03_CONTEUDO\site-post-para-blog\historia-do-shibari\`). O Hugo viu no celular e aprovou ("ficou ótimo"). Este arquivo guarda o padrão de HTML, o passo a passo de publicar e o que se aprendeu, para os próximos artigos nascerem já assim.

**Fonte única das decisões:** `sb_cerebro/04_formatos/blog.md` (seção 8) e a posição **P98** (`sb_cerebro/01_identidade/posicoes.md`). Em conflito, o `blog.md` vence. Este arquivo é a versão operacional: o que o time faz, na ordem.

**Arquivo-modelo (copiar e preencher):** `contexto/formatos/modelos/post-para-blog-modelo.html`. Todos os componentes já vêm com o estilo em linha do design system; os trechos em `{{ ... }}` são o que se preenche. Não reescrever os estilos à mão: copiar do modelo.

---

## 1. Quem faz o quê

1. **Julia** escreve o `texto.md` (campos de `post-para-blog.md`), com a voz carregada, e deve entregar também: imagens previstas (com legenda neutra e texto alternativo), os 3 posts do "Leia a seguir" e o endereço desejado.
2. **Ana** revisa (voz, P96, P97, estrutura) e confere imagens, legendas e textos alternativos.
3. **Bibliotecário** confere os fatos contra a biblioteca (nos trechos que mudarem depois da primeira conferência).
4. **Mari** monta o `publicacao.html` a partir do modelo, junto com o pacote de publicação (ver `agente-coordenador`).
5. **Hugo** aprova e publica, ou autoriza o agente a colar e publicar pelo Chrome dele.

## 2. Componentes do modelo (todos testados no editor da Nuvemshop em 04/11/2026)

| Componente | Marcação | Como fica |
|---|---|---|
| Resposta rápida | `aside data-sb="resposta-rapida"` | Caixa `deep-plum` (#5b1e4b), texto `warm-light`, rótulo `scarlet-200`. Logo abaixo do título |
| Linha de confiança | `p data-sb="linha-confianca"` | Texto de apoio 12 px em `taupe-700`: atualizado em, tempo de leitura, assinatura, linha de uso |
| Índice | `ul data-sb="indice"` | Linhas com divisória; âncoras para os `id` dos `h2` (3 seções ou mais, ou mais de 800 palavras) |
| Título de seção | `h2 id=...` | Playfair Display Bold, **minúsculas** (via `text-transform:lowercase`), 24 a 32 px, em forma de pergunta; o corpo começa em `h2` porque o tema já mostra o `h1` |
| Parágrafo | `p` | Montserrat 14 px, entrelinha 1,7, `carbon-black` |
| Caixa "Na nossa leitura" | `aside data-sb="nossa-leitura"` | Fundo **branco** com contorno de 1 px `deep-plum`, rótulo em plum |
| Imagem | `figure data-sb="imagem"` | `img` com `alt`, `width` e `height`, e `figcaption` de 12 px em `taupe-700`; retrato até 420 px de largura, paisagem em 100% |
| Lista em linhas | `ul data-sb="lista"` | Linhas com divisória e nome em `strong` |
| Perguntas frequentes | `h2 data-sb="faq"` e `h3` + `p` | Sempre visíveis; `h3` em Playfair minúsculo |
| Fontes | `h2 data-sb="fontes"` e `ul` | Livros primeiro, depois artigos, ensaios e verbetes; 13 px em `taupe-700` |
| Leia a seguir | `div data-sb="leia-a-seguir-grid"` | **Grade de 3 cartões** (foto de capa, título e subtítulo), `flex` com quebra, cada cartão com 200 px de base: três por linha no computador, um por linha no celular |
| Convite | `p` | E-mail primeiro (formulário no rodapé), Instagram como link secundário |

**Página sempre em fundo branco.** Nenhuma caixa usa fundo nude ou taupe (decisão do Hugo, 04/11/2026: a opção 2, plum cheio na resposta rápida e contorno plum na leitura; as opções com fio plum, carbon e juta ficaram de fora e estão registradas no `blog.md`).

**O que o estilo não faz:** sem `<style>`, sem classes próprias, sem `@media` (a adaptação ao celular é por `clamp()` e por `flex` com quebra), sem Scarlet (só em botão, e o post não tem botão), sem emoji e sem seta ou glifo decorativo, sem raio de borda (a marca é reta), sem sombra.

## 3. Imagens

- **Fonte da imagem:** (a) foto própria do banco (`SB Audiovisual\02_GERAL`, `01_PRODUTOS`), **sem rosto** e com consentimento da pessoa fotografada; ou (b) imagem histórica ou de terceiros **com crédito e link** ("Imagem retirada do link: ..."), sabendo que autoria, data e licença continuam risco do Hugo. Nunca foto aleatória nem de estoque só para preencher (o Hugo: "não vou colocar uma imagem aleatória").
- **Contexto:** a imagem entra na seção a que se refere (por exemplo, a de época na seção do período; a do artista na seção dele). Foto de prática moderna só quando o texto fala do shibari de hoje.
- **Legenda:** neutra, descreve o que se vê; não data nem atribui autoria sem fonte confirmada. Título de obra no original.
- **Texto alternativo:** obrigatório em toda imagem; descreve a cena para leitor de tela, sem interpretar.
- **Não repetir:** a imagem principal não pode aparecer de novo no corpo (o Hugo tirou do corpo a foto que duplicava a capa).
- **Imagem principal:** o editor **não tem campo de texto alternativo** para ela (o tema usa o título do post). Tamanho mínimo 1024 x 630, PNG, JPEG ou GIF. **O upload da imagem principal não pode ser feito pelo agente** (o campo fica num iframe de outro domínio e abre o seletor de arquivos do Windows): o Hugo carrega pelo editor.
- **Arquivos:** guardar na pasta do post, em `imagens/`, só as imagens usadas, nomeadas `<slug>_<peça>.jpg`. Exportar do `bruto` sem alterar o `bruto`: redimensionar (lado maior até 1200 px, JPEG qualidade 80 a 84, sem metadados) e, se muito escura, clarear de leve.

## 4. "Leia a seguir" em grade

1. Escolher 3 posts publicados do blog, ligados ao tema (próximo passo do leitor); pelo menos um ponto de entrada para quem está começando.
2. De cada um: título, endereço (`/blog/posts/...`), capa (a `og:image` da página do post, em `cdn-blog-backend.tiendanube.com/.../covers/...`) e subtítulo (a descrição SEO ou o resumo, em uma frase curta).
3. **Antes de linkar, conferir o post de destino:** título SEO e descrição certos e endereço certo. O de Aftercare tinha a descrição copiada de outro post e um endereço com nome errado; correção pendente na lista de correções dos posts.
4. Só linkar post publicado. Rascunho não entra.

## 5. Campos do editor (Blog, Nuvemshop)

- **Título:** o do artigo (o tema o mostra como `h1`).
- **Conteúdo:** o HTML do modelo, pelo botão `...` da barra, **Fonte HTML**.
- **Resumo (opcional):** o texto da listagem, até 300 caracteres, convite à leitura.
- **Tags e SEO:** título SEO (o campo aceita até 70; usar até 65 com a palavra-chave), descrição SEO (120 a 160, com a palavra-chave, convite ao clique) e **URL do post** (o nome do endereço; a Nuvemshop acrescenta sozinha ao final os 12 últimos caracteres do identificador do post, e isso não sai).
- **Imagem principal:** ver seção 3.
- **Visibilidade:** Publicado ou Rascunho. **Atenção:** em post que já foi publicado e indexado, "Rascunho" tira o artigo do ar (o endereço continua respondendo, mas sem o conteúdo) e o redirecionamento 301 aponta para essa página vazia. Em revisão de post que ranqueia, editar sem passar por rascunho, ou deixar o rascunho o mais curto possível.

**O SEO e o resumo fazem parte da publicação.** Todo pacote de publicação entrega o título SEO, a descrição SEO, o resumo e o endereço, e quem publica confere que ficaram gravados (reabrir "Tags e SEO" depois de salvar).

## 6. Passo a passo de colar e publicar (pelo Chrome do Hugo, com autorização)

1. **Backup do HTML que está no ar:** editor, `...`, Fonte HTML, Ctrl+A, Ctrl+C, e salvar num arquivo `backup_html_no_ar_AAAA-MM-DD.html` na pasta do post (a Nuvemshop não guarda versões).
2. **Montar o `publicacao.html`** a partir do modelo, com a data do dia no lugar do marcador, e colocá-lo na área de transferência.
3. **Colar:** Fonte HTML, Ctrl+A, Ctrl+V, "Salvar" na janela.
4. **Preencher** título, resumo, Tags e SEO, e salvar o post. **Esperar a página carregar por completo antes de clicar** (num carregamento lento um clique caiu no botão "Rascunho"; conferir sempre pelo print que "Publicado" continua marcado antes de salvar).
5. **Conferir a página pública** (`curl` ou navegador): título, `canonical`, descrição, os blocos `data-sb`, as figuras, os cartões e o endereço antigo respondendo 301 (quando o nome do endereço mudou). Ver no celular.
6. **Pedir a indexação** no Search Console (P95): Inspeção de URL, "Testar o URL publicado", "Solicitar indexação". Conferir em 7 dias.
7. **Registrar** no `texto.md` (nota de estado), no `registro.md` do `sb_cerebro` e na pauta (endereço final e data do pedido).

**Armadilha técnica (scripts do time):** scripts em PowerShell 5.1 que contenham acentos precisam ser salvos em **UTF-8 com BOM**; sem BOM, os acentos saem quebrados no HTML gerado. Conferir sempre que o arquivo gerado não tem "Ã" nem "Â".

## 7. Ainda não testado no editor (testar em rascunho antes de usar)

- Aviso de segurança em caixa distinta (componente `Aviso`), bloco "Na loja" com 2 a 3 itens (P93), tabela comparativa, dados estruturados de FAQ em `<script type="application/ld+json">`, botão Scarlet. Seguir o design system (`sb_cerebro/03_visual/gramatica-visual.md`) e registrar o resultado do teste no `blog.md`.

## 8. Conferência final (resumo)

- [ ] Texto revisado pela Ana e fatos conferidos; voz, P96 e P97 aplicados
- [ ] HTML gerado do modelo, sem `<style>`, sem classe, sem Scarlet, sem emoji, sem "Ã"
- [ ] Imagens com contexto, legenda neutra, texto alternativo e crédito (terceiros); nenhuma repetida; cópias em `imagens/`
- [ ] "Leia a seguir" com 3 cartões, posts de destino conferidos
- [ ] Título SEO, descrição SEO, resumo e endereço gravados
- [ ] Publicado (sem passar por rascunho em post que ranqueia), página pública conferida e vista no celular
- [ ] Indexação solicitada e registrada; conferir em 7 dias
