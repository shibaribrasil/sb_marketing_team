---
name: hab-google-ads
description: Use esta skill quando o Gui (agente-trafego) for criar, revisar, otimizar ou analisar anúncios e campanhas no Google Ads para a Shibari Brasil. Cobre estrutura de conta, tipos de campanha (Search, Display, Performance Max, Video, Demand Gen, Shopping), palavras-chave, anúncios responsivos, lances inteligentes, rastreamento e first-party data, brand safety no YouTube, métricas e boas práticas de otimização.
---

# Manual de Google Ads — Shibari Brasil

> Habilidade do Gui para criar, gerenciar e analisar campanhas pagas no Google Ads. Combina a documentação oficial do Google com boas práticas do mercado e diretrizes específicas para o nicho da Shibari Brasil.

---

## Capítulo 1 — Visão Geral e Contexto

### 1.1 Como o Google Ads funciona

O Google Ads é uma plataforma de publicidade baseada em **leilão**. Para cada busca ou impressão, o Google decide quais anúncios exibir e em que posição com base em dois fatores combinados:

- **Lance**: quanto o anunciante está disposto a pagar
- **Ad Rank**: pontuação calculada a partir do lance × Quality Score × extensões e contexto do usuário

**Quality Score** (1–10) mede a qualidade relativa do anúncio em três dimensões:
- Relevância do anúncio (correspondência com a intenção de busca)
- Taxa de cliques esperada (CTR histórico)
- Experiência da landing page (velocidade, relevância, usabilidade)

> Quality Score alto = pagar menos por posições melhores. Otimizar a landing page e o copy é tão importante quanto o lance.

### 1.2 Onde os anúncios aparecem

| Canal | Onde aparece | Tipo de campanha |
|-------|-------------|-----------------|
| **Rede de Pesquisa** | Resultados do Google Search | Search |
| **Rede de Display** | Sites parceiros, Gmail, YouTube | Display |
| **YouTube** | Vídeos (in-stream, bumpers, discovery) | Video |
| **Google Shopping** | Resultados de produtos no Google | Shopping |
| **YouTube + Discover + Gmail** | Superfícies visuais do Google | Demand Gen |
| **Todos os canais** | Combinado com IA | Performance Max |

### 1.3 A Shibari Brasil no Google Ads

A SB opera em nicho especializado. No Google, o usuário **busca ativamente** — diferente do Meta, onde o anúncio interrompe o scroll. Isso significa intenção de compra mais alta, especialmente em Search.

**Vantagem estratégica:** Quem busca "corda de juta" ou "corda para shibari" já sabe o que quer. Capturar esse tráfego é converter intenção em venda.

**Contexto de políticas:** O Google Ads tem políticas distintas do Meta para conteúdo adulto. Produtos como cordas e acessórios para amarração são geralmente aceitos sem restrições específicas — o vocabulário técnico (shibari, bondage) não é bloqueado automaticamente como no Meta. A restrição do Google foca em conteúdo sexualmente explícito, nudez e produtos proibidos por lei.

---

## Capítulo 2 — Estrutura da Conta

### 2.1 Os Três Níveis

```
CONTA
  └── Define o faturamento, acesso e configurações gerais

    CAMPANHA
      └── Define o OBJETIVO, ORÇAMENTO e CANAL

        GRUPO DE ANÚNCIOS (Ad Group)
          └── Define as PALAVRAS-CHAVE e os ANÚNCIOS

            ANÚNCIOS
              └── Títulos, descrições e extensões
```

### 2.2 Os ABCs da Estrutura — Princípio Oficial do Google

O Google recomenda estruturas simplificadas para que a IA possa otimizar melhor. O framework oficial é o **ABC**:

**A — Align (Alinhar)**
Consolidar grupos de anúncios temáticos em vez de grupos por palavra-chave única (SKAGs). Grupos amplos por tema permitem que o Smart Bidding otimize com mais dados.

❌ Errado: um grupo só para "corda de juta" + outro só para "corda de juta 6mm" + outro só para "comprar corda de juta"
✅ Correto: um grupo "Cordas de Juta" com todas as variações relevantes

**B — Bring Together (Reunir)**
Combinar todos os tipos de correspondência no mesmo grupo de anúncios, priorizando **correspondência ampla**. A IA usa todos os sinais disponíveis para encontrar buscas relevantes que a correspondência exata não capturaria.

**C — Consolidate (Consolidar)**
- Remover palavras-chave duplicadas entre grupos
- Remover palavras-chave pausadas ou inativas
- Não segmentar por dispositivo — a IA já ajusta lances por dispositivo automaticamente

### 2.3 Boas Práticas de Nomenclatura

Usar nomenclatura clara e padronizada:

```
Campanha: [Tipo] — [Tema ou Produto]
Exemplos:
  Search — Cordas Juta
  Search — Acessórios Shibari
  Display — Remarketing — Visitantes
  PMax — Produtos Gerais
```

```
Grupo de Anúncios: [Tema específico]
Exemplos:
  Corda Juta Natural
  Corda Colorida
  Corda Iniciante
```

---

## Capítulo 3 — Tipos de Campanha

### 3.1 Search (Rede de Pesquisa)

**Quando usar:** Capturar intenção ativa — usuário já está buscando.

**Indicado para SB:** Principal canal de conversão. Buscar por "corda para shibari", "corda de juta para amarração" ou "acessórios bondage" indica intenção de compra clara.

**Configurações essenciais:**
- Ativar **Rede de Pesquisa** apenas (desativar Rede de Display na campanha de Search)
- Definir localização: Brasil
- Configurar correspondência de palavras-chave (ver Capítulo 4)
- Adicionar palavras-chave negativas desde o início
- Criar mínimo 2 RSAs (Responsive Search Ads) por grupo

### 3.2 Display (Rede de Display)

**Quando usar:** Alcance e reconhecimento de marca; remarketing para visitantes do site.

**Indicado para SB:** Principalmente para **remarketing** — impactar visitantes que não converteram e clientes anteriores com novidades.

**Configurações essenciais:**
- Usar **Responsive Display Ads** (RDA) — múltiplas imagens, logos e títulos
- Ativar **Optimized Targeting** para descobrir novos públicos com perfil semelhante aos que convertem
- Implementar **Smart Bidding** (tCPA ou Maximizar Conversões)
- Validar rastreamento de conversões antes de ativar

### 3.3 Performance Max (PMax)

**Quando usar:** Quando há histórico de conversões suficiente e objetivo de maximizar vendas em todos os canais.

**O que é:** Campanha que combina Search, Display, YouTube, Discover, Gmail e Maps — gerenciada inteiramente pela IA do Google com base nos ativos (criativos, copy, URLs) fornecidos.

**Cuidados:**
- Requer volume mínimo de conversões para funcionar bem (recomendado: 30+ conversões/mês antes de ativar)
- Fornecer o máximo de ativos: até 15 imagens, 5 logos, 5 vídeos, 15 títulos, 5 descrições
- Configurar **sinais de audiência** (quem provavelmente converte) — a IA usa como ponto de partida, não como restrição
- Monitorar relatório de insights para entender o que a PMax está fazendo

### 3.4 Video (YouTube)

**Quando usar:** Brand awareness, conteúdo educativo, remarketing por vídeo.

**Dois objetivos distintos no YouTube:**

| Objetivo | Foco | Estratégia de lance |
|----------|------|-------------------|
| **Awareness (Conscientização)** | Alcançar o maior número de pessoas, alto impacto | CPM (custo por mil impressões) |
| **Consideration (Consideração)** | Criar interesse e engajamento com a marca | CPV (custo por visualização) |

**Formatos principais:**
- **In-stream pulável**: aparece antes/durante vídeos, pode ser pulado em 5s — use para awareness e consideration
- **In-stream não pulável**: até 15s, obrigatório assistir — ideal para mensagens curtas de awareness
- **Bumper**: até 6s, não pulável — reforço de marca, complementa campanhas maiores
- **In-feed**: aparece nos resultados de busca do YouTube — gera visualizações qualificadas

**Melhores práticas Video:**
- Misturar formatos (In-Stream + In-Feed + Shorts) aumenta alcance em média **35%** vs. formato único
- **Frequência recomendada:** 3× por semana como base; multiplicar por 2 em períodos sazonais de pico
- Usar **vertical, quadrado e horizontal** em orientações diferentes para cobrir todos os posicionamentos
- Medir resultados com **Brand Lift Studies** (impacto em consciência de marca) e **Search Lift** (impacto em buscas)

**Brand Safety/Suitability no YouTube:**
O Google garante 99% de eficácia de brand safety em todos os formatos YouTube (in-stream, live, Shorts). Controles disponíveis:
- **Inventory types**: Standard Inventory é o recomendado para a maioria das marcas
- **Content types**: excluir live streams ou vídeos incorporados se necessário
- **Excluded themes**: bloquear tópicos específicos nos vídeos onde os anúncios aparecem
- **Negative keywords** a nível de conta: termos incompatíveis com a marca
- **Placement exclusions**: excluir canais ou vídeos específicos

