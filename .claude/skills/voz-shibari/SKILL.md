---
name: voz-shibari
description: Voz da Shibari Brasil — skill fina que aponta para o núcleo da voz (`sb_cerebro`). Carregue ANTES de escrever, revisar ou aprovar qualquer texto da Shibari Brasil para cliente ou público: post, legenda, story, roteiro, anúncio, descrição de produto, e-mail, blog, WhatsApp, mensagem de atendimento, título e meta. Traz a voz do Hugo (praticante entusiasta), o tom por contexto, o vocabulário e o que evitar. NÃO guarda a voz aqui: lê do núcleo, que é a fonte única.
---

# Voz Shibari (skill fina)

Esta skill **não contém a voz**. Ela manda ler o núcleo, para existir uma só fonte e nenhuma cópia ficar velha.

## Quando carregar
Sempre que for escrever, revisar ou aprovar texto da marca: post, legenda, story, roteiro de vídeo, anúncio, descrição de produto, título e meta, e-mail, blog, WhatsApp, atendimento. Vale para criar e para editar.

## O que ler (nesta ordem)
1. **`sb_cerebro/02_voz/voz.md`**: a voz, o teste de 4 perguntas, quem fala em cada lugar, produto, desejo, segurança, termos do meio e o que evitar. É o que importa em quase todo pedido.
2. **`sb_cerebro/02_voz/vocabulario.md` e `termos-do-meio.md`**, quando houver termo do meio (japonês ou inglês) ou dúvida de vocabulário.
3. **`sb_cerebro/01_identidade/identidade.md`**, quando precisar saber quem fala, no que a marca acredita, para quem fala e até onde o Hugo aparece. O detalhe de cada posição está em `posicoes.md`.
4. **`sb_cerebro/02_voz/tom.md`**, para exemplos aprovados e reprovados de texto.

`sb_cerebro` é uma **pasta irmã** deste projeto (os três repositórios, `sb_admin_team`, `sb_marketing_team` e `sb_cerebro`, ficam clonados lado a lado e atualizados com `git pull`). **Se a pasta não existir na máquina, pare e avise o Hugo:** não escreva sem a voz.

## Precedência
O núcleo vence o `tom-de-voz.md` do Guia da Marca, os resumos de tom embutidos em outras skills e qualquer regra de voz copiada. A **técnica de escrita por canal** (lista negra antirrobô, ritmo, SEO, autorrevisão) vem do `hab-produtor-textual` (`sb_marketing_team`), que também abre pela voz. As regras fixas do `CLAUDE.md` do projeto continuam acima de tudo.

## Regra de manutenção
Toda correção do Hugo a um texto gera uma **contrapartida no núcleo** (regra P74): o agente propõe a regra equivalente ao lado do texto revisado, com o contexto e não só a frase literal, e só grava no núcleo depois do "sim" do Hugo. A correção não vai para esta skill nem para o texto-base de um agente.

## O que esta skill NÃO faz
- Não decide estrutura de formato (cada formato tem o seu dono: descrição de produto é do `cadastrador`; formatos de conteúdo são do marketing).
- Não decide preço, oferta, nem fato de produto: fato vem do Notion (Catálogo — Produtos) ou do Hugo.
