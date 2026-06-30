# Google Ads no BigQuery — Resumo Técnico

> Baseado na documentação oficial do Google Cloud:
> - https://cloud.google.com/bigquery/docs/google-ads-transfer
> - https://cloud.google.com/bigquery/docs/google-ads-transformation

---

## 1. Como os dados chegam

O Google Ads usa o **BigQuery Data Transfer Service (BDTS)** para exportar os dados. As tabelas são **particionadas por data** — cada partição corresponde à data dos dados exportados.

- A frequência máxima de transferência é **uma vez por dia**
- Se você rodar múltiplas transferências para a mesma data, a partição é **sobrescrita** com os dados mais recentes (sem duplicação)
- Existe uma **refresh window** (janela de atualização): o número de dias anteriores que o transfer reprocessa a cada execução (geralmente 3 dias)

### Backfill

Se precisar de dados históricos fora da refresh window, é necessário iniciar um **backfill manual**. Isso também é necessário para recuperar dados de períodos com falha na transferência.

---

## 2. Estrutura do dataset

Ao configurar o transfer, um dataset é criado no seu projeto com **dois tipos de tabelas**:

### Stats Tables (Performance)
Contêm métricas de performance particionadas por dia. São as tabelas que você vai usar para analisar resultados.

| Tabela | O que contém |
|--------|-------------|
| `CampaignStats` | Métricas por campanha por dia |
| `AdGroupStats` | Métricas por grupo de anúncios por dia |
| `AdStats` | Métricas por anúncio por dia |
| `KeywordStats` | Métricas por palavra-chave por dia |
| `SearchQueryStats` | Métricas por termo de busca por dia |
| `GeoStats` | Métricas por localização geográfica |
| `AgeRangeStats` | Métricas segmentadas por faixa etária |
| `GenderStats` | Métricas segmentadas por gênero |
| `AudienceStats` | Métricas por audiência |
| `ShoppingProductStats` | Métricas por produto (Shopping) |
| `VideoStats` | Métricas para anúncios de vídeo |

### Match Tables / Attribute Tables (Atributos)
Snapshots dos atributos das entidades (nomes, configurações, status). São atualizados uma vez por dia com o estado atual.

| Tabela | O que contém |
|--------|-------------|
| `Campaign` | Atributos das campanhas (nome, status, tipo, budget, datas) |
| `AdGroup` | Atributos dos grupos de anúncios |
| `Ad` | Atributos dos anúncios (título, descrição, URL) |
| `Keyword` | Atributos das palavras-chave (texto, match type, bid) |
| `Customer` | Atributos da conta (nome, moeda, fuso horário) |
| `CampaignBudget` | Configurações de orçamento por campanha |
| `BiddingStrategy` | Estratégias de lances configuradas |
| `CampaignLabel` | Labels associadas a campanhas |
| `AdGroupLabel` | Labels associadas a grupos de anúncios |
| `AdGroupBidModifier` | Modificadores de lance por grupo de anúncios |

### Tabelas de Performance Max (PMax)
Só existem se você habilitou a opção **"Include PMax Campaign Tables"** na configuração do transfer.

> ⚠️ **Atenção:** ao habilitar PMax, as tabelas acima perdem os campos `ad_group_*` porque a API do Google Ads filtra esses dados para PMax.

| Tabela | O que contém |
|--------|-------------|
| `AssetGroup` | Grupos de assets das campanhas PMax |
| `AssetGroupAsset` | Assets individuais por grupo |
| `CampaignAssetStats` | Métricas de assets em campanhas |

---

## 3. Estrutura das colunas (campos padrão)

Toda tabela criada pelo Google Ads transfer contém os seguintes campos base:

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `_DATA_DATE` | DATE | Data da partição (data dos dados) |
| `_LATEST_DATE` | DATE | Data da partição mais recente disponível |
| `customer_id` | INT64 | ID da conta do Google Ads |

