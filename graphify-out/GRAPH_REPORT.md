# Graph Report - sb_marketing_team  (2026-11-11)

## Corpus Check
- 92 files · ~150,963 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 6)

## Summary
- 692 nodes · 1081 edges · 52 communities (33 shown, 19 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 60 edges (avg confidence: 0.83)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Feed, grid e peças do Instagram
- Dependências do projeto de vídeo
- Davi e edição de vídeo
- Glossário BDSM
- Guia da marca e identidade visual
- Gerador do artefato da sequência
- Modelo HTML do post de blog
- Manual de Meta Ads (guardado)
- Produzido × postado (script)
- Scripts de conferência do Leo
- GA4 no BigQuery
- Insumos da sequência (script)
- Bia e direção de arte
- Fila prioritária e sincronização
- Curadoria de fontes de referência
- Glossário de shibari e kinbaku
- Julia, Ana e revisão de texto
- Estado atual do Leo
- Configuração TypeScript do vídeo
- Mari e publicação
- Planejador de sequência
- Regras do CLAUDE.md
- Diretrizes e protocolos
- Manual de produção textual
- Template do artefato da sequência
- Rotinas e saídas do Leo
- Métricas e revisão semanal
- Revisão de voz do banco de briefings
- Leo e artefato da sequência
- Pacotes Remotion
- Roteiros de Reels
- Revisão de voz da sequência
- Relatório produzido × postado
- Originalidade de foto
- Algoritmo por superfície
- Padrão da referência
- Acesso ao Notion (MCP)
- Gatilho /graphify (skill graphify)
- O que o Instagram nao permite (link em l
- Nota de metodo: Help Center via navegado
- Planilha minima por peca
- Alimentar a biblioteca (nota destilada e
- Filtro antes de registrar uma ideia
- Regra de equilibrio Shibari/Kinbaku e BD
- Armadilhas de leitura (impulsionado, amo
- Elo fraco: do Instagram ao pedido (UTM, 
- Cartela 3x3 com 9 casas e casa central l
- Visual do bingo: Carbon Black, Scarlet P
- Fluxo da foto: foto movida para a pasta,
- Decisoes pendentes do Hugo: C-090, C-079
- Repostagem da C-057 em 18/09 no lugar da

## God Nodes (most connected - your core abstractions)
1. `Glossário BDSM (curadoria)` - 29 edges
2. `main()` - 24 edges
3. `Sequencia de Conteudo Instagram` - 24 edges
4. `Pauta Editorial` - 23 edges
5. `main()` - 20 edges
6. `Post Por Tras do Desejo` - 20 edges
7. `Blog proposta consolidada 04/11/2026` - 19 edges
8. `Carrossel Livre` - 18 edges
9. `Post para Blog` - 17 edges
10. `Design System Shibari Brasil` - 15 edges

## Surprising Connections (you probably didn't know these)
- `Escurecer` --implements--> `remotion`  [INFERRED]
  contexto/formatos/modelos/briefing-video-modelo.md → video/package.json
- `TextoEsfera` --implements--> `remotion`  [INFERRED]
  contexto/formatos/modelos/briefing-video-modelo.md → video/package.json
- `Hojojutsu (nota: influencia, nao origem direta)` --semantically_similar_to--> `Hojojutsu: fonte kinbakutoday nao afirma origem direta`  [INFERRED] [semantically similar]
  assets/docs/Glossario-Shibari.md → contexto/revisao-voz-resumo-para-cerebro.md
- `Instagram Video` --references--> `remotion`  [EXTRACTED]
  contexto/formatos/instagram-video.md → video/package.json
- `Paleta de cores (Carbon Black, Deep Plum, Scarlet Pulse, Skin Nude, Warm Light, Smoke Taupe)` --semantically_similar_to--> `Paleta de cores e hierarquia de uso`  [INFERRED] [semantically similar]
  .claude/skills/agente-diretor-de-arte/SKILL.md → assets/docs/Guia da marca - Shibari Brasil.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Conferencia pauta x perfil: relatorio, briefing para Mari e confirmar postagem** — estrategia_material_produzido_x_postado_2026_10_07_relatorio, estrategia_material_briefing_para_mari_2026_10_07_confirmar_postagem [EXTRACTED 0.95]
- **Reels A, B e C: roteiros de Fase 1 com produto, cashback e arco** — estrategia_material_roteiros_roteiros_reels_fase1_2026_10_19_reel_a, estrategia_material_roteiros_roteiros_reels_fase1_2026_10_19_reel_b, estrategia_material_roteiros_roteiros_reels_fase1_2026_10_19_reel_c [EXTRACTED 0.95]
- **Voz (núcleo) e técnica de escrita** — conceito_nucleo_voz_sb_cerebro, claude_skills_voz_shibari_skill_skill [INFERRED 0.85]
- **Identidade visual da marca (paleta, tipografia, wordmark, grid)** — _claude_skills_agente_diretor_de_arte_skill_paleta_de_cores, assets_docs_guia_da_marca___shibari_brasil_tipografia, _claude_skills_agente_diretor_de_arte_skill_wordmark, _claude_skills_agente_diretor_de_arte_skill_grid_ciclo_9_posts, assets_docs_guia_da_marca___shibari_brasil_paleta_de_cores, assets_docs_guia_da_marca___shibari_brasil_logotipo_tipografico, assets_docs_guia_da_marca___shibari_brasil_sistema_de_grid [INFERRED 0.85]
- **Fluxo de produção puxado pela fila (Leo → Julia → Ana → Bia/Davi → Mari)** — _claude_skills_agente_estrategista_skill_leo, _claude_skills_agente_escritor_skill_julia, _claude_skills_agente_revisor_skill_ana, _claude_skills_agente_diretor_de_arte_skill_bia, _claude_skills_agente_video_skill_davi, _claude_skills_agente_coordenador_skill_mari, _claude_specs_diretrizes_fluxo_completo [EXTRACTED 1.00]
- **Guarda da voz: núcleo, carimbo, âncora e filtro antirrobô** — claude_voz_shibari_nucleo, claude_carimbo_voz_carregada, _claude_skills_agente_estrategista_skill_ancora_obrigatoria, _claude_skills_agente_escritor_skill_cabecalho_texto_md, _claude_skills_hab_produtor_textual_skill_hab_produtor_textual [INFERRED 0.85]
- **Formatos tematicos que implementam o tema legivel no grid** — contexto_formatos_conteudo_tema_legivel_no_grid, contexto_formatos_carrossel_livre_carrossel_livre, contexto_formatos_post_por_tras_do_desejo_post_por_tras_do_desejo, contexto_formatos_post_5_motivos_post_de_5_motivos, contexto_formatos_conteudo_teste_da_miniatura__130px_ [EXTRACTED 1.00]
- **Padrao de publicacao do blog** — contexto_formatos_post_para_blog_post_para_blog, contexto_formatos_post_para_blog_html_post_para_blog_html_e_publicacao, contexto_formatos_modelos_post_para_blog_modelo_modelo_html_post_para_blog, contexto_formatos_post_para_blog_sb_cerebro_blog_md, contexto_formatos_post_para_blog_html_search_console_pedido_de_indexacao, contexto_formatos_post_para_blog_html_editor_nuvemshop [EXTRACTED 1.00]
- **Pipeline de producao Leo Julia Ana Bia Mari** — contexto_pauta_leo_agente_estrategista, contexto_pauta_julia_agente_escritor, contexto_pauta_ana_agente_revisor, contexto_pauta_bia_agente_diretor_de_arte, contexto_pauta_mari_agente_coordenador, contexto_pauta_pipeline_de_producao_de_conteudo_organico [EXTRACTED 1.00]

## Communities (52 total, 19 thin omitted)

### Community 0 - "Feed, grid e peças do Instagram"
Cohesion: 0.05
Nodes (62): Layout Editorial, C-026 wax play qual vela usar, C-046 o que o fetiche revela, Carrossel Livre, Glossario BDSM Shibari Brasil, hab-produtor-textual, Modelo Canva DAHZ47lcb20 (Carrossel Livre Modelo 2), Referencias (rotulo de fontes) (+54 more)

### Community 1 - "Dependências do projeto de vídeo"
Cohesion: 0.05
Nodes (44): eslint, prettier, react-dom, @remotion/cli, @remotion/eslint-config-flat, @remotion/google-fonts, @remotion/layout-utils, @remotion/light-leaks (+36 more)

### Community 2 - "Davi e edição de vídeo"
Cohesion: 0.07
Nodes (36): Davi agente-video, Area segura do Instagram, Briefing de Video (modelo), Escurecer, Registro de alteracoes, TextoEsfera, visual-spec.md, react (+28 more)

### Community 3 - "Glossário BDSM"
Cohesion: 0.07
Nodes (45): Glossário BDSM (curadoria), Aftercare, Amaurofilia (privação visual), Asfixia sexual (hipoxifilia), Bondage, Cena (play, sessão), Consentimento, Dominante (Dom/Domme) (+37 more)

### Community 4 - "Guia da marca e identidade visual"
Cohesion: 0.05
Nodes (34): Wordmark 'shibari brasil' (Cormorant Garamond), Logotipo tipográfico (Cormorant Garamond), Design System Shibari Brasil, Guia da Marca Shibari Brasil, Imagem Principal do Blog (Hero), Layout de Frase, Layout Informativo, Layout Minimalista (+26 more)

### Community 5 - "Gerador do artefato da sequência"
Cohesion: 0.12
Nodes (14): agendamentos(), aplicar_agendamentos(), arte_do_slot(), capa_do_agendado(), capa_em_cache(), chave_tipo(), checar_cores(), _dias() (+6 more)

### Community 6 - "Modelo HTML do post de blog"
Cohesion: 0.11
Nodes (27): Leia a seguir grid de 3 cartoes, Linha de confianca, Modelo HTML Post para Blog, Na nossa leitura (aside data-sb), Resposta rapida (aside data-sb), Bloco Na loja, Endereco limpo e redirecionamento 301, Breve Historia do Shibari (blog) (+19 more)

### Community 7 - "Manual de Meta Ads (guardado)"
Cohesion: 0.09
Nodes (25): Ferramentas Advantage+, Checklist anti-bloqueio, Checklist operacional pré-campanha, Dicionário de substituição, Estrutura de campanha (campanha, conjunto, anúncio), Funil para nicho sensível, Manual de Meta Ads (guardado desde 03/11/2026), Orçamento, lances e ROAS (+17 more)

### Community 8 - "Produzido × postado (script)"
Cohesion: 0.15
Nodes (17): carregar_perfil(), classificar(), _codigo(), _data(), _dir(), _fmt(), _formato(), itens_do_marketing() (+9 more)

### Community 9 - "Scripts de conferência do Leo"
Cohesion: 0.15
Nodes (9): hash_normalizado(), main(), divergencias(), documentos(), ignorado(), main(), padroes_ignorados(), main() (+1 more)

### Community 10 - "GA4 no BigQuery"
Cohesion: 0.12
Nodes (24): Discrepâncias com a interface do GA4, GA4 no BigQuery: resumo técnico, Eventos padrão do GA4, Tabela events_* (uma linha por evento), Export forward-only (sem backfill), Funil de e-commerce (view_item a purchase), Tabelas intraday e campos ausentes, Atualização por até 72 horas (+16 more)

### Community 11 - "Insumos da sequência (script)"
Cohesion: 0.14
Nodes (14): pipeline_e_backlog(), banco_de_midia(), categoria_ciclo(), fundo_da_peca(), fundos_do_historico(), ler_banco_briefings(), luz(), main() (+6 more)

### Community 12 - "Bia e direção de arte"
Cohesion: 0.11
Nodes (17): Bia — Diretora de Arte (agente-diretor-de-arte), briefing-video.md para o Davi, Linha vertical Scarlet (3px, 80px), Paleta de cores (Carbon Black, Deep Plum, Scarlet Pulse, Skin Nude, Warm Light, Smoke Taupe), Sistema de layout: 4 formatos (editorial, frase, informativo, minimalista), visual-spec.md (entrega da Bia, campo Fundo), FUNDOS (mapa de cores da marca), Direção fotográfica (composição, fundos, luz, roupa) (+9 more)

### Community 13 - "Fila prioritária e sincronização"
Cohesion: 0.18
Nodes (10): Fila prioritária do Instagram (obrigatório em toda sessão), Fila prioritária do Instagram (sequência do Hugo), Vínculo pauta e fila [fila:Px], casar(), diff_snapshot(), dmy(), ignorada(), ler_pauta() (+2 more)

### Community 14 - "Curadoria de fontes de referência"
Cohesion: 0.12
Nodes (17): Fonte theduchy.com para foto e descricao da amarracao, Blogs BR de cultura e BDSM (Senhor Verdugo, Dom Barbudo), Curadoria de fontes de referencia da Shibari Brasil, Glossarios e terminologia (Twisted Monk, Reborn Ropes, Nawapedia), Fontes de historia e teoria (Akira Nawa, Kinbaku Today, Wallflower Codex), Perfis de Instagram de referencia (kink_collective, dr.k1nkaware, dominantdiscourse e outros), Ensino, arte e YouTube (Rope365, Shibari Study, The Duchy, Escola de Shibari), Fila prioritaria de producao por data de entrega (+9 more)

### Community 15 - "Glossário de shibari e kinbaku"
Cohesion: 0.12
Nodes (13): Glossario de Shibari e Kinbaku, Fontes: Akira Nawa e Andrea Ropes, Hojojutsu (nota: influencia, nao origem direta), Ito Seiu (pai do shibari moderno), Karada, Kinbaku, Ma (distancia, espaco e ritmo), Shibari (+5 more)

### Community 16 - "Julia, Ana e revisão de texto"
Cohesion: 0.18
Nodes (13): Julia — Autora (agente-escritor), Arquivo legenda.txt (texto publicável via API), Protocolo de Autorrevisão (4 camadas + teste das 4 perguntas), Ana — Revisora (agente-revisor), Checklist de blog (P93–P99), Checklist de formato (gancho, parágrafos, legenda), Revisão de anúncio do Google Ads (para especialista-google), Relatório: APROVADO ou REQUER AJUSTES (+5 more)

### Community 17 - "Estado atual do Leo"
Cohesion: 0.15
Nodes (9): Estado atual do Leo (foto e registro de mudanças), Leitura de resultados: carrossel no topo, post do Hugo sem IA, Pendências abertas (fila v11, backlog, publicador API), Plano v14 (09/11/2026): vídeo do castiçal, Kit Shibari para Estudo, Formatos validados (carrossel livre, Por trás do desejo, Desatando mitos), O que NÃO fazer (não copiar, não burlar política), Regras e decisões do Leo, Regras de leitura de dados (pago×orgânico, n, normalizar) (+1 more)

### Community 18 - "Configuração TypeScript do vídeo"
Cohesion: 0.14
Nodes (13): compilerOptions, esModuleInterop, forceConsistentCasingInFileNames, jsx, lib, module, moduleResolution, noEmit (+5 more)

### Community 19 - "Mari e publicação"
Cohesion: 0.17
Nodes (10): Fase 1: agendamento no mLabs pelo Hugo, Fase 2: publicador por API (sb_data_pipeline), Mari — Coordenadora e Publicação (agente-coordenador), Pacote de publicação (mídia validada, legenda, data e hora de pico), Publicação de post para blog (publicacao.html, indexação), Mapa do projeto em dia (graphify_defasado.py), Tabela de roteamento de pedidos, Padrão de mídia para publicação via API (JPEG sRGB, MP4) (+2 more)

### Community 20 - "Planejador de sequência"
Cohesion: 0.17
Nodes (8): Grid do feed: ciclo de 9 posts, Arco de produto (entrada, prática, produto, fecho), Horário de cada post pela hora de pico (receita 10), Modo Planejador de Sequência, Regras duras de sequenciamento (cor, Scarlet, ciclo de 9, slots seg/qua/sex), Regras macias (descoberta×relacionamento×negócio, persona), Lógica de slot atrasado/suspenso, Sistema de grid (ciclo de 9 posts)

### Community 21 - "Regras do CLAUDE.md"
Cohesion: 0.18
Nodes (9): Cabeçalho do texto.md (o antigo briefing), Tom de voz (frase falável, desejo sugerido, segurança direta), Biblioteca só pelo agente bibliotecário, Ressalva: caminhos fixos da máquina do Hugo (scripts), Código de vídeo Remotion só em video/, Comportamento do Agente (triagem pela Mari, pauta única), Notion Catálogo — Produtos (somente leitura), SB Marketing Team (CLAUDE.md) (+1 more)

### Community 22 - "Diretrizes e protocolos"
Cohesion: 0.17
Nodes (11): Comandos de Uso (Como estamos?, Produzir:, Revisar:, Confirmar postagem:), Critérios de Sucesso por Execução, Diretrizes de Execução do Marketing Team, Formatos cadastrados (14 tipos de conteúdo), Protocolo de Armazenamento de Anúncios (histórico), Protocolo de Armazenamento de Conteúdos (Drive), Protocolo de Pauta (pauta.md único registro de status), Protocolo de Registro de Memória (+3 more)

### Community 23 - "Manual de produção textual"
Cohesion: 0.20
Nodes (10): Manual Geral de Produção de Conteúdo com IA (original), Módulo 1: O Guia do Não-Fazer, Módulo 2: O Guia do Como Fazer, Módulo 3: Protocolo de Autorevisão e Prompt Mestre, Blog e SEO (atomic answers, E-E-A-T), Gatilhos de shadowban e hashtags banidas, Manual Geral de Produção de Conteúdo (Filtro Antirrobô), Lista negra de vocabulário de IA (+2 more)

### Community 24 - "Template do artefato da sequência"
Cohesion: 0.27
Nodes (6): drawBacklog(), drawGrid(), drawProd(), Template HTML do artefato Sequência Instagram, situacao(), tileEl()

### Community 25 - "Rotinas e saídas do Leo"
Cohesion: 0.20
Nodes (8): Análise post a post (intenção × execução × resultado), Concorrentes e referências, Fechar o elo post → venda (UTM, cupom), Produzido × postado (produzido_x_postado.py), Proposta de slot (saída principal do Leo), Roteiro de vídeo/Reel (hook, 3 beats, payoff), Rotinas e modelos do Leo, Recursos 2025-2026 (Trial Reels, hashtags max 5, SEO)

### Community 26 - "Métricas e revisão semanal"
Cohesion: 0.20
Nodes (10): Revisão semanal, Elegibilidade para recomendacao e Status da conta, Lista negra empirica de termos sensiveis, Coleta pelo navegador (so o que a API nao entrega), Hierarquia de metricas (distribuicao a negocio), Razoes normalizadas por alcance (taxa de envio, salvamento), Roteiro de diagnostico de queda de alcance, Tabela de riscos (produto adulto, metafora sexual, imagem de corpo, bio) (+2 more)

### Community 27 - "Revisão de voz do banco de briefings"
Cohesion: 0.25
Nodes (7): Transições artificiais e 'não é X, é Y', C-004 Hojojutsu e shibari: o que as fontes dizem, C-026 Velas para wax play (guia de segurança), C-062 Ser submissa me faz menos feminista?, C-108 e C-109 frases do Hugo, Revisão de voz do banco de briefings (Backlog), Vereditos: Manter, Reescrever, Fundir, Arquivar, Adiar (72 briefings)

### Community 28 - "Leo e artefato da sequência"
Cohesion: 0.33
Nodes (6): Artefato visual da sequência (Grade do feed, Produção e captação), Artefato da sequência (claude.ai artifact, atualizar_artefato.py), BigQuery: 13 consultas de consultas-instagram.md (admin), Leo — Estrategista de Conteúdo (agente-estrategista), Princípios: nunca achismo ([OFICIAL]/[MEDIDO]/[ESTIMATIVA]), estrategia/sequencia-instagram-plano.json

### Community 29 - "Pacotes Remotion"
Cohesion: 0.40
Nodes (4): Candidatos (captions + whisper, noise, shapes), Pacotes instalados (transitions, motion-blur, layout-utils, light-leaks, google-fonts), Pacotes do ecossistema Remotion, Efeitos prontos: TextoEsfera e Escurecer

### Community 30 - "Roteiros de Reels"
Cohesion: 0.40
Nodes (4): Reel A: Primeiros minutos com a corda (Kit Iniciante, posta 26/10), Reel B: O que a gente confere antes de amarrar (tesoura, posta 20/11), Reel C: Tres passos para guardar a corda (oleo e pano, posta 09/11), Roteiros prontos dos Reels A, B e C (Fase 1)

### Community 31 - "Revisão de voz da sequência"
Cohesion: 0.50
Nodes (3): Revisao de voz da sequencia v11, Pet play 30/10: 'entrega' (P69) e quem encarna (P73), 'Sessao' nos roteiros dos Reels A, B e C

### Community 32 - "Relatório produzido × postado"
Cohesion: 0.67
Nodes (3): Briefing para a Mari: confirmar postagem de 8 pecas ja no ar e corrigir data da C-076, Cruzamento por similaridade de legenda (>=88% no ar, 62 a 88% provavel), Relatorio produzido x postado de 07/10/2026

## Ambiguous Edges - Review These
- `estrategia/sequencia-instagram-plano.json` → `Fila prioritária do Instagram (sequência do Hugo)`  [AMBIGUOUS]
  .claude/specs/fila-prioritaria.md · relation: references
- `P91 CTA que convida em vez de prescrever` → `Lembrete de seguranca na legenda`  [AMBIGUOUS]
  contexto/formatos/carrossel-livre.md · relation: semantically_similar_to

## Knowledge Gaps
- **175 isolated node(s):** `Fonte theduchy.com para foto e descricao da amarracao`, `Blogs BR de cultura e BDSM (Senhor Verdugo, Dom Barbudo)`, `Glossarios e terminologia (Twisted Monk, Reborn Ropes, Nawapedia)`, `Fontes de historia e teoria (Akira Nawa, Kinbaku Today, Wallflower Codex)`, `Fila prioritaria de producao por data de entrega` (+170 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 278 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **19 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Bia — Diretora de Arte (agente-diretor-de-arte)` connect `Bia e direção de arte` to `Julia, Ana e revisão de texto`, `Mari e publicação`, `Planejador de sequência`, `Guia da marca e identidade visual`?**
  _High betweenness centrality (0.225) - this node is a cross-community bridge._
- **What connects `Fonte theduchy.com para foto e descricao da amarracao`, `Blogs BR de cultura e BDSM (Senhor Verdugo, Dom Barbudo)`, `Glossarios e terminologia (Twisted Monk, Reborn Ropes, Nawapedia)` to the rest of the system?**
  _175 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Feed, grid e peças do Instagram` be split into smaller, more focused modules?**
  _Cohesion score 0.05472837022132797 - nodes in this community are weakly interconnected._
- **Why does `Design System Shibari Brasil` connect `Guia da marca e identidade visual` to `Feed, grid e peças do Instagram`?**
  _High betweenness centrality (0.215) - this node is a cross-community bridge._
- **Should `Dependências do projeto de vídeo` be split into smaller, more focused modules?**
  _Cohesion score 0.0545790934320074 - nodes in this community are weakly interconnected._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `estrategia/sequencia-instagram-plano.json` and `Fila prioritária do Instagram (sequência do Hugo)`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `P91 CTA que convida em vez de prescrever` and `Lembrete de seguranca na legenda`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._