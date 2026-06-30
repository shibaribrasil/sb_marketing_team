-- ============================================================
-- QUERIES — Relatório Diagnóstico Google Ads · Shibari Brasil
-- Projeto BQ: igneous-sandbox-381622
-- Dataset: datalake_google_ads
-- ID da conta Ads: 4241689372
--
-- INSTRUÇÃO DE USO:
--   Sempre rodar via arquivo para evitar problema de escaping
--   de backticks no PowerShell. Usar:
--     cmd /c "bq query --use_legacy_sql=false --format=json < queries.sql"
--   Ou segmentar por bloco copiando para um .sql temporário.
--
-- NOTAS DE SCHEMA (validadas em 24/06/2026):
--   - ads_CampaignBasicStats não tem campaign_name — requer JOIN com ads_Campaign
--   - ads_CampaignConversionStats não tem campaign_name — requer JOIN com ads_Campaign
--   - ad_group_criterion_negative é BOOL (não STRING) — comparar com false, não 'false'
--   - campaign_budget_type não existe — usar campaign_budget_period se necessário
--   - ads_SearchQueryPerformanceReport não disponível neste dataset
-- ============================================================


-- ────────────────────────────────────────────────────────────
-- Q1 · ESTRUTURA DE CAMPANHAS
-- Uso: HEADER do relatório + Seção 2 (coluna Budget/d e Status)
-- Filtro: _DATA_DATE = _LATEST_DATE (snapshot mais recente)
-- ────────────────────────────────────────────────────────────
SELECT
  campaign_name,
  campaign_status,
  campaign_budget_amount_micros / 1000000 AS orcamento_diario
FROM `igneous-sandbox-381622.datalake_google_ads.ads_Campaign_4241689372`
WHERE _DATA_DATE = _LATEST_DATE
ORDER BY campaign_name;


-- ────────────────────────────────────────────────────────────
-- Q2 · PERFORMANCE POR CAMPANHA (período configurável)
-- Uso: Seção 1 (totais), Seção 2 (tabela), Seção 6 (gasto/d)
-- Parâmetro: ajustar INTERVAL N DAY para o período desejado
-- JOIN obrigatório para obter campaign_name
-- ────────────────────────────────────────────────────────────
SELECT
  c.campaign_name,
  SUM(b.metrics_cost_micros) / 1000000                                                          AS custo_total,
  SUM(b.metrics_impressions)                                                                     AS impressoes,
  SUM(b.metrics_clicks)                                                                          AS cliques,
  SAFE_DIVIDE(SUM(b.metrics_clicks), SUM(b.metrics_impressions))                                AS ctr,
  SAFE_DIVIDE(SUM(b.metrics_cost_micros) / 1000000, SUM(b.metrics_clicks))                     AS cpc_medio,
  SUM(b.metrics_conversions)                                                                     AS conversoes,
  SUM(b.metrics_conversions_value)                                                               AS valor_conversoes,
  SAFE_DIVIDE(SUM(b.metrics_cost_micros) / 1000000, NULLIF(SUM(b.metrics_conversions), 0))     AS cpa,
  SAFE_DIVIDE(SUM(b.metrics_conversions_value), SAFE_DIVIDE(SUM(b.metrics_cost_micros), 1000000)) AS roas,
  MIN(b.segments_date)                                                                           AS data_inicio,
  MAX(b.segments_date)                                                                           AS data_fim
FROM `igneous-sandbox-381622.datalake_google_ads.ads_CampaignBasicStats_4241689372` b
JOIN `igneous-sandbox-381622.datalake_google_ads.ads_Campaign_4241689372` c
  ON b.campaign_id = c.campaign_id AND c._DATA_DATE = c._LATEST_DATE
WHERE b.segments_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 9 DAY)
  AND b.segments_date < CURRENT_DATE()
GROUP BY c.campaign_name
ORDER BY custo_total DESC;


-- ────────────────────────────────────────────────────────────
-- Q3 · TENDÊNCIA DIÁRIA DA CONTA
-- Uso: Seção 3 (gráfico gasto + cliques por dia)
-- Agrega todas as campanhas por data
-- ────────────────────────────────────────────────────────────
SELECT
  segments_date,
  SUM(metrics_cost_micros) / 1000000 AS custo,
  SUM(metrics_impressions)            AS impressoes,
  SUM(metrics_clicks)                 AS cliques,
  SUM(metrics_conversions)            AS conversoes,
  SUM(metrics_conversions_value)      AS valor_conversoes
