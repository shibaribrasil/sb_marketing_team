# Especificações de Execução de Tarefas e Rotinas do Marketing Team - Shibari Brasil

Este arquivo define os critérios de aceitação, os passos obrigatórios que o agente deve seguir em cada ciclo de trabalho e os comandos de uso do projeto.

---

## 👥 Time de Agentes

A produção das tarefas é dividida entre agentes especializados. Cada um tem uma função clara, um status de pauta correspondente e um momento certo de ser acionado:

| Nome | Função | O que faz | Quando acionar | Skill | Status que gerencia |
|---|---|---|---|---|---|
| **Mari** | Coordenadora | Dá o panorama geral, retoma contexto de sessões anteriores e roteia para o membro certo | Para começar qualquer sessão ou quando não souber por onde ir | `agente-coordenador` | Todos — ponto de entrada e roteamento |
| **Leo** | Pescador | Pesquisa tendências e referências, registra ideias no Backlog | Quando quiser novas ideias de conteúdo | `agente-pescador` | Backlog |
| **Caio** | Redator | **Estágio 1:** desdobra territórios do Leo em múltiplas ideias de conteúdo e as registra no banco (`contexto/briefings.md`). **Estágio 2:** desenvolve o briefing completo de uma ideia selecionada pelo Hugo e a move para o pipeline de produção | Quando um território novo entrar no Backlog (Estágio 1) ou quando Hugo selecionar uma ideia do banco para produzir (Estágio 2) | `agente-redator` | Briefing |
| **Julia** | Escritora | Escreve o texto seguindo o briefing e as regras da marca | Quando um briefing estiver aprovado | `agente-escritor` | Em Produção |
| **Ana** | Revisora | Revisa o texto junto com o usuário, aprova ou devolve com instruções. Trabalha somente sobre o `texto.md` — a aprovação visual é feita diretamente pelo Hugo no Canva. | Quando o texto estiver pronto (antes do design) | `agente-revisor` | Aguardando Revisão → Design em Produção |
| **Bia** | Diretora de Arte | Produz a direção visual completa, gera prompts e referências para ferramentas de criação. Quando o design passa pelo Canva, registra o link no `visual-spec.md`. Se houver ajustes manuais pendentes, lista-os em seção "Pendências no Canva" e move para **Pendente de Alteração no Canva** em vez de Pronto - Aguardando Publicação. | Quando o texto for aprovado pela Ana | `agente-diretor-de-arte` | Design em Produção → Pendente de Alteração no Canva (com pendências) ou Pronto - Aguardando Publicação (sem pendências) |
| **Gui** | Tráfego Pago | Criação e otimização de anúncios pagos em dois canais: **Instagram** (Meta Ads) e **Google Ads**. Identifica a plataforma e carrega a skill correspondente (`hab-meta-ads` para Instagram; `hab-google-ads` para Google). Pode ser acionado a qualquer momento, independente do pipeline orgânico | Quando quiser trabalhar com campanhas pagas | `agente-trafego` + skill da plataforma | *(sem status fixo — atua em paralelo)* |
| **Pedro** | Gerente de Produto | Mantém o catálogo da loja, cria descrições de produto e identifica quais produtos têm gancho orgânico com o conteúdo em produção — pode ser acionado pelo usuário ou por qualquer agente do time | Quando quiser trabalhar com produtos, criar descrições ou verificar encaixe de produto em um conteúdo | `agente-gerente-produto` | *(sem status fixo — atua em paralelo)* |

Cada agente lê os arquivos de contexto relevantes e atualiza a pauta ao concluir sua etapa. As instruções completas de cada um estão em `.claude/skills/[nome-do-agente]/SKILL.md`.

**Fluxo completo do pipeline:**
```
Leo (território no Backlog)
  ↓
Caio — Estágio 1: desdobra em ideias → registra em contexto/briefings.md (🗂 Backlog)
  ↓
Hugo seleciona uma ideia do banco
  ↓
Caio — Estágio 2: desenvolve briefing.md completo → move para pipeline (📄 Briefing criado)
  ↓
Julia (Em Produção) → Ana (Aguardando Revisão) → [aprovado] Design em Produção → Bia → [sem pendências] Pronto - Aguardando Publicação → Pronto - Agendado (com data) → Pronto - Publicado
                                                                                                              → [com pendências] Pendente de Alteração no Canva → [Hugo confirma] → Pronto - Aguardando Publicação → Pronto - Agendado (com data) → Pronto - Publicado
```

