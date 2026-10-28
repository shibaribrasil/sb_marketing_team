# Modo Planejador de Sequência — organização e planejamento dos posts do Instagram

> Criado em 19/10/2026 a pedido do Hugo. É o **modo de trabalho principal do Leo (`agente-estrategista`)**, migrado em 27/10/2026 do antigo `especialista-instagram` do admin: quando o pedido for organizar, sequenciar ou planejar o que vai ao ar, o Leo age como **Planejador de Sequência**, segue este roteiro e grava o resultado no arquivo vivo `estrategia/Sequência de Conteúdo Instagram.md`.

## 1. Por que existe

Até 19/10/2026 **quem decidia o que ia ao ar era o que já estava pronto**, sem estratégia (hoje: 2 peças prontas em espera, 6 travadas em design há 37 a 54 dias, e o melhor post recente, de 12/10, nem veio da pauta). O Planejador inverte a ordem: **primeiro define a sequência** (o que, em que dia, em que formato, com que fundo, para que objetivo e com qual hipótese) e **depois orienta a produção** para entregar as peças a tempo.

## 1b. Direção de 19/10/2026: feed mais pessoal e assuntos que conversam

A sequência **não é só de peça de design**: inclui **Reels/vídeos, fotos de prática, fotos de produto e bastidor**, que hoje saem pouco. O feed migra de "conteúdo denso não personalizado" para algo **mais pessoal** (prática real, mãos e corda, bastidor do tratamento, frase curta de identificação como a do post de 12/10, rosto/voz só se o Hugo decidir). **Arco é só para produto** (decisão do Hugo, 19/10): conteúdo avulso não forma série de assunto, e assuntos próximos ficam espaçados. O planejamento de **produto** é por arcos:

- **Arco = âncora (prática ou produto) em 3 a 4 peças, em até ~10 dias, que conversam:** (1) **Entrada** educativa; (2) **Prática** (foto, bastidor ou Reel); (3) **Produto em contexto** (foto/post de produto, "para quem é"); (4) **Fecho** opcional (Stories com link, frase, pergunta).
- **Regra do produto acompanhado:** produto nunca aparece sozinho nem com comando de venda; só entra depois de educativo e prática do **mesmo tema** (até 7 dias antes). A exposição é consciente e traz valor.
- **Produto com estoque conferido** (dossiê, seção "Produtos em foco"): não montar arco comercial em item que vai romper (ex.: juta 8m e kits que a levam, análise de 15/10).
- **Ciclo de 1 mês = 12 posts (4 semanas x 3) e pelo menos 3 diretamente sobre produto** (foto do produto, conteúdo explicativo, post de produto), intercalados e de tipos diferentes (decisão de 20/10). Produto dentro de educativo e de Reel vale a mais e não substitui os 3. Stories mostram produto sempre que couber. Composição de 21/10 a 16/11: 4 carrosséis livres, 2 Por trás do desejo, 1 frase, 1 foto de prática, 2 Reels, 1 foto de produto, 1 post de produto, mais 3 extras. Muda o ciclo de 9 do `design-system.md` §7.
- **Pessoas em cena:** o Hugo aparece (educativos, demonstrações, práticas); quem estiver amarrado ou receber produto, sem rosto; sem pele marcada.
- **Reel nasce com roteiro pronto** (fala, planos, texto na tela, capa, edição), salvo em `estrategia/material/roteiros/`; legenda final é da Julia. O Hugo grava em sessões de captação planejadas pela sequência.
- **A fila de produção da sequência é a prioridade do time de marketing;** o Planejador entrega o briefing de mudanças para o projeto (`estrategia/material/briefing-mudancas-projeto-marketing-*.md`) e não edita o repositório do marketing.
- **A sequência orienta captação:** para cada arco, listar **o que o Hugo precisa fotografar/gravar** (lista de captação), conferindo antes o **banco de mídia** (dossiê, seção 7: o que existe e o que falta).
- **Métrica do arco:** visitas ao perfil, cliques na bio e pedidos orgânicos do Instagram (peça de produto não se mede por views); envio e salvamento por peça de ensino.

## 2. Papel e limites

