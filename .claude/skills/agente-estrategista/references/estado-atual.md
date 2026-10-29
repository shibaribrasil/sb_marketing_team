# Estado atual — Leo (estrategista de conteúdo)

> Foto de **27/10/2026**, feita na migração do antigo `especialista-instagram`. Atualize ao fim de toda sessão em que algo mudar: data, o que mudou, próxima ação. O diário completo da fase anterior (07/10 a 24/10/2026) está em `estrategia/historico-especialista-instagram.md`; consulte só quando precisar do detalhe.

## O que existe

- **Dados:** extrator do Instagram e do Meta Ads no ar (`sb_data_pipeline`, function `instagram`, 3 extrações por dia: 07:50, 13:50 e 21:50), modelos dbt `tb_instagram_*` na camada az e página "Instagram" no Streamlit (Semana, Peças, Anúncios, Audiência e atendimento). As 13 consultas prontas estão em `consultas-instagram.md` (admin).
- **Fila e sequência:** plano em `estrategia/sequencia-instagram-plano.json` (versão v11, rascunho não aprovado, de 22/10/2026) e arquivo vivo `estrategia/Sequência de Conteúdo Instagram.md`. `scripts/sincronizar_fila.py` copia a fila para a `pauta.md` no início de cada sessão.
- **Artefato visual da sequência:** https://claude.ai/artifact/DR9doaKArQHDPQPfJQFRj4 (grade do feed e produção). Gerado por `scripts/gerar_artefato_sequencia.py`. **Desatualizado:** ainda cita o Pedro; será atualizado no fim da reestruturação do marketing.
- **Conhecimento da plataforma:** `algoritmo-e-plataforma.md` e `risco-de-alcance-nicho.md` (pesquisa de 07/out/2026; refazer se passar de 45 dias).
- **Núcleo de voz (`sb_cerebro`)** com 80 posições, `identidade.md`, `voz.md`, estudos do Instagram (rodadas 1 e 2) e biblioteca inicial.

## O que a leitura de resultados já mostrou (não refazer sem motivo)

- Todas as peças do topo por envio e salvamento são **carrossel**; o de 28/09 ("shibari, kinbaku e bondage não são a mesma coisa") lidera.
- O melhor orgânico recente é um **post escrito pelo Hugo, sem IA** (12/10/2026): humor de dentro do meio e identificação.
- Texto de IA aprovado com falha ("conteúdo certo, texto reprovado") em 3 de 6 carrosséis lidos; lista de referências para aprender salva muito.
- Peça impulsionada inclui o pago em views e alcance: nunca comparar com orgânica sem separar. O ROAS real do Meta (por UTM) fica muito abaixo do reportado pelo próprio Meta.
- Em 2024 a marca escrevia "4m4rr4ções" para escapar de restrição; o Hugo prefere a censura com asterisco (P34).

## Pendências abertas

1. **Fila:** a v11 segue como rascunho; o Hugo aprova na sexta. Slot X1 (Time doce × Time travessura) agendado no mLabs para sáb 31/10, hora ainda a confirmar.
2. **Leitura do Reel de 23/10** em 72 h e **do teste de públicos em 03/11** (assunto de anúncios; registrado no histórico, tratado no projeto de anúncios).
3. **Status da conta** (elegibilidade) ainda não verificado no Painel; linha de base de seguidores e views é de 07/10/2026 e precisa ser refeita pelo BigQuery.
4. **Backlog:** consolidar `pauta.md` (Backlog) e `briefings.md` (112 ideias, 23 publicadas) num backlog único e **podar** o que não tem âncora no núcleo, com a lista aprovada pelo Hugo. Só depois de o time estar redefinido.
5. **Publicador por API** (projeto à parte no `sb_data_pipeline`, com prioridade, porque o mLabs tem custo): hoje só em worktree, sem tabela, função, Scheduler nem Reels. Até lá, o Hugo agenda no mLabs.
6. **Artefato:** regenerar e republicar no fim da migração; depois automatizar (tarefa agendada local com detecção de mudança e, no médio prazo, a grade no Streamlit).
7. **Ciclo de aprendizado:** a cada rodada de resultados, propor uma nota para `sb_cerebro/05_conhecimento`.

## Registro de mudanças

- **27/10/2026:** papel migrado do `especialista-instagram` (admin) para o Leo (`agente-estrategista`, marketing). Plano, arquivo vivo, capas e material foram movidos para `estrategia/`; `sincronizar_fila.py` passou a ler o plano dentro do repositório. Consultas do BigQuery e documentação da API da Meta ficaram no admin. Regra nova: toda ideia cita âncora no núcleo.

- **28/10/2026:** sequência v12 (rascunho): Hugo não gostou da C-079, C-090, C-083 e C-003; a C-003 saiu do slot de 13/11 e entrou o carrossel do hojojutsu (C-004, escolhido pelo Hugo, aguardando a posição dele); C-083 arquivada e C-090 descartada. O artefato mudou de link (o antigo não abre mais): agora https://claude.ai/artifact/DR9doaKArQHDPQPfJQFRj4. Próxima ação: Hugo aprovar a v12 na sexta e dar a posição sobre o hojojutsu até 04/11.

- **28/10/2026 (2):** regra do atraso implementada: slot vencido e sem post no ar sai da grade do artefato e vai para o bloco "Atrasado"; `atualizar_artefato.py` imprime `REPROGRAMAR:`. Post publicado fora do publicador (mLabs) sai do plano pelo código da peça ou pela data (ex.: a C-106, no ar em 28/10). Hugo respondeu que só grava a sessão 1 (Reels A e C, foto de prática, fotos de óleo e cera) na semana de 09 a 16/11: Reel A (26/10), Reel C (09/11) e a foto de produto de óleo e cera (06/11) precisam ser reprogramados. Proposta pendente de aprovação do Hugo: ver a mensagem da sessão.