> Atenção: campanhas com controles excessivos registram CPMs até **40% maiores**. Não exagerar nas exclusões — a maioria das campanhas exclui 10 tópicos ou menos.

### 3.5 Demand Gen

**O que é:** Campanha que combina YouTube (incluindo Shorts), Google Discover e Gmail em uma experiência visual e nativa. Diferente do Video puro, a Demand Gen inclui imagens e é orientada a geração de demanda e conversão — não só awareness.

**Quando usar para SB:**
- Criar desejo pelo produto em públicos que ainda não estão buscando ativamente
- Remarketing visual com produtos em múltiplas superfícies
- Complementar Search (que captura demanda) criando demanda nova

**Os Quatro Pilares da Demand Gen (framework oficial do Google):**

**1. Data Strength (Força de Dados)**
Implementar medição precisa: Google Tag + GA4 + dados offline quando disponível. Quanto mais dados, melhor a IA otimiza.

**2. Conversion Volume (Volume de Conversões)**
Fornecer volume suficiente ao algoritmo. Orçamentos mínimos recomendados:
- Estratégias Maximize: $100+/dia (≈ R$ 550+)
- Estratégias com target (tCPA): 10× o CPA alvo por dia

**3. AI Targeting (Segmentação por IA)**
- Ativar **Optimized Targeting** com listas de dados próprios
- Incluir remarketing de clientes existentes
- Usar objetivo "new customer acquisition" para aquisição de novos usuários

**4. Creative Variety (Diversidade Criativa)**
- Incluir pelo menos **3 imagens verticais + 3 quadradas + 3 horizontais** por campanha
- Incluir pelo menos **3 vídeos** em orientações diferentes
- Combinar vídeos e imagens gera **+6% mais conversões por real investido** vs. imagens apenas

**Especificações de ativos Demand Gen:**
- Títulos: até 5 (40 caracteres)
- Descrições: até 5 (90 caracteres)
- Imagens: até 20 (landscape 1,91:1 + square 1:1 + portrait 4:5)
- Vídeos: até 5 (horizontal + vertical + quadrado)
- Logo: até 5

**Resultado comprovado:** Anunciantes que adotaram 3+ dos 4 pilares alcançaram **+40% mais conversões** e **+30% mais valor de conversão**.

### 3.6 Shopping

**O que é:** Anúncios de produto com imagem, título, preço e nome da loja exibidos diretamente nos resultados de busca do Google.

**Quando considerar para SB:** Pode ser ativado se a loja tiver feed de produtos configurado no Google Merchant Center. Benefício: anúncio com foto e preço diretamente na busca — alta intenção de compra.

**Requisitos:**
- Conta no Google Merchant Center com feed de produtos atualizado
- Dados precisos: título do produto, preço, disponibilidade, imagem de alta qualidade
- Foto do produto com 75–90% da imagem ocupada pelo produto

> Para SB hoje: avaliar Shopping como expansão futura. Prioridade inicial: Search + Display + PMax.

---

## Capítulo 4 — Palavras-chave e Segmentação

### 4.1 Tipos de Correspondência

| Tipo | Notação | Como funciona | Quando usar |
|------|---------|--------------|-------------|
| **Ampla** | `corda juta` | Ativa para buscas relacionadas, sinônimos e variações | Principal — deixar IA trabalhar |
| **Frase** | `"corda de juta"` | Ativa quando a frase aparece na busca (em qualquer ordem com termos adicionais) | Controle médio |
| **Exata** | `[corda de juta]` | Ativa apenas para essa busca específica (com variações próximas) | Termos críticos com alto CPC |

**Recomendação Google/SB:** Priorizar **correspondência ampla + Smart Bidding**. A IA usa os sinais da conta para encontrar buscas relevantes. Correspondência exata deve ser reservada para termos com intenção muito específica e histórico de conversão.

### 4.2 Palavras-chave Negativas

Negativas evitam exibir anúncios para buscas irrelevantes, economizando orçamento.

**Lista de negativas obrigatória para SB (início de campanha):**

```
grátis
gratuito
download
curso
tutorial
como fazer
DIY
receita
-[nome de concorrente específico se não quiser aparecer na busca deles]
```

**Processo de expansão de negativas:**
1. Acessar **Relatório de Termos de Pesquisa** semanalmente
2. Identificar termos que geraram cliques sem conversão
3. Adicionar à lista de negativas (nível de grupo ou campanha, conforme o caso)

### 4.3 Palavras-chave Sugeridas para SB

**Termos de alta intenção (Search principal):**
```
corda para shibari
corda de juta shibari
corda bondage
corda juta natural
corda para amarração
comprar corda shibari
corda juta artesanal
acessórios shibari
kit shibari
corda juta colorida
```

**Termos de marca:**
```
shibari brasil
shibari brasil loja
```

**Termos educativos (menor intenção, usar com cuidado):**
```
shibari o que é
como praticar shibari
iniciar no shibari
```

### 4.4 Segmentação em Display e PMax

**Para Display e PMax, usar sinais de audiência:**

| Tipo | O que inclui |
|------|-------------|
| **In-Market** | Pessoas pesquisando produtos similares ativamente |
| **Affinity** | Interesses declarados e comportamentos habituais |
| **Remarketing** | Visitantes do site, clientes, quem abandonou carrinho |
| **Similar Audiences** | Perfis semelhantes aos da lista de remarketing |
| **Customer Match** | Upload de lista de e-mails de clientes |

**Sinal de audiência recomendado para PMax da SB:**
- Visitantes do site (últimos 30 dias)
- Clientes que compraram (Customer Match)
- In-Market: "Roupas e Acessórios", "Produtos artesanais"

---

## Capítulo 5 — Anúncios (RSA e RDA)

### 5.1 Anúncios Responsivos de Pesquisa (RSA)

O RSA é o formato padrão da Rede de Pesquisa. O Google testa automaticamente combinações de títulos e descrições para encontrar as que convertem mais.

**Especificações:**

| Elemento | Limite por campo | Quantidade |
|----------|-----------------|-----------|
| Títulos | 30 caracteres | Até 15 (mínimo: 3) |
| Descrições | 90 caracteres | Até 4 (mínimo: 2) |

**Meta de Ad Strength:** Manter no mínimo "Bom" — de "Pobre" para "Excelente" gera em média 15% mais cliques e conversões.

**Regras para títulos RSA:**
- Incluir palavras-chave principal no Título 1 ou 2
- Variar abordagens: benefício, urgência, especificação do produto, prova social
- Fixar (pin) apenas se um título for obrigatório em toda exibição — pinagem limita os testes
- Evitar repetições de palavras entre títulos

**Exemplo de estrutura RSA para SB:**

```
Títulos (variar abordagens):
1. Corda de Juta para Shibari
2. Corda Artesanal Premium
3. Feita à Mão — Qualidade Garantida
4. Envio para Todo o Brasil
5. Cordas Shibari | Loja Especializada
6. Material Selecionado e Tratado
7. Compre Sua Corda de Juta
8. Para Iniciantes e Experientes
9. Shibari Brasil — Loja Oficial
10. Peça Artesanal com Acabamento Impecável

Descrições (máximo de detalhes por 90 chars):
1. Cordas de juta 100% natural, tratadas artesanalmente. Escolha o tamanho e a cor ideal para sua prática.
2. Frete para todo o Brasil. Embalagem discreta. Qualidade premium para praticantes exigentes.
3. Cada corda é produzida à mão com materiais selecionados. Durabilidade e textura ideais para amarração.
4. Loja especializada em shibari. Atendimento por WhatsApp. Compra segura e entrega rápida.
```

### 5.2 Anúncios Responsivos de Display (RDA)

**Especificações:**

| Elemento | Limite | Quantidade |
|----------|--------|-----------|
| Títulos curtos | 30 caracteres | Até 5 |
| Títulos longos | 90 caracteres | Até 5 |
| Descrições | 90 caracteres | Até 5 |
| Imagens (paisagem 1,91:1) | 1200×628px | Até 15 |
| Imagens (quadrado 1:1) | 1200×1200px | Até 15 |
| Logos | 1200×1200px | Até 5 |

**Dimensões obrigatórias de imagem (padrão Google Ads):**
| Proporção | Dimensão | Uso |
|-----------|---------|-----|
| 16:9 (paisagem) | 1200×628px | Display, PMax, Demand Gen, Search com imagem |
| 1:1 (quadrado) | 1200×1200px | Display, PMax, Demand Gen, Shopping |
| 4:5 (retrato) | 960×1200px | Demand Gen mobile, YouTube Shorts |

**Boas práticas RDA:**
- Fornecer o máximo de imagens possível — mais variedade = mais testes
- Garantir que cada imagem funciona sozinha (sem texto sobreposto obrigatório)
- Logo com fundo branco ou transparente
- Imagens de alta resolução sem texto excessivo na arte
- **Dynamic Image Resources:** Ativar a funcionalidade que usa machine learning para selecionar automaticamente imagens relevantes das landing pages — reduz o trabalho manual de upload e mantém criativos atualizados com o catálogo