FROM `igneous-sandbox-381622.datalake_google_ads.ads_AccountStats_4241689372`
WHERE segments_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 9 DAY)
  AND segments_date < CURRENT_DATE()
GROUP BY segments_date
ORDER BY segments_date;


-- ────────────────────────────────────────────────────────────
-- Q4 · CONVERSÕES POR TIPO (separar compras de micro-conversões)
-- Uso: Seção 3 (tabela de eventos), Seção 1 (receita real)
-- CRÍTICO: filtrar segments_conversion_action_category = 'PURCHASE'
--          para calcular ROAS e ROI reais (excluir PAGE_VIEW, etc.)
-- Exemplos observados: PURCHASE, PAGE_VIEW, BEGIN_CHECKOUT
-- ────────────────────────────────────────────────────────────
SELECT
  c.campaign_name,
  cv.segments_conversion_action_name,
  cv.segments_conversion_action_category,
  SUM(cv.metrics_conversions)       AS conversoes,
  SUM(cv.metrics_conversions_value) AS valor
FROM `igneous-sandbox-381622.datalake_google_ads.ads_CampaignConversionStats_4241689372` cv
JOIN `igneous-sandbox-381622.datalake_google_ads.ads_Campaign_4241689372` c
  ON cv.campaign_id = c.campaign_id AND c._DATA_DATE = c._LATEST_DATE
WHERE cv.segments_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 9 DAY)
  AND cv.segments_date < CURRENT_DATE()
GROUP BY c.campaign_name, cv.segments_conversion_action_name, cv.segments_conversion_action_category
ORDER BY c.campaign_name, conversoes DESC;


-- ────────────────────────────────────────────────────────────
-- Q5 · KEYWORDS E QUALITY SCORE
-- Uso: Seção 4 (tabela de keywords e LP experience)
-- Notas:
--   - ad_group_criterion_negative é BOOL → comparar com false (não 'false')
--   - Campos de qualidade disponíveis:
--       ad_group_criterion_quality_info_quality_score         (0–10)
--       ad_group_criterion_quality_info_search_predicted_ctr  (ABOVE_AVERAGE / AVERAGE / BELOW_AVERAGE)
--       ad_group_criterion_quality_info_creative_quality_score
--       ad_group_criterion_quality_info_post_click_quality_score
--   - Campo que NÃO existe: ad_group_criterion_quality_info_ad_relevance
--     (usar creative_quality_score no lugar)
-- ────────────────────────────────────────────────────────────
SELECT
  c.campaign_name,
  k.ad_group_criterion_keyword_text                             AS keyword,
  k.ad_group_criterion_keyword_match_type                       AS match_type,
  k.ad_group_criterion_quality_info_quality_score               AS quality_score,
  k.ad_group_criterion_quality_info_search_predicted_ctr        AS predicted_ctr,
  k.ad_group_criterion_quality_info_creative_quality_score      AS ad_relevance,
  k.ad_group_criterion_quality_info_post_click_quality_score    AS lp_experience,
  k.ad_group_criterion_status                                   AS status
FROM `igneous-sandbox-381622.datalake_google_ads.ads_Keyword_4241689372` k
JOIN `igneous-sandbox-381622.datalake_google_ads.ads_Campaign_4241689372` c
  ON k.campaign_id = c.campaign_id AND c._DATA_DATE = c._LATEST_DATE
WHERE k._DATA_DATE = k._LATEST_DATE
  AND k.ad_group_criterion_negative = false
ORDER BY k.ad_group_criterion_quality_info_quality_score DESC
LIMIT 50;


-- ────────────────────────────────────────────────────────────
-- Q6 · ANÁLISE DE ORÇAMENTO (Seção 6)
-- Uso: Seção 6 — budget atual, gasto médio diário, utilização
-- Parâmetro: INTERVAL 14 DAY para referência de médio prazo
--            INTERVAL 9 DAY para alinhar com período do relatório
-- ATENÇÃO: LEFT JOIN para incluir campanhas sem gasto no período
-- ────────────────────────────────────────────────────────────
SELECT
  c.campaign_name,
  c.campaign_status,
  c.campaign_budget_amount_micros / 1000000                                               AS orcamento_diario,
  SUM(b.metrics_cost_micros) / 1000000 / 9                                               AS gasto_medio_diario,
  SAFE_DIVIDE(
    SUM(b.metrics_cost_micros) / 1000000 / 9,
    c.campaign_budget_amount_micros / 1000000
  )                                                                                       AS utilizacao_pct,
  SAFE_DIVIDE(SUM(b.metrics_cost_micros) / 1000000, NULLIF(SUM(b.metrics_conversions), 0)) AS cpa_periodo,
  SAFE_DIVIDE(SUM(b.metrics_conversions_value), SAFE_DIVIDE(SUM(b.metrics_cost_micros), 1000000)) AS roas_periodo
