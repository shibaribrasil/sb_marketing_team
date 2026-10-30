# SB Marketing Team — Shibari Brasil

Este projeto é um **time de marketing especialista** para a loja virtual Shibari Brasil. O time reúne agentes com habilidades específicas de marketing — geração de conteúdo orgânico, criação de peças publicitárias, anúncios pagos e gestão editorial, gestão de produtos e campanhas — operando de forma coordenada para produzir e distribuir conteúdo de alta conversão. O responsável dessa loja e operador de todo esse projeto é o Hugo Barcellos.

## Time de Agentes
O projeto opera com um time de agentes especializados, redefinido em 27/10/2026 (ver `planejamento/Motor de Conteúdo e Voz — Plano (Out 2026).md` no `sb_admin_team`). A **Mari** (`agente-coordenador`) é o ponto de entrada: lê a pauta, roteia para o agente certo e cuida da **publicação** (pacote de publicação, agendamento, status). Os demais: **Leo** (`agente-estrategista`: dono da fila e da sequência do Instagram, da leitura de resultados e das ideias, sempre ancoradas no núcleo de voz), **Julia** (`agente-escritor`: autora e dona da voz de ponta a ponta; consolida o ângulo, escreve texto e legenda e aciona a Ana), **Ana** (`agente-revisor`: segunda leitura com contexto limpo, invocada pela Julia), **Bia** (`agente-diretor-de-arte`: visual, em paralelo ao texto) e **Gui** (`agente-trafego`: anúncios; por ora como está, **anúncios são projeto à parte**). O Caio foi extinto: o briefing virou o cabeçalho do `texto.md`. A fila é puxada pelo Leo e aprovada pelo Hugo; só se produz o que está na fila. Consulte o `.claude/specs/diretrizes.md` para os comandos de cada um.

## Estrutura de Skills
- `.claude/skills/agente-*/` — código de cada membro do time (ex: `agente-coordenador`, `agente-escritor`, `agente-estrategista`)
- `estrategia/` — plano da sequência do Instagram, arquivo vivo, capas e material do Leo
- `.claude/skills/hab-*/` — habilidades especializadas carregadas pelos agentes (ex: `hab-produtor-textual`, `hab-meta-ads`)

## Especificações de Tarefas e Rotinas
O projeto conta com a pasta `.claude/specs/` que contém o arquivo `diretrizes.md`. Nesse arquivo estão as orientações de tarefas específicas e obrigatórias, como a rotina de atualização da pauta, a rotina de armazenamento de conteúdo, a rotina que estrutura novos formatos de conteúdo feitos pelo usuário e diversas outras. Além disso, características gerais dos integrantes do time estão definidas nesse arquivo. Esse arquivo define a expectativa e as regras de execução de processos dentro do projeto.

