# Especificações de Execução de Tarefas e Rotinas do Marketing Team - Shibari Brasil

Este arquivo define os critérios de aceitação, os passos obrigatórios que o agente deve seguir em cada ciclo de trabalho e os comandos de uso do projeto.

---

## 👥 Time de Agentes

A produção das tarefas é dividida entre agentes especializados. Cada um tem uma função clara, um status de pauta correspondente e um momento certo de ser acionado:

| Nome | Função | O que faz | Quando acionar | Skill | Status que gerencia |
|---|---|---|---|---|---|
| **Mari** | Coordenadora e Publicação | Dá o panorama, retoma contexto, roteia, monta o **pacote de publicação** (mídia validada, legenda, data e hora de pico) e acompanha o agendamento (hoje no mLabs, depois pela API). Mantém a pauta em dia a partir do perfil do Instagram | Para começar qualquer sessão, quando não souber por onde ir ou quando uma peça estiver pronta para publicar | `agente-coordenador` | Pronto - Aguardando Publicação → Agendado → Publicado |
| **Leo** | Estrategista de conteúdo | Mantém a fila e a sequência do Instagram (`estrategia/`), lê os resultados dos posts, minera ideias e propõe slots **com âncora no núcleo de voz** (tema sem posição do Hugo vira pergunta para ele). Também pesquisa fontes e alimenta a biblioteca do núcleo | Para decidir o que entra na fila, ler resultados, pedir ideia ou pesquisar referência | `agente-estrategista` | Backlog e fila |
| **Julia** | Autora | Recebe um **slot aprovado** na fila, consolida o ângulo (o antigo briefing vira o cabeçalho do `texto.md`), escreve texto e legenda na voz da marca, **aciona a Ana** (revisão com contexto limpo) e entrega ao Hugo um pacote único. É a dona da voz de ponta a ponta | Quando o Hugo aprovar um slot da fila | `agente-escritor` | Briefing → Em Produção → Aguardando Revisão → Design em Produção |
| **Ana** | Revisora | Segunda leitura com contexto limpo, invocada pela Julia (ou pelo Hugo, direto): aplica o teste de voz e a técnica sobre `texto.md` e `legenda.txt` e devolve o veredicto. Não move status. A aprovação visual é feita pelo Hugo no Canva | Ao fechar o rascunho (pela Julia) ou sob pedido | `agente-revisor` | Nenhum (devolve relatório) |
| **Bia** | Diretora de Arte | Produz a direção visual e as referências e leva o design ao Canva. Pode começar o conceito visual em paralelo à aprovação do texto; a arte final vai depois dela. Preenche o Fundo no `visual-spec.md`. Se houver ajustes manuais pendentes, lista-os em "Pendências no Canva" | Quando o texto estiver aprovado (conceito pode começar antes) | `agente-diretor-de-arte` | Design em Produção → Pendente de Alteração no Canva ou Pronto - Aguardando Publicação |
| **Gui** | Tráfego Pago | Criação e otimização de anúncios pagos em dois canais: **Instagram** (Meta Ads) e **Google Ads**. Identifica a plataforma e carrega a skill correspondente (`hab-meta-ads` para Instagram; `hab-google-ads` para Google). Pode ser acionado a qualquer momento, independente do pipeline orgânico | Quando quiser trabalhar com campanhas pagas | `agente-trafego` + skill da plataforma | *(sem status fixo — atua em paralelo)* |

Cada agente lê os arquivos de contexto relevantes e atualiza a pauta ao concluir sua etapa. As instruções completas de cada um estão em `.claude/skills/[nome-do-agente]/SKILL.md`.

