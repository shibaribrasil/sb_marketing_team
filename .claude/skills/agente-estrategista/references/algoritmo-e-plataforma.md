# Algoritmo e plataforma — o que sabemos (pesquisa de 07/out/2026)

> **Regra de leitura:** cada afirmação traz o nível de confiança. **[OFICIAL]** = dito pela Meta/Mosseri (Help Center, blog, vídeos). **[MEDIDO]** = estudo com amostra grande (Socialinsider, Buffer, Metricool). **[ESTIMATIVA]** = blog/agência sem fonte rastreável — tratar como hipótese a testar nos NOSSOS dados, nunca como fato. Quando um número de terceiros conflita com o que medimos no @shibari.brasil, vale o nosso.
> Esta página é uma foto. Antes de afirmar algo "novo", rode o protocolo de `atualizacao-da-pesquisa.md`.

## 1. Como o Instagram decide o que mostrar

Não existe "o algoritmo": são **sistemas separados por superfície** (Feed, Stories, Reels, Explorar/Search), cada um prevendo o que *aquele usuário* tem mais chance de consumir. **[OFICIAL]**

| Superfície | O que pesa mais (ordem aproximada) | Observação |
|---|---|---|
| **Reels** (descoberta) | tempo assistido / retenção, **envios por DM (sends) por alcance**, curtidas por alcance | Mostra muito a quem **não segue**. Reels de até 3 min são elegíveis a recomendação **[OFICIAL, jan/2025]**. |
| **Feed** | relação com quem postou (histórico de interação), recência, interesse previsto | Quem já interage vê mais. Seguidor frio quase não vê. |
| **Stories** | histórico de visualização, frequência de interação (respostas/DM/stickers), proximidade | Só quem já tem vínculo. Serve para **retenção e confiança**, não para crescer. Precisa ser postado nas últimas 24 h. |
| **Explorar / Search** | popularidade do post (curtidas, comentários, envios, salvamentos + velocidade), interesse do usuário, histórico da conta | **Excluídos:** conteúdo sensível/regulado, marca d'água de outro app, baixa qualidade, conta que reposta o que não é original, violações recentes. |

Os três sinais que Mosseri nomeou (jan/2025) **[OFICIAL]**: **tempo assistido**, **envios por alcance** (um pouco mais importante para não seguidores) e **curtidas por alcance** (um pouco mais importante para seguidores).

Consequências práticas aceitas pelo mercado (e coerentes com o oficial):
- **Envio por DM é o sinal mais forte de alcance novo** — "mando isso pra alguém". O multiplicador "3–5× o peso de uma curtida" é **[ESTIMATIVA]** (sem fonte oficial), mas a direção é confirmada.
- **Salvamento** = valor duradouro (referência). Orientação da Meta (jul/2026, via Mosseri) **[reportado por terceiros, confirmar]**: muito salvamento + pouco envio = conteúdo "de guardar", não "de espalhar". Carrossel de aprendizado tende a ser assim, o que é bom para autoridade e conversão, não para alcance frio.
- **Primeiros 3 segundos** decidem o Reel. Métrica nativa nova: **skip rate** (substituiu "view rate") e **retenção** **[OFICIAL, 2025]**.
- **Comentário raso** pesa menos que conversa; responder comentário e DM conta como vínculo.

## 2. Originalidade (ponto onde o time de marketing pode ganhar ou perder)

- Reels: 10+ repostagens do mesmo conteúdo em 30 dias tira a conta das recomendações; cópias duplicadas são trocadas pelo original **[OFICIAL, abr/2024]**.
- **Desde 30/abr/2026 a regra vale também para foto e carrossel**: a maioria do que a conta postou nos últimos 30 dias precisa ser original **[OFICIAL, via cobertura de imprensa; a Meta diz que ~75% das recomendações nos EUA já vêm de posts originais]**.
- Conta com remix/edição que **agrega contexto** (texto, gráfico novo, comentário) conta como original. Só borda, marca d'água, legenda ou crédito **não** conta.
- Imagem polida demais perdeu vantagem: Mosseri (31/dez/2025) disse que "o estético perfeito morreu" e que o crédito vai para conteúdo **cru, real, humano**. **[OFICIAL, memorando de fim de ano; interpretação de terceiros varia]**.
- Rótulos: "AI Info" em posts e rótulo de **perfil gerado por IA**; conta de IA sem rótulo perde elegibilidade (ago/2026) **[OFICIAL via cobertura]**. Imagem de IA em post nosso: **decisão do Hugo** (hoje o time usa fotos próprias; manter e rotular se um dia usarmos IA).

> Implicação para nós: o que o time de marketing produz tem de ser **nosso** (foto própria, texto autoral, vídeo próprio). "Fazer parecido com um concorrente" = **reinterpretar a ideia com nosso conteúdo**, nunca reaproveitar peça deles.

## 3. Busca dentro do Instagram (SEO)

- O Instagram funciona cada vez mais como buscador: **legenda, bio, nome do perfil, texto na imagem/vídeo, alt text e áudio** alimentam a descoberta **[OFICIAL em parte; Meta passou a usar legenda como dado de descoberta, ago/2026]**.
- **Palavra-chave principal nas primeiras palavras da legenda** (a primeira linha pesa mais) **[ESTIMATIVA, consenso]**.
- **Hashtags: teto de 5 por post/Reel** (mudança nov–dez/2025; alguns usuários veem 3) **[OFICIAL via cobertura]**. Hoje funcionam como metadado de classificação, não de alcance: 3–5 específicas, nada de #reels/#explore genéricas. Hashtag banida/sob revisão reduz distribuição.
- Palavra-chave em **texto na tela do vídeo** e **fala** (o sistema transcreve) ajuda a classificar.