### 5.3 Extensões de Anúncio (Assets)

Extensões são adicionais gratuitos que ampliam o anúncio e aumentam o CTR. Sempre configurar:

| Extensão | O que adiciona | Prioridade para SB |
|----------|---------------|-------------------|
| **Sitelinks** | Links extras para páginas específicas | ✅ Obrigatória |
| **Callouts** | Frases de destaque (frete grátis, embalagem discreta) | ✅ Obrigatória |
| **Snippets estruturados** | Lista de produtos ou categorias | ✅ Recomendada |
| **Chamada** | Número de telefone/WhatsApp | ✅ Recomendada |
| **Preço** | Mostra preços de produtos diretamente | Testar |
| **Promoção** | Destaca descontos e ofertas | Usar em campanhas sazonais |

**Sitelinks sugeridos para SB:**
- Cordas de Juta → link da categoria
- Acessórios → link da categoria
- Sobre a Loja → página institucional
- WhatsApp → link do WhatsApp Business

---

## Capítulo 6 — Lances e Estratégias de Orçamento

### 6.1 Estratégias de Lance

| Estratégia | Como funciona | Quando usar |
|------------|--------------|-------------|
| **Maximizar Cliques** | Google gasta o orçamento buscando mais cliques | Início de campanha sem dados de conversão |
| **Maximizar Conversões** | IA otimiza para o máximo de conversões | Quando há histórico de conversões |
| **CPA Alvo (tCPA)** | Google tenta manter custo por conversão próximo do alvo | Quando há CPA definido e histórico mínimo |
| **ROAS Alvo (tROAS)** | Google otimiza para o retorno sobre gasto definido | E-commerce com dados sólidos de valor de conversão |
| **Maximizar Valor de Conversão** | Google foca em conversões de maior valor | Quando produtos têm preços variados |
| **CPC Manual** | Controle manual do lance por palavra-chave | Raramente — perda de eficiência de IA |

**Recomendação para SB:**
- **Início de campanha:** Maximizar Conversões (deixar a IA aprender)
- **Com histórico (30+ conversões/mês):** tCPA ou tROAS
- **PMax:** Maximizar Valor de Conversão ou tROAS

**Framework de 4 etapas para Smart Bidding (oficial Google):**

1. **Configuração:** Criar campanhas com objetivo único e dados de conversão precisos. Sem rastreamento confiável, o Smart Bidding otimiza com base incorreta.
2. **Escolha da estratégia:** Selecionar baseado na meta comercial principal — volume de conversões (Maximizar Conversões/tCPA) ou valor (Maximizar Valor/tROAS).
3. **Testes:** Usar **Experimentos do Google Ads** para validar a estratégia antes de aplicar em toda a conta.
4. **Avaliação:** Consultar **Relatório de Estratégia de Lances** para entender como o algoritmo está tomando decisões.

> Smart Bidding funciona melhor pareado com **correspondência ampla + RSAs**. Os três trabalham juntos: ampla captura variações de busca → Smart Bidding otimiza o lance → RSA testa o melhor anúncio.

### 6.2 AI Max para Search

**AI Max** é o conjunto de recursos de IA para campanhas de Search que oferece:
- **Correspondência de termos de busca expandida**: o Google usa IA para encontrar variações relevantes além das palavras-chave cadastradas
- **Personalização de texto**: adapta titles e descrições conforme a busca
- **Expansão de URL final**: direciona para a landing page mais relevante da campanha

Resultado: aproximadamente **+14% de conversões ou valor de conversão** com CPA/ROAS similar.

> Ativar AI Max com um clique nas configurações da campanha Search. Usar controles de marca e localização para manter precisão.

### 6.3 Orçamento

**Orçamento diário:** valor médio que o Google pode gastar por dia. O Google pode gastar até 2× o orçamento diário em dias de alta demanda, compensando com dias abaixo.

**Referências de CPC no Brasil (e-commerce geral):**
| Nível de competição | CPC médio |
|--------------------|----------|
| Baixa concorrência | R$ 0,80–R$ 2,00 |
| Média concorrência | R$ 2,00–R$ 8,00 |
| Alta concorrência | R$ 8,00–R$ 25,00 |

> Para o nicho da SB (cordas, acessórios shibari), a concorrência é baixa a média — CPC estimado entre R$ 1,00 e R$ 5,00 em Search.

**Investimento mínimo recomendado:**
- Abaixo de R$ 2.000–3.000/mês: dados insuficientes para o Smart Bidding aprender bem
- Período de otimização: **60–90 dias** para resultados completos e confiáveis

**Como dimensionar orçamento:**
1. Definir o CPA alvo (quanto custa uma venda)
2. Estimar conversões desejadas por mês
3. Calcular orçamento: `CPA alvo × conversões desejadas por mês ÷ 30`

**Exemplo:** CPA alvo R$ 80 × 20 vendas/mês = R$ 1.600/mês = ~R$ 53/dia

**Distribuição de orçamento recomendada (quando usar múltiplos tipos):**
| Tipo de campanha | % do orçamento |
|-----------------|---------------|
| Performance Max | ~40% |
| Search | ~35% |
| Display / Demand Gen / outros | ~25% |

> Esta distribuição é uma referência inicial. Ajustar com base nos dados de performance — se Search estiver com ROAS superior, aumentar proporcionalmente.

**Regra de escalada:**
- Aumentar orçamento gradualmente: máximo **20% por vez**
- Aguardar ao menos **7 dias** após cada aumento antes do próximo
- Mudanças bruscas afetam o aprendizado do Smart Bidding

### 6.4 Fase de Aprendizado

Ao criar uma campanha ou fazer mudanças significativas, o Google entra em **fase de aprendizado** — período em que o Smart Bidding coleta dados. Durante esse período:

- Performance pode ser instável
- **Não fazer alterações** desnecessárias (podem reiniciar a fase)
- Fase dura até 7 dias e/ou 50 conversões

**O que reinicia a fase de aprendizado:**
- Mudança de estratégia de lance
- Mudança de orçamento (acima de 20%)
- Mudança de segmentação ou palavras-chave
- Pausa e reativação de campanha

---

## Capítulo 7 — Rastreamento e Conversões

### 7.1 O Que Configurar

Antes de qualquer campanha, garantir que o rastreamento está funcional:

**Eventos prioritários para SB:**
| Evento | O que rastreia | Tipo |
|--------|---------------|------|
| **Purchase** | Compra concluída | Conversão primária |
| **Add to Cart** | Produto adicionado ao carrinho | Micro-conversão |
| **Begin Checkout** | Início do checkout | Micro-conversão |
| **Page View** | Visita a qualquer página | Audiência |
| **View Item** | Visita à página de produto | Audiência |

### 7.2 Google Tag e Google Analytics 4 (GA4)

**Fluxo recomendado:**
```
Google Tag (instalada no site)
  → Envia dados para GA4
  → GA4 importa eventos como conversões no Google Ads
```

**Alternativa direta:**
```
Google Tag → Tag de conversão direta no Google Ads
```

Preferir a integração via GA4 — oferece mais dados e análise de funil completo.

### 7.3 Server-Side Tracking

Rastreamento convencional (client-side) perde dados por:
- Bloqueadores de anúncios
- iOS/Safari (restrições de cookies)
- Lentidão de carregamento de scripts

**Server-Side Tracking** (via Google Tag Manager Server ou Stape Gateway) captura eventos diretamente do servidor, contornando essas limitações. Resultado: dados mais precisos, melhor otimização do Smart Bidding.

> Recomendado para qualquer loja com volume relevante de vendas. Discutir com o time técnico da SB a viabilidade de implementação.

### 7.4 Segmentação de Audiences via GA4

No GA4, criar segmentos de usuários por comportamento para uso como públicos no Google Ads:

- Visitantes que chegaram a "Adicionar ao Carrinho" mas não compraram → remarketing com oferta
- Clientes que compraram → excluir de campanhas de aquisição / incluir em campanhas de recompra
- Visitantes de categorias específicas → retargeting por interesse de produto

### 7.5 Data Strength — First-Party Data

**Por que importa:** First-party data (dados próprios da SB) alimenta a IA do Google para melhorar significativamente o ROAS. Quanto mais dados confiáveis, melhor o Smart Bidding otimiza.

**Quatro ações de Data Strength:**

**1. Conectar fontes de dados**
- Google Tag instalada no site → rastrear todas as interações
- GA4 vinculado ao Google Ads
- Dados offline (lista de clientes) → importar via **Customer Match**

**2. Maximizar sinais**
- **Customer Match:** fazer upload da lista de e-mails de clientes para criar audiências e lookalikes no Google Ads
- **Enhanced Conversions:** envia dados hasheados de conversão (e-mail, telefone, endereço) para melhorar a precisão do rastreamento mesmo com bloqueadores
- Incluir valor de conversão em todos os eventos de compra (não só contar a conversão — enviar o valor em R$)

