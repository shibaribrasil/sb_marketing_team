---
name: hab-meta-ads
description: Use esta skill quando o Gui (agente-trafego) for criar, revisar, otimizar ou analisar anúncios e campanhas no Meta Ads focados em Instagram para a Shibari Brasil. Cobre estrutura de campanhas, formatos, criativos, segmentação, orçamento, Advantage+, testes A/B, métricas, políticas do Meta e estratégias para operar no nicho sensível (fetiche/BDSM) de forma compliant.
---

# Manual de Meta Ads — Shibari Brasil

> Habilidade do Gui para criar, gerenciar e analisar campanhas pagas no Meta Ads com foco em Instagram. Combina a documentação oficial do Meta com boas práticas do mercado e diretrizes específicas para o nicho sensível da Shibari Brasil.

---

## Capítulo 1 — Visão Geral e Contexto

### 1.1 O que é Meta Ads

Meta Ads é a plataforma de publicidade do Meta que abrange Facebook, Instagram, Messenger e Audience Network. Para a Shibari Brasil, o único canal ativo é o **Instagram** — Feed, Stories e Reels.

**Regra de posicionamento:** Não veicular anúncios para Facebook, Audience Network ou Messenger. Todo ad set deve ter posicionamento restrito ao Instagram. Ao usar Advantage+ Placements, desativar manualmente os demais canais.

A plataforma permite criar campanhas segmentadas com base em interesses, comportamentos, dados demográficos e histórico de interação do usuário.

### 1.2 O Nicho da Shibari Brasil no Meta

A Shibari Brasil opera em um nicho **sensível mas legítimo**. Os produtos são 100% legais no Brasil; a comunicação é que determina se um anúncio será aprovado ou bloqueado.

O Meta classifica anunciantes em quatro zonas de risco:

| Zona | Situação | Status para SB |
|------|----------|---------------|
| **Sensível** | Produto legal + anúncio compliant | ✅ Onde queremos estar |
| **Zona Cinzenta** | Produto legal + linguagem ambígua | ⚠️ Aceitável com cautela |
| **Black Legal** | Produto legal + promessas proibidas | ❌ Evitar |
| **Black Ilegal** | Produto proibido por lei | ❌ Nunca |

**Regra fundamental:** A Shibari Brasil anuncia **arte, prática, conexão e qualidade** — nunca conteúdo sexual explícito. O posicionamento correto é o de marca de lifestyle e curadoria de produtos especializados.

---

## Capítulo 2 — Estrutura de Campanhas

### 2.1 Os Três Níveis

Todo anúncio no Meta é organizado em três níveis hierárquicos:

```
CAMPANHA
  └── Define o OBJETIVO (o que queremos alcançar)

    CONJUNTO DE ANÚNCIOS
      └── Define PÚBLICO + ORÇAMENTO + POSICIONAMENTO + AGENDA

        ANÚNCIOS
          └── Define CRIATIVO + COPY + CTA
```

### 2.2 Objetivos de Campanha

Escolher o objetivo correto é decisivo — ele determina como o algoritmo distribui o orçamento e para quem entrega.

| Objetivo | Quando usar para SB |
|----------|---------------------|
| **Reconhecimento** | Lançamento de produto novo, expansão de marca |
| **Tráfego** | Direcionar para blog, página de produto ou WhatsApp |
| **Engajamento** | Aumentar interações em posts orgânicos impulsionados |
| **Cadastros** | Capturar leads para lista de e-mail |
| **Vendas** | Conversões diretas no site (requer Pixel configurado) |

> **Padrão SB:** Para campanhas de produto, priorizar **Vendas** ou **Tráfego**. Para aquecimento de audiência, usar **Engajamento** ou **Reconhecimento**.

### 2.3 Estrutura Recomendada por Campanha

```
Campanha: [Objetivo] — [Nome do Produto ou Tema]
  ├── Ad Set 1: Público Frio (Interesses)
  │     └── Anúncio A: Criativo 1
  │     └── Anúncio B: Criativo 2
  ├── Ad Set 2: Público Morno (Engajamento)
  │     └── Anúncio A: Criativo 1
  └── Ad Set 3: Retargeting (Visitantes/Clientes)
        └── Anúncio A: Oferta direta
```