**Fluxo completo (puxado pela fila):**
```
Leo: lê resultados + núcleo + biblioteca → propõe slots com âncora → Hugo aprova a fila
  ↓ (slot aprovado = ordem de produção; status Briefing)
Julia: cabeçalho (ângulo) + texto + legenda → aciona Ana (contexto limpo) → pacote único ao Hugo (Aguardando Revisão)
  ↓ Hugo aprova
Bia: conceito (pode começar antes) → Canva → Hugo aprova a arte (Design em Produção → Pronto - Aguardando Publicação)
  ↓
Mari: pacote de publicação → mLabs (Fase 1) ou fila por API (Fase 2) → Pronto - Agendado → Pronto - Publicado (do perfil)
  ↓
Resultado volta ao Leo (estudo no núcleo `sb_cerebro/05_conhecimento`, com o Hugo)
```

A `contexto/pauta.md` é o **único registro de status**. O `contexto/briefings.md` (banco do antigo Caio) e o `contexto/historico-conteudos.md` estão **congelados desde 27/10/2026**: não recebem entrada nova; os scripts do Leo ainda os leem para as peças antigas. O backlog será consolidado e podado pelo Leo, com a aprovação do Hugo.

---

## 🗂️ Estrutura de Arquivos

```
├── CLAUDE.md                    → instruções de comportamento do agente
│
├── contexto/
│   ├── historico-conteudos.md   → registro das peças aprovadas até 27/10/2026 (CONGELADO)
│   ├── loja.md                  → informações da Shibari Brasil (a voz mora no núcleo `sb_cerebro`, via skill `voz-shibari`)
│   ├── personas.md              → perfis do público-alvo
│   ├── referencias.md           → referências de estilo e campanhas
│   ├── formatos-conteudo.md     → índice dos formatos cadastrados
│   ├── formatos/                → um arquivo .md por formato de conteúdo
│   ├── briefings.md             → banco legado do antigo Caio (CONGELADO; será podado pelo Leo)
│   └── pauta.md                 → backlog de territórios, produções em andamento e prontos
│
├── conteudos/                   → NÃO fica neste repositório: mora no Drive, em `G:\Meu Drive\SB Audiovisual\03_CONTEUDO\`
│   └── [tipo]/
│       └── [titulo]/            → arquivos do conteúdo orgânico (texto, legenda, imagens, variações)
│
├── estrategia/                  → do Leo: plano da sequência (JSON), arquivo vivo, capas e material
│
├── anuncios/
│   ├── instagram/
│   │   └── [nome-da-campanha]/  → materiais de campanhas pagas no Instagram
│   └── google/
│       └── [nome-da-campanha]/  → materiais de campanhas pagas no Google Ads
│
└── .claude/
    ├── skills/
    │   ├── agente-*/            → skill de cada membro do time
    │   └── hab-*/               → habilidades especializadas carregadas pelos agentes
    └── specs/
        └── diretrizes.md        → este arquivo — regras de execução e comandos
```

---

## 🚀 Antes de Começar a Produzir

Para que o agente gere conteúdo alinhado com a Shibari Brasil, os arquivos abaixo precisam estar preenchidos e a skill `voz-shibari` (núcleo `sb_cerebro`) precisa estar carregada. Enquanto estiverem vazios, o conteúdo gerado será genérico.

| Arquivo | O que colocar | Prioridade |
|---|---|---|
| `contexto/loja.md` | Produtos, público, dores, diferenciais da loja | Alta |
| `contexto/personas.md` | Perfis detalhados do cliente ideal | Alta |
| `contexto/referencias.md` | Posts que funcionaram, referências de estilo | Média |

Para preencher qualquer um deles, basta dizer ao agente:
```
Vamos montar o [nome do arquivo]
```

---

## 💬 Comandos de Uso

Os comandos abaixo são prompts que o usuário digita diretamente na conversa com o agente.

### Entrada e Status Geral

**Iniciar a sessão ou pedir o panorama do time:**
```
Boa tarde / Como estamos? / O que temos em andamento?
```
Aciona a Mari (Coordenadora). Ela lê a pauta e a memória da sessão anterior e entrega um resumo do que está em cada etapa, com sugestão do próximo passo.

**Não saber o que fazer a seguir:**
```
Por onde começo?
```
A Mari avalia o que está mais adiantado ou parado e indica o agente certo.

---

### Pauta e Planejamento