**3. Consent Mode**
Configurar o **Consent Mode** do Google para respeitar preferências de privacidade dos usuários e manter rastreamento modelado quando o consentimento não é dado. Necessário para Enhanced Conversions funcionar corretamente.

**4. Ativar IA com os dados**
Com dados robustos, ativar:
- Smart Bidding (Maximize Conversion Value ou tROAS)
- Lookalike segments a partir das listas de Customer Match
- Performance Max com sinais de audiência baseados em clientes reais

**Enhanced Conversions for Leads:** Se SB coletar leads (ex: cadastros para lista de e-mail), usar essa funcionalidade para integrar com CRM e importar dados de qualidade de lead, ajustando o algoritmo para otimizar por leads que efetivamente compram.

### 7.6 Customer Match — Detalhamento

**Tipos de dados aceitos:**
- Endereços de e-mail
- Números de telefone
- Endereços físicos (nome + CEP + cidade + estado)
- Identificadores de dispositivos móveis

> Incluir múltiplos tipos de dado na mesma linha (e-mail + telefone do mesmo cliente) aumenta a taxa de correspondência.

**Taxa de correspondência típica:** 29–62%. Ou seja, de cada 100 e-mails enviados, o Google encontra entre 29 e 62 contas Google ativas. Para SB, o tamanho mínimo da lista é **100 usuários correspondidos** para ativar qualquer audiência.

**Frequência de atualização da lista:**
| Método | Frequência mínima |
|--------|------------------|
| Upload manual | Semanal |
| API do Google Ads | Diária |
| Parceiros certificados | Frequente |
| Solução automatizada | Tempo real (ideal) |

**Como usar Customer Match na prática para SB:**
1. Exportar lista de clientes do sistema da loja (e-mail + telefone quando disponível)
2. Formatar conforme template do Google Ads
3. Fazer upload em Ferramentas → Audiências → Customer Match
4. Usar a lista como:
   - Sinal de audiência na PMax (quem são os compradores)
   - RLSA em Search (aumentar lance para clientes que retornam)
   - Exclusão em campanhas de aquisição (não impactar quem já comprou com mensagem de primeiro contato)
   - Base para geração de **lookalike segments** (Similar Audiences)

### 7.7 GA4 + Audiências Preditivas

A integração GA4 → Google Ads habilita **audiências preditivas** — públicos gerados por IA com base em comportamento de navegação, sem necessidade de dados históricos de compra extensos.

**Como configurar:**
1. Vincular propriedade GA4 ao Google Ads (Administrador → Vinculações de produtos)
2. Ativar **auto-tagging** na conta do Google Ads
3. No GA4, marcar o evento `purchase` como evento-chave
4. Publicar audiências preditivas para uso no Google Ads

**Audiências preditivas disponíveis:**
- **Compradores prováveis** — usuários com alta probabilidade de comprar nos próximos 7 dias
- **Churners prováveis** — clientes que provavelmente vão parar de comprar
- **Alto valor de receita** — usuários com maior potencial de gasto

**Resultado de referência:** Varejista BAUR aumentou vendas em 56% usando audiências de compradores prováveis — 70% dos clientes alcançados eram acessíveis apenas por essas audiências preditivas.

**Para SB:** Usar "Compradores prováveis" como sinal de audiência na PMax e em Display para remarketing de alta precisão.

---

## Capítulo 8 — Performance Max (PMax)

### 8.1 Como a PMax Funciona

A Performance Max usa IA para encontrar os melhores momentos, canais e públicos para exibir os anúncios. Opera em todos os canais do Google com base nos **ativos** fornecidos.

**Resultado comprovado:** Anunciantes que adotam PMax veem em média **+27% mais conversões ou valor de conversão** vs. campanhas tradicionais.

**O que a PMax precisa:**
- Títulos (até 15), descrições (até 5)
- Imagens (até 15 de diferentes formatos — vertical, quadrada, landscape)
- Logos (até 5)
- Vídeos (até 5 — se não fornecidos, o Google cria automaticamente com qualidade baixa; **fornecer sempre**)
- Sinais de audiência (quem tem perfil de comprador)
- URL final e configuração de expansão de URL

**Impacto dos vídeos na PMax:**
- Incluir vídeos gera **+12% de conversões adicionais**
- Incluir vídeos em orientações diferentes (vertical + horizontal + quadrado) gera **+20% mais conversões no YouTube**

### 8.2 Boas Práticas PMax

- **Fornecer vídeos próprios** — evitar geração automática do Google a todo custo
- **Múltiplos grupos de ativos** por tema (ex: um grupo "Cordas de Juta", outro "Acessórios") — cada grupo tem criatividade e copy específicos
- **Sinais de audiência precisos** — usar listas de Customer Match e visitantes do site como ponto de partida
- **Monitorar relatório de Insights** diariamente para entender o que a campanha está fazendo
- **Aguardar 4–6 semanas** antes de avaliar performance — a PMax precisa de tempo para aprender
- **Usar Search Themes** — lista de termos-chave que orientam a IA sobre quais buscas são relevantes (ver 8.4)
- **Ativar Expansão de URL Final** — permite ao Google redirecionar para a página mais relevante (ver 8.5)

### 8.3 PMax × Search

**Usar PMax e Search juntas é possível.** A Search capta buscas específicas; a PMax expande para mais canais. O Google prioriza a campanha mais específica (Search) quando há sobreposição de intenção.

### 8.4 New Customer Value Mode

Configuração que orienta a PMax a **priorizar aquisição de novos clientes**, atribuindo valor maior às conversões vindas de usuários que nunca compraram antes.

**Como funciona:**
- Modo "New Customer Acquisition": a IA favorece impressões para pessoas fora da lista de clientes existentes
- Ideal quando o objetivo é crescer a base de clientes, não apenas vender para quem já comprou

**Para SB:** Ativar quando a SB quiser escalar aquisição de novos clientes — definir as listas de clientes existentes via Customer Match para a IA saber quem excluir/deprioritizar.

### 8.5 Search Themes

**O que são:** Lista de termos relacionados ao negócio que orientam a IA da PMax sobre quais intenções de busca são relevantes — funciona como "dica" para a IA sem restringir sua atuação.

**Quando usar:** Especialmente no início, quando a campanha ainda não tem histórico. Os Search Themes ajudam a IA a não desperdiçar o período de aprendizado em buscas irrelevantes.

**Exemplos para SB:**
```
corda de juta
corda para shibari
acessórios bondage
kit shibari iniciante
corda natural artesanal
```

### 8.6 Expansão de URL Final

Deixar habilitada — permite ao Google direcionar o usuário para a página de produto mais relevante dentro do site, não apenas para a URL definida na campanha.

**O que excluir da expansão** (páginas que não devem receber tráfego de anúncios):
- Página de carreiras
- FAQ ou páginas de suporte
- Páginas de login/minha conta

---

## Capítulo 9 — Campanhas de Display

### 9.1 Quando Usar Display para SB

- **Remarketing:** principal uso — impactar quem visitou o site e não comprou
- **Brand awareness:** alcançar novos públicos com perfil semelhante ao dos clientes
- **Lançamento de produto:** criar exposição ampla antes de uma campanha de Search focada

### 9.2 Optimized Targeting

Ferramenta de IA do Google que expande o público além do segmento definido manualmente, buscando perfis com maior probabilidade de conversão. Ativar por padrão em campanhas de Display orientadas a conversão.

### 9.3 RLSAs (Remarketing Lists for Search Ads)

Aplicar listas de remarketing em campanhas de **Search** para personalizar lances e mensagens:

| Lista | Ação |
|-------|------|
| Visitantes de produto sem compra | Aumentar lance em 30–50% |
| Clientes que já compraram | Diminuir lance (já converteram) ou usar para cross-sell |
| Visitantes do carrinho sem compra | Aumentar lance + usar copy com urgência |

---

## Capítulo 10 — Métricas e Análise de Performance

### 10.1 KPIs Principais

| Métrica | O que mede | Referência |
|---------|-----------|-----------|
| **CTR** | % de cliques/impressões | Search: ~6,66% (benchmark geral); > 2% aceitável; Display: > 0,5% |
| **CPC** | Custo médio por clique | E-commerce BR: R$ 0,80–R$ 5,00 (nicho SB: R$ 1–5) |
| **CPA** | Custo por aquisição (compra) | Definir meta por produto |
| **ROAS** | Receita ÷ gasto em anúncios | Meta mínima: 2×; objetivo: 3–5× |
| **ROI** | (Receita – Custo) ÷ Custo | Principal métrica de saúde geral da conta |
| **Impression Share** | % das impressões capturadas | 90%+ em low competition; 60%+ em alta |
| **Quality Score** | Qualidade do anúncio (1–10) | Almejar 7+ nas principais palavras |
| **Conv. Rate** | % dos cliques que convertem | Depende do produto e landing page |

### 10.2 Sinais de Alerta e Ações