---

## Capítulo 3 — Formatos e Especificações Técnicas

### 3.1 Feed (Instagram)

| Parâmetro | Valor |
|-----------|-------|
| Formatos aceitos | JPG, PNG, MP4 |
| Proporções ideais | 1:1 (quadrado), 4:5 (retrato), 1,91:1 (paisagem) |
| Resolução 1:1 | 1080×1080px |
| Resolução 4:5 | 1080×1350px |
| Resolução 1,91:1 | 1200×628px |
| Texto principal | Até 125 caracteres (trunc. depois) — ideal: 50–80 chars |
| Título (headline) | Até 27 caracteres |
| Margem segura | 10–15% nas bordas |

> **Recomendação SB:** Preferir proporção **4:5** (1080×1350px) — ocupa mais espaço no feed e tem melhor performance geral.

### 3.2 Stories

| Parâmetro | Valor |
|-----------|-------|
| Proporção | 9:16 (vertical) |
| Resolução | 1080×1920px |
| Formatos | JPG, PNG, MP4 |
| Zona segura — topo | 14% livre (250px) — sem texto/logo |
| Zona segura — inferior | 20% livre (340px) — sem elementos |
| Zona segura — laterais | 6% em cada lado |
| Duração de imagem | 5 segundos visíveis |
| Texto principal | Até 40 caracteres |
| Título | Até 55 caracteres |

### 3.3 Reels

| Parâmetro | Valor |
|-----------|-------|
| Proporção | 9:16 (vertical, tela cheia) |
| Resolução | 1080×1920px |
| Zona segura — topo | 14% livre |
| Zona segura — inferior | 35% livre (maior que Stories — barra de interação) |
| Zona segura — laterais | 6% em cada lado |
| Texto principal | Até 40 caracteres |
| Título | Até 55 caracteres |
| Duração ideal | 15–30 segundos |

### 3.4 Carrossel

| Parâmetro | Valor |
|-----------|-------|
| Proporção | 1:1 ou 4:5 (para Advantage+) |
| Nº de cards | 2 a 10 |
| Cada card | Link independente possível |
| Texto principal | Até 125 caracteres |
| Headline por card | Até 40 caracteres |

**Boas práticas de carrossel:**
- Usar estilo visual coeso em todos os cards
- Vincular cada card à página de produto correspondente
- Primeiro card deve parar o scroll — ser impactante
- Usar autoplay de música quando disponível

### 3.5 Vídeo (geral)

| Parâmetro | Valor |
|-----------|-------|
| Duração possível | 1 segundo a 241 minutos |
| Duração ideal | 15–30 segundos (feed/stories/reels) |
| Formatos | MP4, MOV, GIF |
| Otimizar para | Som ligado E desligado (legendas sempre) |
| Peso máx. | 4GB |

---

## Capítulo 4 — Criativos e Copy

### 4.1 Princípios de Copy

**Estrutura de texto para feed:**
1. **Gancho** — Primeira frase para o scroll parar (pergunta, tensão, afirmação forte)
2. **Desenvolvimento** — Conectar o gancho ao produto ou benefício
3. **CTA** — Uma ação clara: "Acesse o link", "Garanta o seu", "Saiba mais"

**Regras de texto:**
- Máximo 125 caracteres para o texto principal (leitura sem truncamento)
- Voz ativa, frases curtas, sem jargão excessivo
- Uma oferta por anúncio — nunca duas propostas ao mesmo tempo
- CTA com verbo no imperativo e foco no benefício, não na ação mecânica

**O que funciona:**
- Benefício concreto na primeira linha
- Prova social quando disponível ("X clientes", "mais vendido")
- Urgência real (não artificial)
- Linguagem do público, não da marca

### 4.2 Criativos Visuais

