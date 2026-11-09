import React, { useEffect, useRef, useState } from "react";
import { cancelRender, continueRender, delayRender } from "remotion";
import { loadFont } from "@remotion/google-fonts/InstrumentSerif";

// Texto "estufado" como se estivesse colado numa esfera (referência: print de Reel do Hugo).
// Instrument Serif (serifa condensada de alto contraste), palavras romanas e itálicas misturadas.
// O texto é desenhado num canvas com supersampling e deformado uma única vez (mapeamento inverso
// com interpolação bilinear); o resultado é fixo durante o vídeo todo.
//
// Regra do raio: ele deve ser da ordem da meia-diagonal do bloco de texto antes da deformação;
// com raio grande a esfera fica quase plana e as linhas ficam retas.

export type Pedaco = { t: string; it?: boolean };

export type TextoEsferaProps = {
  /** Cada linha é uma lista de pedaços; marque `it: true` nas palavras em itálico. */
  linhas: Pedaco[][];
  cor?: string;
  /** Tamanho da fonte em px, antes da esfera (no centro o texto cresce ~1,4x). */
  tam?: number;
  /** Entrelinha em em. */
  entrelinha?: number;
  /** Entreletras em em (negativo aperta). */
  entreletras?: number;
  /** Posição vertical do centro do bloco no vídeo (px). */
  centroY?: number;
  /** Raio da esfera em px. */
  raio?: number;
  /** 0 = sem esfera; 1 = esfera plena. */
  forca?: number;
};

const LARGURA = 1080;
const ALTURA = 1100;
const SS = 2;

const normal = loadFont("normal", { subsets: ["latin", "latin-ext"] });
const italico = loadFont("italic", { subsets: ["latin", "latin-ext"] });

type Cfg = Required<Omit<TextoEsferaProps, "linhas">>;

const desenharFonte = (ctx: CanvasRenderingContext2D, linhas: Pedaco[][], c: Cfg): void => {
  ctx.clearRect(0, 0, LARGURA * SS, ALTURA * SS);
  ctx.textBaseline = "alphabetic";
  ctx.fillStyle = c.cor;
  ctx.shadowColor = "rgba(0,0,0,0.55)";
  ctx.shadowBlur = 14 * SS;
  ctx.shadowOffsetY = 3 * SS;
  (ctx as unknown as { letterSpacing: string }).letterSpacing = `${c.entreletras * c.tam * SS}px`;

  const fonte = (it?: boolean) =>
    `${it ? "italic " : ""}${c.tam * SS}px "${it ? italico.fontFamily : normal.fontFamily}"`;
  const alturaLinha = c.entrelinha * c.tam * SS;
  const n = linhas.length;

  linhas.forEach((linha, i) => {
    const larguras = linha.map((p) => {
      ctx.font = fonte(p.it);
      return ctx.measureText(p.t).width;
    });
    const total = larguras.reduce((a, b) => a + b, 0);
    let x = (LARGURA * SS - total) / 2;
    const y = (ALTURA * SS) / 2 + (i - (n - 1) / 2) * alturaLinha + c.tam * SS * 0.3;
    linha.forEach((p, k) => {
      ctx.font = fonte(p.it);
      ctx.fillText(p.t, x, y);
      x += larguras[k];
    });
  });
};

// Para cada pixel de saída, busca o pixel de origem num raio menor (centro ampliado, bordas
// comprimidas): s = (1-F)·r + F·(2/π)·asin(r), r = distância ao centro / raio.
const aplicarEsfera = (origem: ImageData, destino: ImageData, c: Cfg): void => {
  const cx = LARGURA / 2;
  const cy = ALTURA / 2;
  const ow = origem.width;
  const oh = origem.height;
  const od = origem.data;
  const dd = destino.data;

  for (let y = 0; y < ALTURA; y++) {
    for (let x = 0; x < LARGURA; x++) {
      const dx = x + 0.5 - cx;
      const dy = y + 0.5 - cy;
      const r = Math.sqrt(dx * dx + dy * dy) / c.raio;
      let k = 1;
      if (r > 0 && r < 1) {
        const s = (1 - c.forca) * r + c.forca * ((2 / Math.PI) * Math.asin(r));
        k = s / r;
      }
      const sx = (cx + dx * k) * SS - 0.5;
      const sy = (cy + dy * k) * SS - 0.5;
      const x0 = Math.floor(sx);
      const y0 = Math.floor(sy);
      const fx = sx - x0;
      const fy = sy - y0;
      let ar = 0;
      let ag = 0;
      let ab = 0;
      let aa = 0;
      for (let j = 0; j < 2; j++) {
        for (let i = 0; i < 2; i++) {
          const px = x0 + i;
          const py = y0 + j;
          if (px < 0 || py < 0 || px >= ow || py >= oh) continue;
          const w = (i ? fx : 1 - fx) * (j ? fy : 1 - fy);
          const idx = (py * ow + px) * 4;
          const a = od[idx + 3] / 255;
          ar += od[idx] * a * w;
          ag += od[idx + 1] * a * w;
          ab += od[idx + 2] * a * w;
          aa += a * w;
        }
      }
      const o = (y * LARGURA + x) * 4;
      if (aa > 0) {
        dd[o] = ar / aa;
        dd[o + 1] = ag / aa;
        dd[o + 2] = ab / aa;
        dd[o + 3] = aa * 255;
      } else {
        dd[o + 3] = 0;
      }
    }
  }
};

export const TextoEsfera: React.FC<TextoEsferaProps> = ({
  linhas,
  cor = "#FFFACE",
  tam = 78,
  entrelinha = 0.93,
  entreletras = -0.02,
  centroY = 520,
  raio = 400,
  forca = 0.8,
}) => {
  const ref = useRef<HTMLCanvasElement>(null);
  const [handle] = useState(() => delayRender("texto-esfera"));

  useEffect(() => {
    const cfg: Cfg = { cor, tam, entrelinha, entreletras, centroY, raio, forca };
    (async () => {
      await Promise.all([normal.waitUntilDone(), italico.waitUntilDone()]);
      const origem = document.createElement("canvas");
      origem.width = LARGURA * SS;
      origem.height = ALTURA * SS;
      const octx = origem.getContext("2d");
      const dctx = ref.current?.getContext("2d");
      if (!octx || !dctx) throw new Error("canvas indisponível");
      desenharFonte(octx, linhas, cfg);
      const src = octx.getImageData(0, 0, origem.width, origem.height);
      const dst = dctx.createImageData(LARGURA, ALTURA);
      aplicarEsfera(src, dst, cfg);
      dctx.putImageData(dst, 0, 0);
      continueRender(handle);
    })().catch((e) => cancelRender(e));
    // desenhado uma vez só: as props são fixas durante o vídeo
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [handle]);

  return (
    <canvas
      ref={ref}
      width={LARGURA}
      height={ALTURA}
      style={{ position: "absolute", left: 0, top: centroY - ALTURA / 2 }}
    />
  );
};