| Sinal | Causa provável | Ação |
|-------|---------------|------|
| CTR baixo | Anúncio pouco relevante ou Ad Rank baixo | Melhorar copy, aumentar Ad Strength |
| CPA alto | Landing page fraca ou público errado | Revisar landing page + segmentação |
| Quality Score baixo | Anúncio, keyword e LP desalinhados | Alinhar mensagem entre os três |
| Impression Share baixo | Orçamento insuficiente ou lance baixo | Aumentar orçamento ou lance |
| Conversões caindo | Sazonalidade ou competitor | Analisar histórico + monitorar leilão |
| Gasto sem conversão | Palavras-chave amplas gerando tráfego irrelevante | Revisar Search Terms Report + adicionar negativas |

### 10.2a Processo de Análise em 5 Passos (Google)

1. **Rastreamento de conversões:** Verificar se os eventos estão disparando corretamente. Sem dados confiáveis, toda análise fica comprometida.
2. **Medição de ROI:** `ROI = (Receita gerada – Custo dos anúncios) ÷ Custo dos anúncios`. É a métrica principal que o Google recomenda monitorar de forma consistente.
3. **Análise de Termos de Pesquisa:** Comparar as buscas reais que ativaram os anúncios vs. as palavras-chave cadastradas — identificar oportunidades de expansão e termos a negativar.
4. **Revisão de Quality Score:** Identificar palavras com pontuação baixa e alinhar copy do anúncio + landing page com a intenção de busca delas.
5. **Relatórios integrados GA4 + Google Ads:** Ver o comportamento pós-clique — o usuário chegou na página, mas o que fez depois? Taxa de rejeição, tempo na página, funil de conversão.

### 10.3 Frequência de Análise

| Frequência | O que verificar |
|-----------|----------------|
| **Diária** | Gasto, conversões, CPA — alertas de anomalias |
| **Semanal** | Search Terms Report + negativas, CTR, Quality Score |
| **Mensal** | ROAS, tendência de CPA, ajuste de lances, expansão de palavras-chave |
| **Trimestral** | Revisão de estrutura, novos tipos de campanha, benchmarks |

---

## Capítulo 11 — Otimização Contínua

### 11.1 Single Theme Ad Groups (STAGs)

Agrupar palavras-chave por **tema**, não por palavra individual. Isso melhora a relevância do anúncio para o grupo e alimenta o Smart Bidding com mais dados por grupo.

### 11.2 Expansão de Palavras-chave

1. Abrir **Search Terms Report** semanalmente
2. Identificar termos que geraram conversões mas não estão na lista de palavras-chave
3. Adicionar esses termos como palavras-chave
4. Identificar termos que geraram cliques sem conversão → adicionar como negativas

### 11.3 Otimização de Landing Page

A landing page é determinante para Quality Score e conversão. Verificar:

- [ ] Velocidade de carregamento (Google PageSpeed Insights — meta: 90+ mobile)
- [ ] Responsividade mobile — a maioria do tráfego é mobile
- [ ] Mensagem consistente com o anúncio (título do anúncio = headline da LP)
- [ ] CTA visível sem scroll (above the fold)
- [ ] Formulário ou botão de compra com poucos passos
- [ ] Prova social (avaliações, depoimentos) visível

### 11.4 Testes A/B

**Regra:** Testar uma variável por vez.

**Variáveis para testar em Search:**
- Títulos diferentes no RSA (fixar alternativas e comparar)
- Landing page (usar experimento de campanha do Google)
- Estratégia de lance (tCPA vs. Maximizar Conversões)

**Variáveis para testar em Display:**
- Imagem (produto vs. lifestyle)
- Copy de título
- Público (in-market vs. affinity)

**Protocolo:**
1. Definir hipótese e duração mínima (14 dias / 100 cliques por variante)
2. Usar **Experimentos de Campanha** do Google Ads para testes válidos
3. Documentar resultado e aprendizado

### 11.5 Erros Comuns a Evitar

| Erro | Por que prejudica | Solução |
|------|------------------|---------|
| Rodar sem palavras-chave negativas | Orçamento gasto em buscas irrelevantes | Adicionar lista básica antes de ativar; revisar Search Terms semanalmente |
| Mandar tráfego para a homepage | Alta taxa de rejeição, Quality Score baixo | Criar landing pages de produto ou categoria correspondentes |
| Testar apenas uma variação de anúncio | Sem aprendizado, perde potencial de otimização | Criar mínimo 2 RSAs por grupo + testar ativos |
| Ignorar a análise semanal | Problemas não detectados consomem orçamento | Reservar tempo fixo todo início de semana |
| Concentrar todo o orçamento em uma campanha | Sem diversificação, risco alto se a campanha falhar | Distribuir entre Search + PMax desde o início |
| Avaliar campanha nova antes de 30–60 dias | Decisões prematuras interrompem o aprendizado | Aguardar o período mínimo antes de julgar resultados |
| Não configurar valor de conversão | Smart Bidding otimiza por volume, não por valor | Sempre enviar o valor em R$ no evento de compra |

### 11.6 Análise Demográfica

Verificar performance por segmento demográfico (Idade, Gênero, Renda familiar):

- Identificar segmentos com CPA acima da média → reduzir lance ou excluir
- Identificar segmentos com CPA abaixo da meta → aumentar lance

---

## Capítulo 12 — Nicho SB no Google Ads

### 12.1 Políticas do Google para o Nicho

Ao contrário do Meta, o Google Ads permite anunciar produtos relacionados a shibari e bondage de forma mais direta, desde que:

- O produto seja legal no Brasil ✅
- Não haja nudez ou conteúdo sexualmente explícito no criativo ✅
- A landing page seja adequada para o público anunciado ✅
- Não haja claims enganosos ou exagerados ✅

**O vocabulário técnico do nicho (shibari, bondage, BDSM) pode ser usado em palavras-chave e anúncios.** A restrição do Google foca em conteúdo explícito, não em categorias de produto.

### 12.2 Zona de Atenção

Evitar criativos (em Display e PMax) que contenham:
- Imagens com poses sexualmente explícitas
- Nudez (parcial ou total)
- Copy que prometa benefícios sexuais ou experiências adultas explícitas

**O que funciona e é seguro:**
- Foto do produto (corda, acessórios)
- Imagens de prática artística (amarração estética, sem conotação sexual explícita)
- Copy focado em qualidade, artesanato e especificação técnica

### 12.3 Checklist Pré-Campanha — Nicho SB

- [ ] Produto é legal no Brasil
- [ ] Criativo não contém nudez ou conotação sexual explícita
- [ ] Copy não contém claims enganosos ou promessas de experiência sexual
- [ ] Landing page está dentro das políticas do Google (sem conteúdo adulto irrestrito)
- [ ] Rastreamento de conversão ativo e validado
- [ ] Palavras-chave negativas básicas adicionadas
- [ ] Ad Strength dos RSAs em "Bom" ou "Excelente"
- [ ] Mínimo 2 RSAs por grupo de anúncios
- [ ] Extensões configuradas (sitelinks, callouts, snippets)

---

## Capítulo 13 — Checklists Operacionais

### 13.1 Checklist — Nova Campanha Search

- [ ] Objetivo definido (conversões, tráfego ou leads)
- [ ] Palavras-chave mapeadas e organizadas por grupo temático
- [ ] Negativas básicas adicionadas desde o início
- [ ] Mínimo 2 RSAs por grupo com Ad Strength "Bom" ou melhor
- [ ] Extensões configuradas: sitelinks, callouts, snippets estruturados
- [ ] Landing page verificada: velocidade, relevância, CTA
- [ ] Rastreamento de conversão validado
- [ ] Estratégia de lance escolhida conforme histórico disponível
- [ ] Orçamento diário calculado com base no CPA alvo
- [ ] Localização: Brasil (ou estados específicos se relevante)
- [ ] AI Max configurado (ativar após período de aprendizado inicial se aplicável)

### 13.2 Checklist — Nova Campanha Display/Remarketing

- [ ] Lista de remarketing configurada no Google Ads (via GA4 ou tag direta)
- [ ] Mínimo 100 usuários na lista para ativar
- [ ] RDA criado com máximo de imagens e logos
- [ ] Optimized Targeting ativado
- [ ] Smart Bidding configurado (Maximizar Conversões ou tCPA)
- [ ] Rastreamento de conversão validado
- [ ] Exclusão de clientes que já compraram (se o objetivo for aquisição)

### 13.3 Checklist — Durante a Campanha (Semanal)

- [ ] Revisar Search Terms Report e adicionar negativas necessárias
- [ ] Verificar CTR, CPA e ROAS em relação às metas
- [ ] Conferir Ad Strength dos RSAs — criar variações se necessário
- [ ] Verificar Budget Utilization (campanha limitada por orçamento?)
- [ ] Analisar performance demográfica (ajustar lances se necessário)
- [ ] Checar Impression Share — há perda por orçamento ou ranking?

### 13.4 Checklist — Pós-Campanha

