# Graph Report - sb_marketing_team  (2026-10-28)

## Corpus Check
- 70 files · ~0 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 594 nodes · 1002 edges · 39 communities (27 shown, 12 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 57 edges (avg confidence: 0.76)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Script: gerar artefato da sequência
- Guia da marca e leitura de PDF
- Glossário BDSM
- Fila prioritária e sincronização
- Personas e referências salvas
- Glossário Shibari e Kinbaku
- GA4 no BigQuery
- Time de agentes e produção
- Formatos: vídeo, foto e carrosséis
- Regras da sequência do Instagram
- Meta Ads: nicho sensível
- Peças da fila e arcos de produto
- Artefato e planejador da sequência
- Vícios de IA e autorrevisão
- Mari, pauta e grafo
- Escrita: hook e SEO
- Diretrizes e pipeline
- Status da pauta e alertas
- Leo, estratégia e núcleo de voz
- Risco de alcance e métricas
- Google Ads e funil
- Voz Shibari e rascunhos piloto
- Tom de voz da marca
- Publicação e legenda
- Formatos casuais: bingo e duelo
- Carrossel Livre e hashtags
- Produto e Notion
- Aprendizados da voz
- Algoritmo e estado atual do Leo
- Post para blog
- Post de inspiração e fontes
- Originalidade e decisões de peças
- Meta: pixel e teste de públicos
- Regra de originalidade
- Análise post a post
- Regras de leitura de dados
- Notion MCP
- Help Center Meta
- Community 38

## God Nodes (most connected - your core abstractions)
1. `Glossário BDSM (curadoria)` - 30 edges
2. `Glossário de Shibari e Kinbaku` - 30 edges
3. `diretrizes.md (especificações e rotinas do time)` - 28 edges
4. `Julia (agente-escritor, autora)` - 28 edges
5. `Mari (agente-coordenador)` - 24 edges
6. `main()` - 22 edges
7. `Guia da marca - Shibari Brasil (.md é a verdade)` - 22 edges
8. `hab-produtor-textual (técnica de escrita por canal)` - 22 edges
9. `Leo (agente-estrategista)` - 21 edges
10. `main()` - 20 edges

## Surprising Connections (you probably didn't know these)
- `Quatro layouts: editorial, frase, informativo, minimalista` --references--> `Bia (agente-diretor-de-arte)`  [INFERRED]
  assets/docs/Guia da marca - Shibari Brasil.md → .claude/skills/agente-diretor-de-arte/SKILL.md
- `F13 CTA por palavra-chave` --conceptually_related_to--> `Blacklist de termos que acionam shadowban/NSFW`  [AMBIGUOUS]
  contexto/referencias-posts-salvos-2026-10-09.md → .claude/skills/hab-produtor-textual/MANUAL_ORIGINAL.md
- `F13 CTA por palavra-chave` --conceptually_related_to--> `Método Hook-and-Loop`  [AMBIGUOUS]
  contexto/referencias-posts-salvos-2026-10-09.md → .claude/skills/hab-produtor-textual/MANUAL_ORIGINAL.md
- `Planejador de Sequencia (referencia do Leo)` --conceptually_related_to--> `Leo (agente-estrategista)`  [INFERRED]
  estrategia/Sequência de Conteúdo Instagram.md → .claude/skills/agente-estrategista/SKILL.md
- `Rascunho educativo (legenda de carrossel, fala a marca)` --references--> `Julia (agente-escritor, autora)`  [INFERRED]
  contexto/rascunhos-voz-piloto.md → .claude/skills/agente-escritor/SKILL.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Identidade visual da marca** — conceito_paleta_cores, conceito_tipografia_marca, conceito_wordmark_shibari_brasil, conceito_linha_vertical_scarlet, conceito_grid_ciclo_9_posts [EXTRACTED 0.75]
- **Pipeline de produção orgânica** — agente_leo, agente_julia, agente_ana, agente_bia, agente_mari [EXTRACTED 0.75]
- **Conferencia pauta x perfil: relatorio, briefing para Mari e confirmar postagem** — estrategia_material_produzido_x_postado_2026_10_07_relatorio, estrategia_material_briefing_para_mari_2026_10_07_confirmar_postagem, agente_mari [EXTRACTED 0.95]
- **Pipeline de producao: Leo, Julia, Ana, Bia, Mari** — agente_leo, agente_julia, agente_ana, agente_bia, agente_mari, conceito_fluxo_producao [EXTRACTED 0.95]
- **Reels A, B e C: roteiros de Fase 1 com produto, cashback e arco** — estrategia_material_roteiros_roteiros_reels_fase1_2026_10_19_reel_a, estrategia_material_roteiros_roteiros_reels_fase1_2026_10_19_reel_b, estrategia_material_roteiros_roteiros_reels_fase1_2026_10_19_reel_c, conceito_cashback_10, conceito_arco_de_produto [EXTRACTED 0.95]
- **Produto no feed: ciclo mensal, arcos de produto e cashback** — estrategia_sequ_ncia_de_conte_do_instagram_ciclo_mensal, estrategia_sequ_ncia_de_conte_do_instagram_arcos_produto, estrategia_sequ_ncia_de_conte_do_instagram_cashback [EXTRACTED 1.00]
- **Anatomia do carrossel Desatando Mitos (capa, mitos, finalizacao)** — contexto_formatos_post_desatando_mitos_capa, contexto_formatos_post_desatando_mitos_pagina_mito, contexto_formatos_post_desatando_mitos_finalizacao_fixa [EXTRACTED 1.00]
- **Time de producao organica: Leo, Julia, Ana, Bia e Mari** — agente_leo, claude_julia, agente_ana, agente_bia, agente_mari [EXTRACTED 1.00]
- **Formatos de Instagram que seguem a hab-produtor-textual e o limite de hashtags** — formato_carrossel_livre, formato_post_de_frase, formato_post_desatando_mitos, formato_post_por_tras_do_desejo, conceito_lista_negra_hab_produtor_textual, conceito_limite_5_hashtags [INFERRED 0.85]
- **Pacote de publicacao: midia, legenda e horario** — conceito_pacote_publicacao, conceito_padrao_midia_api, conceito_legenda_txt, conceito_horario_de_pico, agente_mari, agente_bia [INFERRED 0.85]
- **Voz (núcleo) e técnica de escrita** — conceito_nucleo_voz_sb_cerebro, claude_skills_voz_shibari_skill_skill, claude_skills_hab_produtor_textual_skill_habilidade, assets_docs_guia_da_marca_doc [INFERRED 0.85]

## Communities (39 total, 12 thin omitted)

### Community 0 - "Script: gerar artefato da sequência"
Cohesion: 0.05
Nodes (50): hash_normalizado(), main(), agendamentos(), aplicar_agendamentos(), capa_do_agendado(), capa_em_cache(), chave_tipo(), _dias() (+42 more)

### Community 1 - "Guia da marca e leitura de PDF"
Cohesion: 0.05
Nodes (48): Comandos de uso (Ver pauta, Produzir, Revisar, Tráfego...), diretrizes.md (especificações e rotinas do time), Acesso ao Meta Ads por MCP ainda não liberado para a conta SB, Protocolo de registro de memória, Protocolo de novo formato de conteúdo, Fluxo típico de uma sessão, Pasta de conteúdos no Drive (03_CONTEUDO), Maximo 5 hashtags ao final da legenda (+40 more)

### Community 2 - "Glossário BDSM"
Cohesion: 0.06
Nodes (44): Cores oficiais (Carbon, Deep Plum, Scarlet, Skin Nude, Warm Light, Smoke Taupe), Guia da marca - Shibari Brasil (.md é a verdade), Essência, propósito, missão e visão, Estrutura de texto Instagram, produto e e-mail, Fotografia de produto e de prática, direção fotográfica, Hierarquia e proporção de cores, Quatro layouts: editorial, frase, informativo, minimalista, O que a marca não é (sex shop, apelativa, catálogo genérico) (+36 more)

### Community 3 - "Fila prioritária e sincronização"
Cohesion: 0.07
Nodes (37): Capa (tema + 3 faixas Skin Nude), Direcao visual (paleta, balao Deep Plum, negrito manual), Estrutura fixa de 7 paginas (capa, 5 mitos, finalizacao), Pagina de finalizacao fixa (CTA), Formato Post Desatando Mitos, hab-produtor-textual (Capitulos 1 e 2), Layout novo Desatando Mitos (out/2026), Mitos da capa (decisao do Hugo apos os 5 mitos) (+29 more)

### Community 4 - "Personas e referências salvas"
Cohesion: 0.11
Nodes (29): Glossário BDSM (curadoria), Amaurofilia (privação visual), Asfixia sexual (hipoxifilia), Bondage, Cena (play, sessão), Consentimento, Dominante (Dom/Domme), D/s: Dominação e Submissão (+21 more)

### Community 5 - "Glossário Shibari e Kinbaku"
Cohesion: 0.11
Nodes (29): Glossário de Shibari e Kinbaku, Akechi Denki, Asanawa (corda de fibra natural), Daruma Shibari, Deshi, Ebi Shibari (camarão), Gote (mãos atrás), Hishi Shibari (diamantes) (+21 more)

### Community 6 - "GA4 no BigQuery"
Cohesion: 0.10
Nodes (20): Scripts com caminhos fixos da maquina do Hugo, Histórico de conteúdos e briefings.md congelados desde 27/10/2026, Protocolo de pauta: quem move cada status, fila-prioritaria.md (como o time acompanha a sequência), Fluxo de mudança: editar JSON, republicar artefato, sincronizar, Hook SessionStart em .claude/settings.json, Ponte com a skill de Instagram (no ar e agendado), Regras da fila para Mari e demais agentes (+12 more)

### Community 7 - "Time de agentes e produção"
Cohesion: 0.10
Nodes (27): Público: iniciantes, praticantes, comunidade BDSM, LGBTQIA+, Segmentação: frio, morno, retargeting, lookalike, Aftercare, Frase autossuficiente: max 15 palavras, minusculas, sem ponto final, Template Canva Post Frase Efeito (EAHMvTf7Hkk), Playfair 103pt, sem linha Scarlet, Perfis de público, Dor comum: sex shops tradicionais (vergonha, plástico, heteronormatividade), Nota: skills trazem resumos embutidos das personas (+19 more)

### Community 8 - "Formatos: vídeo, foto e carrosséis"
Cohesion: 0.12
Nodes (24): Discrepâncias com a interface do GA4, GA4 no BigQuery: resumo técnico, Eventos padrão do GA4, Tabela events_* (uma linha por evento), Export forward-only (sem backfill), Funil de e-commerce (view_item a purchase), Tabelas intraday e campos ausentes, Atualização por até 72 horas (+16 more)

### Community 9 - "Regras da sequência do Instagram"
Cohesion: 0.15
Nodes (17): Ferramentas Advantage+, Ângulos de comunicação seguros, Procedimento em caso de bloqueio recorrente, Checklist anti-bloqueio, Dicionário de substituição para anúncios, Estrutura campanha / conjunto / anúncio, Fase de aprendizado (7 dias, 50 eventos), Especificações de Feed, Stories, Reels e Carrossel (+9 more)

### Community 10 - "Meta Ads: nicho sensível"
Cohesion: 0.14
Nodes (16): Artefato visual da sequencia (abas e molduras de agendado), Ciclo mensal: 12 posts, minimo 3 de produto, Modo Planejador de Sequencia, Prazos de producao por tipo, Regras duras de sequenciamento (cor, Scarlet, claro/escuro, slots), Extras casuais em ritmo leve (1 a cada 2 semanas), Aba Grade do feed (capas reais, slots planejados, agendados), Aba Producao e captacao (fila, kanban, ordens, roteiros, backlog) (+8 more)

### Community 11 - "Peças da fila e arcos de produto"
Cohesion: 0.12
Nodes (16): Engenharia do hook (erro oculto, contraste prático), SEO semântico, LSI e E-E-A-T narrativo, Escrita para Instagram: hook, checklist, Hook-and-Loop, SEO técnico (URL, meta 120-160, alt, links internos), Conclusões dramáticas vazias ("isso muda tudo"), hab-produtor-textual (técnica de escrita por canal), Base anexa MANUAL_ORIGINAL.md, Sem emoji, parágrafo máximo de 2 linhas no mobile (+8 more)

### Community 12 - "Artefato e planejador da sequência"
Cohesion: 0.17
Nodes (15): Conectores de redação escolar e "não apenas... mas também", E-mail: assunto antispam e CTA natural, Iscas de engajamento (comente, marque, link da bio), Fact-checking e validação de alucinações, Falsa oposição "não é sobre X, é sobre Y", Redundância e fluff, Atributos pessoais e foco na dor (políticas de anúncios), Isocronismo e adjetivação simétrica (+7 more)

### Community 13 - "Vícios de IA e autorrevisão"
Cohesion: 0.24
Nodes (13): Ana (agente-revisor), Bia (agente-diretor-de-arte), Julia (agente-escritor, autora), Tipografia e wordmark (Playfair, Montserrat, Cormorant), Revisao invocada da Ana (subagente com contexto limpo), Recursos 2025-2026 (Trial Reels, hashtags max 5, SEO), Roteiro de Reel (hook, 3 beats, payoff, Trial Reel), Veredicto APROVADO ou REQUER AJUSTES (+5 more)

### Community 14 - "Mari, pauta e grafo"
Cohesion: 0.15
Nodes (14): Comando Confirmar postagem, Elegibilidade para recomendacao e Status da conta, Lista negra empirica de termos sensiveis, Coleta pelo navegador (so o que a API nao entrega), Hierarquia de metricas (distribuicao a negocio), Razoes normalizadas por alcance (taxa de envio, salvamento), O que o Leo nao faz, Roteiro de diagnostico de queda de alcance (+6 more)

### Community 15 - "Escrita: hook e SEO"
Cohesion: 0.20
Nodes (12): Limites: não decide estrutura de formato, preço nem fato de produto, Ordem de leitura: voz.md, vocabulario, identidade, tom, ajustes, sb_cerebro como pasta irmã; se faltar, parar e avisar o Hugo, Precedência: o núcleo vence Guia da Marca e resumos de tom, voz-shibari (skill fina que aponta para o núcleo), Teste de 4 perguntas da voz, Rascunho de anúncio do Kit Shibari Iniciante, Aviso: não dizer "sem fiapos" nem focar em bondage (P76 e P77) (+4 more)

### Community 16 - "Diretrizes e pipeline"
Cohesion: 0.20
Nodes (9): Mari (agente-coordenador), Tabela de roteamento da Mari, Rede de seguranca do grafo (graphify_defasado.py), Fila prioritaria do Instagram (do Leo), Extrator Instagram + Meta Ads no BigQuery e dbt (no ar desde 07/out), Linha de base da conta @shibari.brasil (seguidores, views, melhor peca), Briefing para a Mari: confirmar postagem de 8 pecas ja no ar e corrigir data da C-076, Cruzamento por similaridade de legenda (>=88% no ar, 62 a 88% provavel) (+1 more)

### Community 17 - "Status da pauta e alertas"
Cohesion: 0.18
Nodes (11): Como falar de desejo: sugere, não explicita, Como falar de produto (o que é, para que serve, como se encaixa), Como falar de segurança: direta, leve e com fonte, Frase falável em voz alta, O que evitar sempre (apelo, urgência, clichê, sexualização), Personalidade revisada: didática, leve, bem-humorada, não arrogante, Quem fala: voz do Hugo como praticante, Tom de voz e como a marca escreve (+3 more)

### Community 18 - "Leo, estratégia e núcleo de voz"
Cohesion: 0.18
Nodes (11): Elo fraco: do Instagram ao pedido (UTM, cupom), Fechar o elo post para venda, Skills por plataforma (hab-meta-ads, hab-google-ads), Estrutura de conta e framework ABC, Estrategia full-funnel da Shibari Brasil em fases, Smart Bidding, orcamento e fase de aprendizado, Palavras-chave, correspondencia e negativas, Performance Max (Search Themes, New Customer Value Mode) (+3 more)

### Community 19 - "Risco de alcance e métricas"
Cohesion: 0.22
Nodes (9): Aba Formatos e extras (composicao por mes, assuntos a decidir), Arco de produto (3 a 4 pecas que conversam), Cashback de 10% em pecas com produto, Nova orientacao de Instagram: sequencia manda na producao (11 decisoes do Hugo), Rotinas novas: fila prioritaria, roteiro de video, captacao, confirmar postagem, planejado x postado, Reel A: Primeiros minutos com a corda (Kit Iniciante, posta 26/10), Reel B: O que a gente confere antes de amarrar (tesoura, posta 20/11), Reel C: Tres passos para guardar a corda (oleo e pano, posta 09/11) (+1 more)

### Community 20 - "Google Ads e funil"
Cohesion: 0.20
Nodes (9): Gui (agente-trafego), .claude/specs/diretrizes.md, SB Marketing Team (projeto), O que o Instagram nao permite (link em legenda, anuncio adulto), Armazenamento de campanhas em anuncios/[plataforma]/[slug], Protocolo de armazenamento de anúncios (anuncios/plataforma/slug), Time de Agentes, Dominio shibaribrasil.com.br bloqueado no pixel pela Meta (+1 more)

### Community 21 - "Voz Shibari e rascunhos piloto"
Cohesion: 0.27
Nodes (9): Leo (agente-estrategista), Hugo Barcellos (responsavel e operador), Filtro antes de registrar uma ideia, Regra de equilibrio Shibari/Kinbaku e BDSM, Modelo de proposta de slot (saida principal do Leo), Dependencias fora do marketing (BigQuery, API Meta, Notion), Ancora obrigatoria no nucleo, Fluxo propor, Hugo aprova, Julia, Ana, Bia, Mari, resultado volta (+1 more)

### Community 22 - "Tom de voz da marca"
Cohesion: 0.20
Nodes (10): Conteudos produzidos ficam no Drive (03_CONTEUDO), Julia (agente-escritor), Voz da marca (sb_cerebro / skill voz-shibari), Checklist de entrega da Julia, Backlog — Leo (territorios), Gui — Trafego Pago (paralelo), Inspiracao de Amarracao — Backlog, Pauta Editorial — Shibari Brasil (+2 more)

### Community 23 - "Publicação e legenda"
Cohesion: 0.22
Nodes (9): Nota: exemplos do guia mostram ordem, não redação final, Padrões de edição do Hugo moram em ajustes-recorrentes.md, Aprendizados da prática (correções reais), Evitar eco de palavra no mesmo período, Página de respiro precisa de referente, Seção 0: voz da marca vem do núcleo, Critérios de sucesso por execução, Fidelidade comercial: só produtos do Catálogo (Notion) (+1 more)

### Community 24 - "Formatos casuais: bingo e duelo"
Cohesion: 0.25
Nodes (9): Pendencias abertas (fila v11, backlog, publicador por API), Protocolo de sessao do Planejador com o Hugo, Decisao de 22/10: horario explicito e canal de agendamento, Checklist de formato da revisao, Hashtags proibidas (#bdsm, #impactplay) e teto de 5, Horario de pico (dos dados, nao do Hugo), legenda.txt (so o texto publicavel), Pacote de publicacao (Fase 1 mLabs, Fase 2 API) (+1 more)

### Community 25 - "Carrossel Livre e hashtags"
Cohesion: 0.29
Nodes (6): Introdução invertida (search intent), Estrutura obrigatória do artigo de blog (H1, H2, 1.000+ palavras), Blog: imagem principal é foto real 1024x630, sem IA, Campos SEO do blog: titulo SEO 65 car., meta descricao 140 car., resumo 300 car., Bloco de CTA fixo e secao de bibliografia ao final do post, Formato Post para Blog

### Community 26 - "Produto e Notion"
Cohesion: 0.40
Nodes (6): Algoritmo por superficie (Reels, Feed, Stories, Explorar), Protocolo de atualizacao da pesquisa (45 dias), Achados de resultado (carrossel lidera, post do Hugo sem IA), Estado atual do Leo (foto de 27/10/2026), Protocolo de inicio de sessao do Leo, Rotulos [OFICIAL] [MEDIDO] [ESTIMATIVA]

## Ambiguous Edges - Review These
- `Vocabulário proibido em anúncios (shibari, bondage, BDSM, fetiche...)` → `Núcleo da voz (sb_cerebro)`  [AMBIGUOUS]
  .claude/skills/hab-meta-ads/SKILL.md · relation: conceptually_related_to
- `Blacklist de termos que acionam shadowban/NSFW` → `F13 CTA por palavra-chave`  [AMBIGUOUS]
  contexto/referencias-posts-salvos-2026-10-09.md · relation: conceptually_related_to
- `Método Hook-and-Loop` → `F13 CTA por palavra-chave`  [AMBIGUOUS]
  contexto/referencias-posts-salvos-2026-10-09.md · relation: conceptually_related_to
- `Lista negra de vocabulário de IA` → `F5 Série "não é X, é Y"`  [AMBIGUOUS]
  contexto/referencias-posts-salvos-2026-10-09.md · relation: conceptually_related_to
- `Google Ads no BigQuery: resumo técnico` → `Gui (agente-trafego)`  [AMBIGUOUS]
  assets/docs/google_ads_bigquery_resumo.md · relation: references

## Knowledge Gaps
- **161 isolated node(s):** `Estrutura de texto Instagram, produto e e-mail`, `Fotografia de produto e de prática, direção fotográfica`, `O que a marca não é (sex shop, apelativa, catálogo genérico)`, `Uso por mídia: Instagram, site, e-mail, físico`, `Todo heading termina com marca de página (p. N)` (+156 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 206 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **12 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Mari (agente-coordenador)` connect `Diretrizes e pipeline` to `Guia da marca e leitura de PDF`, `Fila prioritária e sincronização`, `GA4 no BigQuery`, `Time de agentes e produção`, `Vícios de IA e autorrevisão`, `Mari, pauta e grafo`, `Google Ads e funil`, `Voz Shibari e rascunhos piloto`, `Tom de voz da marca`, `Formatos casuais: bingo e duelo`?**
  _High betweenness centrality (0.326) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Julia (agente-escritor, autora)` (e.g. with `Glossário de Shibari e Kinbaku` and `Rascunho educativo (legenda de carrossel, fala a marca)`) actually correct?**
  _`Julia (agente-escritor, autora)` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Estrutura de texto Instagram, produto e e-mail`, `Fotografia de produto e de prática, direção fotográfica`, `O que a marca não é (sex shop, apelativa, catálogo genérico)` to the rest of the system?**
  _161 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Script: gerar artefato da sequência` be split into smaller, more focused modules?**
  _Cohesion score 0.05212716222533895 - nodes in this community are weakly interconnected._
- **Why does `Julia (agente-escritor, autora)` connect `Vícios de IA e autorrevisão` to `Guia da marca e leitura de PDF`, `Glossário Shibari e Kinbaku`, `Time de agentes e produção`, `Meta Ads: nicho sensível`, `Peças da fila e arcos de produto`, `Mari, pauta e grafo`, `Escrita: hook e SEO`, `Diretrizes e pipeline`, `Risco de alcance e métricas`, `Voz Shibari e rascunhos piloto`, `Formatos casuais: bingo e duelo`, `Carrossel Livre e hashtags`?**
  _High betweenness centrality (0.278) - this node is a cross-community bridge._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `Vocabulário proibido em anúncios (shibari, bondage, BDSM, fetiche...)` and `Núcleo da voz (sb_cerebro)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Blacklist de termos que acionam shadowban/NSFW` and `F13 CTA por palavra-chave`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._