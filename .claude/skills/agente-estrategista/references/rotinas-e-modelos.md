# Rotinas e modelos do Leo (estrategista de conteúdo)

Todas as rotinas são **ler → analisar → propor → Hugo decide**. O Leo não escreve a peça final (isso é da Julia); ele mantém a sequência e a fila (`estrategia/`) e propõe, e a pauta só muda depois da aprovação do Hugo. Saída padrão: texto no chat; relatório/estudo só se o Hugo pedir ou for rotina semanal (e então gravar em `estrategia/material/` e, com o pedido do Hugo, no Notion).

## 0. Produzido x postado (rodar antes da revisão semanal e sempre que o Hugo perguntar "o que falta postar?")

```bash
/c/Users/HTK1562/venvs/sb_relatorios/Scripts/python.exe /c/Users/HTK1562/Documents/GitHub/sb_admin_team/.claude/skills/agente-estrategista/scripts/produzido_x_postado.py                 # relatório em Markdown
/c/Users/HTK1562/venvs/sb_relatorios/Scripts/python.exe /c/Users/HTK1562/Documents/GitHub/sb_admin_team/.claude/skills/agente-estrategista/scripts/produzido_x_postado.py --debug         # 2 melhores candidatos de cada peça (para auditar um casamento)
/c/Users/HTK1562/venvs/sb_relatorios/Scripts/python.exe /c/Users/HTK1562/Documents/GitHub/sb_admin_team/.claude/skills/agente-estrategista/scripts/produzido_x_postado.py --out C:/Users/HTK1562/Documents/GitHub/sb_admin_team/estrategia/material/produzido-x-postado-AAAA-MM-DD.md
```
Somente leitura: não altera pauta, histórico nem pastas do marketing e não escreve no banco. **A pauta não é a fonte de verdade de "postou"; o perfil é.**
- **Como casa:** compara a legenda planejada (`legenda.txt` da pasta do conteúdo no Drive, `03_CONTEUDO/<tipo>/<pasta>/`; nas peças antigas, a seção Legenda do `texto.md`) com a legenda postada em `tb_instagram_midia` (ignora acento, pontuação, emoji e hashtag). ≥ 88% = no ar; 62–88% = provável (legenda editada). Entre candidatos parecidos, o post não pode ser anterior à aprovação da peça e o empate vai para a data da pauta. Sem legenda planejada, só por palavras do título (no máximo "provável", e exige a data).
- **O que entrega:** (1) produzido e não postado, com dias parados; (2) já no ar mas a pauta ainda diz pendente; (3) pauta diz publicado e não achei; (4) data da pauta ≠ data real; (4b) mesma legenda em mais de um post (repostagem); (5) em produção, com dias na etapa; (5b) posts no ar sem peça na pauta desde 01/06/2026.
- **O que fazer com o resultado:** quem confirma a postagem é a **Mari** (`Confirmar postagem: <título>`, com a data real); eu não mexo na pauta. Peça pronta e parada há mais de 14 dias: decisão do Hugo (entra na semana ou descarta). Primeira execução (07/10/2026): 24 peças no ar, **8 já postadas mas ainda "Aguardando Publicação" na pauta** (C-091, 094, 096, 093, 081, 080, 092, 095), **2 prontas e não postadas** (C-090 há 23 dias; C-079 há 42 dias), C-057 repostada em 18/09 (11,6 mil views) e 6 peças em design paradas há 25 a 42 dias.
- **Limites:** legenda muito editada no mLabs/Instagram baixa a similaridade; peça sem legenda é cruzada só por título; Stories e blog não entram; a extração do Instagram roda 3x por dia (peça postada há poucas horas pode não aparecer).

## 1. Revisão semanal (segunda ou sexta, ~30 min)

1. **Cobrar a fonte:** rodar a receita 0 (frescor) e as 1, 2 e 5 de `consultas-instagram.md` (no `sb_admin_team`, skill `analista-de-dados`) (semana x semana, peças, anúncios). Só no navegador (`coleta-de-dados.md`): **Status da conta**, skip rate e retenção dos Reels. `fg_impulsionada` e a receita 5 já dizem se houve anúncio ativo.
2. **Cruzar produzido × postado:** ler `pauta.md` e `historico-conteudos.md` do MKT; listar o que a pauta diz que saiu vs. o que `tb_instagram_midia` mostra (permalink e data real; a chave é a legenda/data, ver `mapa-do-projeto.md` §4) (usar `mapa-do-projeto.md` §5 para as divergências conhecidas). Apontar peças prontas e não postadas (peça parada = alcance perdido).
3. **Tabela da semana** (`metricas-e-leitura.md` §5) com Δ vs. semana anterior; marcar o que é pago.
4. **Post a post** (§2) das 2–3 peças que mais se afastam da mediana (melhor e pior).
5. **Cadência e mix:** posts da semana vs. meta de 3/sem; formatos usados vs. experimento do Plano Out/Nov (2 carrosséis conceituais + 1 Reel + 1 produto).
6. **Três decisões para o Hugo:** 1 manter, 1 mudar, 1 testar (com hipótese e métrica de sucesso) → PDCA.
7. **Registrar** em `estado-atual.md` (o que mudou, próximo passo) e, a pedido, na página Notion do relatório semanal (formato em memória `relatorio-semanal-instagram`; escrever no Notion só com pedido do Hugo e conferindo formatação com `notion-fetch`).