**Princípios gerais:**
- Visual ousado que pare o scroll — mas dentro das zonas de segurança
- Marca visível mas não dominante
- CTA visível no criativo (além do botão do anúncio)
- Testar imagem estática vs. vídeo — não assumir qual performa melhor

**Para vídeo:**
- Capturar atenção nos **primeiros 2–3 segundos**
- Otimizar para sem som (legendas em texto na tela)
- Testimonial ou demonstração de produto funcionam bem
- Incluir CTA verbal e visual ao final

**Pipeline de criativos:**
- Manter produção contínua de novos criativos para combater fadiga de audiência
- Rotacionar criativos regularmente
- Testar: proporção, cores, abordagem (produto vs. lifestyle vs. testimonial)

### 4.3 Copy para Nicho Sensível — Shibari Brasil

#### Vocabulário proibido em anúncios pagos

A IA de revisão do Meta associa certos termos a conteúdo adulto e aciona rejeição automática. Nenhuma dessas palavras pode aparecer em copy, headline, texto no criativo ou URL de destino visível:

| Termo proibido | Motivo |
|----------------|--------|
| **shibari** | Associado pelo Meta a conteúdo adulto/sexual |
| **bondage** | Idem |
| **BDSM** | Idem |
| **fetiche / fetichismo** | Idem |
| **erótico / erotismo** | Idem |
| **sexual / sexualidade** | Idem |
| **prazer** (isolado) | Contexto adulto implícito para a IA |
| **dominação / submissão** | Idem |

> Esses termos podem existir na página de destino, mas não devem aparecer em nenhum elemento do anúncio em si.

#### Dicionário de Substituição

Para comunicar a marca ao público certo sem acionar bloqueios, usar equivalentes que mantêm o sentido para quem conhece o universo, mas passam invisíveis para a IA do Meta:

| O que a marca é | O que dizemos no anúncio |
|-----------------|--------------------------|
| Shibari / bondage | Amarração artesanal · técnica de amarração · arte dos laços |
| Corda de shibari | Corda artesanal · corda de juta · corda natural tratada |
| Prática fetichista | Prática especializada · exploração consciente · experiência sensorial |
| Comunidade BDSM | Comunidade · praticantes · pessoas que levam a prática a sério |
| Fetiche | Prática · universo · nicho |
| Dominação / submissão | Dinâmica · conexão · entrega |
| Prazer (contexto adulto) | Experiência · sensação · intensidade |

#### Ângulos de comunicação seguros para SB

| Ângulo | Exemplo de copy |
|--------|-----------------|
| Arte e craft | "Cada corda, uma peça. Feita à mão, com intenção." |
| Qualidade artesanal | "Material selecionado. Acabamento impecável. Pronto para usar." |
| Prática consciente | "Para quem leva a amarração a sério." |
| Conexão e experiência | "A experiência começa pelo equipamento certo." |
| Curadoria especializada | "Produtos selecionados para quem sabe o que quer." |
| Identidade de comunidade | "Feito para quem entende." |

#### Regra de ouro

Antes de finalizar qualquer copy, perguntar: **"Isso faria sentido para quem não conhece o universo?"** Se a resposta for sim e o copy não contiver nenhuma palavra da lista proibida acima, está seguro para veiculação.

---

## Capítulo 5 — Segmentação de Público

### 5.1 Tipos de Público

**Público Frio (Interesses):**
Pessoas que nunca interagiram com a SB mas têm o perfil das personas.

Para a Persona 1 (Iniciante Curiosa):
- Autoconhecimento, psicologia, feminismo, bem-estar
- Yoga, meditação, autocuidado
- Moda alternativa, moda consciente
- Podcasts de comportamento e sexualidade

Para a Persona 2 (Praticante Exigente):
- Design, artesanato premium, curadoria
- Lifestyle masculino sofisticado
- Cultura alternativa, expressão artística
- Interesse em qualidade e materiais

Para Comunidade LGBTQIA+:
- Segmentar via interesses de comunidade e eventos

**Público Morno (Engajamento):**
Pessoas que já interagiram com a conta, viram vídeos ou clicaram em anúncios anteriores.