## Onde ficam os conteúdos produzidos
A produção de cada conteúdo (briefing, texto, legenda, imagens e vídeos) **não fica mais neste repositório**. Ela mora no Drive, em `G:\Meu Drive\SB Audiovisual\03_CONTEUDO\[tipo]\[titulo]\`, com texto e mídia juntos na mesma pasta. O Google Drive para computador precisa estar aberto (unidade `G:`); se a pasta não abrir, avisar o Hugo e parar, sem salvar em outro lugar.

Nos registros (`contexto/pauta.md`; `briefings.md` e `historico-conteudos.md` estão congelados) e nos formatos, o caminho `conteudos/[tipo]/[titulo]/` continua escrito assim e **equivale a essa pasta do Drive** (`conteudos/` = `03_CONTEUDO\`). Não existe pasta `conteudos/` no repositório.

Fotos e vídeos do banco (produtos, prática, acervo) ficam em `G:\Meu Drive\SB Audiovisual\` (`01_PRODUTOS`, `02_GERAL`); ao usar um arquivo do banco, registrar o caminho no `visual-spec.md`. O que não é mídia (`contexto/`, `assets/docs`, `.claude/`) continua neste repositório. Regras do banco: `LEIA-ME.md` na raiz do `SB Audiovisual`.

## Voz (Hugo, 27/10/2026)
A voz da marca mora no núcleo `sb_cerebro`, e a skill `voz-shibari` a carrega. **Antes de escrever, revisar ou aprovar qualquer texto, carregue a `voz-shibari`**; ela vence qualquer resumo de tom embutido nas skills dos agentes. O antigo `contexto/tom-de-voz.md` foi apagado em 27/10/2026. Os repositórios `sb_admin_team`, `sb_marketing_team` e `sb_cerebro` precisam estar clonados lado a lado e atualizados.

## Produtos: o marketing não gerencia produto (Hugo, 27/10/2026)
O time de marketing **não cadastra, não descreve nem define produto**. Isso é do **cadastrador** (projeto `sb_admin_team`). Para saber a descrição, as características, o diferencial ou o uso de **qualquer produto da loja**, consulte o **Notion**, na base **Catálogo — Produtos** (database `f8dbad60-7e2a-45b9-ac22-cbebe11420d4`; hub "Catálogo — Base de Produtos"). Ela cobre todos os produtos. Fato que faltar no Notion vai ao Hugo; nunca se inventa dado de produto.

## Acesso ao Notion (vale para todo mundo que clonar o repositório)
O acesso é por MCP e está **configurado no repositório**: o `.mcp.json` declara o servidor `notion` e o `.claude/settings.json` libera só as ferramentas de **leitura** (`notion-fetch`, `notion-search`, `notion-query-data-sources`). O servidor já vem habilitado (`enableAllProjectMcpServers`); na primeira vez, autenticar com `/mcp` (login no Notion com uma conta que enxergue o workspace da Shibari Brasil). O time **só lê** o Notion; nenhum agente cria ou edita página lá. Se o Notion não responder, parar e avisar o Hugo, sem inventar dado.

## Ressalva: caminhos fixos da máquina do Hugo
Só o Hugo roda os scripts de `scripts/` (hook de início de sessão). Eles têm caminhos da máquina dele gravados: `sincronizar_fila.py` lê o plano em `C:\Users\HTK1562\Documents\GitHub\sb_admin_team\planejamento\sequencia-instagram-plano.json` (sobrescrevível pela variável `SB_PLANO_JSON`), e `status_instagram.py` usa o Python de `C:\Users\HTK1562\venvs\sb_relatorios` (variável `SB_VENV_PYTHON`) e a pasta de scripts do `analista-de-dados` no `sb_admin_team`. **Se o Hugo trocar de máquina ou de usuário do Windows, ajustar esses caminhos antes de abrir a sessão** (ou definir as variáveis); sem isso o hook falha ou a fila deixa de atualizar.

## Comportamento do Agente
1. Toda entrada do usuário deve ser triada pela **Mari** para garantir que ela acionará o agente correto para seguir com a tarefa.
2. A pasta `contexto/` tem todas as informações da loja, da marca e dos formatos de conteúdo.
3. Depois da triagem feita pela **Mari** e pela interação com o usário, o agente que será o responsável pela tarefa deve seguir estritamente os parâmetros de sua função.
4. É necessário questionar o usuário a todo momento sobre a personalização das tarefas, afim de aprender e melhorar a produção a partir das skills.
5. Manter `contexto/pauta.md` (único registro de status) atualizada a cada mudança de status, como orientado na skill de cada agente. `contexto/briefings.md` e `contexto/historico-conteudos.md` estão **congelados desde 27/10/2026**: ninguém adiciona entrada.
6. Antes de salvar ou ler qualquer conteúdo, conferir que a pasta do Drive abre (ver "Onde ficam os conteúdos produzidos").

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- When graphify-out/graph.json exists, run `graphify query "<question>"` before your first grep, search or source-file read for a codebase question, and put this rule in every subagent prompt that explores code. Read raw files only for lines the graph or an earlier read already located. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
- **Regra do projeto (Hugo, 28/10/2026): grafo sempre em dia.** Depois de **cada commit feito na sessão**, invocar a skill `graphify` com `. --update` (incremental: só reprocessa o que mudou, e sem mudança não gasta nada). Isso cobre os `.md` e os scripts. Antes de rodar, dizer ao Hugo quantos arquivos serão reprocessados. O `graphify-out/` é versionado (grafo, relatório e cache); depois de atualizar o grafo, incluir as mudanças dele no próximo commit. Os arquivos locais da máquina (`.graphify_python`, `.graphify_root`, `cache/hook_sessions/`) ficam no `.gitignore`. Commit feito fora da sessão não dispara a regra; a **Mari** cobre isso ao ler a pauta (ver `agente-coordenador`).
- A committed graphify-out/graph.json is rewritten whole on every build, so a large diff to it in a pull request is expected. Do not flag it as churn or suggest skipping the graph rebuild or its hooks.