Nas Stats Tables, os campos de métricas mais comuns são:

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `metrics_impressions` | INT64 | Número de impressões |
| `metrics_clicks` | INT64 | Número de cliques |
| `metrics_cost_micros` | INT64 | Custo em micros (dividir por 1.000.000 para obter o valor real) |
| `metrics_conversions` | FLOAT64 | Número de conversões |
| `metrics_conversions_value` | FLOAT64 | Valor das conversões |
| `metrics_all_conversions` | FLOAT64 | Todas as conversões (incluindo view-through) |
| `metrics_view_through_conversions` | INT64 | Conversões por visualização |
| `metrics_video_views` | INT64 | Visualizações de vídeo |

---

## 4. Como fazer JOINs entre tabelas

O padrão é sempre juntar uma **Stats Table** com a **Match Table** correspondente pelo campo de ID.

### Exemplo: performance por nome de campanha

```sql
SELECT
  s._DATA_DATE AS data,
  c.campaign_name AS campanha,
  s.metrics_impressions AS impressoes,
  s.metrics_clicks AS cliques,
  s.metrics_cost_micros / 1000000 AS custo,
  s.metrics_conversions AS conversoes
FROM
  `seu_projeto.seu_dataset.CampaignStats` s
LEFT JOIN
  `seu_projeto.seu_dataset.Campaign` c
  ON s.campaign_id = c.campaign_id
  AND s._DATA_DATE = c._DATA_DATE
WHERE
  s._DATA_DATE BETWEEN '2024-01-01' AND '2024-01-31'
ORDER BY
  s._DATA_DATE, custo DESC
```

### Exemplo: análise por palavra-chave com grupo e campanha

```sql
SELECT
  s._DATA_DATE AS data,
  c.campaign_name AS campanha,
  ag.ad_group_name AS grupo,
  k.ad_group_criterion_keyword_text AS palavra_chave,
  k.ad_group_criterion_keyword_match_type AS match_type,
  s.metrics_clicks AS cliques,
  s.metrics_cost_micros / 1000000 AS custo,
  s.metrics_conversions AS conversoes
FROM
  `seu_projeto.seu_dataset.KeywordStats` s
LEFT JOIN `seu_projeto.seu_dataset.Keyword` k
  ON s.ad_group_criterion_criterion_id = k.ad_group_criterion_criterion_id
  AND s._DATA_DATE = k._DATA_DATE
LEFT JOIN `seu_projeto.seu_dataset.AdGroup` ag
  ON s.ad_group_id = ag.ad_group_id
  AND s._DATA_DATE = ag._DATA_DATE
LEFT JOIN `seu_projeto.seu_dataset.Campaign` c
  ON s.campaign_id = c.campaign_id
  AND s._DATA_DATE = c._DATA_DATE
WHERE
  s._DATA_DATE BETWEEN '2024-01-01' AND '2024-01-31'
```

---

## 5. Métricas principais e como calculá-las

| Métrica | Fórmula |
|---------|---------|
| **CPC médio** | `metrics_cost_micros / 1000000 / metrics_clicks` |
| **CTR** | `metrics_clicks / metrics_impressions` |
| **Taxa de conversão** | `metrics_conversions / metrics_clicks` |
| **CPA (custo por aquisição)** | `metrics_cost_micros / 1000000 / metrics_conversions` |
| **ROAS** | `metrics_conversions_value / (metrics_cost_micros / 1000000)` |
| **CPM** | `(metrics_cost_micros / 1000000 / metrics_impressions) * 1000` |

> ⚠️ **Custo em micros:** o campo `metrics_cost_micros` armazena o custo multiplicado por 1.000.000. Sempre divida por 1.000.000 para obter o valor em moeda real.

---

## 6. Cuidados essenciais nas consultas

### 6.1 Sempre filtre por `_DATA_DATE`
As tabelas são particionadas. Não filtrar por data resulta em varredura completa e custo alto no BigQuery.

```sql
-- ✅ Correto
WHERE _DATA_DATE = '2024-01-15'

-- ✅ Intervalo
WHERE _DATA_DATE BETWEEN '2024-01-01' AND '2024-01-31'

-- ✅ Dados mais recentes
WHERE _DATA_DATE = (SELECT MAX(_DATA_DATE) FROM `...CampaignStats`)
```

