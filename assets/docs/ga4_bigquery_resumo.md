# Google Analytics 4 (GA4) no BigQuery — Resumo Técnico

> Baseado na documentação oficial do Google:
> - https://support.google.com/analytics/answer/7029846 (schema events)
> - https://support.google.com/analytics/answer/12769371 (schema user data)

---

## 1. Como os dados chegam

O GA4 exporta dados para o BigQuery via integração nativa na própria interface do GA4 (Admin > BigQuery Linking). Ao ativar, um dataset chamado `analytics_<property_id>` é criado automaticamente no seu projeto.

> ⚠️ **O export é forward-only:** você só recebe dados a partir do momento em que ativou o link. Não há backfill automático de dados históricos.

### Tipos de export disponíveis

| Tipo | Tabela gerada | Atualização |
|------|--------------|-------------|
| **Daily** | `events_YYYYMMDD` | Uma vez por dia (dados do dia anterior) |
| **Streaming** | `events_intraday_YYYYMMDD` | Contínua ao longo do dia |

A tabela `events_intraday_YYYYMMDD` é **deletada automaticamente** ao final do dia quando a tabela diária fica pronta.

### Latência e reprocessamento
As tabelas diárias continuam sendo **atualizadas por até 72 horas** após a data do evento. Isso ocorre porque eventos de apps mobile e Measurement Protocol podem chegar com atraso. Para análises definitivas, evite consultar os últimos 3 dias.

---

## 2. Estrutura das tabelas

### Diferença fundamental em relação ao Google Ads

No GA4, **não há dezenas de tabelas separadas**. Praticamente tudo fica em uma única tabela (`events_*`), onde **cada linha representa um evento**. Isso é diferente do Google Ads, onde há tabelas separadas por entidade.

### Tabelas no dataset

| Tabela | O que contém |
|--------|-------------|
| `events_YYYYMMDD` | Todos os eventos do dia (tabela principal) |
| `events_intraday_YYYYMMDD` | Eventos do dia atual em tempo quase-real |
| `pseudonymous_users_YYYYMMDD` | Dados de usuários pseudônimos (se ativado) |
| `users_YYYYMMDD` | Dados de usuários identificados por User ID (se ativado) |

---

## 3. Schema da tabela events_*

### Campos de nível raiz (flat)

Esses campos são acessados diretamente, sem necessidade de `UNNEST`.

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `event_date` | STRING | Data do evento (formato YYYYMMDD) |
| `event_timestamp` | INT64 | Timestamp do evento em microssegundos (UTC) |
| `event_name` | STRING | Nome do evento (ex: `page_view`, `purchase`) |
| `event_value_in_usd` | FLOAT64 | Valor do evento em USD |
| `event_bundle_sequence_id` | INT64 | ID do batch de envio |
| `user_id` | STRING | User ID definido pelo seu código (pode ser nulo) |
| `user_pseudo_id` | STRING | Client ID anonimizado (cookie/device ID) |
| `stream_id` | STRING | ID do data stream GA4 |
| `platform` | STRING | Plataforma (`WEB`, `ANDROID`, `IOS`) |

### Campos de dispositivo (device.*)

Acessados com dot notation: `device.category`, `device.browser`, etc.

| Campo | Descrição |
|-------|-----------|
| `device.category` | Categoria do dispositivo (`desktop`, `mobile`, `tablet`) |
| `device.mobile_brand_name` | Marca do dispositivo mobile |
| `device.mobile_model_name` | Modelo do dispositivo mobile |
| `device.operating_system` | Sistema operacional |
| `device.operating_system_version` | Versão do SO |
| `device.browser` | Navegador |
| `device.browser_version` | Versão do navegador |
| `device.language` | Idioma configurado no dispositivo |
| `device.web_info.hostname` | Domínio do site onde o evento ocorreu |

### Campos de geo (geo.*)

| Campo | Descrição |
|-------|-----------|
| `geo.country` | País |
| `geo.region` | Estado/região |
| `geo.city` | Cidade |
| `geo.continent` | Continente |

### Campos de origem de tráfego (traffic_source.*)

> ⚠️ Esses campos representam a **primeira fonte de tráfego do usuário** (first touch), não necessariamente a da sessão atual.

| Campo | Descrição |
|-------|-----------|
| `traffic_source.source` | Fonte (ex: `google`, `facebook`) |
| `traffic_source.medium` | Meio (ex: `cpc`, `organic`) |
| `traffic_source.name` | Nome da campanha |

> ⚠️ **Esses campos nunca são populados nas tabelas intraday.** Use apenas as tabelas diárias para análise de tráfego.

### Campos de usuário (user_ltv.*)

| Campo | Descrição |
|-------|-----------|
| `user_ltv.revenue` | Receita total do usuário ao longo do tempo |
| `user_ltv.currency` | Moeda da receita |

