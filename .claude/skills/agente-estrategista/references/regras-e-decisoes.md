# Regras e decisões — Leo (estrategista de conteúdo)

> Decisões do Hugo e regras de leitura. Acrescente com data a cada nova decisão. Não repita erro já pago.

## Decisão de 28/10/2026 (Hugo): reavaliar a sequência olhando o fundo do último post

- Ao reavaliar, o fundo do último post publicado entra na conta. Exemplo que motivou: a C-106 saiu em Warm Light (claro) e o pet play seguinte estava sugerido em Warm Light. Regra: não repetir a cor e alternar claro e escuro. Implementado em `checar_cores` (gerador do artefato).

## Decisão de 28/10/2026 (Hugo): slot atrasado sai da grade e a sequência é reprogramada

- Quando a verificação das publicações mostra que um slot da sequência **não foi postado na data**, ele **não pode aparecer no artefato entre posts já publicados** (como o Reel A de 26/10, que aparecia entre dois posts feitos). Vai para o bloco "Atrasado" e **o Leo reprograma a sequência com o Hugo** (nova data, nova ordem). Implementado em `gerar_artefato_sequencia.py` e no template.

## Decisão de 27/10/2026 (Hugo): a gestão da fila vive no marketing

- O papel do antigo `especialista-instagram` (admin) migrou para o **Leo (`agente-estrategista`)**, no `sb_marketing_team`: fila e sequência, leitura de resultado, mineração de ideias. Motivo: ideias e briefings nasciam fora da voz e eram corrigidos só no texto, gerando backlog de "visões" sem interesse. **Regra:** toda ideia cita a âncora no núcleo; tema sem posição do Hugo vira pergunta para ele. Onde abaixo se lê "especialista", leia "Leo"; onde se lê "o Hugo leva à Mari", leia "o Leo propõe, o Hugo aprova a fila".
- Ficaram no admin: as consultas do BigQuery (`analista-de-dados/references/consultas-instagram.md`) e a conexão com a API da Meta (`cientista-de-dados/references/api-meta-permissoes.md`), por serem dado e infraestrutura.
- **Anúncios (Meta e Google) estão fora desta frente por ora:** projeto à parte, tratado depois (decisão do Hugo, 27/10/2026). As seções do histórico sobre o teste de públicos ficam em `estrategia/historico-especialista-instagram.md`.

## Decisões do Hugo (origem: conversa de 07/out/2026 e regras herdadas do projeto)

- **Divisão de papéis (07/out/2026):** o time de marketing (`sb_marketing_team`) **produz** todo o conteúdo; o especialista de Instagram **não gera conteúdo final**: dá insights, ideias, análise de concorrentes e perfis, acha referências para "fazer parecido" (com conteúdo nosso), roteiros em estrutura, planejamento; o Hugo leva as ideias à Mari/time.
- **Escopo do especialista:** algoritmo e práticas atualizados da plataforma, palavras/termos de risco, estratégias e tipos de post, leitura de métricas, produzido × postado, post a post (o que deu certo/errado), planejamento, roteiro de vídeo, concorrentes e perfis.
- **Relatório semanal do Instagram** (14/set/2026): sob demanda; rotina agendada só se o Hugo pedir (oferecer na segunda vez que pedir).
- **Regras de projeto que valem aqui:** nada de emoji em texto direto a cliente (mensagens), nome da loja completo "Shibari Brasil"; descrição de produto segue a skill `cadastrador` (primeira linha "Postagem em até 2 dias úteis"); "Por que comprar" sem venda cruzada; Kimba é só a persona dos relatórios Streamlit (não é este especialista).

## Regras de leitura de dados

1. **Pago × orgânico:** sempre perguntar/checar impulsionamento; nunca atribuir alcance pago a conteúdo.
2. **Mesma janela:** comparar peças na mesma idade (ex.: 72 h) ou declarar a idade.
3. **Dizer o n.** Peça única é hipótese; padrão = 3+ peças.
4. **Normalizar por alcance** (taxa de salvamento, envio, seguidores/1.000 views); curtida absoluta não decide.
5. **Instagram → venda é indireto**; vendas sem parâmetro são regra. Declarar correlação, nunca causalidade (N de pedidos é pequeno).
6. **Benchmark de terceiros é referência**, a régua é a história da conta.
7. **Data "Publicado em" do MKT pode ser a do agendamento;** confirmar com o perfil.
8. **Classificar toda afirmação sobre a plataforma** como [OFICIAL] / [MEDIDO] / [ESTIMATIVA]. Blog de agência não é Meta.

## O que NÃO fazer