O banco de briefings (`contexto/briefings.md`) é permanente e cresce continuamente. Cada território do Leo pode gerar múltiplas ideias no banco. As ideias saem do banco para o pipeline apenas quando Hugo selecionar uma para produção.

---

## 🗂️ Estrutura de Arquivos

```
├── CLAUDE.md                    → instruções de comportamento do agente
├── memory.md                    → aprendizados acumulados entre sessões
│
├── contexto/
│   ├── historico-conteudos.md   → registro permanente de todos os conteúdos aprovados
│   ├── loja.md                  → informações da Shibari Brasil
│   ├── personas.md              → perfis do público-alvo
│   ├── tom-de-voz.md            → como a marca fala
│   ├── referencias.md           → referências de estilo e campanhas
│   ├── formatos-conteudo.md     → índice dos formatos cadastrados
│   ├── formatos/                → um arquivo .md por formato de conteúdo
│   ├── briefings.md             → banco permanente de ideias briefadas pelo Caio (cresce continuamente)
│   └── pauta.md                 → backlog de territórios, produções em andamento e prontos
│
├── conteudos/
│   └── [tipo]/
│       └── [titulo]/            → arquivos do conteúdo orgânico (texto, imagens, variações)
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

Para que o agente gere conteúdo alinhado com a Shibari Brasil, os arquivos abaixo precisam estar preenchidos. Enquanto estiverem vazios, o conteúdo gerado será genérico.

| Arquivo | O que colocar | Prioridade |
|---|---|---|
| `contexto/loja.md` | Produtos, público, dores, diferenciais da loja | Alta |
| `contexto/personas.md` | Perfis detalhados do cliente ideal | Alta |
| `contexto/tom-de-voz.md` | Como a marca fala, o que nunca diz, exemplos | Média |
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

**Escolher uma ideia do backlog para produzir:**
```
Produzir ideia do backlog: [título ou tema da ideia]
```
O agente move o item para **Em Produção**, cria a pasta correspondente em `conteudos/` e inicia a geração.

---

### Acionar Agentes

**Pesquisar novas ideias:**
```
Pesquisar ideias de conteúdo
```
Aciona o Leo (Pescador). Ele pesquisa referências e tendências e registra as ideias no Backlog.

**Ver ideias no banco do Caio:**
```
Ver banco de briefings
```
Caio lista as ideias registradas em `contexto/briefings.md` com status e formato, organizadas por território.

**Desdobrar um território em ideias (Estágio 1 do Caio):**
```
Caio, desdobra o território: [nome do território]
```
Aciona o Caio (Estágio 1). Ele gera 2 a 4 ideias distintas de conteúdo a partir do território e as registra em `contexto/briefings.md` com status Backlog.

**Produzir uma ideia do banco (Estágio 2 do Caio):**
```
Produzir: [C-XXX ou título da ideia]
```
Aciona o Caio (Estágio 2). Ele desenvolve o briefing completo, cria a pasta do conteúdo e move a ideia para o pipeline de produção.

**Escrever o conteúdo:**
```
Escrever conteúdo: [título]
```
Aciona a Julia (Escritora). Ela lê o briefing e produz o texto final seguindo as regras da marca.

**Revisar o texto:**
```
Revisar: [título]
```
Aciona a Ana (Revisora). Ela analisa o texto, apresenta o relatório e aguarda a decisão do usuário. A aprovação visual é feita pelo Hugo diretamente no Canva após a Bia entregar o design.

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

**Trabalhar com produtos (cadastrar, descrever, identificar encaixe em conteúdo):**
```
Produto: [o que precisa]
```
Exemplos: `Produto: cadastrar produto novo`, `Produto: qual produto encaixa no conteúdo sobre iniciantes`, `Produto: criar descrição do [nome do produto]`.
Aciona o Pedro (Gerente de Produto). Ele trabalha em paralelo ao time e também pode ser consultado por outros agentes durante a produção para identificar produtos com gancho orgânico para o conteúdo em desenvolvimento.

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

1. Abrir o projeto no Claude Code
2. Digitar `Ver pauta` ou acionar a Mari para checar o que está em andamento (ela lê pauta + briefings.md)
3. **Se quiser novas ideias:** acionar Leo → Leo registra territórios → Caio desdobra em banco de briefings (Estágio 1)
4. **Se quiser avançar na produção:** escolher uma ideia do banco → Caio desenvolve briefing completo (Estágio 2) → Julia escreve → Ana revisa o texto → Bia faz o visual → Hugo aprova no Canva
5. Revisar e aprovar o conteúdo final
6. Os agentes atualizam pauta, briefings.md e histórico conforme avançam

---

## 📋 Tipos de Conteúdo Suportados

Os formatos são definidos de forma incremental. Cada formato tem seu próprio arquivo em `contexto/formatos/`. A cada novo tipo de conteúdo criado, o agente:
1. Levanta as especificações com o usuário (objetivo, plataforma, tamanho, CTA).
2. Cria um novo arquivo `contexto/formatos/[slug-do-formato].md` com as especificações levantadas (usar o modelo em `contexto/formatos-conteudo.md`).
3. Adiciona o nome do tipo na lista abaixo e no índice `contexto/formatos-conteudo.md`.
4. Cria uma pasta para o tipo dentro de `conteudos/` (ver protocolo abaixo).
5. Gera o conteúdo seguindo as especificações recém-definidas.

**Formatos cadastrados:**
1. Post para Blog → `contexto/formatos/post-para-blog.md`
2. Post de Frase → `contexto/formatos/post-de-frase.md`
3. Post Por Trás do Desejo → `contexto/formatos/post-por-tras-do-desejo.md`
4. Post Inspiração de Amarração → `contexto/formatos/post-inspiracao-de-amarracao.md`
5. Carrossel Livre → `contexto/formatos/carrossel-livre.md`
6. Descrição de Produto — Site, versão antiga → `contexto/formatos/descricao-de-produto-old.md` — substituído pelo formato 7
7. Descrição de Produto — Site → `contexto/formatos/descricao-de-produto.md` — padrão ativo desde 19/06/2026
8. Post Desatando Mitos (Instagram) → `contexto/formatos/post-desatando-mitos.md`
9. Post de Foto (Instagram) → `contexto/formatos/post-de-foto.md` — foto do acervo pessoal movida de `assets/arquivo/Post de Fotos - A Publicar/`; pipeline direto: Julia (legenda) → Ana (revisão) → Publicação

---

## 📄 Protocolo de Leitura de PDFs (Obrigatório)

Toda vez que o usuário pedir para ler ou consultar um arquivo PDF — seja diretamente ou indiretamente durante uma tarefa — o agente deve acionar a skill `hab-leitor-pdf` **antes de tentar acessar o PDF**.

A skill verifica se já existe um arquivo markdown espelho (`.md`) com o mesmo nome na mesma pasta do PDF. Se existir, usa o markdown. Se não existir, extrai o texto do PDF e cria o espelho.

**Nunca ler ou citar um PDF diretamente sem passar pela skill.**

Exemplos de situações que ativam este protocolo:
- Usuário pede: "lê o guia da marca a partir da página X"
- Agente precisa consultar um documento técnico em PDF para embasar uma decisão
- Qualquer referência a `assets/docs/[nome].pdf` durante a produção

---

## 📋 Protocolo de Pauta (Obrigatório)

A `contexto/pauta.md` é o centro de controle de toda produção. O agente deve:

- **Ao iniciar uma sessão:** verificar se há itens em qualquer status ativo antes de começar algo novo.
- **Pescador** → adiciona território em **Backlog** de `pauta.md`
- **Redator (Estágio 1)** → lê território do Backlog e registra ideias desdobradas em `contexto/briefings.md` (sem mover nada na pauta ainda)
- **Redator (Estágio 2)** → quando Hugo selecionar uma ideia do banco, desenvolve o briefing completo, cria pasta e `briefing.md` em `conteudos/`, move para **Briefing** na pauta e atualiza o status em `briefings.md` para **Briefing criado**
- **Escritor** → move de Briefing para **Em Produção** durante a escrita, depois para **Aguardando Revisão** ao concluir; atualiza status em `briefings.md`
- **Revisor** → move de **Aguardando Revisão** para **Design em Produção** após aprovação textual pelo usuário, ou devolve para **Em Produção** com instruções de correção para a Julia; atualiza o status da peça em `contexto/briefings.md` para **🎨 Design em Produção** (se tiver código C-XXX)
- **Diretor de Arte** → ao concluir a produção visual:
  - Se o design não tiver pendências manuais: move para **Pronto - Aguardando Publicação**; atualiza `contexto/briefings.md` para **✅ Aguardando Publicação**; adiciona entrada em `contexto/historico-conteudos.md` com código, título, tipo, **fundo** (nome da cor conforme `visual-spec.md`, ou `—` se não houver), data de aprovação (hoje) e "Publicado em: —"; **se o conteúdo for para o Instagram**, cria também entrada no banco de dados Notion "Histórico Instagram" (data source ID: `63ad0101-4eaf-4995-9c3e-f76e8fffea6c`) com os mesmos campos
  - Se o design tiver ajustes manuais pendentes no Canva (ex: cor de fundo, formatação parcial de texto): move para **Pendente de Alteração no Canva**, registra o link do Canva no `visual-spec.md` e lista as pendências em seção "⚠️ Pendências no Canva"
- **Usuário** → ao confirmar que fez os ajustes manuais no Canva: item avança diretamente para **Pronto - Aguardando Publicação**; Bia então atualiza `contexto/briefings.md` e `contexto/historico-conteudos.md` (incluindo o campo Fundo) e, se for Instagram, cria entrada no Notion conforme acima
- **Coordenadora** → quando o usuário confirmar data de publicação: move de Pronto - Aguardando Publicação para **Pronto - Agendado**; atualiza a entrada correspondente no Notion ♊ Histórico Instagram (data source ID: `63ad0101-4eaf-4995-9c3e-f76e8fffea6c`) com a data de publicação agendada; atualiza `contexto/briefings.md` para **📅 Agendado (DD/MM)**. Quando o usuário confirmar postagem: move para **Pronto - Publicado**; preenche "Publicado em" em `contexto/historico-conteudos.md`; atualiza `contexto/briefings.md` para **✅ Publicado (DD/MM)**. Na abertura de sessão: (1) move automaticamente para **Pronto - Publicado** qualquer item em **Pronto - Agendado** cuja data já chegou ou passou — sem precisar de confirmação do usuário — registrando a data de agendamento como "Publicado em" no `historico-conteudos.md` e atualizando `briefings.md` para **✅ Publicado (DD/MM)** se tiver código C-XXX; (2) destaca itens em **Pendente de Alteração no Canva** com o link direto e lista das pendências
- Nunca duplicar uma entrada — cada conteúdo tem uma única linha que percorre o pipeline.

---

## 🗂️ Protocolo de Armazenamento de Conteúdos (Obrigatório)

Todos os arquivos gerados (textos, imagens, variações) são salvos na pasta `conteudos/`, seguindo esta hierarquia:

```
conteudos/
└── [slug-do-tipo]/
    └── [slug-do-titulo]/
        ├── texto.md
        └── [outros arquivos gerados]
