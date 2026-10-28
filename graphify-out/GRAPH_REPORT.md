# Graph Report - sb_marketing_team  (2026-10-28)

## Corpus Check
- 70 files · ~118,318 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 4 file(s) not represented in the graph (top: (none) 4)

## Summary
- 604 nodes · 1103 edges · 38 communities (32 shown, 6 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 64 edges (avg confidence: 0.75)
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

## God Nodes (most connected - your core abstractions)
1. `Julia (agente-escritor, autora)` - 32 edges
2. `Glossário BDSM (curadoria)` - 30 edges
3. `Glossário de Shibari e Kinbaku` - 30 edges
4. `diretrizes.md (especificações e rotinas do time)` - 28 edges
5. `Mari (agente-coordenador)` - 27 edges
6. `Leo (agente-estrategista)` - 23 edges
7. `main()` - 22 edges
8. `hab-produtor-textual (técnica de escrita por canal)` - 22 edges
9. `Guia da marca - Shibari Brasil (.md é a verdade)` - 22 edges
10. `main()` - 20 edges

## Surprising Connections (you probably didn't know these)
- `Quatro layouts: editorial, frase, informativo, minimalista` --references--> `Bia (agente-diretor-de-arte)`  [INFERRED]
  assets/docs/Guia da marca - Shibari Brasil.md → .claude/skills/agente-diretor-de-arte/SKILL.md
- `Rascunho educativo (legenda de carrossel, fala a marca)` --references--> `Julia (agente-escritor, autora)`  [INFERRED]
  contexto/rascunhos-voz-piloto.md → .claude/skills/agente-escritor/SKILL.md
- `Google Ads no BigQuery: resumo técnico` --references--> `Gui (agente-trafego)`  [AMBIGUOUS]
  assets/docs/google_ads_bigquery_resumo.md → .claude/skills/agente-trafego/SKILL.md
- `O que evitar sempre (apelo, urgência, clichê, sexualização)` --semantically_similar_to--> `Lista negra de vocabulário de IA`  [INFERRED] [semantically similar]
  assets/docs/Guia da marca - Shibari Brasil.md → .claude/skills/hab-produtor-textual/MANUAL_ORIGINAL.md
- `F5 Série "não é X, é Y"` --conceptually_related_to--> `Lista negra de vocabulário de IA`  [AMBIGUOUS]
  contexto/referencias-posts-salvos-2026-10-09.md → .claude/skills/hab-produtor-textual/MANUAL_ORIGINAL.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Pipeline de producao: Leo, Julia, Ana, Bia, Mari** — agente_leo, agente_julia, agente_ana, agente_bia, agente_mari, conceito_fluxo_producao [EXTRACTED 0.95]
- **Voz unica do nucleo aplicada por Leo, Julia, Ana e Gui** — conceito_voz_shibari, conceito_nucleo_sb_cerebro, agente_leo, agente_julia, agente_ana, agente_gui [EXTRACTED 0.95]
- **Pacote de publicacao: midia, legenda e horario** — conceito_pacote_publicacao, conceito_padrao_midia_api, conceito_legenda_txt, conceito_horario_de_pico, agente_mari, agente_bia [INFERRED 0.85]
- **Pipeline de produção orgânica** — agente_leo, agente_julia, agente_ana, agente_bia, agente_mari [EXTRACTED 0.75]
- **Voz (núcleo) e técnica de escrita** — conceito_nucleo_voz_sb_cerebro, claude_skills_voz_shibari_skill_skill, claude_skills_hab_produtor_textual_skill_habilidade, assets_docs_guia_da_marca_doc [INFERRED 0.85]
- **Identidade visual da marca** — conceito_paleta_cores, conceito_tipografia_marca, conceito_wordmark_shibari_brasil, conceito_linha_vertical_scarlet, conceito_grid_ciclo_9_posts [EXTRACTED 0.75]
- **Formatos de Instagram que seguem a hab-produtor-textual e o limite de hashtags** — formato_carrossel_livre, formato_post_de_frase, formato_post_desatando_mitos, formato_post_por_tras_do_desejo, conceito_lista_negra_hab_produtor_textual, conceito_limite_5_hashtags [INFERRED 0.85]
- **Reels A, B e C: roteiros de Fase 1 com produto, cashback e arco** — estrategia_material_roteiros_roteiros_reels_fase1_2026_10_19_reel_a, estrategia_material_roteiros_roteiros_reels_fase1_2026_10_19_reel_b, estrategia_material_roteiros_roteiros_reels_fase1_2026_10_19_reel_c, conceito_cashback_10, conceito_arco_de_produto [EXTRACTED 0.95]
- **Conferencia pauta x perfil: relatorio, briefing para Mari e confirmar postagem** — estrategia_material_produzido_x_postado_2026_10_07_relatorio, estrategia_material_briefing_para_mari_2026_10_07_confirmar_postagem, agente_mari, agente_hugo [EXTRACTED 0.95]

## Communities (38 total, 6 thin omitted)

### Community 0 - "Script: gerar artefato da sequência"
Cohesion: 0.06
Nodes (43): agendamentos(), aplicar_agendamentos(), capa_do_agendado(), capa_em_cache(), chave_tipo(), _dias(), estatistica_por_formato(), historico() (+35 more)

### Community 1 - "Guia da marca e leitura de PDF"
Cohesion: 0.06
Nodes (44): Cores oficiais (Carbon, Deep Plum, Scarlet, Skin Nude, Warm Light, Smoke Taupe), Guia da marca - Shibari Brasil (.md é a verdade), Essência, propósito, missão e visão, Estrutura de texto Instagram, produto e e-mail, Fotografia de produto e de prática, direção fotográfica, Hierarquia e proporção de cores, Quatro layouts: editorial, frase, informativo, minimalista, O que a marca não é (sex shop, apelativa, catálogo genérico) (+36 more)

### Community 2 - "Glossário BDSM"
Cohesion: 0.08
Nodes (39): Glossário BDSM (curadoria), Aftercare, Amaurofilia (privação visual), Asfixia sexual (hipoxifilia), Bondage, Cena (play, sessão), Consentimento, Dominante (Dom/Domme) (+31 more)

### Community 3 - "Fila prioritária e sincronização"
Cohesion: 0.09
Nodes (21): hash_normalizado(), main(), fila-prioritaria.md (como o time acompanha a sequência), Fluxo de mudança: editar JSON, republicar artefato, sincronizar, Hook SessionStart em .claude/settings.json, Ponte com a skill de Instagram (no ar e agendado), Troca de peça na fila e "substituição não registrada", Fila prioritária do Instagram (+13 more)

### Community 4 - "Personas e referências salvas"
Cohesion: 0.09
Nodes (31): Público: iniciantes, praticantes, comunidade BDSM, LGBTQIA+, Segmentação: frio, morno, retargeting, lookalike, Frase autossuficiente: max 15 palavras, minusculas, sem ponto final, Template Canva Post Frase Efeito (EAHMvTf7Hkk), Playfair 103pt, sem linha Scarlet, Dor comum: sex shops tradicionais (vergonha, plástico, heteronormatividade), Nota: skills trazem resumos embutidos das personas, Perfis de Instagram de referencia (kink_collective, dr.k1nkaware, dominantdiscourse e outros), Legenda de ação: A aproveitar, B adaptar, C só formato, X não usar (+23 more)

### Community 5 - "Glossário Shibari e Kinbaku"
Cohesion: 0.10
Nodes (31): Glossário de Shibari e Kinbaku, Akechi Denki, Asanawa (corda de fibra natural), Daruma Shibari, Deshi, Ebi Shibari (camarão), Gote (mãos atrás), Hishi Shibari (diamantes) (+23 more)

### Community 6 - "GA4 no BigQuery"
Cohesion: 0.12
Nodes (24): Discrepâncias com a interface do GA4, GA4 no BigQuery: resumo técnico, Eventos padrão do GA4, Tabela events_* (uma linha por evento), Export forward-only (sem backfill), Funil de e-commerce (view_item a purchase), Tabelas intraday e campos ausentes, Atualização por até 72 horas (+16 more)

### Community 7 - "Time de agentes e produção"
Cohesion: 0.17
Nodes (20): Ana (agente-revisor), Bia (agente-diretor-de-arte), Gui (agente-trafego), Julia (agente-escritor, autora), Tipografia e wordmark (Playfair, Montserrat, Cormorant), Revisao invocada da Ana (subagente com contexto limpo), O que o Instagram nao permite (link em legenda, anuncio adulto), Recursos 2025-2026 (Trial Reels, hashtags max 5, SEO) (+12 more)

### Community 8 - "Formatos: vídeo, foto e carrosséis"
Cohesion: 0.12
Nodes (18): Protocolo de novo formato de conteúdo, Índice de formatos de conteúdo (formatos-conteudo.md), Modelo de arquivo de formato (objetivo, estrutura, direção visual, checklist), Formatos 6 e 7 (descrição de produto) saíram do marketing, Fluxo do Instagram Video: tecnica, video, Julia legenda, Ana revisa, Aguardando Publicacao, Fluxo da foto: foto movida para a pasta, Julia legenda, Ana revisa, sem etapa de design, Legenda em tres passos: o que e, como se comporta, onde faz sentido, Carrossel de 7 paginas: capa, 5 mitos, finalizacao fixa (+10 more)

### Community 9 - "Regras da sequência do Instagram"
Cohesion: 0.13
Nodes (18): Hugo Barcellos (responsavel e operador), Aba Formatos e extras (composicao por mes, assuntos a decidir), Regras da fila para Mari e demais agentes, Arco de produto (3 a 4 pecas que conversam), Assuntos proximos avaliados caso a caso com leitura em 72 h, Black Friday 27/11 (conversa separada, 4 slots reservados), Cashback de 10% em pecas com produto, Regra de cor de fundo: sem repetir em posts seguidos, Scarlet max 1 a cada 9, alternar claro e escuro (+10 more)

### Community 10 - "Meta Ads: nicho sensível"
Cohesion: 0.13
Nodes (19): Ferramentas Advantage+, Ângulos de comunicação seguros, Procedimento em caso de bloqueio recorrente, Checklist anti-bloqueio, Dicionário de substituição para anúncios, Estrutura campanha / conjunto / anúncio, Fase de aprendizado (7 dias, 50 eventos), Especificações de Feed, Stories, Reels e Carrossel (+11 more)

### Community 11 - "Peças da fila e arcos de produto"
Cohesion: 0.27
Nodes (16): Arcos de produto (1 kit iniciante, 2 segurança, 3 cuidado e curadoria), Slots reservados da Black Friday (23, 25, 27, 30/11), Bloco Fila prioritária (gerado por script, não editar à mão), C-003: curadoria de cordas da Shibari Brasil (Post de produto, 13/11), C-026: velas que podem e velas que nunca, guia de segurança do wax play (11/11), C-046: o que o fetiche revela sobre você (Carrossel livre, 28/10), C-106: 5 mitos sobre submissão (Desatando mitos, 02/11), C-107: o limite de alguém não é um desafio (Post de frase, 04/11) (+8 more)

### Community 12 - "Artefato e planejador da sequência"
Cohesion: 0.15
Nodes (15): Artefato visual da sequencia (abas e molduras de agendado), Ciclo mensal: 12 posts, minimo 3 de produto, Modo Planejador de Sequencia, Prazos de producao por tipo, Regras duras de sequenciamento (cor, Scarlet, claro/escuro, slots), Extras casuais em ritmo leve (1 a cada 2 semanas), Aba Grade do feed (capas reais, slots planejados, agendados), Aba Producao e captacao (fila, kanban, ordens, roteiros, backlog) (+7 more)

### Community 13 - "Vícios de IA e autorrevisão"
Cohesion: 0.17
Nodes (15): Conectores de redação escolar e "não apenas... mas também", E-mail: assunto antispam e CTA natural, Iscas de engajamento (comente, marque, link da bio), Fact-checking e validação de alucinações, Falsa oposição "não é sobre X, é sobre Y", Redundância e fluff, Atributos pessoais e foco na dor (políticas de anúncios), Isocronismo e adjetivação simétrica (+7 more)

### Community 14 - "Mari, pauta e grafo"
Cohesion: 0.18
Nodes (13): Mari (agente-coordenador), Gatilho /graphify (skill graphify), Tabela de roteamento da Mari, Rede de seguranca do grafo (graphify_defasado.py), Pasta de conteudos no Drive (03_CONTEUDO), Fluxo propor, Hugo aprova, Julia, Ana, Bia, Mari, resultado volta, Grafo graphify sempre em dia (regra de 28/10/2026), contexto/pauta.md (unico registro de status) (+5 more)

### Community 15 - "Escrita: hook e SEO"
Cohesion: 0.14
Nodes (14): Engenharia do hook (erro oculto, contraste prático), SEO semântico, LSI e E-E-A-T narrativo, Escrita para Instagram: hook, checklist, Hook-and-Loop, SEO técnico (URL, meta 120-160, alt, links internos), Conclusões dramáticas vazias ("isso muda tudo"), hab-produtor-textual (técnica de escrita por canal), Base anexa MANUAL_ORIGINAL.md, Sem emoji, parágrafo máximo de 2 linhas no mobile (+6 more)

### Community 16 - "Diretrizes e pipeline"
Cohesion: 0.18
Nodes (14): Comandos de uso (Ver pauta, Produzir, Revisar, Tráfego...), diretrizes.md (especificações e rotinas do time), Fluxo completo puxado pela fila, Histórico de conteúdos e briefings.md congelados desde 27/10/2026, Acesso ao Meta Ads por MCP ainda não liberado para a conta SB, Protocolo de registro de memória, Protocolo de pauta: quem move cada status, Fluxo típico de uma sessão (+6 more)

### Community 17 - "Status da pauta e alertas"
Cohesion: 0.23
Nodes (13): Alertas: entrega atrasada, troca não registrada, post no ar, C-086: sinais de quem pratica com responsabilidade (Carrossel livre, publicada 21/10), pauta.md (pauta editorial), Extra casual 1: Time doce x Time travessura (spanking, Halloween), Ordem de leitura: fila, em andamento, prontos, publicados, backlog, Status Aguardando Revisão (Hugo), Status Backlog (Leo), Status Design em Produção (Bia) (+5 more)

### Community 18 - "Leo, estratégia e núcleo de voz"
Cohesion: 0.21
Nodes (11): Leo (agente-estrategista), Scripts de scripts/ com caminhos fixos da maquina do Hugo, Alimentar a biblioteca (nota destilada em primeira pessoa), Filtro antes de registrar uma ideia, Regra de equilibrio Shibari/Kinbaku e BDSM, Modelo de proposta de slot (saida principal do Leo), Dependencias fora do marketing (BigQuery, API Meta, Notion), Ancora obrigatoria no nucleo (+3 more)

### Community 19 - "Risco de alcance e métricas"
Cohesion: 0.18
Nodes (12): Elegibilidade para recomendacao e Status da conta, Lista negra empirica de termos sensiveis, Coleta pelo navegador (so o que a API nao entrega), Hierarquia de metricas (distribuicao a negocio), Razoes normalizadas por alcance (taxa de envio, salvamento), O que o Leo nao faz, Roteiro de diagnostico de queda de alcance, Tabela de riscos (produto adulto, metafora sexual, imagem de corpo, bio) (+4 more)

### Community 20 - "Google Ads e funil"
Cohesion: 0.18
Nodes (11): Elo fraco: do Instagram ao pedido (UTM, cupom), Fechar o elo post para venda, Skills por plataforma (hab-meta-ads, hab-google-ads), Estrutura de conta e framework ABC, Estrategia full-funnel da Shibari Brasil em fases, Smart Bidding, orcamento e fase de aprendizado, Palavras-chave, correspondencia e negativas, Performance Max (Search Themes, New Customer Value Mode) (+3 more)

### Community 21 - "Voz Shibari e rascunhos piloto"
Cohesion: 0.22
Nodes (11): Ordem de leitura: voz.md, vocabulario, identidade, tom, ajustes, sb_cerebro como pasta irmã; se faltar, parar e avisar o Hugo, Precedência: o núcleo vence Guia da Marca e resumos de tom, voz-shibari (skill fina que aponta para o núcleo), Teste de 4 perguntas da voz, Rascunho de anúncio do Kit Shibari Iniciante, Aviso: não dizer "sem fiapos" nem focar em bondage (P76 e P77), Rascunhos do piloto da voz (27/10/2026) (+3 more)

### Community 22 - "Tom de voz da marca"
Cohesion: 0.20
Nodes (10): Como falar de desejo: sugere, não explicita, Como falar de segurança: direta, leve e com fonte, Frase falável em voz alta, O que evitar sempre (apelo, urgência, clichê, sexualização), Personalidade revisada: didática, leve, bem-humorada, não arrogante, Quem fala: voz do Hugo como praticante, Tom de voz e como a marca escreve, Vocabulário clichê de IA (superlativos, metáforas, verbos, jargão) (+2 more)

### Community 23 - "Publicação e legenda"
Cohesion: 0.22
Nodes (10): Comando Confirmar postagem, Protocolo de sessao do Planejador com o Hugo, Decisao de 22/10: horario explicito e canal de agendamento, Rotina produzido x postado, Checklist de formato da revisao, Hashtags proibidas (#bdsm, #impactplay) e teto de 5, Horario de pico (dos dados, nao do Hugo), legenda.txt (so o texto publicavel) (+2 more)

### Community 24 - "Formatos casuais: bingo e duelo"
Cohesion: 0.22
Nodes (7): Formatos casuais em teste (extras de identificacao e viralizacao), Cartela 3x3 com 9 casas e casa central livre, Visual do bingo: Carbon Black, Scarlet Pulse, circulos a mao, template Canva Bingo, Dois times com 4 itens paralelos por coluna e conector ou, Template Canva Post Duelo - Modelo (layout aprovado 23/10/2026), Post de Bingo (Instagram), Post de Duelo (Instagram)

### Community 25 - "Carrossel Livre e hashtags"
Cohesion: 0.22
Nodes (8): Maximo 5 hashtags ao final da legenda, Lista negra e regras da hab-produtor-textual, Capa com frase dominante e frase de contraste, Estrutura fixa de 8 slides (capa, 5 conteudo, respiro, finalizacao), Template Canva Post Carrossel Livre (EAHM8m_nVF4), Território: feminismo e BDSM, C-062: ser submissa me faz menos feminista? (16/11), Formato Carrossel Livre

### Community 26 - "Produto e Notion"
Cohesion: 0.29
Nodes (7): Como falar de produto (o que é, para que serve, como se encaixa), Limites: não decide estrutura de formato, preço nem fato de produto, Critérios de sucesso por execução, Fidelidade comercial: só produtos do Catálogo (Notion), Catalogo - Produtos (Notion), Marketing nao gerencia produto, Acesso ao Notion por MCP somente leitura

### Community 27 - "Aprendizados da voz"
Cohesion: 0.29
Nodes (7): Nota: exemplos do guia mostram ordem, não redação final, Padrões de edição do Hugo moram em ajustes-recorrentes.md, Aprendizados da prática (correções reais), Evitar eco de palavra no mesmo período, Página de respiro precisa de referente, Seção 0: voz da marca vem do núcleo, Núcleo da voz (sb_cerebro)

### Community 28 - "Algoritmo e estado atual do Leo"
Cohesion: 0.33
Nodes (7): Algoritmo por superficie (Reels, Feed, Stories, Explorar), Protocolo de atualizacao da pesquisa (45 dias), Achados de resultado (carrossel lidera, post do Hugo sem IA), Estado atual do Leo (foto de 27/10/2026), Pendencias abertas (fila v11, backlog, publicador por API), Protocolo de inicio de sessao do Leo, Rotulos [OFICIAL] [MEDIDO] [ESTIMATIVA]

### Community 29 - "Post para blog"
Cohesion: 0.29
Nodes (6): Introdução invertida (search intent), Estrutura obrigatória do artigo de blog (H1, H2, 1.000+ palavras), Blog: imagem principal é foto real 1024x630, sem IA, Campos SEO do blog: titulo SEO 65 car., meta descricao 140 car., resumo 300 car., Bloco de CTA fixo e secao de bibliografia ao final do post, Formato Post para Blog

### Community 30 - "Post de inspiração e fontes"
Cohesion: 0.29
Nodes (7): Fonte theduchy.com para foto e descricao da amarracao, Blogs BR de cultura e BDSM (Senhor Verdugo, Dom Barbudo), Curadoria de fontes de referencia da Shibari Brasil, Glossarios e terminologia (Twisted Monk, Reborn Ropes, Nawapedia), Fontes de historia e teoria (Akira Nawa, Kinbaku Today, Wallflower Codex), Ensino, arte e YouTube (Rope365, Shibari Study, The Duchy, Escola de Shibari), Formato Post Inspiracao de Amarracao

### Community 31 - "Originalidade e decisões de peças"
Cohesion: 0.50
Nodes (3): Regra: usar o padrao da referencia, nunca copiar (originalidade), Repostagem da C-057 em 18/09 no lugar da C-079 (legenda igual), Decisoes sobre C-079, C-082, C-083, C-088, C-090 (descartar) e C-003

## Ambiguous Edges - Review These
- `Gui (agente-trafego)` → `Google Ads no BigQuery: resumo técnico`  [AMBIGUOUS]
  assets/docs/google_ads_bigquery_resumo.md · relation: references
- `Núcleo da voz (sb_cerebro)` → `Vocabulário proibido em anúncios (shibari, bondage, BDSM, fetiche...)`  [AMBIGUOUS]
  .claude/skills/hab-meta-ads/SKILL.md · relation: conceptually_related_to
- `Lista negra de vocabulário de IA` → `F5 Série "não é X, é Y"`  [AMBIGUOUS]
  contexto/referencias-posts-salvos-2026-10-09.md · relation: conceptually_related_to
- `Método Hook-and-Loop` → `F13 CTA por palavra-chave`  [AMBIGUOUS]
  contexto/referencias-posts-salvos-2026-10-09.md · relation: conceptually_related_to
- `Blacklist de termos que acionam shadowban/NSFW` → `F13 CTA por palavra-chave`  [AMBIGUOUS]
  contexto/referencias-posts-salvos-2026-10-09.md · relation: conceptually_related_to

## Knowledge Gaps
- **145 isolated node(s):** `Marketing nao gerencia produto`, `Acesso ao Notion por MCP somente leitura`, `.claude/specs/diretrizes.md`, `Gatilho /graphify (skill graphify)`, `Tabela de roteamento da Mari` (+140 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 189 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Julia (agente-escritor, autora)` connect `Time de agentes e produção` to `Personas e referências salvas`, `Glossário Shibari e Kinbaku`, `Formatos: vídeo, foto e carrosséis`, `Regras da sequência do Instagram`, `Peças da fila e arcos de produto`, `Artefato e planejador da sequência`, `Mari, pauta e grafo`, `Escrita: hook e SEO`, `Status da pauta e alertas`, `Leo, estratégia e núcleo de voz`, `Risco de alcance e métricas`, `Voz Shibari e rascunhos piloto`, `Publicação e legenda`, `Carrossel Livre e hashtags`, `Post para blog`, `Post de inspiração e fontes`?**
  _High betweenness centrality (0.241) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Julia (agente-escritor, autora)` (e.g. with `Glossário de Shibari e Kinbaku` and `Rascunho educativo (legenda de carrossel, fala a marca)`) actually correct?**
  _`Julia (agente-escritor, autora)` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Marketing nao gerencia produto`, `Acesso ao Notion por MCP somente leitura`, `.claude/specs/diretrizes.md` to the rest of the system?**
  _145 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Script: gerar artefato da sequência` be split into smaller, more focused modules?**
  _Cohesion score 0.060939060939060936 - nodes in this community are weakly interconnected._
- **Why does `Mari (agente-coordenador)` connect `Mari, pauta e grafo` to `Personas e referências salvas`, `Time de agentes e produção`, `Regras da sequência do Instagram`, `Peças da fila e arcos de produto`, `Diretrizes e pipeline`, `Status da pauta e alertas`, `Leo, estratégia e núcleo de voz`, `Publicação e legenda`?**
  _High betweenness centrality (0.230) - this node is a cross-community bridge._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `Gui (agente-trafego)` and `Google Ads no BigQuery: resumo técnico`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `Núcleo da voz (sb_cerebro)` and `Vocabulário proibido em anúncios (shibari, bondage, BDSM, fetiche...)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._