## 2. Análise post a post (o "o que deu certo e o que não deu")

Para cada peça: **cruzar três camadas** e dizer o porquê.

| Camada | O que olhar | Pergunta |
|---|---|---|
| Intenção (MKT) | `briefing.md`: objetivo (salvamento? compartilhamento? alcance?), persona, ângulo, CTA | O que o time quis que acontecesse? |
| Execução (MKT) | `texto.md`, `visual-spec.md`, imagens: gancho da capa, nº de slides, densidade do texto, fundo, CTA, hashtags, legenda | Como foi feito? |
| Resultado (Insights) | alcance, % não seguidores, salvamentos, envios, comentários, seguidores ganhos, (Reel) skip rate/retenção, idade da peça, pago? | O que aconteceu, normalizado por alcance? |

**Saída por peça (modelo):**

```
Peça: <título> · <formato> · <data real> · código C-XXX
Objetivo do briefing: <...>   Resultado: <números normalizados> vs. mediana do formato
Veredito: acertou / acertou em parte / errou o objetivo — e por quê (1 causa principal)
O que repetir: <elemento concreto: capa, tema, estrutura, tamanho>
O que mudar: <elemento concreto>
Confiança: alta/média/baixa (n, idade da peça, pago ou não)
```

Regras: comparar com a **mediana do mesmo formato** (não com o recorde); dizer sempre o `n`; separar **causa provável** de **fato**; não concluir com 1 peça — marcar como hipótese e propor o teste que a confirma. Padrões se confirmam com ≥ 3 peças de mesmo tipo.

**Variáveis a catalogar por peça** (para virar base de aprendizado): pilar/tema (educativo, conceitual, produto, bastidor, comunidade), formato, nº de slides/duração, tipo de gancho (pergunta, afirmação contrária, lista, mito, "red flag"), CTA (encaminhar, salvar, comentar, nenhum), fundo/estilo, presença de pessoa/mão/corda, hashtags, hora/dia, idade na coleta. Planilha em `estrategia/material/registro-de-posts.md`.

## 3. Proposta de slot (a saída principal do Leo)

Toda ideia nasce **na voz** e **com âncora no núcleo** (`sb_cerebro`). Sem âncora, a ideia não é proposta. Se o tema não tem posição do Hugo, o Leo **não inventa a visão**: registra uma pergunta curta para ele e a resposta alimenta o núcleo. Formato curto, autossuficiente, com evidência e sem escrever a peça:

```
SLOT / IDEIA: <título provisório>
Âncora no núcleo: <posição P# do Hugo | nota da biblioteca | resultado medido nosso> (obrigatória; sem ela vira PERGUNTA ao Hugo)
Tese em uma frase (na voz do Hugo, primeira pessoa quando couber):
Teste das 4 perguntas do voz.md aplicado ao ângulo e ao gancho: <passou / ajustar>
Formato sugerido: <carrossel livre / post de frase / desatando mitos / Reel / foto / story série>
Pilar e público: <...> (conforme contexto/personas.md)
Por que agora (evidência): <dado nosso + referência externa>
Objetivo e métrica de sucesso: <ex.: envios por mil views; seguidores por mil views>
Gancho (3 opções de primeira linha ou capa):
Estrutura em tópicos (sem texto final): <slides/cenas>
Referência de inspiração: <perfil/post>, o que aproveitar e o que NÃO copiar
Cuidados de plataforma: <termos, imagem, hashtag; ver risco-de-alcance-nicho.md>
Gancho de produto (se houver): consultar o Catálogo — Produtos (Notion); sem venda cruzada forçada
Teste proposto: <variação A/B ou Trial Reel>
```

Respeitar: a skill `voz-shibari` (sem emoji em nenhum texto), 5 hashtags no máximo, grid de 9 posts (`contexto/design-system.md` §7), formatos existentes em `contexto/formatos/` (formato novo passa pelo protocolo de novos formatos das diretrizes).