### 6.2 Use `_LATEST_DATE` para dados atuais
Para relatórios que sempre mostram o estado mais recente, use o campo `_LATEST_DATE`:

```sql
WHERE _DATA_DATE = _LATEST_DATE
```

### 6.3 JOINs precisam incluir a data
Match Tables também são particionadas. Se você não incluir a data no JOIN, pode obter múltiplas linhas ou dados desatualizados.

```sql
-- ✅ Correto
ON s.campaign_id = c.campaign_id AND s._DATA_DATE = c._DATA_DATE

-- ❌ Incorreto (pode duplicar linhas)
ON s.campaign_id = c.campaign_id
```

### 6.4 Divisão por zero
Ao calcular taxas, sempre proteja contra divisão por zero:

```sql
SAFE_DIVIDE(metrics_conversions, metrics_clicks) AS taxa_conversao
-- ou
CASE WHEN metrics_clicks > 0 THEN metrics_conversions / metrics_clicks ELSE 0 END
```

### 6.5 PMax muda o schema
Se você ativou PMax, algumas tabelas **não possuem campos de ad_group**. Verifique antes de fazer JOINs com `AdGroup`.

### 6.6 Múltiplas contas (MCC)
Se sua transferência foi feita no nível de Manager Account (MCC), todas as contas ficam na mesma tabela. Use `customer_id` para filtrar por conta específica.

```sql
WHERE customer_id = 123456789
```

### 6.7 Backfills e refresh window
Dados dos últimos dias podem ainda estar sendo atualizados pela refresh window. Para análises definitivas, prefira datas com mais de 3 dias de antecedência.

---

## 7. Relatórios comuns

### Performance de campanhas no mês

```sql
SELECT
  c.campaign_name,
  SUM(s.metrics_impressions) AS impressoes,
  SUM(s.metrics_clicks) AS cliques,
  SUM(s.metrics_cost_micros) / 1000000 AS custo_total,
  SUM(s.metrics_conversions) AS conversoes,
  SAFE_DIVIDE(SUM(s.metrics_cost_micros) / 1000000, SUM(s.metrics_conversions)) AS cpa,
  SAFE_DIVIDE(SUM(s.metrics_conversions_value), SUM(s.metrics_cost_micros) / 1000000) AS roas
FROM `seu_projeto.seu_dataset.CampaignStats` s
LEFT JOIN `seu_projeto.seu_dataset.Campaign` c
  ON s.campaign_id = c.campaign_id AND s._DATA_DATE = c._DATA_DATE
WHERE s._DATA_DATE BETWEEN '2024-01-01' AND '2024-01-31'
GROUP BY c.campaign_name
ORDER BY custo_total DESC
```

### Top palavras-chave por custo

```sql
SELECT
  k.ad_group_criterion_keyword_text AS palavra_chave,
  k.ad_group_criterion_keyword_match_type AS match_type,
  SUM(s.metrics_clicks) AS cliques,
  SUM(s.metrics_cost_micros) / 1000000 AS custo,
  SUM(s.metrics_conversions) AS conversoes,
  SAFE_DIVIDE(SUM(s.metrics_cost_micros) / 1000000, SUM(s.metrics_conversions)) AS cpa
FROM `seu_projeto.seu_dataset.KeywordStats` s
LEFT JOIN `seu_projeto.seu_dataset.Keyword` k
  ON s.ad_group_criterion_criterion_id = k.ad_group_criterion_criterion_id
  AND s._DATA_DATE = k._DATA_DATE
WHERE s._DATA_DATE BETWEEN '2024-01-01' AND '2024-01-31'
GROUP BY 1, 2
ORDER BY custo DESC
LIMIT 50
```

---

## 8. Links úteis

- [Documentação oficial do transfer](https://cloud.google.com/bigquery/docs/google-ads-transfer)
- [Mapeamento de relatórios e tabelas](https://cloud.google.com/bigquery/docs/google-ads-transformation)
- [Google Ads Query Builder (GAQL)](https://developers.google.com/google-ads/api/fields/v17/overview_query_builder)
- [Referência de campos da API do Google Ads](https://developers.google.com/google-ads/api/fields/v17/overview)