### Campos de informações de sessão (collected_traffic_source.*)

Esses campos capturam a fonte de tráfego **da sessão atual** (mais úteis que `traffic_source.*` para análise de campanha):

| Campo | Descrição |
|-------|-----------|
| `collected_traffic_source.manual_source` | Parâmetro `utm_source` |
| `collected_traffic_source.manual_medium` | Parâmetro `utm_medium` |
| `collected_traffic_source.manual_campaign_name` | Parâmetro `utm_campaign` |
| `collected_traffic_source.gclid` | Google Click ID (integração com Google Ads) |

---

## 4. Campos aninhados: RECORD e REPEATED

### Campos RECORD
Funcionam como sub-objetos. Acesse com **dot notation**:
```sql
SELECT device.category, geo.country FROM `...events_*`
```

### Campos REPEATED (arrays)
Contêm múltiplos valores em uma única linha. Precisam de **UNNEST** para serem consultados.

Os principais campos REPEATED são:

- `event_params` — parâmetros do evento (chave/valor)
- `user_properties` — propriedades do usuário
- `items` — itens de e-commerce

### Como usar UNNEST em event_params

`event_params` é onde ficam os parâmetros customizados e os padrão do GA4 (como `page_location`, `session_id`, `ga_session_number`, etc.).

**Padrão recomendado — inline subquery (mais eficiente):**
```sql
SELECT
  event_name,
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'page_location') AS pagina,
  (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'ga_session_id') AS session_id,
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'source') AS fonte
FROM `seu_projeto.analytics_XXXXXXX.events_*`
WHERE _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
```

**Quando o valor pode ser string ou int (use COALESCE):**
```sql
COALESCE(
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'value'),
  CAST((SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'value') AS STRING)
) AS valor
```

---

## 5. Eventos padrão do GA4

Estes eventos são coletados automaticamente pelo GA4 e estarão presentes em praticamente qualquer propriedade web:

| Evento | Quando ocorre |
|--------|--------------|
| `session_start` | Início de uma sessão |
| `first_visit` | Primeira visita do usuário |
| `page_view` | Visualização de página |
| `scroll` | Scroll de 90% da página |
| `click` | Clique em link externo |
| `view_search_results` | Resultado de busca no site |
| `file_download` | Download de arquivo |
| `video_start` | Início de vídeo YouTube |
| `video_progress` | Progresso de vídeo (25%, 50%, 75%) |
| `video_complete` | Conclusão de vídeo |
| `purchase` | Compra concluída (e-commerce) |
| `add_to_cart` | Item adicionado ao carrinho |
| `begin_checkout` | Início do checkout |

---

## 6. Como filtrar as tabelas (wildcard vs suffix)

As tabelas do GA4 usam **date-sharding** (sufixo de data no nome), não particionamento nativo. Para consultar múltiplas datas, use o padrão wildcard `events_*` com filtro em `_TABLE_SUFFIX`:

```sql
-- ✅ Correto: filtra por sufixo (não escaneia tabelas fora do range)
FROM `seu_projeto.analytics_XXXXXXX.events_*`
WHERE _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'

-- ✅ Para um dia específico
FROM `seu_projeto.analytics_XXXXXXX.events_20240115`

-- ✅ Para incluir intraday junto com histórico (combinar)
FROM `seu_projeto.analytics_XXXXXXX.events_*`
WHERE _TABLE_SUFFIX >= '20240101'

-- ❌ Incorreto: sem filtro de suffix escaneia TODAS as tabelas (caro!)
FROM `seu_projeto.analytics_XXXXXXX.events_*`
```

---

## 7. Métricas principais e como calculá-las

### Sessões
> ⚠️ **Nunca conte `session_start` para calcular sessões.** Use a combinação `user_pseudo_id + ga_session_id` como chave única.

```sql
-- Contagem correta de sessões únicas
SELECT
  COUNT(DISTINCT CONCAT(
    user_pseudo_id,
    CAST((SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'ga_session_id') AS STRING)
  )) AS sessoes
FROM `seu_projeto.analytics_XXXXXXX.events_*`
WHERE _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
```

### Usuários únicos
```sql
SELECT COUNT(DISTINCT user_pseudo_id) AS usuarios
FROM `seu_projeto.analytics_XXXXXXX.events_*`
WHERE _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
```

### Pageviews
```sql
SELECT COUNT(*) AS pageviews
FROM `seu_projeto.analytics_XXXXXXX.events_*`
WHERE _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
  AND event_name = 'page_view'
```

### Receita (e-commerce)
```sql
SELECT
  SUM(event_value_in_usd) AS receita_usd
FROM `seu_projeto.analytics_XXXXXXX.events_*`
WHERE _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
  AND event_name = 'purchase'
```

