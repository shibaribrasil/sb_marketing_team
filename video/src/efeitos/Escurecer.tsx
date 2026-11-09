import React from "react";
import { AbsoluteFill, Easing, interpolate, useCurrentFrame } from "remotion";

// Escurecer a tela até o preto (e voltar do preto com o movimento contrário).
// Usado com o corpo do Hugo passando na frente da câmera: a tela escurece junto com o movimento.
// Curva aprovada pelo Hugo (08/11/2026): opacidade 0 → 0,92 → 1, com Easing.in(quad).
//
// Use dentro de uma <Sequence>: os quadros são relativos ao início dela.
//  - modo "escurecer": em `de` começa a escurecer, em `ate` chega a 92% e em `fim` a 100%.
//  - modo "clarear": o espelho exato; no quadro 0 da Sequence está 100% preto e em (fim - de)
//    está 100% claro. Os parâmetros são os mesmos do escurecer correspondente.

export type EscurecerProps = {
  modo: "escurecer" | "clarear";
  /** Quadro em que o escurecimento começa (modo escurecer). */
  de: number;
  /** Quadro em que chega a 92% (modo escurecer). */
  ate: number;
  /** Quadro em que chega ao preto total (modo escurecer). */
  fim: number;
  cor?: string;
};

export const Escurecer: React.FC<EscurecerProps> = ({ modo, de, ate, fim, cor = "#000" }) => {
  const f = useCurrentFrame();
  const total = fim - de;
  const opcoes = {
    easing: Easing.in(Easing.quad),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  } as const;
  const opacidade =
    modo === "escurecer"
      ? interpolate(f, [de, ate, fim], [0, 0.92, 1], opcoes)
      : interpolate(Math.max(0, total - f), [0, ate - de, total], [0, 0.92, 1], opcoes);
  return <AbsoluteFill style={{ backgroundColor: cor, opacity: opacidade }} />;
};

/** Duração (em quadros) do escurecimento ou da volta, para sincronizar áudio e Sequences. */
export const duracaoEscurecer = (de: number, fim: number): number => fim - de;