## 4. Elegibilidade para recomendação (a parte mais importante para o nosso nicho)

- Conteúdo que a Meta chama de **sensível** (sexualmente sugestivo, **produtos adultos**, regulados) pode **ficar visível aos seguidores, mas não ser recomendado** a quem não segue **[OFICIAL — Recommendation Guidelines]**. O padrão para recomendar é **mais alto** que o padrão para existir na conta.
- Se a **conta** fica inelegível, **nenhum** conteúdo é recomendado, mesmo o que não viola nada.
- **Onde ver:** Configurações → Conta → **Status da conta** (conta profissional). Mostra se está elegível, o que viola (inclui foto de perfil e bio) e deixa **editar, apagar ou pedir revisão**. **Primeira coisa a checar em qualquer análise de queda de alcance.**
- O usuário controla quanto conteúdo sensível quer ver (Controle de Conteúdo Sensível: Menos/Padrão/Mais). Conta de nicho adulto sempre perde parte do alcance frio — é o **teto estrutural** que o conteúdo precisa contornar com enquadramento (ver `risco-de-alcance-nicho.md`).
- "Shadowban" não é termo oficial; o oficial é **inelegibilidade para recomendação**. Gatilhos documentados: hashtag banida, violação de diretrizes, comportamento de spam (seguir/comentar em massa, ferramenta de terceiros com API não oficial), conteúdo não original.

## 5. Recursos que mudam o jogo (2025–2026)

| Recurso | O que é | Como usamos |
|---|---|---|
| **Trial Reels** | Mostra o Reel só a **não seguidores** antes de publicar no perfil; se performar, publica para todos. Dá para agendar (fev/2026); limite de 30 dias para publicar (abr/2026) | **Teste de hook e de enquadramento sensível**: se o Trial passa de X% de skip baixo, vai ao ar. Mosseri recomendou para 2026. |
| **Reels em carrossel / carrossel misto** | Carrossel com slides de vídeo | Mixed-format teve a maior taxa de engajamento medida (2,33% mediana, Metricool) **[MEDIDO]** |
| **Compare Reels / Insights por post** | Painel novo (abr/2026): taxa de envio, skip rate, retenção, comparação entre Reels | Base do relatório semanal |
| **Reordenar grade e carrossel** | Reorganizar o perfil; trocar música depois de postar; editar miniatura | Corrigir peça fraca sem apagar |
| **Link clicável em Reel (Edits)** | Cartão com link para outro perfil/Reel (não externo) | Encadear séries |
| **Acesso antecipado 24 h** para seguidores | Reel só seguidores antes de abrir ao público | Recompensar quem segue |
| **"Your Algorithm"** | O usuário escolhe os temas dos Reels | Reforça: **tema consistente** da conta vence |
| **Edits (app)** | Editor oficial: legenda automática, corte de silêncio, teleprompter | Produção mais rápida do time |
| **Bônus a criador de foto e carrossel** | Programa em expansão (ago/2026) | Não se aplica por ora |
| **WhatsApp/DM** | Chamada WhatsApp no perfil, automações de DM, rastreador de resposta | Canal de conversão da nossa loja |

## 6. O que o Instagram NÃO nos deixa fazer (e tem que ficar claro ao planejar)

- **Link em legenda não é clicável** (só Meta Verified). Conversão = **link da bio, sticker de link nos Stories, DM, WhatsApp**.
- **Anúncio/impulsionamento de produto adulto** é restrito pela política de anúncios (nudez, "sexualmente sugestivo", produto de prazer/aprimoramento sexual). Frente educativa/bem-estar passa melhor. Alinhar com `gui` (tráfego) e `especialista-google` antes de impulsionar; **post impulsionado mistura alcance pago e orgânico** nos Insights — nunca comparar sem separar.

## 7. Frequência e consistência

- Reels eram o principal mecanismo de descoberta; o Instagram "incentiva postar Reels de forma consistente" (set/2026). Constância > pico. **[consenso + nossa evidência: o silêncio de mai/jun e jul–ago/2026 coincidiu com queda de receita — correlação, não causa; ver `dados/Análise de Instagram.md`]**
- Mix de mercado (**[ESTIMATIVA]**): 60–70% Reels (descoberta), 20–30% carrossel (salvamento/autoridade), ~10% foto/cultura, Stories diários. **Para uma marca de nicho educativo, a ordem tende a inverter** (carrossel carrega a autoridade, vide os dados da conta); só os nossos números dizem o mix certo.

## 8. Fontes consultadas (07/out/2026)

Meta Help Center (Recommendation Guidelines, Status da conta, Controle de Conteúdo Sensível), Meta Transparency Center (Sexual Solicitation; Ad Standards), e leituras de mercado: Creatorflow, Socialinsider (2026 Instagram Organic Engagement Benchmarks), Buffer (45M posts), Metricool (estudo Instagram 2026), SocialBee (tracker de atualizações), Social Media Examiner (hashtags e links clicáveis), biird (restrições para bem-estar sexual), Tuche Digital (marketing para sex shop no Brasil), ESPM Nota Alta (mitos do algoritmo). Links completos e data em `atualizacao-da-pesquisa.md`.