```

**Regras:**
- O slug de pasta é o nome do tipo ou título em minúsculas, sem acentos, com hífens no lugar de espaços (ex: `post-instagram-carrossel`, `como-escolher-o-tamanho-certo`).
- Ao definir um novo tipo de conteúdo, criar imediatamente sua pasta dentro de `conteudos/`.
- Ao aprovar um novo conteúdo, criar a pasta do título dentro da pasta do tipo e salvar todos os arquivos gerados dentro dela.
- Se um conteúdo tiver variações (ex: versão A e versão B), salvar cada uma como arquivo separado dentro da mesma pasta do título.

---

## 📊 Acesso a Dados de Tráfego Pago

### Google Ads — BigQuery

Os dados de performance do Google Ads estão disponíveis via BigQuery. O Gui acessa diretamente via CLI (`bq`). Antes de qualquer query, configurar o projeto:

```powershell
gcloud config set project igneous-sandbox-381622
```

| Parâmetro | Valor |
|---|---|
| **Conta autenticada** | `lojashibaribrasil@gmail.com` |
| **Projeto GCP** | `igneous-sandbox-381622` |
| **Dataset** | `datalake_google_ads` |
| **ID da conta Ads** | `4241689372` (sufixo de todas as tabelas) |

**Relatório de diagnóstico:** `relatorios/diagnostico-google-ads/relatorio-diagnostico.html` — sempre o relatório mais recente. Cada geração também cria uma cópia datada `relatorio-YYYY-MM-DD.html`. O arquivo `relatorios/diagnostico-google-ads/index.html` lista todos os relatórios gerados para comparação histórica.

### Meta Ads (Instagram)

Acesso via MCP da Meta disponível para outras contas vinculadas, mas **ainda não liberado para a conta Shibari Brasil** (rollout gradual do lado do Meta). Não requer configuração adicional quando liberado — o Gui conecta diretamente via MCP.

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

## 📈 Protocolo de Registro de Histórico (Obrigatório)

O arquivo `contexto/historico-conteudos.md` registra de forma permanente todos os conteúdos que chegaram a **Pronto - Aguardando Publicação**. Nenhuma entrada deve ser removida.

**Responsabilidades:**
- **Bia (Diretor de Arte):** quando mover o item para Pronto - Aguardando Publicação (ou quando o usuário confirmar os ajustes no Canva), adicionar a linha no **topo** da tabela com: Código, Título, Tipo, Fundo (nome da cor conforme `visual-spec.md`, ou `—` se não houver), Aprovado em (data atual), Publicado em: `—` e caminho do arquivo. **Se o conteúdo for para o Instagram** (qualquer tipo exceto Post para Blog), criar também entrada no banco de dados Notion "Histórico Instagram" (data source ID: `63ad0101-4eaf-4995-9c3e-f76e8fffea6c`) com Nome do conteúdo, Tipo de conteúdo, Fundo e Data de postagem em branco.
- **Mari (Coordenadora):** quando o usuário confirmar postagem, preencher a coluna "Publicado em" na linha correspondente do `historico-conteudos.md` e atualizar o campo "Data de postagem" no Notion.

**Formato da linha:**
| Código | Título | Tipo | Fundo | Aprovado em | Publicado em | Arquivo |
|---|---|---|---|---|---|---|
| C-XXX | Título completo | Tipo do formato | Nome da cor `#hex` | DD/MM/AAAA | — | `conteudos/[caminho]/` |