- **Faz:** minera o projeto de marketing e os dados do perfil; traz ideias novas (concorrentes, salvos, formatos novos, o que deu certo); propõe a sequência e as alternativas; aplica as regras da marca; gera as **ordens de produção** (quem faz o quê, para quando) e os briefings de ideia; confere semanalmente o planejado × postado.
- **Não faz:** não escreve a legenda/texto final, não arte, não posta, não move a pauta do marketing, não aciona a Mari, não impulsiona. **Quem decide a sequência é o Hugo**; o Planejador propõe, justifica e registra. Quem confirma postagem é a Mari.
- **Sem rotina agendada** (decisão de 07/10): roda só quando o Hugo pedir.

## 3. Fontes (o que minerar, nesta ordem)

| # | Fonte | Para quê | Como |
|---|---|---|---|
| 1 | **Dossiê de insumos** | cadência, grade recente, verificações de cor e mix, estoque, banco de briefings, desempenho, calendário | `/c/Users/HTK1562/venvs/sb_relatorios/Scripts/python.exe .claude/skills/agente-estrategista/scripts/insumos_sequencia.py [--dias 21] [--out arquivo.md]` |
| 2 | Produzido × postado | o que está pronto/travado, repostagens, posts sem peça | `scripts/produzido_x_postado.py` (rotinas §0) |
| 3 | Pauta, histórico e **banco de briefings** do marketing | estoque por etapa; 37+ ideias de Instagram ainda sem produção; território já coberto | `sb_marketing_team/contexto/pauta.md`, `historico-conteudos.md`, `briefings.md`, backlog do Leo |
| 4 | **Regras da marca** | cores de fundo, ciclo de 9, Scarlet, personas, tom | `sb_marketing_team/contexto/design-system.md` §6 e §7, `personas.md`, `formatos/*.md` e a skill `voz-shibari` (núcleo `sb_cerebro`) |
| 5 | **Desempenho** nosso | formato, tipo de peça, melhores posts, pago × orgânico, horário, público | `consultas-instagram.md` (no `sb_admin_team`, skill `analista-de-dados`) (semana × semana, mix por formato, post a post, horário, público); análise de 18/10 em `dados/analises/` |
| 6 | **Concorrentes e referências** | padrões, formatos novos, o que performa fora | `consultas-instagram.md` (no `sb_admin_team`, skill `analista-de-dados`) (concorrentes), `estrategia/material/referencias/briefing-posts-salvos-2026-10-09.md` (15 formatos novos, 8 briefings), `contexto/referencias.md` do marketing; navegador só para observar |
| 6b | **Produtos em foco e banco de mídia** | produto do arco (vendas, MC, estoque) e o que há de foto/vídeo | dossiê, seções 6 e 7; `dados/analises/previsao-ruptura-juta-8m-*.md` |
| 7 | **Risco de alcance** | termo, imagem, tema de risco | `risco-de-alcance-nicho.md` antes de qualquer tema novo |
| 8 | **Plano e capacidade** | experimento Out/Nov, seg/qua/sex, agendamento na sexta (mLabs), gargalo de design | `planejamento/Plano Outubro-Novembro 2026.md`, `Organização Semanal.md`, `Backlog.md` |

Regras de leitura: pago separado de orgânico; mesma janela de idade; dizer o n; normalizar por alcance; peça de benchmark é referência, a régua é a nossa série (`regras-e-decisoes.md`).

## 4. Regras de sequenciamento

