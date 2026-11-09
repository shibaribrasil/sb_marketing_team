# Briefing de vídeo — [título da peça]

**Status:** rascunho | aprovado pelo Hugo em DD/MM/AAAA
**Preparado por:** Bia (com o Hugo) em DD/MM/AAAA · **Para:** Davi (`agente-video`)
**Texto aprovado:** `texto.md` (Julia/Ana) · **Direção visual:** `visual-spec.md` (Bia)

> Orientação do que vai ser feito no editor. **Pode mudar durante a edição**: toda mudança entra no "Registro de alterações" no fim, para o briefing continuar sendo a verdade da peça.

## 1. Ideia e intenção
O que o vídeo precisa transmitir e o que foi pensado (2 a 4 linhas): objetivo, sensação, o momento-chave e onde ele cai no vídeo.

## 2. Material de origem (bruto)
- Arquivo(s) e caminho no Drive (`02_GERAL`, `01_PRODUTOS` ou pasta do conteúdo): …
- Resolução, fps, duração, rotação, áudio original (tem fala? ruído?): …
- Mapa do bruto, com tempos (o que acontece em cada trecho, o que está bom, o que não presta, ex.: "braço na frente da câmera de 5,4 a 14 s"): …

## 3. Estrutura e cortes
- Duração desejada: … (Reel: 3 s a 15 min; padrão da marca 1080×1920, 30 fps)
- Roteiro em linhas, com tempos do bruto → tempos do vídeo final: …
- **Momento-chave cedo**: cena parada longa antes do ponto principal é recusada pelo Hugo.
- Trechos a **cortar** e por quê: …

## 4. Transições e efeitos
- Preferência do Hugo (ver "Efeitos disponíveis" abaixo): …
- Onde cada efeito entra e por quê (ex.: usar o corpo dele passando na frente da câmera como transição): …
- **Não usar** (reprovado antes ou sem sentido para a peça): …

## 5. Texto na tela
- Texto literal (vem do `texto.md`; o Davi não escreve nem altera): …
- Estilo: fonte, tamanho, cor, posição, formato (reto, curvo, em esfera), referência (print): …
- Aparece quando e por quanto tempo (fixo do início ao fim, por trecho…): …
- Respeitar a área segura do Instagram (sem texto nos ~250 px de baixo nem ~150 px de cima).

## 6. Legenda queimada (sim/não)
Se sim: o que aparece, de onde vem (fala transcrita, texto do `texto.md`), estilo.

## 7. Áudio
Original, música ou silêncio; se música, a origem e a licença (sem origem registrada, não usa). Fades e volumes: …

## 8. Capa
Qual quadro ou composição, com o tema legível na miniatura do grid (~130 px): …

## 9. Entrega
- Pasta: `G:\Meu Drive\SB Audiovisual\03_CONTEUDO\instagram-videos\[nome]\` (nome da pasta definido pelo Hugo)
- Arquivos: `video.mp4` (1080×1920, 30 fps, H.264 `yuv420p` + AAC) e `capa.jpg`
- Rascunho para o Hugo aprovar antes do render final.

## Efeitos disponíveis (o que o Davi já fez e testou)
- **Texto em esfera** (bloco de texto "estufado", Instrument Serif): pronto, componente `TextoEsfera` em `video/src/efeitos/`.
- **Escurecer com o corpo e voltar do preto ao contrário**: pronto, aprovado pelo Hugo, componente `Escurecer` em `video/src/efeitos/`.
- **Estilhaços digitais** (blocos que se encaixam): feito e rejeitado nesta peça.
- Cortes, fusões (dissolve), zoom que assenta, fade de áudio, texto reto: o Remotion faz sem dependência nova.
- **Pacotes que dá para instalar** (transições prontas, desfoque de movimento, vazamento de luz, legenda automática etc.): lista em `.claude/skills/agente-video/references/pacotes-remotion.md`.
- **Outro efeito:** descrever aqui; o Davi diz se faz com o que há ou se precisa de pacote novo (pede o aval do Hugo).

## Registro de alterações
| Data | O que mudou | Por quê / quem pediu |
|---|---|---|
| | | |