**Retargeting (Público Quente):**
- Visitantes do site (via Pixel)
- Quem adicionou ao carrinho sem comprar
- Clientes que já compraram (para cross-sell e fidelização)

**Lookalike (Semelhante):**
- Criar a partir da lista de clientes ou de quem mais converte
- Começar com lookalike 1–3% (mais semelhante) antes de ampliar

### 5.2 Boas Práticas de Segmentação

- **Nunca segmentação muito restrita**: Limitar demais prejudica o aprendizado do algoritmo. Deixar o Meta encontrar quem converte dentro de públicos amplos.
- **Consolidar ad sets sobrepostos**: Evitar que ad sets do mesmo público concorram entre si (leilão interno).
- **Escada de temperaturas**: Construir funil — frio → morno → quente — não tentar converter público frio direto.
- **Advantage+ Audience**: Quando usar Advantage+, o algoritmo expande a segmentação automaticamente.

### 5.3 Regra de Segmentação do Meta (Anti-discriminação)

O Meta proíbe usar segmentação para discriminar por raça, religião, orientação sexual, identidade de gênero ou outras características protegidas. Segmentar público LGBTQIA+ por interesses é permitido — segmentar com base em dados privados ou de forma excludente/discriminatória não é.

---

## Capítulo 6 — Orçamento, Lances e ROAS

### 6.1 Tipos de Orçamento

| Tipo | Como funciona | Quando usar |
|------|---------------|-------------|
| **Diário** | Valor fixo por dia, gasto consistente | Campanhas contínuas |
| **Vitalício** | Total para toda a campanha, Meta distribui | Campanhas com data de início/fim definida |

**Orçamentos mínimos recomendados pelo Meta:**
- Por ad set (com otimização por clique/alcance): ~R$ 6/dia
- Por ad set (com otimização por conversão): ~R$ 50/dia (para sair da fase de aprendizado)

### 6.2 Estratégias de Lance

| Estratégia | Comportamento | Quando usar |
|------------|---------------|-------------|
| **Lance automático** (padrão) | Meta gerencia para maximizar resultados | Início de campanha, fase de aprendizado |
| **Limite de custo** | Meta tenta ficar abaixo de um custo alvo | Quando há CPA definido |
| **Limite de lance** | Máximo por leilão | Controle rigoroso de custo, risco de menor volume |
| **Meta de ROAS** | Otimiza para atingir retorno sobre gasto definido | E-commerce com dados sólidos |

**Boas práticas de orçamento:**
- Aumentar orçamento **gradualmente** (máximo 20–30% por vez) para não resetar a fase de aprendizado
- Agrupar edições significativas para evitar resets múltiplos
- Aguardar pelo menos **7 dias e 50 eventos** antes de avaliar e otimizar

### 6.3 Fase de Aprendizado

O algoritmo do Meta precisa de dados para otimizar. Enquanto aprende, o custo é instável.

- **Gatilho de aprendizado**: Cada ad set entra em aprendizado ao ser criado ou modificado significativamente
- **Saída do aprendizado**: Após ~50 eventos de otimização em 7 dias
- **O que reseta o aprendizado**: Editar público, orçamento (>20%), criativo, posicionamento ou lance

> Evitar edições desnecessárias durante a fase de aprendizado.

### 6.4 ROAS — Boas Práticas

- Usar públicos amplos + lookalike e deixar a IA do Meta encontrar quem converte
- Rastrear com Pixel + Conversions API (dados mais precisos)
- Otimizar a landing page: velocidade de carregamento, coerência com anúncio, CTA claro
- Monitorar ROAS, CPA e CTR diariamente
- Remover criativos que não performam; aumentar orçamento nos que funcionam

---

## Capítulo 7 — Ferramentas Advantage+

### 7.1 O que é Advantage+

Advantage+ é o conjunto de ferramentas de automação do Meta que usa IA para otimizar campanhas com menos configuração manual.