- [ ] Registrar métricas finais (CTR, CPA, ROAS, Conversões)
- [ ] Documentar aprendizados de palavras-chave (quais funcionaram, quais não)
- [ ] Documentar aprendizados de criativos (RSA/RDA)
- [ ] Registrar segmentações e lances que performaram melhor
- [ ] Comparar com meta inicial e campanha anterior equivalente
- [ ] Salvar relatório em `relatorios/diagnostico-google-ads/[slug-campanha]/relatorio-final.md`

### 13.5 Checklist — Nova Campanha Performance Max

- [ ] Histórico mínimo: 30+ conversões/mês antes de ativar
- [ ] Mínimo 2 grupos de ativos (por tema de produto)
- [ ] Por grupo: 15 títulos, 5 descrições, 15 imagens (vertical + quadrada + landscape), 5 logos, 5 vídeos próprios
- [ ] Vídeos em múltiplas orientações (vertical + horizontal + quadrado)
- [ ] Search Themes definidos (5–10 termos por grupo de ativos)
- [ ] Sinais de audiência configurados: Customer Match + visitantes do site
- [ ] Expansão de URL Final habilitada + páginas excluídas definidas
- [ ] New Customer Value Mode avaliado (ativar se objetivo for aquisição)
- [ ] Estratégia de lance: Maximizar Valor de Conversão ou tROAS
- [ ] Rastreamento com valor de conversão em R$ configurado
- [ ] Aguardar 4–6 semanas antes de avaliar e ajustar

### 13.6 Checklist — Nova Campanha Demand Gen

- [ ] Objetivo definido: awareness, consideration ou conversão
- [ ] Mínimo 3 imagens por orientação (vertical + quadrada + horizontal = 9 imagens total)
- [ ] Mínimo 3 vídeos em orientações diferentes
- [ ] Títulos (até 5) e descrições (até 5) criados
- [ ] Optimized Targeting ativado com listas de dados próprios como sinal
- [ ] Orçamento diário compatível com o CPA alvo (mínimo 10× o CPA alvo/dia)
- [ ] Rastreamento de conversão validado
- [ ] Segmentação definida: remarketing e/ou Optimized Targeting para aquisição
- [ ] Brand Safety: Inventory Type configurado (Standard recomendado)
- [ ] Aguardar 4+ semanas para análise completa de performance

---

## Capítulo 14 — Análise de Dados

> Dados são o principal ativo de uma conta de Google Ads. Sem análise estruturada e recorrente, o investimento em mídia paga vira aposta. Esta seção define o que analisar, como interpretar e quando agir.

### 14.1 Princípio de Análise Baseada em Dados

**Regra fundamental:** Nunca otimizar por intuição antes de verificar os dados. Nunca pausar, escalar ou mudar uma campanha sem ter ao menos uma hipótese baseada em uma métrica.

**Hierarquia de decisão:**
```
DADO (o que está acontecendo)
  ↓
DIAGNÓSTICO (por que está acontecendo)
  ↓
HIPÓTESE (o que pode resolver)
  ↓
AÇÃO (uma mudança por vez)
  ↓
VALIDAÇÃO (medir o impacto)
```

**O que NÃO é análise:**
- Ver que o CPA subiu e pausar a campanha sem investigar causa
- Comparar semanas sem considerar sazonalidade
- Avaliar PMax nova com menos de 30 dias de dados
- Tomar decisão com menos de 50 conversões no período

### 14.2 Relatórios Principais da Interface do Google Ads

#### Relatório de Termos de Pesquisa
**Onde acessar:** Campanhas → Palavras-chave → Termos de pesquisa

O que revela:
- Buscas reais que ativaram os anúncios (podem diferir das palavras-chave cadastradas)
- Termos que convertem mas não estão na lista → adicionar como palavras-chave
- Termos irrelevantes que geraram cliques → adicionar como negativas
- Intenção real do usuário que a conta está capturando

**Cadência:** Revisar semanalmente. É o relatório mais acionável da conta.

#### Relatório de Performance de Anúncios
**Onde acessar:** Campanhas → Anúncios

O que revela:
- CTR e taxa de conversão por anúncio individual
- Ad Strength de cada RSA
- Quais títulos e descrições o Google está priorizando (via relatório de combinações)
- Anúncios com baixo desempenho que devem ser substituídos

#### Relatório de Estratégia de Lances
**Onde acessar:** Ferramentas → Estratégias de lance → selecionar estratégia → Relatório

O que revela:
- Como o Smart Bidding está se comportando
- Se o CPA alvo está sendo atingido
- Variações de CPA/ROAS ao longo do tempo
- Se a campanha está em fase de aprendizado ou estável

#### Relatório de Impressões (Auction Insights)
**Onde acessar:** Campanhas → selecionar campanha → Mais → Insights do leilão

O que revela:
- Participação no leilão vs. concorrentes (Impression Share)
- Position Above Rate (% em que o concorrente aparece acima do seu anúncio)
- Overlap Rate (% de vezes que o concorrente aparece junto com o seu anúncio)
- Top of Page Rate (% de vezes que aparece no topo)

**Como usar:** Monitorar se concorrentes novos entraram no leilão ou se um já existente escalou investimento.

#### Relatório de Canais (Demand Gen)
**Onde acessar:** Campanhas Demand Gen → Segmentar por rede

O que revela:
- Performance separada por canal: YouTube, Google Discover, Gmail, Display Network, Maps
- Quais canais geram mais engajamentos, views e conversões
- Permite pausar canais com baixo ROAS individualmente

#### Relatório de Ativos (Assets)
**Onde acessar:** Campanhas → Grupos de ativos (PMax) ou Anúncios → Ativos

O que revela:
- Performance de cada ativo individual (imagem, vídeo, título, descrição)
- Classificação: Melhor, Bom, Baixo, Em aprendizado
- Quais ativos o Google está priorizando e quais estão sendo ignorados

**Ação:** Remover ativos com classificação "Baixo" e criar novas variações.

#### Relatório de Posicionamentos ("Where ads showed")
**Onde acessar:** Campanhas Display/Video → Posicionamentos → Onde os anúncios foram exibidos

O que revela:
- Sites, apps e canais do YouTube onde os anúncios apareceram
- CPM e taxa de conversão por posicionamento
- Posicionamentos ineficientes que devem ser excluídos

**Para SB:** Excluir apps de jogos mobile (geralmente geram cliques acidentais) e canais sem relação com o nicho.

### 14.3 Métricas por Tipo de Campanha

#### Search
| Métrica | O que indica | Sinal de alerta |
|---------|-------------|----------------|
| CTR | Relevância do anúncio para a busca | < 2%: copy fraco ou keywords erradas |
| CPC | Competição no leilão | Subindo sem conversões: rever relevância |
| Quality Score | Alinhamento ad + keyword + LP | < 6: investigar componente mais fraco |
| Conv. Rate | Eficiência da landing page | < 1%: problema na LP ou no público |
| CPA | Custo por compra | Acima da meta: ajustar lance ou LP |

#### Display e Remarketing
| Métrica | O que indica | Sinal de alerta |
|---------|-------------|----------------|
| CPM | Custo de alcance | Muito alto: público muito estreito |
| CTR | Engajamento com o criativo | < 0,3%: trocar criativo |
| View-through Conv. | Conversões após visualização (sem clique) | Útil para medir impacto de awareness |
| Freq. | Quantas vezes o usuário viu | > 5×: fadiga de criativo, rodar novos |

#### Video / Demand Gen
| Métrica | O que indica | Definição exata |
|---------|-------------|----------------|
| **Engajamentos** | Interação com o anúncio | Imagens: primeiro clique em anúncio Gmail; Vídeo: assistir 10s in-stream ou 5s em feed/Shorts, ou clicar na LP |
| **Views** | Visualização qualificada | In-stream: 30 segundos ou clique; In-feed/Shorts: 10 segundos ou clique |
| **VTR** (View-Through Rate) | % de impressões que viraram views | Benchmark: 15–30% in-stream |
| **CPV** | Custo por visualização qualificada | Depende do objetivo e formato |
| **Clicks** | Cliques diretos para LP | Navegação direta para a landing page |

#### Performance Max
| Métrica | O que indica | Sinal de alerta |
|---------|-------------|----------------|
| Conv. Value | Valor total gerado | Principal métrica — rastrear junto com ROAS |
| ROAS | Eficiência do gasto | Abaixo de 2×: revisar ativos e sinais |
| Asset Strength | Qualidade dos grupos de ativos | "Baixo": substituir ativos fracos |
| Conversion lag | Delay entre clique e conversão | Normal: 1–7 dias dependendo do produto |

### 14.4 Segmentações para Análise

A interface do Google Ads permite aplicar segmentações (dimensões) em praticamente qualquer relatório. As mais úteis:

| Segmentação | O que revela | Quando usar |
|-------------|-------------|-------------|
| **Rede** | Search vs. Display vs. YouTube | Verificar se Search ou Display performa melhor |
| **Dispositivo** | Mobile vs. Desktop vs. Tablet | Identificar se mobile tem CPA acima do alvo |
| **Dia da semana** | Performance por dia | Ajustar programação de anúncios |
| **Hora do dia** | Performance por horário | Identificar picos e vales de conversão |
| **Localização** | Estado ou cidade | Aumentar lance em regiões que convertem mais |
| **Demográfico** | Idade e gênero | Identificar segmentos com CPA fora do alvo |
| **Canal (Demand Gen)** | YouTube, Discover, Gmail, Display | Alocar budget para canais mais eficientes |

**Como aplicar:** Em qualquer tabela de relatório, clicar em "Segmentar" e escolher a dimensão desejada.

### 14.5 Tipos de Conversão — Definições e Rastreamento

| Tipo | O que conta | Como configurar |
|------|------------|----------------|
| **Compra no site** | Checkout concluído com valor em R$ | Tag de conversão ou GA4 → Google Ads |
| **Add to Cart** | Produto adicionado ao carrinho | Evento GA4 importado |
| **Clique em botão** | CTA específico (ex: WhatsApp) | Tag de evento ou GTM |
| **Chamada telefônica** | Clique em número de telefone no anúncio | Extensão de chamada com rastreamento |
| **Conversão offline** | Vendas por WhatsApp ou telefone importadas | Upload manual ou integração CRM |

**Regra crítica:** Sempre enviar o **valor em R$** junto com o evento de compra — sem isso, o tROAS não tem base para otimizar e os relatórios de ROAS ficam zerados.

**Conversões primárias vs. secundárias:**
- **Primária:** Purchase — usada para otimização pelo Smart Bidding
- **Secundária:** Add to Cart, Begin Checkout — usadas para análise, não para lances

### 14.6 Atribuição e Janela de Conversão

**Modelo de atribuição recomendado:** Baseado em dados (Data-Driven Attribution) — distribui o crédito da conversão entre todos os pontos de contato com base em dados reais da conta. Disponível quando há volume mínimo de conversões.

**Alternativa:** Último clique — simples, mas subestima campanhas de topo de funil.

**Janela de conversão:** Período em que uma conversão é atribuída a um clique no anúncio.
- Padrão Google Ads: 30 dias para cliques, 1 dia para visualizações
- Para SB (produto de decisão mais rápida): 7–14 dias pode ser suficiente
- Nunca reduzir a janela sem entender o ciclo de decisão real do cliente

**Latência de conversão:** A maioria das conversões não acontece no mesmo dia do clique. Verificar o relatório de "Atraso de conversão" para entender o ciclo médio antes de julgar performance de campanhas recentes.

### 14.7 Relatórios Customizados e Dashboards

**Relatórios salvos:** Na aba "Relatórios" do Google Ads, é possível criar e salvar visualizações customizadas com as métricas mais relevantes. Salvar ao menos dois:

1. **Visão Semanal Operacional**
   - Colunas: Campanha | Impressões | Cliques | CTR | CPC | Conversões | CPA | Conv. Value | ROAS
   - Período: últimos 7 dias vs. 7 dias anteriores

2. **Visão Mensal Estratégica**
   - Colunas: Campanha | Gasto | Conversões | CPA | Conv. Value | ROAS | Impression Share
   - Período: mês atual vs. mês anterior

**Google Ads × GA4 — Relatórios integrados:**
- Ativar **auto-tagging** no Google Ads para que o GA4 capture a origem de cada sessão
- Em GA4: Aquisição → Aquisição de tráfego → filtrar por "google / cpc" para ver comportamento pós-clique
- Verificar: taxa de rejeição, páginas por sessão, tempo médio, funil de conversão por campanha

### 14.8 BigQuery — Análise Avançada (Referência)

O **BigQuery Data Transfer Service** permite exportar todos os dados do Google Ads para o BigQuery (banco de dados SQL do Google Cloud) para análises que a interface nativa não suporta.

**Quando considerar:**
- Volume alto de dados (múltiplas campanhas, muitos produtos)
- Necessidade de cruzar dados de Google Ads com dados do CRM ou da loja
- Análises históricas longas (a interface do Google Ads limita alguns relatórios)
- Dashboards customizados no Looker Studio com dados brutos

**O que é transferido:**
- Dados de campanhas, grupos de anúncios, anúncios e palavras-chave
- Dados de conversão e performance diária
- Dados de audiência e segmentação

> Para SB hoje: não é prioridade. Avaliar quando a conta atingir volume que justifique a complexidade técnica.

### 14.9 Rotina de Análise da Conta

#### Diária (5–10 min)
- [ ] Verificar gasto vs. orçamento diário (campanha limitada por orçamento?)
- [ ] Checar conversões do dia — alguma anomalia (zero ou pico?)
- [ ] Alertas de política (anúncio reprovado?)

#### Semanal (30–60 min)
- [ ] **Search Terms Report:** identificar novos termos a adicionar ou negativar
- [ ] Conferir CTR por campanha — queda indica fadiga ou problema de relevância
- [ ] Verificar Ad Strength dos RSAs — criar variações se necessário
- [ ] Checar Impression Share — há perda por orçamento ou por ranking?
- [ ] Revisar performance demográfica — ajustar modificadores de lance
- [ ] Conferir posicionamentos (Display/Video) — excluir ineficientes
- [ ] Atualizar lista de Customer Match se houver novos clientes

#### Mensal (2–3 horas)
- [ ] Comparar ROAS, CPA e conversões com mês anterior
- [ ] Análise de ativos (PMax/Demand Gen): substituir classificados como "Baixo"
- [ ] Revisar Auction Insights — novos concorrentes no leilão?
- [ ] Analisar relatório de atribuição — funil está funcionando?
- [ ] Revisar estrutura de campanhas — consolidar grupos com poucos dados?
- [ ] Verificar latência de conversão — janela está correta?
- [ ] Documentar aprendizados no relatório mensal

#### Trimestral (revisão estratégica)
- [ ] Revisar distribuição de orçamento entre campanhas (PMax/Search/outros)
- [ ] Avaliar novos tipos de campanha (está na hora de ativar Demand Gen? Video?)
- [ ] Revisar palavras-chave da conta — remover inativas, expandir com novos termos
- [ ] Comparar performance com benchmarks de mercado
- [ ] Definir metas para o próximo trimestre (CPA, ROAS, volume de conversões)

---

## Capítulo 15 — Estratégia Full-Funnel

### 15.1 Por que Pensar em Funil

Um funil de vendas representa a jornada do cliente desde o primeiro contato com a marca até a compra — e além. Para o Google Ads, ignorar as etapas superiores do funil significa competir apenas com quem já está pronto para comprar, pagando CPCs mais altos por um volume menor de oportunidades.

**O argumento quantitativo:** Estratégias de nutrição ao longo do funil aumentam as oportunidades de venda em até **30%** (Demand Gen Report). Quem só anuncia para fundo de funil perde a chance de criar demanda e educar o mercado.

**Para a SB:** A maioria das pessoas ainda não sabe que pode comprar cordas de shibari de alta qualidade online. Criar demanda nas etapas superiores do funil amplia o pool de clientes que chegam ao fundo.

### 15.2 As Quatro Etapas do Funil

```
TOPO (ToFu) — Atração e Consciência
  Muitos → Descobrem a marca / o universo
  ↓
MEIO (MoFu) — Engajamento e Consideração
  Alguns → Pesquisam, comparam, consideram
  ↓
FUNDO (BoFu) — Decisão e Compra
  Poucos → Alta intenção, prontos para comprar
  ↓
PÓS-VENDA — Fidelização e Recompra
  Clientes → Voltam, indicam, recompram
```

### 15.3 Campanhas por Etapa do Funil

| Etapa | Objetivo | Tipos de Campanha | Estratégia de Lance |
|-------|---------|------------------|-------------------|
| **Topo (ToFu)** | Alcance e awareness | Video (VRC), Demand Gen, Display | CPM |
| **Meio (MoFu)** | Consideração e engajamento | Video (VVC), Search broad, Display retargeting | CPV, Maximizar Cliques |
| **Fundo (BoFu)** | Conversão | Search (alta intenção), RLSA, PMax | tCPA, tROAS |
| **Pós-venda** | Recompra e fidelização | Customer Match, Display, Demand Gen | tCPA (cross-sell) |

**Palavras-chave por etapa — exemplo SB:**

| Etapa | Tipo de busca | Exemplos |
|-------|-------------|---------|
| **Topo** | Genérica, educativa | `shibari o que é`, `corda artesanal`, `arte japonesa com cordas` |
| **Meio** | Específica, comparativa | `corda de juta shibari`, `melhor corda para bondage`, `corda natural para amarração` |
| **Fundo** | Transacional, de compra | `comprar corda shibari`, `corda juta 6mm preço`, `shibari brasil loja` |

### 15.4 Full-Funnel no YouTube — Reach Planner

O Google oferece o **Reach Planner** para planejar estratégias full-funnel no YouTube com alocação de orçamento por etapa.

**Três objetivos no funil do YouTube:**

