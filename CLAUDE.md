# SB Marketing Team — Shibari Brasil

Este projeto é um **time de marketing especialista** para a loja virtual Shibari Brasil. O time reúne agentes com habilidades específicas de marketing — geração de conteúdo orgânico, criação de peças publicitárias, anúncios pagos e gestão editorial, gestão de produtos e campanhas — operando de forma coordenada para produzir e distribuir conteúdo de alta conversão. O responsável dessa loja e operador de todo esse projeto é o Hugo Barcellos.

## Time de Agentes
O projeto opera com um time de agentes especializados. A **Mari** (`agente-coordenador`) é o ponto de entrada de tudo — ela lê a pauta e o contexto de sessões anteriores e roteia para o membro certo. É ela que vai interpretar o pedido do Hugo (usuário) e vai direcionar ao agente especializado. Os demais membros são: **Leo** (pescador), **Caio** (redator), **Julia** (escritora), **Bia** (diretora de arte), **Ana** (revisora), **Gui** (tráfego pago) e **Pedro** (gerente de produto). Consulte o `.claude/specs/diretrizes.md` para os comandos de cada um.

## Estrutura de Skills
- `.claude/skills/agente-*/` — código de cada membro do time (ex: `agente-coordenador`, `agente-escritor`)
- `.claude/skills/hab-*/` — habilidades especializadas carregadas pelos agentes (ex: `hab-produtor-textual`, `hab-leitor-pdf`)

## Especificações de Tarefas e Rotinas
O projeto conta com a pasta `.claude/specs/` que contém o arquivo `diretrizes.md`. Nesse arquivo estão as orientações de tarefas específicas e obrigatórias, como a rotina de atualização da pauta, a rotina de armazenamento de conteúdo, a rotina que estrutura novos formatos de conteúdo feitos pelo usuário e diversas outras. Além disso, características gerais dos integrantes do time estão definidas nesse arquivo. Esse arquivo define a expectativa e as regras de execução de processos dentro do projeto.

## Comportamento do Agente
1. Toda entrada do usuário deve ser triada pela **Mari** para garantir que ela acionará o agente correto para seguir com a tarefa.
2. A pasta `contexto/` tem todas as informações da loja, da marca e dos formatos de conteúdo.
3. Depois da triagem feita pela **Mari** e pela interação com o usário, o agente que será o responsável pela tarefa deve seguir estritamente os parâmetros de sua função.
4. É necessário questionar o usuário a todo momento sobre a personalização das tarefas, afim de aprender e melhorar a produção a partir das skills.
5. Manter `contexto/pauta.md` atualizada a cada mudança de status de uma tarefa, como orientado na skill de cada agente.