| Ferramenta | O que faz |
|------------|-----------|
| **Advantage+ Placements** | Meta distribui automaticamente pelos melhores posicionamentos — **para SB: restringir manualmente ao Instagram** |
| **Advantage+ Creative** | Sistema otimiza automaticamente imagens, vídeos e texto conforme resposta da audiência |
| **Advantage+ Audience** | Expande a segmentação automaticamente para encontrar quem converte |
| **Advantage+ Shopping** | Campanha totalmente automatizada para e-commerce — gerencia público, posicionamento e orçamento |

### 7.2 Quando Usar Advantage+

- **Advantage+ Placements**: Ao habilitar, desativar manualmente Facebook, Audience Network e Messenger — manter apenas Instagram Feed, Stories e Reels
- **Advantage+ Creative**: Habilitar sempre que possível — melhora resultados com ajustes automáticos de criativo
- **Advantage+ Shopping**: Testar quando volume de dados for suficiente (histórico de vendas no Pixel)

### 7.3 Limitation

Advantage+ tem menos controle manual. Quando o objetivo é testar hipóteses específicas (ex: "qual criativo funciona"), manter controle manual e usar A/B teste dedicado.

---

## Capítulo 8 — Testes A/B

### 8.1 Como Fazer Testes A/B no Meta

**Regra de ouro:** Testar uma variável por vez. Se mudar criativo + público ao mesmo tempo, não dá para saber o que causou a diferença.

**Variáveis possíveis para testar:**
- Criativo (imagem vs. vídeo; estilo A vs. estilo B)
- Copy (gancho diferente, CTA diferente, ângulo de comunicação)
- Público (interesse A vs. interesse B; lookalike 1% vs. 3%)
- Formato (carrossel vs. imagem única)
- Posicionamento dentro do Instagram (Feed vs. Stories vs. Reels)

### 8.2 Protocolo de Teste

1. Definir hipótese: "Acredito que criativo de produto funciona melhor que criativo de lifestyle"
2. Criar ad sets idênticos exceto pela variável testada
3. Usar audiência sem sobreposição entre os ad sets
4. Orçamentar para **ao menos 50 eventos de otimização** por variante
5. Executar por **mínimo 7 dias**
6. Não editar durante o teste (reseta aprendizado e invalida resultado)
7. Documentar o resultado para informar futuras campanhas

### 8.3 O que Documentar Após Cada Teste

- Hipótese testada
- Período
- Orçamento por variante
- Resultado (qual venceu, por qual métrica)
- Aprendizado transferível (o que isso diz sobre o público SB)

---

## Capítulo 9 — Métricas e Análise de Performance

### 9.1 KPIs Principais

| Métrica | O que mede | Meta referência |
|---------|-----------|-----------------|
| **CPM** | Custo por mil impressões | Varia por público; monitorar tendência |
| **CTR** | % de cliques sobre impressões | > 1% feed; > 0,5% stories |
| **CPC** | Custo por clique | Depende do produto e objetivo |
| **CPL** | Custo por lead | Definir meta por campanha |
| **CPA** | Custo por aquisição (compra) | Definir meta por produto |
| **ROAS** | Retorno sobre gasto | Mínimo 2×; meta 3–5× |
| **Frequência** | Quantas vezes mesmo usuário viu | Acima de 3–4×: risco de fadiga |

### 9.2 Sinais de Alerta

| Sinal | Possível causa | Ação |
|-------|----------------|------|
| CTR caindo | Fadiga de criativo | Trocar criativo |
| CPM subindo | Público muito estreito ou leilão acirrado | Ampliar público |
| Frequência alta | Público pequeno ou campanha muito longa | Expandir público ou pausar |
| CPA muito alto | Criativo fraco, landing page ruim ou público errado | Revisar um por vez |
| Anúncio rejeitado | Violação de política | Ver Capítulo 11 |

### 9.3 Ferramentas de Rastreamento

**Facebook Pixel:**
- Código instalado no site da SB
- Rastreia: visitas, eventos (AddToCart, Purchase, ViewContent), cria públicos personalizados
- Necessário para campanhas de Vendas e Retargeting