| Etapa | Formato | Métrica principal | Lance |
|-------|---------|-----------------|-------|
| **Awareness** | Video Reach Campaign (VRC) — In-stream, Bumper, Shorts | Alcance único (Reach) | CPM |
| **Consideration** | Video View Campaign (VVC) — In-stream, In-feed | Visualizações (Views) | CPV |
| **Action** | Demand Gen, campanhas de ação | Conversões | CPA |

**Dois modos de planejamento no Reach Planner:**
- **Conversion Creation:** ênfase em awareness e consideração para criar novos clientes e ampliar conversões futuras — ideal para fase de crescimento
- **Conversion Generation:** foco em ação e consideração para converter quem já conhece a marca — ideal quando há base de audiência estabelecida

### 15.5 Métricas por Etapa do Funil

| Etapa | O que medir |
|-------|------------|
| **Topo** | Alcance, Impressões, CPM, Brand Lift |
| **Meio** | CTR, Visualizações, CPV, Taxa de engajamento, Tempo no site |
| **Fundo** | Conversões, CPA, ROAS, ROI, Taxa de conversão |
| **Pós-venda** | Taxa de recompra, Ticket médio, CAC, LTV |

**Métricas de saúde do funil (monitorar mensalmente):**
- **Taxa de abandono de carrinho** — identifica atrito no BoFu
- **Tempo médio entre primeira visita e compra** — indica tamanho do ciclo de decisão
- **CAC (Custo de Aquisição de Cliente)** — total investido ÷ novos clientes adquiridos
- **LTV (Lifetime Value)** — receita média por cliente ao longo do tempo

### 15.6 Funil de Vendas da Shibari Brasil — Estratégia Recomendada

**Situação atual:** A SB tem produto de nicho com intenção de compra alta (quem busca já sabe o que quer) mas mercado ainda pouco educado sobre qualidade e onde comprar.

**Estratégia em fases:**

**Fase 1 — Capturar demanda existente (prioridade imediata)**
- Search com palavras-chave de alta intenção (BoFu)
- RLSA para visitantes que não converteram
- Resultado esperado: conversões diretas

**Fase 2 — Expandir com Performance Max**
- PMax cobre todos os canais com base nos compradores existentes
- Gera novos clientes além da busca ativa
- Resultado esperado: volume maior a CPA controlado

**Fase 3 — Criar demanda nova (ToFu/MoFu)**
- Demand Gen: YouTube + Discover com conteúdo de produto/lifestyle
- Video: awareness de marca com bumpers e in-stream
- Resultado esperado: ampliar o público que chega ao BoFu

**Pós-venda contínuo:**
- Customer Match com lista de clientes → campanhas de cross-sell e recompra
- Segmentação por produto comprado → oferecer complementos (acessórios, outras cordas)

### 15.7 Boas Práticas de Funil para E-commerce

- **Mandar tráfego para a página de produto, não para a homepage** — cada anúncio deve levar exatamente ao produto anunciado
- **Simplicidade no checkout** — reduzir campos e etapas diminui abandono no BoFu
- **Recuperação de carrinho** — usuários que abandonaram o carrinho são o público de maior conversão para remarketing
- **Multicanal mobile → desktop** — usuários pesquisam pelo celular e fecham no desktop; garantir experiência fluida nos dois
- **Não concentrar todo o orçamento em BoFu** — distribuir por etapas cria pipeline sustentável de novos clientes

---

## Glossário Rápido

| Termo | Significado |
|-------|-------------|
| **Ad Rank** | Pontuação que determina posição do anúncio (lance × Quality Score × extensões) |
| **Ad Strength** | Métrica de qualidade do RSA (Pobre → Boa → Excelente) |
| **BoFu** | Bottom of Funnel — etapa de decisão/compra, alta intenção |
| **CAC** | Custo de Aquisição de Cliente — total investido ÷ novos clientes |
| **Asset Report** | Relatório que mostra performance individual de cada ativo (imagem, vídeo, título) em PMax e Demand Gen |
| **Atribuição** | Modelo que distribui o crédito da conversão entre os pontos de contato do usuário |
| **Audiências Preditivas** | Públicos gerados por IA do GA4 com alta probabilidade de compra nos próximos 7 dias |
| **Auction Insights** | Relatório de Impressões que mostra participação no leilão vs. concorrentes |
| **Auto-tagging** | Configuração do Google Ads que permite ao GA4 rastrear o comportamento pós-clique |
| **Dynamic Image Resources** | Funcionalidade de ML que seleciona automaticamente imagens das landing pages para os anúncios |
| **Janela de Conversão** | Período (dias) em que uma conversão é atribuída a um clique no anúncio |
| **Keyword Planner** | Ferramenta gratuita do Google para descobrir palavras-chave e estimar volume de busca |
| **Latência de Conversão** | Tempo entre o clique no anúncio e a conclusão da conversão (pode ser dias) |
| **Lookalike Segment** | Audiência similar à lista de Customer Match, expandida pela IA do Google |
| **LTV** | Lifetime Value — receita média gerada por um cliente ao longo do tempo |
| **Match Rate** | Taxa de correspondência do Customer Match (típico: 29–62%) |
| **MoFu** | Middle of Funnel — etapa de consideração e engajamento |
| **Período de Otimização** | Tempo mínimo (60–90 dias) para campanhas novas atingirem performance estável |
| **Reach Planner** | Ferramenta do Google para planejar estratégias full-funnel no YouTube |
| **ROI** | Retorno sobre investimento: (receita – custo) ÷ custo |
| **ToFu** | Top of Funnel — etapa de atração e awareness |
| **VRC** | Video Reach Campaign — campanha de alcance no YouTube com CPM |
| **VVC** | Video View Campaign — campanha de visualizações no YouTube com CPV |
| **Brand Lift Study** | Pesquisa para medir impacto de campanhas de vídeo na consciência de marca |
| **Brand Safety** | Garantia de que anúncios não aparecem em conteúdo prejudicial à marca |
| **Brand Suitability** | Controle fino sobre adequação do contexto onde o anúncio aparece |
| **Bumper** | Formato de vídeo não pulável de até 6 segundos |
| **Consent Mode** | Configuração que respeita preferências de privacidade e mantém rastreamento modelado |
| **CPA** | Custo por aquisição (conversão) |
| **CPC** | Custo por clique |
| **CPM** | Custo por mil impressões — métrica de campanhas de awareness |
| **CPV** | Custo por visualização — métrica de campanhas de video consideration |
| **CTR** | Taxa de cliques (cliques ÷ impressões) |
| **Customer Match** | Upload de lista de clientes (e-mails) para criar audiências e lookalikes no Google |
| **Data Manager** | Ferramenta do Google para conectar fontes de dados próprios (CRM, offline) |
| **Data Strength** | Pilar estratégico: qualidade e volume de dados próprios que alimentam a IA |
| **Demand Gen** | Campanha visual que combina YouTube, Discover e Gmail para criar demanda |
| **Enhanced Conversions** | Envio de dados hasheados para melhorar precisão do rastreamento pós-consentimento |
| **Fase de Aprendizado** | Período em que o Smart Bidding coleta dados para otimizar |
| **First-Party Data** | Dados próprios da SB: clientes, visitantes, eventos de compra |
| **Full-Funnel** | Estratégia que cobre todas as etapas do funil (ToFu → MoFu → BoFu → Pós-venda) |
| **Impression Share** | % das impressões capturadas vs. total disponível |
| **Inventory Type** | Controle de segurança de marca que define tipos de conteúdo onde o anúncio aparece |
| **Negativas** | Palavras-chave que bloqueiam exibição em buscas irrelevantes |
| **New Customer Value Mode** | Configuração da PMax para priorizar aquisição de novos clientes |
| **PMax** | Performance Max — campanha multicanal gerida por IA |
| **Quality Score** | Pontuação de qualidade do anúncio (1–10) |
| **RDA** | Responsive Display Ad — anúncio responsivo de display |
| **ROAS** | Retorno sobre gasto em anúncios (receita ÷ gasto) |
| **RLSA** | Remarketing Lists for Search Ads |
| **RSA** | Responsive Search Ad — anúncio responsivo de pesquisa |
| **Search Terms Report** | Relatório de termos reais buscados pelos usuários |
| **Search Themes** | Termos que orientam a IA da PMax sobre intenções de busca relevantes |
| **Smart Bidding** | Estratégias de lance automatizadas por IA do Google |
| **STAGs** | Single Theme Ad Groups — grupos de anúncios por tema |
| **tCPA** | CPA Alvo — estratégia de lance para custo por conversão alvo |
| **tROAS** | ROAS Alvo — estratégia de lance para retorno alvo |
| **URL Expansion** | Funcionalidade da PMax que redireciona para a LP mais relevante do site |
| **View-through Conv.** | Conversão atribuída a quem viu o anúncio mas não clicou — indicador de impacto de awareness |
| **VTR** | View-Through Rate — % de impressões que resultaram em visualização qualificada |