### 4.1 Regras duras (a sequência não pode violar)
1. **Cor de fundo nunca repete em posts seguidos.** Não existe ordem fixa; a regra é não repetir em sequência (Hugo, 19/10/2026). Conferir também contra os últimos posts já no ar.
2. **Scarlet:** no máximo **1 post totalmente Scarlet a cada 9**; Scarlet é "corte", não parede (`design-system.md` §6–§7).
3. **Alternar claro e escuro ao longo do ciclo** (claro = Warm Light, Skin Nude; escuro = Deep Plum, Carbon Black).
4. **Fundo combina com o tipo** (§6): educativo e rapidinha em Warm Light/Skin Nude; conceitual/frase em Deep Plum/Carbon Black; minimalista em Carbon Black/Deep Plum/Scarlet (ocasional); produto em Skin Nude/Warm Light; foto de prática em Carbon Black/Deep Plum/neutros.
5. **Ciclo de 9 posts:** 3 educativo, 2 conceitual, 1 minimalista, 1–2 produto, 1 foto de prática, 1 foto de produto. É referência de ritmo, não obrigação: desvio precisa de justificativa escrita (ex.: Reel no lugar de minimalista).
6. **Slots:** feed segunda, quarta e sexta; **a semana seguinte é agendada na sexta** (mLabs): tudo que entra na semana S+1 precisa estar pronto até a quinta da semana S.
6b. **Assuntos: sem blocos e sem distância mínima.** O Hugo não quer padrão de alternância (limita a criatividade e a leitura do que dá resultado). Regra: **não repetir assunto, avaliando caso a caso com o Hugo.** Ao montar a sequência, registrar o **assunto** de cada slot, sinalizar os próximos entre si e perguntar; depois do primeiro post de um assunto, ler o resultado em 72 h e decidir com ele se o seguinte fica, troca ou antecipa. Se o estoque estiver concentrado em um assunto (hoje conversa e segurança), propor produzir outros, sem impor ordem.
6c. **Extras de fim de semana: só casuais por ora e em ritmo leve** (decisão de 20/10): no máximo 1 extra a cada 2 semanas, nunca todo sábado, para caber na capacidade do time; frases de posicionamento ficam nos slots normais. São apostas de identificação e viralização, fora dos slots de seg, qua e sex; 3 posts por formato antes de decidir, 1 fator por teste, leitura em 72 h e 7 dias, barra de envio ≥ 1,0% e ≥ 20 repostagens; frase de posicionamento só com **posição clara** (as suaves rendem pouco). O Hugo traz as ideias casuais.
7. **Conteúdo avulso não forma série:** o arco é só de produto. Assuntos próximos são decididos caso a caso com o Hugo (item 6b); território repetido só com a decisão dele;
8. **Originalidade:** nenhuma peça copia referência; repostagem do próprio conteúdo só com valor novo e registrada.
9. **Itens em espera por decisão do Hugo** (C-090, C-079) **não entram** sem ele retomar; perguntar na abertura da sessão.
10. **Nada com risco de plataforma/marca** (age play, blood play, sexo explícito, pele marcada, produto adulto impulsionado) sem passar por `risco-de-alcance-nicho.md` e pelo Hugo.

### 4.2 Regras macias (ajustam a ordem; dizer qual pesou)
- **Descoberta × relacionamento × negócio:** em cada semana, 1 peça de descoberta (Reel/carrossel conceitual), 1 de ensino salvável e 1 de negócio/vínculo (produto, Primeiras Cordas, bio). O funil que vende é "conteúdo orgânico → perfil → bio → home ou Primeiras Cordas".
- **Uma peça forte logo após uma fraca**, nunca três de baixa expectativa seguidas; abrir a semana com a de maior expectativa quando houver comparação.
- **Rodízio de persona** (Mariana, Thiago, Alex): não passar de 2 posts seguidos para a mesma.
- **Reel:** 1 por semana como teste (Trial Reel antes); registrar a lacuna se não houver produção.
- **Um experimento por vez:** 1 slot de "teste" por semana com hipótese, métrica e data de leitura.
- **Sazonalidade e datas:** Black Friday (27/11), Halloween (31/10) e outras confirmadas com o Hugo.
- **Peça de produto só com produto em estoque** (conferir catálogo/ruptura).

### 4.3 Como escolher uma candidata (justificar cada slot em uma linha, com evidência)
| Critério | Pergunta |
|---|---|
| Desempenho esperado | O formato/tipo teve envio e salvamento acima da mediana da conta? (n e janela) |
| Papel no funil | Descobre, ensina/salva ou leva à loja? Liga a algum produto ou à bio? |
| Aderência à marca e risco | Cabe no tom? Algum termo/imagem de risco? |
| Esforço e prazo de produção | Está pronta, em design, só em briefing ou do zero? Quantos dias de produção? |
| Novidade e evidência externa | É formato/ângulo novo? Há sinal em concorrentes ou nos salvos? |
| Cobertura | Quais persona e território já saíram recentemente? |

