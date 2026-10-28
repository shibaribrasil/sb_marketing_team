# Métricas — o que olhar, como ler, que armadilhas evitar

> Fonte dos dados: Painel Profissional do Instagram (@shibari.brasil) via Claude in Chrome, logado na conta do Hugo. Procedimento de coleta passo a passo em `coleta-de-dados.md`. Benchmarks são **referência**, não meta; o termômetro é a história da nossa conta.

## 1. Hierarquia de métricas (do que mais importa ao que menos importa)

| Nível | Métrica | Pergunta que responde | Como ler |
|---|---|---|---|
| **Distribuição** | Visualizações, contas alcançadas, **% não seguidores** | A peça saiu da bolha? | % de não seguidores alto = descoberta. Baixo = só atende quem já segue. |
| **Qualidade da atenção** | **Skip rate** (Reels), **retenção / tempo médio assistido**, rewatch | O hook funcionou? o conteúdo segurou? | Referência de terceiros: skip < 20% nos 3 s bom; 20–30% saudável; > 40% hook ruim **[ESTIMATIVA]**. Curtida alta com skip alto = "hook problem wearing a success costume". |
| **Valor percebido** | **Envios (sends)**, **salvamentos** | Alguém mandou ou guardou? | Envio = alcance novo. Salvamento = utilidade/autoridade. Razão envios/alcance e saves/alcance comparam peças de tamanhos diferentes. |
| **Relacionamento** | Comentários (qualidade), respostas a Story, DMs | Virou conversa? | Comentário de pergunta/relato vale mais que emoji. |
| **Crescimento** | Seguidores ganhos por peça, visitas ao perfil, toques no link | A peça converteu atenção em seguidor/visita? | Seguidores por mil visualizações = métrica de conversão de alcance em audiência. |
| **Negócio** | Cliques no link, DMs de compra, pedidos com origem Instagram (UTM/cupom) | Vendeu? | Ver §4: o elo mais fraco da nossa medição hoje. |
| **Vaidade** | Curtidas absolutas, seguidores totais | — | Contexto, nunca decisão. |

## 2. Razões que usamos para comparar peças (normalizam por alcance)

- **Taxa de salvamento** = salvamentos ÷ contas alcançadas
- **Taxa de envio** = envios ÷ contas alcançadas
- **Taxa de interação** = (curtidas + comentários + envios + salvamentos) ÷ contas alcançadas
- **Seguidores ganhos por mil views** = seguidores ganhos ÷ visualizações × 1.000
- **% não seguidores** = alcance de não seguidores ÷ alcance total
- **Atenção** (Reel) = retenção média ÷ duração do vídeo; skip rate nos 3 s

Benchmarks de mercado para taxa de engajamento (**[MEDIDO]**, Socialinsider, 1º–2º tri/2026, por seguidor): carrossel ≈ 0,50–0,55%; Reels ≈ 0,48%; imagem única ≈ 0,33%. Mixed-format carousel (Metricool) ≈ 2,33% mediana (base de cálculo diferente — não misturar). O engajamento orgânico geral caiu ~24% a/a em 2025. Nossa referência histórica (Análise de Instagram, ago/2026): ~1,1% de curtida ÷ seguidor, 0–1 comentário por post.

## 3. Armadilhas de leitura (todas já aconteceram ou vão acontecer)

1. **Post impulsionado.** Aviso "turbinado" no post e abas "Tudo/Anúncio" no insights. Visualização paga não é orgânica. O painel de **conta** soma pago + orgânico (houve anúncio ativo em 20/set). **Sempre separar** antes de concluir.
2. **Filtro de período.** Trocar o dropdown não atualiza; recarregar a URL com `?timeframe=7` (ver `coleta-de-dados.md`).
3. **Amostra pequena.** Uma peça não é tendência; 3 peças do mesmo tipo/tema começam a ser. Dizer o "n" sempre.
4. **Idade do post.** Visualização acumulada de peça de 3 semanas × peça de 3 dias: comparar na mesma janela (ex.: primeiras 72 h) ou citar a idade.
5. **Pico de seguidores sem peça.** Seguidor ganho na semana pode vir de impulsionamento, menção de terceiros ou Stories — cruzar antes de atribuir.
6. **Alcance de Stories ≠ de feed.** Stories alcançam quem já segue; não medir descoberta com Story.
7. **Viés de sobrevivente.** O que foi postado é o que o time achou bom; descartes e atrasos não aparecem. Cruzar com a pauta.
8. **Correlação com vendas.** Instagram influencia por efeito indireto (busca da marca, WhatsApp, lembrança). Vendas sem parâmetro são a regra, não a exceção (`dados/Ponte Pedido x GA4 x Ads — vendas sem parametro`). Não prometer "esse post vendeu R$ X" sem rastro (cupom, UTM, DM).

## 4. O elo fraco: do Instagram ao pedido

Hoje não temos atribuição direta de Instagram a pedido além de: link da bio (UTM, se configurado), cupom por canal e a pergunta "como conheceu?". Antes de cobrar "post → venda", **fechar o rastro** (proposta em `rotinas-e-modelos.md` §6): UTM no link da bio e do sticker, cupom exclusivo de Story, contagem de DMs/WhatsApp vindos de Instagram. Dados de pedido e origem via `analista-de-dados`; UTM/atribuição via `especialista-google`.

## 5. Painel semanal — tabela mínima (formato do relatório Notion)

| Métrica | Semana | Semana anterior | Δ% | Leitura |
|---|---|---|---|---|
| Visualizações (total, orgânico) | | | | |
| Contas alcançadas / % não seguidores | | | | |
| Interações | | | | |
| Seguidores (fim, líquidos na semana) | | | | |
| Posts por formato (Reel / Carrossel / Foto / Story) | | | | |
| Melhor peça (por taxa, não por volume) | | | | |
| Pior peça | | | | |
| Anúncio ativo na semana? | sim/não | | | (se sim, separar) |

## 6. Série histórica já registrada (para não reabrir)

- **08–14/set/2026:** relatório no Notion (cadência 5–6 posts normalizada).
- **14–20/set/2026:** 33.449 views (+19%), 1.765 interações (+22%), 11.080 seguidores (+110). Carrossel "red flags em dinâmicas bdsm" (18/set): 7.831 views, 45,8% de não seguidores, +30 seguidores. Nenhum Reel na semana. Anúncio "Teste Geral 17/09/26" ativo.
- **Recorde de peça:** carrossel de 7/set — 9.810 views vitalícias (conferir se ainda é o maior antes de dizer "melhor da série").
- **Ago/2026 (público):** 10.854 seguidores, 0 Reels, ~118 curtidas/post, post de produto (Kit Shibari Iniciante, 18/abr) com 648 curtidas = outlier.
