# Protocolo de atualização da pesquisa (o conhecimento envelhece rápido)

O Instagram muda de regra todo mês. A foto atual está em `algoritmo-e-plataforma.md` (**pesquisa de 07/out/2026**). Regra: **se a última pesquisa tem mais de 45 dias, ou o pedido depende de uma regra da plataforma ("pode?", "o algoritmo agora...", "mudou?"), refaça uma pesquisa curta antes de responder.**

## Como pesquisar (ferramentas: WebSearch / WebFetch)

1. 4–6 buscas em paralelo, modo `extended` para o que é recente: (a) "Instagram algorithm <mês/ano> Mosseri", (b) "Instagram updates <mês/ano>" (SocialBee/NapoleonCat mantêm tracker), (c) "Instagram Recommendation Guidelines" / Status da conta, (d) buscas em português ("algoritmo do Instagram <ano>"), (e) tema do pedido (formato, hashtag, link, anúncio).
2. **Preferir fonte primária:** Help Center (`help.instagram.com`), Transparency Center (`transparency.meta.com`), `creators.instagram.com`, posts/vídeos do Adam Mosseri (@mosseri), Meta Newsroom. Depois estudos com amostra declarada (Socialinsider, Buffer, Metricool, Rival IQ). Por último blogs de agência.
3. Classificar cada achado: **[OFICIAL] / [MEDIDO] / [ESTIMATIVA]** (definição no topo de `algoritmo-e-plataforma.md`). Número sem fonte rastreável = estimativa. Duas agências repetindo o mesmo número não o tornam oficial.
4. Registrar o que **mudou** (data, o que era, o que virou, impacto para nós) em `estado-atual.md` e atualizar a seção correspondente de `algoritmo-e-plataforma.md`.
5. Se a mudança afeta o time de marketing (formato, limite, regra), levar ao Hugo como recomendação de pauta/ajuste para a Mari.

## Termos sensíveis — a pesquisa que nunca termina

A Meta **não publica lista de palavras proibidas**. O que existe: Diretrizes de Recomendação, Padrões da Comunidade (Sexual Solicitation / Adult Nudity), Padrões de Anúncio e hashtags banidas (lista não oficial que muda). Por isso a "lista negra" da Shibari é **empírica**: nasce dos nossos dados (peça com % de não seguidores anormalmente baixo, aviso em Status da conta, hashtag que some). Ver `risco-de-alcance-nicho.md`.

## Fontes-base desta foto (07/out/2026)

- Meta — Diretrizes de Recomendação: https://help.instagram.com/313829416281232 · Status da conta: https://help.instagram.com/653964212890722 · Controle de Conteúdo Sensível: https://help.instagram.com/1055538028699165 · Sexual Solicitation: https://transparency.meta.com/policies/community-standards/sexual-solicitation/ · Anúncios, nudez e atividade sexual: https://transparency.meta.com/policies/ad-standards/objectionable-content/adult-nudity-and-sexual-activity
- Algoritmo 2026: https://creatorflow.so/blog/instagram-algorithm-2026/ · https://www.eclincher.com/articles/how-the-instagram-algorithm-works-in-2026 · https://meetedgar.com/blog/instagram-algorithm-updates · https://keywordseverywhere.com/news/instagram-algorithm-updates/ · https://creatorlanehq.com/blog/instagram-algorithm-2026-mosseri-vs-measured
- Em português: https://agenciagram.com.br/blog/algoritmo-instagram-2026-como-funciona · https://rafaelterra.com.br/guia-algoritmo-instagram-2026/ · https://notaalta.espm.br/o-melhor-de-hoje/algoritmo-do-instagram-o-que-influencia-o-engajamento-e-o-que-e-mito/
- Formatos e benchmarks: https://www.socialinsider.io/social-media-benchmarks/instagram · https://buffer.com/resources/data-best-content-format-social-media/ · https://metricool.com/press-release-instagram-study-2026/
- Atualizações mês a mês: https://socialbee.com/blog/instagram-updates/ · hashtags e links: https://www.socialmediaexaminer.com/what-clickable-reels-links-and-hashtag-limits-mean-for-your-2026-instagram-strategy/
- Insights/Reels: https://www.inro.social/blog/instagram-insights-update · https://www.socialmediatoday.com/news/instagram-adds-retention-insights-reels/758464/
- Nicho adulto/bem-estar: https://www.biird.co/blogs/sexual-wellness/understanding-instagram-restrictions-on-sexual-wellness-content-1 · https://www.tuchedigital.com.br/post/marketing-digital-para-sex-shop-tuche-referencia

> Nota de método: páginas do Help Center **não carregam por WebFetch** (conteúdo dinâmico). Usar o navegador embutido (`mcp__Claude_Browser__navigate` + `get_page_text`). As Diretrizes de Recomendação foram lidas assim em 07/out/2026 e estão resumidas (com trechos literais) em `risco-de-alcance-nicho.md` §1. Reler quando passar de 90 dias.
