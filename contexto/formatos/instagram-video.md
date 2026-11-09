# Instagram Vídeo `instagram-videos`

**Objetivo:** Legenda de apoio para vídeos educativos/demonstrativos (ex: passo a passo de nó, técnica de amarração) publicados no Instagram. O vídeo carrega a demonstração — a legenda contextualiza e reforça pontos de segurança, sem repetir o que já está na tela.

**Plataforma:** Instagram (Reels ou vídeo de feed)

**Pasta de conteúdos:** `conteudos/instagram-videos/`

**Regras de escrita:** Seguir os Capítulos 1 e 2 da skill `hab-produtor-textual`.

---

### Fluxo de produção

1. Definir o território/técnica a ser demonstrada (a partir de um slot aprovado da fila ou pedido direto do Hugo)
2. **Briefing de vídeo** (`briefing-video.md`, modelo em `contexto/formatos/modelos/briefing-video-modelo.md`): a Bia prepara com o Hugo, depois do texto aprovado; sem ele o Davi não edita
3. Produção do vídeo: a gravação é do Hugo; a **edição é do Davi** (`agente-video`, Remotion, em `video/`), depois do texto aprovado e do `visual-spec.md` da Bia. O Davi entrega `video.mp4` e `capa.jpg` na pasta do conteúdo, no padrão de mídia para a API, depois de o Hugo aprovar o rascunho. Vídeo já editado pelo Hugo fora do Remotion segue direto para a Mari, com a mesma checagem de mídia
4. Julia escreve a legenda de apoio em `texto.md`
5. Ana revisa
6. Segue para **Pronto - Aguardando Publicação**

---

### Estrutura obrigatória de entrega

O arquivo `texto.md` de um Instagram Vídeo deve conter os campos abaixo:

---

**1. Legenda**
Texto de apoio ao vídeo.
- Abertura que contextualiza a técnica ou o tema demonstrado
- Desenvolvimento com pontos de atenção (segurança, execução) que complementam o vídeo — não descrevem o que já é visível nele
- Fechamento que reforça um cuidado de segurança ou aponta o próximo passo da prática
- Extensão: 60 a 150 palavras
- Máximo 5 hashtags ao final, após linha em branco

---

### Checklist de entrega (Julia preenche antes de passar para a Ana)

- [ ] Legenda entre 60 e 150 palavras
- [ ] Pontos de segurança relevantes à técnica estão presentes
- [ ] Legenda complementa o vídeo em vez de repeti-lo
- [ ] Máximo 5 hashtags ao final da legenda
- [ ] Nenhuma palavra da lista negra da hab-produtor-textual
- [ ] Autorevisão executada
- [ ] `briefing-video.md` pronto para o Davi (Bia) e atualizado com o que de fato foi feito (Davi)