**Conversions API (CAPI):**
- Rastreamento server-side, complementa o Pixel
- Mais robusto contra bloqueadores de cookies e iOS 14+
- Recomendado para qualquer loja com volume de vendas

**Relatórios:**
- Criar visualizações salvas por conjunto de métricas relevantes
- Acompanhar diariamente para detectar quedas ou picos
- Exportar relatórios semanais para comparação histórica

---

## Capítulo 10 — Nicho Sensível — Comunicação da SB no Meta

### 10.1 Posicionamento Correto

A Shibari Brasil é uma **curadoria de produtos para práticas fetichistas** com foco em qualidade, segurança e arte. Esse posicionamento é legítimo e comunicável no Meta — desde que a abordagem seja adequada.

**O que o Meta aceita para a SB:**
- Comunicação de produto focada em qualidade, material, acabamento
- Lifestyle de prática consciente e segura
- Arte e estética do shibari
- Educação sobre a prática (sem conteúdo explícito)
- Comunidade e identidade

**O que o Meta não aceita:**
- Nudez ou imagens sexualmente sugestivas
- Copy com linguagem sexual explícita
- Claims que associem diretamente o produto a atividade sexual
- Landing pages com conteúdo adulto não restrito

### 10.2 Estrutura de Funil para Nicho Sensível

Para públicos frios, a abordagem direta de produto pode ter mais rejeições. Usar funil:

```
TOPO — Conteúdo de arte/lifestyle (sem produto explícito)
  ↓
MEIO — Conteúdo educativo ou de produto com foco em qualidade
  ↓
FUNDO — Oferta direta para público que já conhece a marca
```

### 10.3 Checklist Anti-Bloqueio

Antes de publicar um anúncio, verificar cada item abaixo. Qualquer "sim" exige revisão antes de publicar.

**Vocabulário:**
- [ ] O copy contém alguma palavra da lista proibida do Capítulo 4.3? (shibari, bondage, BDSM, fetiche, erótico, sexual, prazer, dominação, submissão)
- [ ] O texto visível no criativo (imagem/vídeo) contém alguma dessas palavras?
- [ ] A URL de destino contém termos sensíveis visíveis?

**Criativo:**
- [ ] O criativo contém nudez ou imagem sexualmente explícita ou sugestiva?
- [ ] O criativo mostra poses, gestos ou contextos que o Meta pode classificar como adulto?

**Destino:**
- [ ] A landing page de destino tem conteúdo adulto irrestrito (sem aviso de idade)?
- [ ] O produto anunciado corresponde ao que aparece na landing page?

**Posicionamento:**
- [ ] O ad set está configurado exclusivamente para Instagram? (Feed, Stories, Reels)
- [ ] Advantage+ Placements com Facebook/Audience Network/Messenger desativados?

**Geral:**
- [ ] O anúncio faz claims que não consegue provar (ex: "o melhor do Brasil")?
- [ ] A segmentação respeita as regras de não-discriminação do Meta?

### 10.4 Em Caso de Bloqueio Recorrente

1. Revisar qual elemento específico está causando a rejeição (criativo, copy ou landing page)
2. Ajustar somente o elemento problemático
3. Submeter como anúncio novo (não editar o rejeitado)
4. Solicitar revisão humana via Account Quality se a rejeição parecer erro
5. Documentar o padrão para evitar repetição

---

## Capítulo 11 — Políticas do Meta

### 11.1 O que é Proibido (sem exceção)

- Conteúdo que explore ou ponha em risco crianças
- Discriminação por raça, religião, orientação sexual ou outras características protegidas
- Discurso de ódio ou conteúdo que ataque grupos
- Desinformação verificada por fact-checkers
- Tráfico humano ou exploração
- Fraude ou práticas enganosas
- Nudez e atividade sexual adulta explícita
- Conteúdo violento ou chocante
- Armas, drogas ilícitas, produtos proibidos por lei

### 11.2 Bens e Serviços Restritos (Requerem Cuidado)