### Taxa de engajamento
```sql
-- Sessões engajadas = duração > 10s OU 2+ pageviews OU conversão
SELECT
  SAFE_DIVIDE(
    COUNTIF((SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'session_engaged') = 1),
    COUNT(DISTINCT CONCAT(user_pseudo_id, CAST((SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'ga_session_id') AS STRING)))
  ) AS taxa_engajamento
FROM `seu_projeto.analytics_XXXXXXX.events_*`
WHERE _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
  AND event_name = 'session_start'
```

---

## 8. Cuidados essenciais nas consultas

### 8.1 Sempre filtre por `_TABLE_SUFFIX`
Sem esse filtro, o BigQuery escaneia todas as tabelas do dataset — custo altíssimo.

### 8.2 Tabelas intraday têm campos ausentes
Nunca use `traffic_source.*`, `user_ltv.*` e `is_active_user` em consultas nas tabelas intraday — esses campos sempre aparecem nulos nelas.

### 8.3 `user_pseudo_id` não é único por usuário real
Um mesmo usuário em dispositivos diferentes terá `user_pseudo_id` diferentes. Use `user_id` (que você define no código) para identificação cross-device, mas ele pode ser nulo se não implementado.

### 8.4 `ga_session_id` não é único por si só
Dois usuários diferentes podem ter o mesmo `ga_session_id` por coincidência. **Sempre combine com `user_pseudo_id`** para identificar sessões únicas:
```sql
CONCAT(user_pseudo_id, '-', CAST(session_id AS STRING)) AS session_key
```

### 8.5 Discrepâncias com a interface do GA4
Os números no BigQuery podem diferir da interface do GA4 por:
- A UI usa aproximações (HyperLogLog++) para contagens de alta cardinalidade
- O BigQuery fornece contagens exatas
- Consent Mode: quando o usuário nega `analytics_storage`, o GA4 ainda registra eventos como "cookieless pings" sem `user_pseudo_id`, inflando contagem de eventos mas sem atribuição

### 8.6 Sampling não existe no BigQuery
Diferente da interface do GA4 (que aplica sampling em propriedades gratuitas), o BigQuery sempre retorna dados completos e exatos.

### 8.7 Evento vs. sessão vs. usuário
O GA4 é orientado a eventos. Para cada análise, deixe claro qual é a granularidade:
- Contar linhas = contar eventos
- Contar usuários = `COUNT(DISTINCT user_pseudo_id)`
- Contar sessões = `COUNT(DISTINCT CONCAT(user_pseudo_id, session_id))`

### 8.8 Cuidado com o `event_date` vs `_TABLE_SUFFIX`
O campo `event_date` (STRING no formato YYYYMMDD) é a data do evento. O `_TABLE_SUFFIX` é a data da tabela. Em geral são iguais, mas podem diferir para eventos que chegaram com atraso.

---

## 9. Relatórios comuns

### Top páginas por pageviews

```sql
SELECT
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'page_location') AS pagina,
  COUNT(*) AS pageviews,
  COUNT(DISTINCT user_pseudo_id) AS usuarios_unicos
FROM `seu_projeto.analytics_XXXXXXX.events_*`
WHERE _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
  AND event_name = 'page_view'
GROUP BY 1
ORDER BY pageviews DESC
LIMIT 20
```

### Performance por canal (source/medium da sessão)

```sql
SELECT
  collected_traffic_source.manual_source AS source,
  collected_traffic_source.manual_medium AS medium,
  COUNT(DISTINCT user_pseudo_id) AS usuarios,
  COUNT(DISTINCT CONCAT(
    user_pseudo_id,
    CAST((SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'ga_session_id') AS STRING)
  )) AS sessoes
FROM `seu_projeto.analytics_XXXXXXX.events_*`
WHERE _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
  AND event_name = 'session_start'
GROUP BY 1, 2
ORDER BY sessoes DESC
```

### Funil de e-commerce

```sql
SELECT
  event_name,
  COUNT(DISTINCT CONCAT(
    user_pseudo_id,
    CAST((SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'ga_session_id') AS STRING)
  )) AS sessoes
FROM `seu_projeto.analytics_XXXXXXX.events_*`
WHERE _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
  AND event_name IN ('view_item', 'add_to_cart', 'begin_checkout', 'purchase')
GROUP BY 1
ORDER BY sessoes DESC
```

---

## 10. Links úteis

- [Schema oficial do export de eventos GA4](https://support.google.com/analytics/answer/7029846)
- [Schema do export de usuários GA4](https://support.google.com/analytics/answer/12769371)
- [Schemas para developers (Firebase)](https://developers.google.com/analytics/bigquery/schemas)
- [Dataset público de amostra GA4 (Google Merchandise Store)](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=ga4_obfuscated_sample_ecommerce&t=events_20210131&page=table)