### 4.4 Horário de cada post (decisão de 21/10/2026)
O Hugo não define horário post a post. Cada post da sequência sai com a **hora de pico do público no dia da semana** (receita 10 de `consultas-instagram.md` (no `sb_admin_team`, skill `analista-de-dados`), já em horário de Brasília), com a origem rotulada e o 2º lugar ao lado. Horário específico só quando ele disser explicitamente; aí ele vale. O horário fica no plano e entra na aprovação do post.

## 5. Protocolo de sessão com o Hugo (passo a passo)

1. **Rodar o dossiê** (fonte 1) e ler `estrategia/Sequência de Conteúdo Instagram.md` (versão vigente, decisões e pendências).
2. **Diagnóstico em até 6 linhas:** cadência, o que está no ar/pronto/travado, desvios de cor e mix, o que o desempenho diz, o que mudou desde a última versão.
2b. **Horizonte por mês de calendário (decisão de 20/10):** o plano cobre o resto do mês corrente e o mês seguinte inteiro; a partir de cerca do dia 20, abrir o planejamento do mês seguinte. Cada mês tem cerca de 12 posts (4 semanas x 3) e pelo menos 3 diretamente sobre produto; datas comerciais (Black Friday) entram como slots reservados.
3. **Perguntar o que só o Hugo decide** (uma rodada, objetiva): quem aparece (rosto/voz ou só mãos e corda), reposição dos produtos do arco, composição por ciclo, horizonte (3 semanas/9 posts?), C-090 e C-079 (retomar, descartar, manter em espera), capacidade de vídeo (quantos Reels), datas especiais, prioridade de design (Bia), teto de produção do time.
4. **Propor a sequência por arcos** (incluindo as propostas para peças em espera, o roteiro dos Reels e, perto de datas comerciais, os temas de campanha) em tabela (modelo no arquivo vivo): data, passo do arco, categoria, formato (inclui vídeo, foto de prática e de produto), tema/peça, fundo sugerido, métrica, produção; mais **lista de captação**. Dar **uma recomendada** e, se a decisão mudar muito o resultado, **uma alternativa** (ex.: "segura" = o que existe + 2 apostas; "estratégica" = apostas desde a primeira semana).
5. **Editar com o Hugo** até ele aprovar; mostrar a cada mudança as verificações das regras duras (cor, Scarlet, mix, território).
6. **Congelar a versão** (v1, v2…) no arquivo vivo, com data e decisões; **gerar as ordens de produção** por papel (Julia/Ana/Bia/Hugo; o Caio foi extinto) com prazo = data do slot menos o prazo de produção, e as propostas de slot (formato em `rotinas-e-modelos.md` §3, **com âncora no núcleo obrigatória**) para o que ainda não existe. O Hugo aprova a fila; só então a Julia recebe a ordem.
7. **Fecho semanal (quando o Hugo pedir):** rodar produzido × postado, marcar o planejado × postado, registrar desvios e a causa, ajustar as semanas seguintes e pedir à Mari `Confirmar postagem` do que foi ao ar.
8. **Leitura por ciclo (9 posts):** comparar hipótese × resultado por slot (pago separado do orgânico, mesma janela de idade), registrar o que aprendeu e o que muda.

## 6. Prazos de produção (por tipo) — [ESTIMATIVA], confirmar com a Mari

| Tipo | Prazo mínimo hoje | Observação |
|---|---|---|
| Post de frase | 2–3 dias | texto curto + arte simples |
| Carrossel educativo | 5–7 dias | texto + revisão + arte |
| Post de produto / foto | depende de foto | pedir foto antecipada |
| Reel | 7+ dias | roteiro, gravação do Hugo, edição |
| **Gargalo atual** | design da Bia: **5 peças paradas há 37 dias** | destravar é a ação de maior retorno por real |

## 7. Saídas

- **Sequência** (tabela) e **ordens de produção** (lista por papel e prazo) em `estrategia/Sequência de Conteúdo Instagram.md`.
- **Briefings de ideia** para o que falta (modelo §3 de `rotinas-e-modelos.md`), em `estrategia/material/referencias/` ou na própria sessão.
- **Relatório de desvio** semanal (planejado × postado).
- Ao fim de toda sessão: atualizar a seção "Versão vigente" do arquivo vivo, `estado-atual.md` e, se houver decisão nova, `regras-e-decisoes.md`.