---

## 🧠 Protocolo de Registro de Memória (Obrigatório)

Ao final de cada sessão de trabalho, o agente deve atualizar o arquivo `memory.md` na raiz do projeto com qualquer informação que seja útil para sessões futuras. Registrar apenas o que não é óbvio a partir dos arquivos do projeto — preferências expressas pelo usuário, correções de rota, decisões tomadas, padrões de conteúdo que funcionaram ou não. Não registrar tarefas em andamento nem resumos do que foi feito (isso fica no histórico).

Exemplos do que registrar:
- Tom de voz ou estilo que o usuário aprovou ou rejeitou
- Decisões sobre a marca que influenciam gerações futuras
- Novos formatos definidos (além de criar o arquivo em `contexto/formatos/` e atualizar o índice em `contexto/formatos-conteudo.md`)
- Qualquer ajuste de comportamento pedido pelo usuário

---

## 🔄 Evolução do Projeto

Caso as metas da loja virtual mudem, este arquivo deve ser atualizado antes de iniciar as novas gerações. O mesmo vale para `contexto/formatos-conteudo.md` e para a lista de formatos acima.

> ⚠️ **Nota de manutenção — skills com contexto embutido:** Para reduzir o carregamento de contexto por sessão, vários skills de agentes (`agente-redator`, `agente-escritor`, `agente-revisor`, `agente-pescador`, `agente-diretor-de-arte`, `agente-trafego`) contêm resumos embutidos de arquivos como `contexto/loja.md`, `contexto/personas.md` e `contexto/tom-de-voz.md`. Se qualquer um desses arquivos for atualizado, verificar os skills correspondentes e atualizar os resumos embutidos onde as mudanças forem relevantes para o trabalho de cada agente.

---

## 🎯 Critérios de Sucesso por Execução

Sempre que o usuário pedir para gerar um conteúdo, o agente deve garantir que:
1. **Fidelidade Comercial:** O conteúdo use exclusivamente os produtos e dores mapeados em `contexto/loja.md`.
2. **Estilo Antirrobô:** O texto passe obrigatoriamente pelo crivo da skill `hab-produtor-textual`.
3. **Formato Correto:** Consultar o arquivo do formato correspondente em `contexto/formatos/` (ver índice em `contexto/formatos-conteudo.md`) e aplicar as especificações do tipo solicitado. Se o tipo ainda não estiver cadastrado, seguir o protocolo de novo formato antes de gerar.
4. **Formato Mobile:** Se for para redes sociais ou e-mail, o texto tenha parágrafos de no máximo 2 linhas.
5. **Pauta Atualizada:** Mover o item na `contexto/pauta.md` conforme o estado da produção avança (ver protocolo acima).
