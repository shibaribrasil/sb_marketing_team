# Pacotes do ecossistema Remotion — o que existe e o que vale instalar

Mapeado em 08/11/2026 (versão `4.0.541`, a mesma do projeto: todos os `@remotion/*` precisam estar na **mesma versão exata**). Descrição, licença e tamanho vêm do registro do npm; o "serve para a Shibari?" é avaliação do Davi. **Nada abaixo, além do que já está instalado, é instalado sem o aval do Hugo.** Como instalar: `(cd video && npm install --save-exact @remotion/<pacote>@4.0.541)`.

**Licença:** o Remotion é de uso gratuito para pessoa física; uso por empresa/equipe pede licença (decisão de 08/11/2026: uso pessoal do Hugo). Os pacotes MIT não têm restrição própria; os marcados "Remotion" seguem a licença do Remotion. Se o uso virar de equipe, reavaliar em remotion.dev/license.

## Já instalado
| Pacote | Para quê |
|---|---|
| `remotion` | Núcleo: `interpolate`, `spring`, `Easing`, `Sequence`, `OffthreadVideo`, `Audio`, `Freeze`, `staticFile`. Cobre cortes, fusões, zoom, escurecer, fade, movimento e texto |
| `@remotion/cli` | Comandos `render`, `still`, `ffprobe`, estúdio |
| `@remotion/google-fonts` | Fontes do Google (Instrument Serif já em uso) |
| `@remotion/transitions` | **Instalado em 08/11/2026** (aval do Hugo). Transições prontas com `TransitionSeries`. A licença aparece como "UNLICENSED" no `package.json`, mas é do mesmo repositório do Remotion, sem licença própria (só a transição `cube` é MIT): vale a licença do Remotion (uso pessoal) |
| `@remotion/motion-blur` | **Instalado em 08/11/2026.** `Trail` e `CameraMotionBlur` |
| `@remotion/layout-utils` | **Instalado em 08/11/2026.** `fitText`, `measureText` |
| `@remotion/light-leaks` | **Instalado em 08/11/2026.** Vazamentos de luz; traz `@remotion/effects` e `zod` |

## Já feito no código (`video/src/efeitos/`, sem pacote novo)
- **`TextoEsfera`**: texto em esfera, aprovado.
- **`Escurecer`** (modos escurecer e clarear): escurecer com o corpo e voltar do preto, aprovado.

## Candidatos, do mais ao menos útil para nós
| Pacote | O que faz | Peso | Serve para a Shibari? |
|---|---|---|---|
| `@remotion/transitions` | Transições prontas entre cenas (fade, slide, wipe, flip, relógio) com `TransitionSeries` | 0,5 MB; depende de `paths` e `shapes`; **licença "UNLICENSED" no npm** (conferir a página de licença antes de instalar) | **Sim.** Evita refazer à mão cada fusão e corte; boa para vídeos com várias cenas |
| `@remotion/captions` + `@remotion/install-whisper-cpp` | Legenda automática a partir da fala: transcreve (Whisper, **modelo de IA que roda local no PC**, baixa de ~150 MB a 1,5 GB) e queima a legenda em palavras | pequenos; Whisper pede baixar o motor e o modelo | **Só se houver vídeo com fala.** O teste atual não tem. Exige conferir o texto transcrito (a voz da marca vem da Julia/Ana, o Davi não reescreve) |
| `@remotion/light-leaks` | Vazamentos de luz (clarões quentes) sobre o vídeo | 0,01 MB; traz `zod` e `@remotion/effects`; licença Remotion | **Sim, para clima romântico/vela.** Dá para cobrir transições com um clarão |
| `@remotion/motion-blur` | Desfoque de movimento (`Trail`, `CameraMotionBlur`) | 0,03 MB; MIT | **Sim**, para zooms e movimentos rápidos ficarem naturais. Aumenta o tempo de render |
| `@remotion/noise` | Ruído suave (simplex) para movimento orgânico: tremor leve, grão, "respiração" da câmera | 0,01 MB; MIT | **Talvez.** Dá vida a texto e elementos parados |
| `@remotion/layout-utils` | Mede texto antes de desenhar (`fitText`, `measureText`) | 0,02 MB; MIT | **Sim para legenda e títulos**: garante que o texto cabe na área segura do Instagram |
| `@remotion/shapes` + `@remotion/paths` | Formas e caminhos em SVG, com animação de traço (`evolvePath`) | 0,15 e 0,31 MB; MIT | **Talvez.** A linha vertical scarlet da marca desenhando-se, molduras, sublinhados |
| `@remotion/fonts` | Carrega fonte local (arquivo `.ttf`/`.otf`) | 0,01 MB; MIT | **Quando a pasta `04_MARCA/tipografia` tiver os arquivos** (hoje vazia) |
| `@remotion/media-utils` | Informações de mídia e dados de áudio (ondas, picos), usa `mediabunny` | 0,12 MB; MIT | **Talvez.** Barra de áudio, sincronizar com batida de música |
| `@remotion/sfx` | Biblioteca de efeitos sonoros | 0,01 MB; MIT | **Conferir a licença de cada som antes de usar.** Regra do time: áudio só com origem e licença registradas |
| `@remotion/lottie`, `@remotion/rive`, `@remotion/gif` | Animações vetoriais (Lottie, Rive) e GIF dentro do vídeo | 0,03 a 0,16 MB; licenças próprias | **Pouco.** Só se o Hugo tiver arquivos prontos dessas animações |
| `@remotion/animated-emoji` | Emojis animados do Google | 0,17 MB; MIT | **Não.** A marca não usa emoji |
| `@remotion/three`, `@remotion/skia` | 3D (React Three Fiber) e gráficos 2D avançados (Skia) | 0,05 e 0,01 MB; MIT, mas pesados em render e complexidade | **Não por enquanto.** Só para um efeito que o Remotion básico não faça |
| `@remotion/preload`, `@remotion/media-parser`, `@remotion/webcodecs` | Pré-carregamento e leitura/conversão de vídeo no navegador | 0,01 a 2,8 MB; licença Remotion | **Não.** Para aplicações web, não para render local |

## Recomendação do Davi para a primeira rodada
1. **`@remotion/transitions`** (depois de conferir a licença na página do npm) e **`@remotion/motion-blur`**: base de todo corte e movimento.
2. **`@remotion/layout-utils`**: texto sempre dentro da área segura.
3. **`@remotion/light-leaks`**: quando o briefing pedir clima de vela ou romance.
4. **`@remotion/captions` + `@remotion/install-whisper-cpp`**: só quando houver o primeiro vídeo com fala.

Primeira rodada **instalada em 08/11/2026** (transitions, motion-blur, layout-utils, light-leaks). Ainda não usados em nenhuma peça: testar no primeiro briefing que pedir. Captions e Whisper, e os demais, ficam na lista para quando um briefing pedir.