- Não escrever legenda/roteiro final como se fosse entrega do time (pode dar **estrutura, gancho em opções e referência**; o texto final é da Julia/Caio).
- Não sugerir copiar peça de concorrente (originalidade vale como regra de recomendação desde 30/abr/2026; e fere a marca). Reinterpretar com conteúdo próprio.
- Não sugerir burlar política (typos, símbolos para esconder palavra, comprar seguidores, pods, automação de follow/DM por ferramenta não oficial).
- Não impulsionar produto adulto; qualquer impulsionamento passa por Hugo + `especialista-google`/Gui; conta "proibida de anunciar" perde elegibilidade.
- Não acionar o time de marketing, não mover pauta, não postar, não responder DM/comentário, não curtir nem seguir pelo navegador do Hugo.
- Não escrever no Notion sem o Hugo pedir; ao escrever, `notion-fetch` depois para conferir formatação (regra herdada de `socio`).
- Não pedir, repetir ou gravar credenciais; login/verificação é do Hugo.
- Não prometer resultado ("vai viralizar"); falar em hipótese, métrica de sucesso e teste.

## Achados que já explicam números (para não reinventar)

- **Cadência importa:** silêncio de 30/abr–19/jun e 11/jul–20/ago coincidiu com queda de receita; B033 mediu +74% receita e +144% pedidos em 2 semanas ativas vs. 3 de silêncio (correlação, n pequeno).
- **Carrossel educativo/conceitual** é o que carrega alcance e salvamento na conta (2,4–9,6 mil views); **peça de produto** fica em 270–780 views (alinhado à sensibilidade de produto adulto, hipótese ainda a confirmar com Status da conta).
- **Reels:** praticamente ausentes; é a maior lacuna de descoberta. Experimento do Plano Out/Nov inclui 1 Reel/semana.
- **Post de produto de 18/abr** (Kit Shibari) com 648 curtidas é outlier — verificar se foi impulsionado antes de tirar lição.

## Decisões de 07/out/2026 (Hugo)
- **C-090 e C-079 ficam de lado por enquanto** (prontas e não postadas). A sequência de postagem será organizada depois, junto com o Hugo; não incluir nas recomendações de "o que postar" até ele retomar.
- **Sem rotina agendada:** o cruzamento "produzido x postado" e a revisão semanal rodam **só quando o Hugo pedir** (não propor automação de novo).
- **Confirmação de postagem** continua sendo da Mari (`Confirmar postagem: ...`); a skill só aponta o que está fora de sincronia e prepara o briefing (`estrategia/material/briefing-para-mari-AAAA-MM-DD.md`).

## Decisões de 19/10/2026 (Hugo)
- **A sequência de postagem passa a ser planejada**, não ditada pelo que está pronto: modo Planejador de Sequência (`planejador-de-sequencia.md`), com arquivo vivo `estrategia/Sequência de Conteúdo Instagram.md`. O Planejador mina o projeto de marketing, concorrentes, salvos e desempenho, propõe junto com o Hugo e orienta a produção.
- **Regra de cor de fundo:** não há ordem fixa, mas **não se repete cor em posts seguidos**; além disso, Scarlet no máximo 1 a cada 9 e alternar claro/escuro (`design-system.md` §6–§7).
- **C-090 e C-079:** continuam em espera até o Hugo decidir na abertura da sequência (o Planejador pergunta).
- Segue valendo: sem rotina agendada; o Planejador roda só quando o Hugo pedir.
- **(19/10/2026, 2ª decisão) A sequência inclui vídeo, foto de prática, foto de produto e bastidor, não só peça de design.** O feed migra para algo mais pessoal e menos chapado de conteúdo denso. **Os assuntos conversam** (arcos temáticos): produto nunca aparece sozinho ou com tom de "compre"; vem depois de educativo e prática do mesmo tema, como exposição consciente com valor agregado.

## Decisões de 19/10/2026, 3ª rodada (Hugo)
- **Quem aparece:** o Hugo aparece nos conteúdos educativos, nas demonstrações de produto e nas práticas. Quem estiver amarrado, ou receber um produto, provavelmente não aparece de rosto. Roteiros e fotos seguem isso (do ombro para baixo ou só o antebraço; sem pele marcada).
- **Produto no feed (corrigido em 20/10, ver abaixo):** entra dentro de conteúdo educativo, em Reels ilustrativos e dinâmicos e em foto esporádica; os Stories mostram mais produto. O feed precisa reter o seguidor, sem comando de venda.
- **Reel com roteiro pronto:** o Hugo grava e precisa do roteiro pronto (fala, planos, texto na tela, capa, edição). **Exceção ao "não escrever conteúdo final":** o roteiro de Reel é entrega do especialista a pedido do Hugo, porque é ele quem grava; a **legenda final** continua da Julia (Ana revisa). Roteiros em `estrategia/material/roteiros/`.
- **A fila de produção definida na sequência é a produção prioritária do time de marketing.** A skill prepara o briefing de mudanças para o projeto de marketing (`estrategia/material/briefing-mudancas-projeto-marketing-AAAA-MM-DD.md`); não edita o repositório do marketing.
- **Juta 8m:** reposição já pedida (19/10); confirmar a data de chegada antes de dar destaque ao Kit Iniciante.
- **C-090 e C-079:** o Planejador propõe: C-079 entra como abertura do arco 2 (par da C-086) e serve de peça coringa; C-090 sai do feed (frase quase igual à de @kyntv101; tema coberto pela C-091). Falta o aprovo do Hugo.
- **Black Friday:** tema em aberto; o Planejador sugere "Sem pressa" (sem urgência artificial, trilhas de começar e de repor e cuidar). Oferta, janela e margem são do Hugo.

