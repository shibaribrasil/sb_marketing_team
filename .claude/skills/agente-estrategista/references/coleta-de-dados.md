# Coleta de dados do Instagram (@shibari.brasil) — pelo navegador (complemento)

> **Desde 07/out/2026 a fonte padrão é o BigQuery** (`consultas-instagram.md` (no `sb_admin_team`, skill `analista-de-dados`)): peças, insights por peça, conta, anúncios, comentários e concorrentes chegam 3x/dia pela Graph API. Use esta página **só para o que a API não entrega**: **skip rate e retenção dos Reels, Status da conta (elegibilidade), visitas/toques nos formatos que o painel detalha e conferência pontual** do dia corrente.

> Só **leitura**. O navegador do Hugo (Claude in Chrome) já fica logado na conta com Painel Profissional. Carregue a skill/regras do `chrome-browser` antes (1 `ToolSearch` com as ferramentas do núcleo). Nunca curtir, seguir, comentar, postar, responder DM nem mexer em configuração. Se pedir login, senha ou verificação: parar e avisar o Hugo.

## Atalhos de URL que funcionaram (set/2026 — confirmar se ainda valem)

| Para quê | URL |
|---|---|
| Insights da conta, 7 dias já aplicado | `instagram.com/accounts/insights/?timeframe=7` (também `30`, `90`) |
| Lista de peças por formato | `instagram.com/accounts/insights/content/?media_type=all` (ou `reels`, `stories`, `posts`) `&metric=views&sort_by=highest&timeframe=7&view_type=card` |
| Insights de uma peça | clicar no card → `/accounts/insights/media/<id>/` |
| Grade pública | `instagram.com/shibari.brasil/` (curtidas/comentários visíveis; Reels em `/reels/`) |
| Status da conta (elegibilidade) | Menu → Configurações → Conta → **Status da conta** |

**Cuidados:** trocar o filtro no dropdown **não** atualiza os números — recarregar a URL com o parâmetro. Verificar sempre se há **aviso de impulsionamento** (abas "Tudo/Anúncio") e anotar. Anotar a data/hora da coleta: números de peças recentes crescem.

## O que coletar por peça (planilha mínima)

`data` · `formato` (Reel/Carrossel/Foto/Story) · `tema/pilar` · `título/gancho` · `legenda (1ª linha)` · `views` · `alcance` · `% não seguidores` · `curtidas` · `comentários` · `envios` · `salvamentos` · `seguidores ganhos` · `visitas ao perfil` · (Reel) `tempo médio assistido`, `skip rate`, `retenção` · `impulsionado? (sim/não)` · `permalink`.

Salvar em `estrategia/material/AAAA-MM-DD — peças.md` (ou `.csv`) lado a lado com a análise gerada (convenção do projeto: dado bruto e insight juntos na pasta `dados/`). Se for apenas leitura rápida, não precisa gravar.

## Coleta de concorrente e referência (sem login ou com o login do Hugo, só observação)

- Perfil público: seguidores, frequência, mix de formato, 9–12 últimas peças, padrão de legenda, o que mais tem comentário/curtida **relativo ao perfil**, uso de Reels, Stories em destaque, CTA, bio e link.
- Registrar **ângulo e estrutura**, nunca copiar texto/imagem. Guardar em `estrategia/material/referencias/` com data e link.
- Prioridade de busca: contas de **shibari/kinbaku/bondage educativo** (BR e exterior), **lojas de cordas/bondage**, **educação em BDSM/consentimento**, **bem-estar sexual com bom alcance** (como contornam a restrição), e perfis fora do nicho com **formatos replicáveis** (carrossel de aprendizado, série fixa, "mito vs. verdade").
