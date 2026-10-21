# Fila prioritária do Instagram (sequência do Hugo)

A sequência de conteúdo do Instagram, definida pelo Hugo, é a **produção prioritária do time**. A fonte da verdade fica fora deste projeto e é somente leitura aqui:

`sb_admin_team/planejamento/sequencia-instagram-plano.json` (visual em `Sequência de Conteúdo Instagram.md`, na mesma pasta). Quem altera a sequência é o Hugo com a skill de Instagram; o time de marketing só lê.

## Como o time fica sabendo de mudanças

`scripts/sincronizar_fila.py` lê o plano e:
1. regrava o bloco **Fila prioritária** no topo de `contexto/pauta.md` (entre as marcas `FILA-PRIORITARIA`; não editar à mão);
2. compara com o último estado salvo (`contexto/fila-snapshot.json`) e lista o que mudou (peça nova, peça que saiu, data de postagem, prazo, responsável, troca de peça), registrando em `contexto/fila-historico.md`;
3. cruza a fila com as linhas da pauta e avisa de: peça da fila sem linha na pauta, **produção fora da fila**, **substituição não registrada** (a pauta tem uma peça diferente da que a fila diz) e **entrega atrasada**.

O script roda **automaticamente no início de cada sessão** (hook `SessionStart` em `.claude/settings.json`). Para rodar na hora: `python scripts/sincronizar_fila.py` (use `--check` para só ver, sem gravar).

## Ponte com a skill de Instagram (o que está no ar e o que está agendado)

`scripts/status_instagram.py` consulta, em modo somente leitura, o mesmo que a skill de Instagram usa: os posts no ar (`tb_instagram_midia`, últimos 45 dias) e a fila de publicação (`raw_instagram.fila_publicacao`, com status e hora de cada post agendado). Grava `contexto/status-instagram.json` e `contexto/status-instagram.md`. O `sincronizar_fila.py` lê esse arquivo e, para cada slot da fila:
- mostra **Instagram: AGENDADO dd/mm hh:mm**, **NO AR**, **FALHOU**, **ATRASOU**, etc.;
- avisa quando o Instagram está à frente da pauta (por exemplo, agendado na fila e a pauta ainda em "Pronto, aguardando publicação": mover para **Pronto - Agendado**; no ar: confirmar e mover para **Pronto - Publicado**);
- avisa de post no ar no dia de um slot que a pauta ainda não tem como publicado.

O perfil do Instagram é a fonte de verdade de "postou"; a pauta é o que o time acredita. A extração do perfil roda 3 vezes por dia, então um post de poucas horas pode demorar a aparecer. Os dois scripts rodam no hook de início de sessão; para atualizar na hora: `python scripts/status_instagram.py` e depois `python scripts/sincronizar_fila.py`.

Mudança de fila e artefato: quando o Hugo e a skill de Instagram mudam a sequência, o fluxo é (1) editar o JSON e o `.md` da sequência no sb_admin_team, (2) regerar e republicar o artefato, (3) rodar `python scripts/sincronizar_fila.py` aqui. O artefato do Hugo e a pauta do marketing leem o mesmo JSON, então não podem divergir; se divergirem, o script avisa.

## Regras para os agentes

- **Mari:** no início de toda sessão, lê o resumo da fila (já injetado pelo hook), abre a pauta e começa pelo bloco Fila prioritária. Se a fila mudou, **avisa o Hugo e os agentes afetados antes de qualquer outra coisa**, e diz qual peça sobe, qual sai e qual prazo muda. Só aceita produção fora da fila com autorização do Hugo.
- **Todos os agentes:** produzem na ordem da fila e no prazo da coluna "Entrega". Dúvida de prioridade: perguntar à Mari.
- **Vínculo pauta e fila:** ao abrir uma linha na pauta para uma peça da fila, colocar `[fila:P4]` (código do slot da fila) no título da linha. Linhas com `PAUSADA` ou `ARQUIVADA` no título são ignoradas na checagem.
- **Troca de peça na fila:** se o Hugo troca uma peça combinada em conversa (por exemplo, C-083 por C-046), a Mari marca a linha com o vínculo `[fila:Px]` e o script passa a apontar "substituição não registrada" até que a sequência do Hugo seja atualizada. Quem registra a troca na sequência é o Hugo com a skill de Instagram.
- O Hugo pode alterar a produção textual direto no time; a Mari só garante que a pauta reflita o que mudou.