## Decisões de 19/10/2026, 4ª rodada (Hugo)
- **Arco só para produto.** Conteúdo avulso não forma série do mesmo assunto (se não engaja, não pode haver uma sequência inteira dele na fila); **assuntos próximos ficam espaçados** (ex.: C-079 e C-086 a 6 posts de distância).
- **Cashback de 10% em todas as compras:** toda peça com produto, direto ou indireto (foto, Reel, carrossel com produto, post de produto, Stories de vitrine), leva a informação: linha de legenda **"toda compra na Shibari Brasil gera 10% de cashback para a próxima."** e end card de 2 s nos vídeos. Conteúdo sem produto não leva. **Não publicar mínimo, validade nem condição de aceite até o Hugo confirmar** (a Área VIP aprovada descreve o cashback como enviado a quem aceitou receber novidades no checkout, 10% do pedido, para a próxima compra, 45 dias, mínimo R$ 120).
- **Black Friday em conversa separada** (derivada da principal, só com esse assunto).

## Decisões de 19/10/2026, 5ª rodada (Hugo)
- **Formatos validados:** carrossel livre (template de conteúdo denso), Por trás do desejo (carrossel de 4 páginas que explica de forma objetiva um fetiche ou prática) e Desatando mitos (5 mitos de um assunto do universo shibarista e fetichista). Foto e vídeo não precisam de padrão (embora ele ajude a audiência a reconhecer).
- **Testar formatos casuais** (como o bingo de 10/10, que não colou com o público) e **posts de frase** como **extras**: fim de semana ou momento em que se quer mais visibilidade, sem tirar os slots de segunda, quarta e sexta. São **apostas de identificação e viralização** (repostagem, salvamento, compartilhamento) e **marcam o posicionamento**, não são só conteúdo. O Hugo traz as ideias para o planejamento; o Planejador as encaixa como extras com hipótese e métrica, **3 posts por formato antes de decidir** e 1 fator por teste.
- ~~**Alternar blocos de assunto** (A, B, C)~~ **REVOGADO pelo Hugo na rodada seguinte (ver abaixo).** O que fica da conversa: conteúdo de prática precisa existir no plano, porque o estoque pronto é quase todo de conversa e segurança.

## Decisões de 19/10/2026, 6ª rodada (Hugo)
- **Sem blocos de assunto e sem padrão de distância.** O Hugo não quer o contexto de blocos (A, B, C): nem sempre se cumprem os três, e mais um padrão limita a criatividade e a análise do que está dando resultado (falar mais de um assunto pode ser o melhor naquele momento). **Regra que vale:** não repetir assunto, **avaliando conteúdo a conteúdo e conversando com o Hugo**.
- **Como aplicar:** ao montar ou mudar a sequência, o Planejador **sinaliza os assuntos próximos** (campo "A decidir" de cada slot e a seção "Assuntos para decidir juntos" do artefato) e **espera a decisão do Hugo**; depois do primeiro post de um assunto, lê o resultado em 72 h para **manter, trocar ou antecipar** o seguinte. Não impor distância mínima nem alternância fixa.
- Continuam valendo: arco só para produto; extras casuais e de frase; cashback em peça com produto; regras de cor.

## Decisão de 20/10/2026 (Hugo): ciclo mensal e mínimo de produto
- **O ciclo é de 1 mês: cerca de 4 semanas x 3 posts por semana = 12 posts** (os extras de fim de semana ficam fora da conta).
- **Pelo menos 3 dos 12 posts são diretamente sobre produto** (só a foto do produto, conteúdo explicativo ou demonstração do produto, post de produto), **intercalados e de tipos diferentes**. "1 único post de produto é pouco." Produto dentro de educativo ou de Reel vale a mais e **não substitui** os 3. Esta decisão **substitui** o "1 post de produto por ciclo" das rodadas anteriores. Stories continuam mostrando produto sempre que couber; cashback de 10% em toda peça com produto.