## 8. Limites conhecidos

- O fundo (cor) vem do `briefing.md`/`visual-spec.md`/histórico da peça; **posts sem peça no marketing não têm cor registrada** (aparecem com "?"): olhar a imagem quando a cor importar.
- O casamento peça × post é por legenda; legenda editada no mLabs baixa a similaridade (ver `rotinas-e-modelos.md` §0).
- N pequeno: 17 carrosséis e 10 imagens orgânicos em 180 dias; tratar diferenças entre tipos como hipótese, não como lei.
- O desempenho de peça impulsionada inclui o pago (ex.: o carrossel de 28/09, campeão de views, foi impulsionado).

## 9. Artefato visual da sequência (criado em 19/10/2026)

- **Onde:** https://claude.ai/artifact/HgQRgWVEAtJhH2oLdprhDF (privado; compartilhar pelo menu da página). **Duas abas (decisão do Hugo, 19/10/2026): "Grade do feed" e "Produção e captação".** Grade = capas reais dos posts já publicados (3 colunas, do mais novo para o mais antigo, como no perfil) com os slots planejados em borda pontilhada no topo e a marca "mesma cor do anterior". Produção e captação = (1) **ordem de produção atual** na ordem da sequência, com etapa real na pauta, dias parados, responsável, entrega até e situação; (2) **status da produção** no marketing por etapa da pauta; (3) ordens por papel; (4) captação do Hugo; (5) **backlog mapeado** (banco de briefings do Caio, por território, com filtro Instagram/Blog/Outros e busca). Arcos, linha do tempo e decisões ficam só nos arquivos por ora.
- **Fonte dos dados:** histórico = BigQuery `tb_instagram_midia` casado com as peças do marketing; plano = `estrategia/sequencia-instagram-plano.json` (fonte do artefato; o texto e as decisões ficam em `estrategia/Sequência de Conteúdo Instagram.md`).
- **Como atualizar (a cada mudança de sequência, a pedido do Hugo):** (1) editar o JSON do plano e o `.md`; (2) rodar `/c/Users/HTK1562/venvs/sb_relatorios/Scripts/python.exe .claude/skills/agente-estrategista/scripts/gerar_artefato_sequencia.py` (gera `estrategia/sequencia-instagram.html` com o histórico atualizado); (3) publicar o mesmo arquivo com a ferramenta Artifact (mantém a URL). Posts fora da pauta sem classificação entram em `classificacao_manual` do JSON; sem isso aparecem como "Sem classificação". As **capas** são baixadas pela Graph API (token no Secret Manager, só leitura) e guardadas em `estrategia/capas/` (a URL da Meta expira); só posts novos são baixados. Cada slot do plano tem `prazo`, `responsavel` e `proximo` (alimentam a ordem de produção).
- **Posts agendados (diretriz de 21/10/2026):** todo post que entra na fila de publicação do `sb_data_pipeline` (`raw_instagram.fila_publicacao`, comandos em `scripts/instagram_publicar.py`) aparece na Grade do feed com **moldura sólida azul-petróleo e faixa no topo com a situação, o dia da semana e a hora** (ex.: "Agendado · qua 21/10 · 18:00"). Slot só planejado segue em borda pontilhada. Moldura verde = já publicado, esperando a extração; vermelha = precisa de atenção (falhou, atrasou, publicação incerta). O gerador lê a fila (somente leitura) e liga o item ao slot pelo id do plano (P1, P2...). **Em toda atualização do artefato ele confere se o post já foi ao ar:** se o item da fila está publicado e o `media_id` já consta no extrato do perfil (`tb_instagram_midia`), o slot sai do plano e o post aparece como os demais publicados (capa real e métricas). Se a fila estiver indisponível, o artefato sai como antes, sem agendados. Atualizar o artefato é pedido do Hugo; após `agendar` um post novo, oferecer a atualização.
- **Limites:** é uma foto (não grava edições); a cor de fundo só aparece para posts com peça no marketing; as métricas são do último extrato (3x ao dia).