FROM `igneous-sandbox-381622.datalake_google_ads.ads_Campaign_4241689372` c
LEFT JOIN `igneous-sandbox-381622.datalake_google_ads.ads_CampaignBasicStats_4241689372` b
  ON c.campaign_id = b.campaign_id
  AND b.segments_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 9 DAY)
  AND b.segments_date < CURRENT_DATE()
WHERE c._DATA_DATE = c._LATEST_DATE
GROUP BY c.campaign_name, c.campaign_status, c.campaign_budget_amount_micros
ORDER BY gasto_medio_diario DESC;


-- ────────────────────────────────────────────────────────────
-- Q7 · IMPRESSION SHARE (quando disponível)
-- Uso: Seção 4 (diagnóstico de perda de impressão)
-- ATENÇÃO: campo frequentemente indisponível no BQ Export.
--          Se retornar NULL, marcar como ⚠ no checklist.
-- ────────────────────────────────────────────────────────────
SELECT
  c.campaign_name,
  AVG(b.metrics_search_impression_share)                    AS impression_share,
  AVG(b.metrics_search_budget_lost_impression_share)        AS perda_budget,
  AVG(b.metrics_search_rank_lost_impression_share)          AS perda_ranking
FROM `igneous-sandbox-381622.datalake_google_ads.ads_CampaignBasicStats_4241689372` b
JOIN `igneous-sandbox-381622.datalake_google_ads.ads_Campaign_4241689372` c
  ON b.campaign_id = c.campaign_id AND c._DATA_DATE = c._LATEST_DATE
WHERE b.segments_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 9 DAY)
  AND b.segments_date < CURRENT_DATE()
GROUP BY c.campaign_name
ORDER BY impression_share DESC;


-- ────────────────────────────────────────────────────────────
-- Q8 · PERFORMANCE POR KEYWORD (gasto + conversões individuais)
-- Uso: Seção 4 (tabela de keywords com gasto)
-- JOIN duplo: Keyword + CampaignBasicStats não é direto —
--   usar KeywordBasicStats se disponível no dataset
-- ────────────────────────────────────────────────────────────
SELECT
  c.campaign_name,
  k.ad_group_criterion_keyword_text     AS keyword,
  k.ad_group_criterion_keyword_match_type AS match_type,
  SUM(kb.metrics_cost_micros) / 1000000 AS custo,
  SUM(kb.metrics_impressions)           AS impressoes,
  SUM(kb.metrics_clicks)                AS cliques,
  SAFE_DIVIDE(SUM(kb.metrics_clicks), SUM(kb.metrics_impressions)) AS ctr,
  SAFE_DIVIDE(SUM(kb.metrics_cost_micros) / 1000000, SUM(kb.metrics_clicks)) AS cpc,
  SUM(kb.metrics_conversions)           AS conversoes
FROM `igneous-sandbox-381622.datalake_google_ads.ads_KeywordBasicStats_4241689372` kb
JOIN `igneous-sandbox-381622.datalake_google_ads.ads_Keyword_4241689372` k
  ON kb.ad_group_criterion_criterion_id = k.ad_group_criterion_criterion_id
  AND kb.ad_group_id = k.ad_group_id
  AND k._DATA_DATE = k._LATEST_DATE
  AND k.ad_group_criterion_negative = false
JOIN `igneous-sandbox-381622.datalake_google_ads.ads_Campaign_4241689372` c
  ON kb.campaign_id = c.campaign_id AND c._DATA_DATE = c._LATEST_DATE
WHERE kb.segments_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 9 DAY)
  AND kb.segments_date < CURRENT_DATE()
GROUP BY c.campaign_name, k.ad_group_criterion_keyword_text, k.ad_group_criterion_keyword_match_type
ORDER BY custo DESC
LIMIT 30;
-- NOTA: ads_KeywordBasicStats ainda não foi validada neste dataset.
--       Se falhar, verificar nome exato da tabela com:
--       SELECT table_name FROM igneous-sandbox-381622.datalake_google_ads.INFORMATION_SCHEMA.TABLES
--       WHERE table_name LIKE '%Keyword%'