## 4. Roteiro de vídeo/Reel (estrutura, não o texto final)

1. **Objetivo** (descoberta? ensino? prova de produto?) e **uma ideia só** por vídeo.
2. **Hook 0–3 s** (pergunta, afirmação contrária, resultado primeiro, "pare de fazer X"). Texto na tela + fala com a palavra-chave.
3. **Desenvolvimento** em 3 beats curtos (cortes a cada 2–4 s; legenda automática; mãos/corda/close, sem exposição de corpo — ver risco §2).
4. **Payoff** claro e **fechamento com gancho de envio/salvamento** ("manda pra quem usa corda de algodão").
5. Duração por objetivo (**[ESTIMATIVA]**): 7–15 s para frio; 21–34 s para ensino curto; 45–60 s para demonstração com payoff. Reels de até 3 min são elegíveis a recomendação **[OFICIAL]**.
6. Checklist de produção: capa legível no grid 3:4, legenda com palavra-chave na primeira linha, ≤ 5 hashtags, áudio (original > tendência para marca de nicho), **Trial Reel antes** de publicar para o perfil.
7. Série repetível ("1 nó em 30 s"): o formato mais fácil de produzir em lote com o material de `assets/videos/` e `Single column tie`.

## 5. Concorrentes e referências (ver `coleta-de-dados.md`)

- Montar/atualizar mapa em `estrategia/material/referencias/`: perfil, nº de seguidores, frequência, mix de formatos, engajamento relativo, **peças campeãs (por comentário/salvamento visível)**, ângulos recorrentes, CTA, como falam de produto, como contornam a restrição.
- Por ideia encontrada, entregar: **o padrão** (o que faz funcionar), **a nossa versão** com conteúdo próprio e **o risco** (originalidade e termos). Nunca "copiar a peça".
- Ponto de partida: 11 contas em `MKT/contexto/referencias.md` + concorrentes da Base §11.3 + busca nova por hashtags e Explorar (via navegador do Hugo; só observar).

## 6. Fechar o elo post → venda (propor ao Hugo, não executar sozinho)

1. UTM nos 4 links de bio e no sticker de link (Notion "Rastreamento de Links"; conferir com `especialista-google`).
2. Cupom exclusivo para Story/DM (sem criar cupom manual com outro código; regra do projeto — usar o fluxo existente).
3. Pergunta "como conheceu?" no checkout/WhatsApp.
4. Contar DMs/WhatsApp originados de Instagram na semana.
5. Cruzar com `tb_atribuicao_pedido` via `analista-de-dados` (declarar correlação, nunca causalidade; N pequeno).

## 7. Planejamento de conteúdo (mensal e semanal)

- **Mensal:** objetivos (alcance novo, autoridade, conversão), pilares, mix de formato com base no que **nossos números** mostram, 3–4 séries repetíveis, datas comerciais (Dia dos Namorados/Black Friday/Natal), lançamentos de produto (vem do `comprador-*`/`cadastrador`), experimentos (1 por vez).
- **Semanal:** 3 feed + stories (sexta agendada) + 1 Reel; casar com a cadência real do Hugo (feed seg/qua/sex; sexta agenda a semana seguinte no mLabs).
- Respeitar capacidade: o gargalo do time é o Hugo (revisar, aprovar no Canva, postar). Proposta que não cabe em 30 min/dia não é plano.
- **Experimento atual (Plano Out/Nov §5, semanas 8–11):** 2 carrosséis conceituais + 1 Reel + 1 peça de produto por semana; métricas: visitas ao perfil > 800/sem, toques no link, pedidos Instagram social > 0,11/dia; primeira leitura em **23/out/2026**. Preparar o painel de leitura para essa data.

## 8. Pesquisa de tendência (sob demanda)

Rodar o protocolo de `atualizacao-da-pesquisa.md`; para tendência de formato/áudio/assunto, observar Explorar e Reels pelo navegador do Hugo (só leitura), listar 5–10 itens e filtrar por **encaixe de marca** (educativo, consentimento, técnica, cultura) e **risco de plataforma**. Tendência de áudio só vale se a peça continuar educativa.

## 9. Perguntas que o especialista faz ao Hugo (não presumir)

Peça foi **impulsionada**? A data de "Publicado" é do post ou do agendamento? Algum Reel/Story saiu que não está no registro? Houve anúncio/recusa? Qual objetivo da semana (alcance, venda, lançamento)? Permite abrir o Painel (login) agora? Mudou a bio/foto?
