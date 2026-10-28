# SB Marketing Team — Shibari Brasil

Este projeto é um **time de marketing especialista** para a loja virtual Shibari Brasil. O time reúne agentes com habilidades específicas de marketing — geração de conteúdo orgânico, criação de peças publicitárias, anúncios pagos e gestão editorial, gestão de produtos e campanhas — operando de forma coordenada para produzir e distribuir conteúdo de alta conversão. O responsável dessa loja e operador de todo esse projeto é o Hugo Barcellos.

## Time de Agentes
O projeto opera com um time de agentes especializados. A **Mari** (`agente-coordenador`) é o ponto de entrada de tudo — ela lê a pauta e o contexto de sessões anteriores e roteia para o membro certo. É ela que vai interpretar o pedido do Hugo (usuário) e vai direcionar ao agente especializado. Os demais membros são: **Leo** (pescador), **Caio** (redator), **Julia** (escritora), **Bia** (diretora de arte), **Ana** (revisora) e **Gui** (tráfego pago). Consulte o `.claude/specs/diretrizes.md` para os comandos de cada um.

## Estrutura de Skills
- `.claude/skills/agente-*/` — código de cada membro do time (ex: `agente-coordenador`, `agente-escritor`)
- `.claude/skills/hab-*/` — habilidades especializadas carregadas pelos agentes (ex: `hab-produtor-textual`, `hab-leitor-pdf`)

## Especificações de Tarefas e Rotinas
O projeto conta com a pasta `.claude/specs/` que contém o arquivo `diretrizes.md`. Nesse arquivo estão as orientações de tarefas específicas e obrigatórias, como a rotina de atualização da pauta, a rotina de armazenamento de conteúdo, a rotina que estrutura novos formatos de conteúdo feitos pelo usuário e diversas outras. Além disso, características gerais dos integrantes do time estão definidas nesse arquivo. Esse arquivo define a expectativa e as regras de execução de processos dentro do projeto.

## Onde ficam os conteúdos produzidos
A produção de cada conteúdo (briefing, texto, legenda, imagens e vídeos) **não fica mais neste repositório**. Ela mora no Drive, em `G:\Meu Drive\SB Audiovisual\03_CONTEUDO\[tipo]\[titulo]\`, com texto e mídia juntos na mesma pasta. O Google Drive para computador precisa estar aberto (unidade `G:`); se a pasta não abrir, avisar o Hugo e parar, sem salvar em outro lugar.

Nos registros (`contexto/pauta.md`, `contexto/briefings.md`, `contexto/historico-conteudos.md`) e nos formatos, o caminho `conteudos/[tipo]/[titulo]/` continua escrito assim e **equivale a essa pasta do Drive** (`conteudos/` = `03_CONTEUDO\`). Não existe pasta `conteudos/` no repositório.

Fotos e vídeos do banco (produtos, prática, acervo) ficam em `G:\Meu Drive\SB Audiovisual\` (`01_PRODUTOS`, `02_GERAL`); ao usar um arquivo do banco, registrar o caminho no `visual-spec.md`. O que não é mídia (`contexto/`, `assets/docs`, `.claude/`) continua neste repositório. Regras do banco: `LEIA-ME.md` na raiz do `SB Audiovisual`.

## Voz (Hugo, 27/10/2026)
A voz da marca mora no núcleo `sb_cerebro`, e a skill `voz-shibari` a carrega. **Antes de escrever, revisar ou aprovar qualquer texto, carregue a `voz-shibari`**; ela vence o `contexto/tom-de-voz.md` e qualquer resumo de tom embutido nas skills dos agentes. Os repositórios `sb_admin_team`, `sb_marketing_team` e `sb_cerebro` precisam estar clonados lado a lado e atualizados.

## Produtos: o marketing não gerencia produto (Hugo, 27/10/2026)
O time de marketing **não cadastra, não descreve nem define produto**. Isso é do **cadastrador** (projeto `sb_admin_team`). Para saber a descrição, as características, o diferencial ou o uso de **qualquer produto da loja**, consulte o **Notion**, na base **Catálogo — Produtos** (database `f8dbad60-7e2a-45b9-ac22-cbebe11420d4`; hub "Catálogo — Base de Produtos"). Ela cobre todos os produtos, e não só os que o time definia internamente. A pasta `produtos/` deste repositório foi apagada. O arquivo `contexto/produtos.md` e o agente Pedro (`agente-gerente-produto`) foram **extintos em 27/10/2026**.

## Comportamento do Agente
1. Toda entrada do usuário deve ser triada pela **Mari** para garantir que ela acionará o agente correto para seguir com a tarefa.
2. A pasta `contexto/` tem todas as informações da loja, da marca e dos formatos de conteúdo.
3. Depois da triagem feita pela **Mari** e pela interação com o usário, o agente que será o responsável pela tarefa deve seguir estritamente os parâmetros de sua função.
4. É necessário questionar o usuário a todo momento sobre a personalização das tarefas, afim de aprender e melhorar a produção a partir das skills.
5. Manter `contexto/pauta.md` atualizada a cada mudança de status de uma tarefa, como orientado na skill de cada agente.
6. Antes de salvar ou ler qualquer conteúdo, conferir que a pasta do Drive abre (ver "Onde ficam os conteúdos produzidos").