**Ver o estado atual da produção:**
```
Ver pauta
```
O agente lê `contexto/pauta.md` e apresenta o que está em cada status.

**Continuar um trabalho que ficou pela metade:**
```
Continuar produção
```
O agente verifica os itens em **Em Produção** e **Aguardando Revisão** e retoma o trabalho mais prioritário.

**Registrar uma ideia sem entrar em produção agora:**
```
Tenho uma ideia: [descreva o tema ou conceito]
```
O agente adiciona a ideia no **Backlog** da pauta sem gerar nenhum conteúdo.

**Produzir um slot aprovado da fila:**
```
Produzir: [título do slot ou código]
```
Aciona a Julia. Ela move o item para **Em Produção**, cria a pasta em `conteudos/` (no Drive, em `03_CONTEUDO\`), escreve cabeçalho, texto e legenda, aciona a Ana e apresenta o pacote. Peça fora da fila só com autorização do Hugo.

---

### Acionar Agentes

**Fila, sequência e resultados:**
```
O que entra na fila? / Monta a sequência / Como foi a semana? / Por que esse post foi bem?
```
Aciona o Leo (Estrategista). Ele propõe slots com âncora no núcleo de voz, mantém a sequência em `estrategia/`, lê os resultados dos posts e pesquisa referências. Tema sem posição do Hugo vira pergunta para ele, não briefing.

**Ver o backlog:**
```
Ver backlog
```
O Leo lista as ideias do Backlog da pauta e as perguntas pendentes para o Hugo.

**Escrever o conteúdo:**
```
Escrever conteúdo: [título]
```
Aciona a Julia (Autora). Ela lê o slot aprovado e produz cabeçalho, texto e legenda na voz da marca.

**Revisar o texto:**
```
Revisar: [título]
```
Aciona a Ana (Revisora) direto. Normalmente a Julia já a chama ao fechar o rascunho, e o Hugo recebe o texto junto com o veredicto. A aprovação visual é feita pelo Hugo diretamente no Canva após a Bia entregar o design.

**Especificar a direção visual:**
```
Direção visual: [título]
```
Aciona a Bia (Diretora de Arte). Ela lê o texto já aprovado pela Ana e cria a especificação visual com prompts e referências.

**Gerar variação de um conteúdo existente:**
```
Variação de: [título do conteúdo]
```
Aciona a Julia (Escritora) para gerar uma segunda versão, salva como arquivo separado na mesma pasta.

**Trabalhar com anúncios pagos:**
```
Tráfego: [o que precisa]
```
Aciona o Gui (Tráfego Pago). Ele pergunta em qual plataforma estamos trabalhando — **Instagram** ou **Google Ads** — e carrega a skill correspondente antes de executar. Trabalha em paralelo ao time, independente do pipeline orgânico.

**Produtos (cadastro, descrição e características):** não são do marketing. São do cadastrador (`sb_admin_team`) e ficam no Notion, na base Catálogo — Produtos (Notion). O time consulta o Notion para qualquer dado de produto; fato que faltar vai ao Hugo.

**Confirmar que um conteúdo foi postado:**
```
Confirmar postagem: [título do conteúdo]
```
Move o item de **Pronto - Aguardando Publicação** para **Pronto - Publicado** na pauta e registra a data. A Mari também lembra dos prontos sem confirmação toda vez que uma sessão é iniciada.

---

### Histórico e Contexto

**Ver o histórico de um tipo de conteúdo:**
```
Ver histórico de [tipo de conteúdo]
```
Exemplo: `Ver histórico de post de Instagram`

**Atualizar informações da loja:**
```
Atualizar loja: [informação]
```
O agente registra a informação em `contexto/loja.md`.

---

## 🔁 Fluxo Típico de uma Sessão

1. Abrir o projeto no Claude Code (o hook injeta o resumo da fila).
2. Acionar a Mari (`Como estamos?`): panorama, o que está pronto para publicar e o que mudou na fila.
3. **Se quiser decidir o que produzir:** acionar o Leo → ele propõe slots com âncora → o Hugo aprova a fila.
4. **Para produzir um slot aprovado:** Julia (texto e legenda, com a Ana) → Hugo aprova o pacote → Bia faz o visual → Hugo aprova no Canva.
5. **Para publicar:** Mari monta o pacote → Hugo agenda (mLabs hoje) → a pauta acompanha o perfil.
6. Os agentes atualizam só a `contexto/pauta.md`.

---

## 📋 Tipos de Conteúdo Suportados

Os formatos são definidos de forma incremental. Cada formato tem seu próprio arquivo em `contexto/formatos/`. A cada novo tipo de conteúdo criado, o agente:
1. Levanta as especificações com o usuário (objetivo, plataforma, tamanho, CTA).
2. Cria um novo arquivo `contexto/formatos/[slug-do-formato].md` com as especificações levantadas (usar o modelo em `contexto/formatos-conteudo.md`).
3. Adiciona o nome do tipo na lista abaixo e no índice `contexto/formatos-conteudo.md`.
4. Cria uma pasta para o tipo dentro de `conteudos/` (no Drive, em `03_CONTEUDO\`; ver protocolo abaixo).
5. Gera o conteúdo seguindo as especificações recém-definidas.

**Formatos cadastrados:**
1. Post para Blog → `contexto/formatos/post-para-blog.md`
2. Post de Frase → `contexto/formatos/post-de-frase.md`
3. Post Por Trás do Desejo → `contexto/formatos/post-por-tras-do-desejo.md` — layout "dicionário" desde 30/10/2026: carrossel de 5 páginas (capa com origem e definição, acepções, figura, termos ligados, finalização fixa com bibliografia e índice de letras); cores pela tabela do fundo do slot; pipeline: Julia (texto + legenda) → Ana (revisão) → Bia (arte e foto)
4. Post Inspiração de Amarração → `contexto/formatos/post-inspiracao-de-amarracao.md`
5. Carrossel Livre → `contexto/formatos/carrossel-livre.md`
6 e 7. (Os formatos de descrição de produto saíram do marketing em 27/10/2026: são do cadastrador, no `sb_admin_team`. A numeração dos demais formatos não muda.)
8. Post Desatando Mitos (Instagram) → `contexto/formatos/post-desatando-mitos.md`
9. Post de Foto (Instagram) → `contexto/formatos/post-de-foto.md` — foto do acervo pessoal movida de `assets/arquivo/Post de Fotos - A Publicar/`; pipeline direto: Julia (legenda) → Ana (revisão) → Publicação
10. Post de Produto (Instagram) → `contexto/formatos/post-de-produto.md` — legenda ancorada nos dados do produto no Catálogo — Produtos (Notion); pipeline: Julia (legenda, com os dados do Notion) → Bia (visual) → Ana (revisão)
11. Instagram Vídeo → `contexto/formatos/instagram-video.md` — legenda de apoio a vídeo demonstrativo; pipeline: Julia (legenda) → Ana (revisão)
12. Post de Bingo (Instagram) → `contexto/formatos/post-de-bingo.md` — post casual de identificação (cartela 3×3, 9 situações); eventual, sob demanda do Hugo; pipeline: Julia (cartela + legenda) → Bia (arte) → Ana (revisão)
13. Post de Duelo (Instagram) → `contexto/formatos/post-de-duelo.md` — post casual de identificação (duas colunas "time A × time B", 4 itens paralelos); eventual, em teste; pipeline: Julia (colunas + legenda) → Bia (arte) → Ana (revisão)
14. Post de 5 Motivos (Instagram) → `contexto/formatos/post-5-motivos.md` — post único com tema no topo, 5 motivos de uma linha e foto lateral; limites de caracteres e cores por fundo definidos no formato; pipeline: Julia (texto + legenda) → Ana (revisão) → Bia (arte a partir do modelo no Canva)

---

## 📋 Protocolo de Pauta (Obrigatório)

A `contexto/pauta.md` é o centro de controle e o **único registro de status**. Cada conteúdo tem uma única linha que percorre as seções. Quem move:

- **Leo** → mantém o **Backlog** e a fila; só entra ideia com âncora no núcleo, aprovada pelo Hugo.
- **Slot aprovado** (seção **Briefing**: "slot aprovado, aguardando a Julia") → a Julia move para **Em Produção** ao começar, e para **Aguardando Revisão** ("aguardando a aprovação do Hugo", texto com o veredicto da Ana) ao entregar o pacote.
- **Julia** → após o OK do Hugo, move para **Design em Produção**.
- **Bia** → ao concluir a arte: sem pendências, **Pronto - Aguardando Publicação**; com ajustes manuais no Canva, **Pendente de Alteração no Canva** (com o link no `visual-spec.md` e a lista de pendências); quando o Hugo confirmar os ajustes, avança para **Pronto - Aguardando Publicação**.
- **Mari** → **Pronto - Agendado** quando o Hugo confirmar data e hora (ou o perfil mostrar); **Pronto - Publicado** quando o perfil mostrar a peça no ar. Na abertura de sessão, move sozinha o que o perfil já mostra e destaca itens em **Pendente de Alteração no Canva**.
- **Ana** não move nada.
- Nunca duplicar uma entrada. Ao iniciar uma sessão, verificar se há itens em qualquer status ativo antes de começar algo novo.

---

## 🗂️ Protocolo de Armazenamento de Conteúdos (Obrigatório)

Todos os arquivos gerados (textos, legendas, imagens, vídeos, variações) são salvos na pasta `conteudos/`, que **mora no Drive**, em `G:\Meu Drive\SB Audiovisual\03_CONTEUDO\` (decisão do Hugo, 21/10/2026: texto e mídia de cada conteúdo ficam juntos, e o repositório não guarda mais nenhum deles). Hierarquia:

```
conteudos/   (= G:\Meu Drive\SB Audiovisual\03_CONTEUDO\)
└── [slug-do-tipo]/
    └── [slug-do-titulo]/
        ├── briefing.md
        ├── texto.md
        ├── legenda.txt          (formatos de Instagram)
        ├── visual-spec.md
        ├── imagem.jpg / imagem-p1.jpg ...
        └── [outros arquivos gerados]
```

**Regras:**
- O slug de pasta é o nome do tipo ou título em minúsculas, sem acentos, com hífens no lugar de espaços (ex: `post-instagram-carrossel`, `como-escolher-o-tamanho-certo`).
- Ao definir um novo tipo de conteúdo, criar imediatamente sua pasta dentro de `conteudos/`.
- Ao aprovar um novo conteúdo, criar a pasta do título dentro da pasta do tipo e salvar todos os arquivos gerados dentro dela.
- Se um conteúdo tiver variações (ex: versão A e versão B), salvar cada uma como arquivo separado dentro da mesma pasta do título.
- **Os registros mantêm o caminho `conteudos/[tipo]/[titulo]/`** (`pauta.md`, `briefings.md`, `historico-conteudos.md`): ele equivale à pasta do Drive acima. Não criar pasta `conteudos/` no repositório.
- **Antes de salvar ou ler, conferir que o Drive está aberto** (unidade `G:`). Se a pasta não abrir, avisar o Hugo e parar; nunca salvar em outro lugar.
- Foto ou vídeo do banco (`01_PRODUTOS`, `02_GERAL`) usado numa peça: registrar o caminho do arquivo no `visual-spec.md`, em vez de copiá-lo para a pasta do conteúdo.

---

## 📊 Acesso a Plataformas de Tráfego Pago

### Meta Ads (Instagram)

Acesso via MCP da Meta disponível para outras contas vinculadas, mas **ainda não liberado para a conta Shibari Brasil** (rollout gradual do lado do Meta). Não requer configuração adicional quando liberado — o Gui conecta diretamente via MCP.

> **Nota:** o Gui atua exclusivamente na produção de anúncios (copy, estrutura de campanha, criativos). Análise de performance e dados de BigQuery não fazem parte do escopo deste projeto.

---

## 📣 Protocolo de Armazenamento de Anúncios (Obrigatório)

Todos os materiais gerados pelo Gui para campanhas pagas são salvos na pasta `anuncios/`, seguindo esta hierarquia:

```
anuncios/
└── [plataforma]/
    └── [slug-da-campanha]/
        └── [arquivos da campanha]
```

**Regras:**
- `[plataforma]` é sempre `instagram` ou `google` — em minúsculas, sem variação.
- `[slug-da-campanha]` é o nome da campanha em minúsculas, sem acentos, com hífens no lugar de espaços (ex: `lancamento-corda-juta-6mm`, `retargeting-carrinho-abandonado`).
- Ao iniciar uma nova campanha, criar imediatamente a pasta `anuncios/[plataforma]/[slug-da-campanha]/`.
- Salvar dentro da pasta os arquivos produzidos: copy, configuração de campanha, especificação de criativo, resultados de testes A/B, etc.
- Nunca misturar arquivos de plataformas diferentes na mesma pasta de campanha.

---

## 📈 Histórico de conteúdos (congelado)

O `contexto/historico-conteudos.md` registrou, até 27/10/2026, os conteúdos que chegaram a **Pronto - Aguardando Publicação**. Está **congelado**: nenhum agente adiciona linha nova, e nenhuma entrada antiga é removida. Os scripts do Leo ainda o leem para as peças antigas. O que é novo vive na `pauta.md` (aprovado em, publicado em) e no `visual-spec.md` de cada peça (campo Fundo).

---

## 🧠 Protocolo de Registro de Memória (Obrigatório)

Ao final de cada sessão de trabalho, o agente deve registrar no sistema de memória entre sessões do Claude Code qualquer informação que seja útil para sessões futuras. Registrar apenas o que não é óbvio a partir dos arquivos do projeto — preferências expressas pelo usuário, correções de rota, decisões tomadas, padrões de conteúdo que funcionaram ou não. Não registrar tarefas em andamento nem resumos do que foi feito (isso fica no histórico).

Exemplos do que registrar:
- Tom de voz ou estilo que o usuário aprovou ou rejeitou
- Decisões sobre a marca que influenciam gerações futuras
- Novos formatos definidos (além de criar o arquivo em `contexto/formatos/` e atualizar o índice em `contexto/formatos-conteudo.md`)
- Qualquer ajuste de comportamento pedido pelo usuário

---

## 🔄 Evolução do Projeto

Caso as metas da loja virtual mudem, este arquivo deve ser atualizado antes de iniciar as novas gerações. O mesmo vale para `contexto/formatos-conteudo.md` e para a lista de formatos acima.

> **Voz e contexto:** nenhum agente guarda cópia de voz, tom ou vocabulário; a fonte única é a skill `voz-shibari` (núcleo `sb_cerebro`). Posicionamento e público não ficam embutidos nas skills: os agentes apontam para `contexto/personas.md`, `contexto/loja.md` e `sb_cerebro/01_identidade/identidade.md`.

---

## 🎯 Critérios de Sucesso por Execução

Sempre que o usuário pedir para gerar um conteúdo, o agente deve garantir que:
1. **Fidelidade Comercial:** O conteúdo use exclusivamente produtos do Catálogo — Produtos (Notion) e as dores mapeadas em `contexto/loja.md`.
2. **Voz e técnica:** O texto seja escrito na voz da skill `voz-shibari` e passe pelo crivo de técnica da skill `hab-produtor-textual`. Sem emoji.
3. **Formato Correto:** Consultar o arquivo do formato correspondente em `contexto/formatos/` (ver índice em `contexto/formatos-conteudo.md`) e aplicar as especificações do tipo solicitado. Se o tipo ainda não estiver cadastrado, seguir o protocolo de novo formato antes de gerar.
4. **Formato Mobile:** Se for para redes sociais ou e-mail, o texto tenha parágrafos de no máximo 2 linhas.
5. **Pauta Atualizada:** Mover o item na `contexto/pauta.md` conforme o estado da produção avança (ver protocolo acima).