| Categoria | Regra |
|-----------|-------|
| Saúde/Bem-estar | Proibido sugerir "tipo de corpo perfeito" ou claims médicos |
| Conteúdo adulto | Nudez proibida; conteúdo de sexualidade requer abordagem sensível |
| Serviços de namoro | Autorização prévia obrigatória |
| Apostas online | Autorização prévia + segmentação 18+ |

### 11.3 Processo de Revisão

- Toda campanha passa por revisão automática de IA antes de ir ao ar
- Revisão típica: até **24 horas**
- O Meta analisa: texto, imagens/vídeos, targeting e landing page de destino
- Anúncios podem ser revisados novamente mesmo após aprovação

**Em caso de rejeição:**
1. Editar o anúncio para adequar à política
2. Submeter como anúncio novo
3. Se a rejeição parecer erro, solicitar revisão humana em `meta.com/accountquality`
4. Em casos específicos, é possível apelar ao Oversight Board

### 11.4 O que o Meta Analisa nos Anúncios

- Componentes do anúncio (imagens, vídeo, texto, headline)
- Informações de segmentação (público-alvo)
- Landing pages e destinos do clique
- Histórico da conta e do domínio

> Manter o histórico da conta saudável é essencial — contas com histórico de violações têm revisões mais rígidas e menor alcance.

---

## Capítulo 12 — Checklist Operacional

### 12.1 Pré-Campanha

- [ ] Objetivo de campanha definido
- [ ] Público mapeado (frio, morno ou quente)
- [ ] Criativo produzido dentro das especificações técnicas do formato
- [ ] Copy revisado — sem palavras da lista proibida do Cap. 4.3, CTA claro
- [ ] Dicionário de substituição aplicado (Cap. 4.3) — nenhum termo do nicho aparece no anúncio
- [ ] Posicionamento configurado: somente Instagram (Feed / Stories / Reels)
- [ ] Landing page verificada: velocidade, coerência com anúncio, CTA na página
- [ ] Pixel instalado e disparando corretamente
- [ ] Orçamento definido (diário ou vitalício)
- [ ] Estratégia de lance escolhida
- [ ] Checklist anti-bloqueio do Capítulo 10.3 feito
- [ ] A/B teste planejado se for testar hipótese

### 12.2 Durante a Campanha

- [ ] Acompanhar KPIs diariamente (CTR, CPA, frequência)
- [ ] Alertar quando frequência > 3 (risco de fadiga)
- [ ] Não editar ad sets em fase de aprendizado sem necessidade
- [ ] Aumentar orçamento gradualmente (máximo 20–30% por vez)
- [ ] Rodar criativos novos antes de fatiga atingir

### 12.3 Pós-Campanha

- [ ] Registrar resultados com métricas principais
- [ ] Documentar aprendizados de A/B testes
- [ ] Comparar com campanha anterior equivalente
- [ ] Atualizar segmentações com base nos dados
- [ ] Arquivar criativos que performaram melhor para referência futura

---

## Glossário Rápido

| Termo | Significado |
|-------|-------------|
| **Ad Set** | Conjunto de anúncios — nível que define público e orçamento |
| **CPA** | Custo por aquisição |
| **CPL** | Custo por lead |
| **CPM** | Custo por mil impressões |
| **CTR** | Taxa de cliques (cliques ÷ impressões) |
| **ROAS** | Retorno sobre gasto em anúncios (receita ÷ gasto) |
| **Pixel** | Código Meta instalado no site para rastrear eventos |
| **CAPI** | Conversions API — rastreamento server-side |
| **Lookalike** | Público semelhante ao público semente |
| **Retargeting** | Anúncios para quem já interagiu com a marca |
| **Fase de aprendizado** | Período em que o algoritmo coleta dados para otimizar |
| **Frequência** | Quantas vezes o mesmo usuário viu o anúncio |
| **Fadiga de criativo** | Queda de performance por exposição repetida ao mesmo criativo |
| **Advantage+** | Ferramentas de automação do Meta por IA |
| **Nicho sensível** | Categoria de produto legal que requer atenção extra nas políticas |