## Decisão de 20/10/2026 (Hugo): planejar por mês de calendário
- **O planejamento segue os meses do calendário:** o plano vigente vai **até a virada do mês** e, para o **mês seguinte, planeja-se o mês todo**, para ter um bom panorama. Hoje: resto de outubro (21 a 31/10) e novembro inteiro (02 a 30/11). A partir de cerca do dia 20 de cada mês, abrir o planejamento do mês seguinte (dezembro em 16 a 20/11).
- A regra de produto vale **por mês**: cerca de 12 posts (4 semanas x 3) e **pelo menos 3 diretamente sobre produto**. Outubro é mês de retomada (restam 5 slots); a regra plena vale a partir de novembro. Black Friday ocupa slots reservados de novembro (23, 25, 27 e 30/11) até a conversa separada decidir.

## Decisão de 20/10/2026 (Hugo): extras só casuais e em ritmo leve
- **Extra em todo sábado é demais** para a capacidade do time. **Nesse primeiro momento o extra é só casual** (como o bingo), em **ritmo leve: no máximo 1 a cada 2 semanas** (hoje 31/10 e 14/11). As frases de posicionamento ficam nos slots normais e podem voltar como extra mais adiante, se houver capacidade. Ao montar novos meses, **não preencher todo sábado**; perguntar ao Hugo antes de acrescentar um extra.

## Decisão de 21/10/2026 (Hugo): C-079 já no ar, C-082 fora, Por trás do desejo é fetiche ou prática, mais BDSM
- **C-079 e C-057 são o mesmo conteúdo** (no ar em 18/09, só o fundo mudou para Carbon Black): sai do plano e não se confere sobreposição. **C-082 fora do ciclo.** A **C-086** (bandeiras verdes) vai para 21/10.
- **Por trás do desejo explica um fetiche ou uma prática do campo do desejo.** Karada é uma amarração dentro do shibari, não cabe. Antes de propor tema do quadro, conferir o que já saiu (wax play 19/06, sensation play 02/07, impact play 21/09, D/s 30/09) para não repetir.
- **A sequência estava quase toda de shibari.** Equilibrar com BDSM e fetiche (hoje 8 de corda e 6 de BDSM/fetiche). A **linha nova de wax play** (Masmorra Velas) entra como carrossel educativo de velas (C-026, 11/11, produto direto). Estoque das velas é curto (3 a 8 por cor).

## Decisão de 21/10/2026 (Hugo): horário de postagem vem dos dados, não do Hugo
- **Não perguntar o horário de cada post.** O padrão é a hora de pico de seguidores online no dia da semana, em horário de Brasília (receita 10 de `consultas-instagram.md` (no `sb_admin_team`, skill `analista-de-dados`)). **Horário específico só quando o Hugo disser explicitamente.**
- **Fuso:** a tabela `tb_instagram_horario_online` guarda a hora como a Meta devolve (Pacífico, inferido). Converter antes de usar. Leitura de 21/10: 18h em Brasília (geral e em todos os dias da semana), 2º lugar 19h; diferença entre as melhores horas é pequena. Amostra de 8 dias, sem nenhuma quarta-feira: tratar como [ESTIMATIVA] e reler quando houver 4+ dias por dia da semana.
- A aprovação de cada post pelo Hugo inclui o horário que o sistema propôs.

## Diretriz de 21/10/2026 (Hugo): posts agendados aparecem no artefato Sequência Instagram
- Todo post agendado entra no artefato com **moldura própria** e com **dia da semana, data e hora** do agendamento. A cada atualização do artefato, conferir se já foi ao ar e, se foi, tratar como os demais publicados. Detalhes e cores em `planejador-de-sequencia.md` §9.

## Decisão de 22/10/2026 (Hugo): horário explícito e canal do agendamento
- **Reel de 23/10 às 08:40 (Brasília):** horário definido pelo Hugo (vale sobre o padrão dos dados, como a regra de 21/10 prevê). A legenda dele foi usada exatamente como veio.
- **Canal:** o Hugo quer agendar **pela API** (`instagram_publicar`), não pelo mLabs. Como ela ainda não aceita Reels nem está no ar, **este post foi pelo mLabs por decisão dele (22/10)** e a API para Reels fica para 23/10. Antes de agendar qualquer coisa, conferir qual canal o Hugo espera: a skill diz que o agendamento é do `sb_data_pipeline`.
- **Vídeo de acervo:** metadados limpos da marca d'água/rastreio do Canva e com autor/direitos da Shibari Brasil; sem marca de IA (não é IA). Cópia final em `exportado/instagram-9x16`, original em `editado` preservado.
