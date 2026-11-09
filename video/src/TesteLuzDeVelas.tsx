import React from "react";
import {
  AbsoluteFill,
  Composition,
  OffthreadVideo,
  Sequence,
  staticFile,
} from "remotion";
import { Escurecer, TextoEsfera } from "./efeitos";
import type { Pedaco } from "./efeitos";

// Teste "castiçal trend" (08/11/2026, aprovado pelo Hugo): C0228.MP4, Sessão 23-10-26
// (G:\Meu Drive\SB Audiovisual\02_GERAL\pratica\video\bruto\).
// O bruto é lido da pasta passada em --public-dir (cópia de trabalho), nunca do repositório.
// Entrega: G:\Meu Drive\SB Audiovisual\03_CONTEUDO\instagram-videos\vídeo-castical-trend\
const SRC = "C0228.MP4";
const FPS = 30;

// O corpo do Hugo cobre a câmera (~5,4 a 7 s) e a tela escurece junto com ele até o preto; a volta
// é o mesmo movimento ao contrário, com pelo menos 3 s de cena plena antes de a luz baixar (~30,8 s).
//   A  0,0 a 7,4 s    (vela acesa; o corpo cobre a câmera; a tela escurece até o preto)
//   C  25,5 a 47,5 s  (sai do preto com a mesma curva ao contrário; luz plena até ~30,8 s)
const q = (t: number) => Math.round(t * FPS);
const A_FIM = q(7.4); // 222
const ESCURECE_DE = q(5.5);
const ESCURECE_ATE = q(7.2);
const C_DE = q(25.5);
const C_QUADROS = q(47.5) - C_DE;
const C_INICIO = A_FIM;

export const DURACAO = C_INICIO + C_QUADROS;

const LINHAS: Pedaco[][] = [
  [{ t: "só quem tem um" }],
  [{ t: "castiçal", it: true }, { t: " desse no" }],
  [{ t: "quarto entende o quanto" }],
  [{ t: "é " }, { t: "romântico", it: true }, { t: " ir dormir" }],
  [{ t: "à " }, { t: "luz de velas", it: true }],
];

const cover = { width: "100%", height: "100%", objectFit: "cover" } as const;

const CenaA: React.FC = () => (
  <AbsoluteFill>
    <OffthreadVideo
      src={staticFile(SRC)}
      muted
      style={cover}
    />
    <Escurecer modo="escurecer" de={ESCURECE_DE} ate={ESCURECE_ATE} fim={A_FIM} />
  </AbsoluteFill>
);

const CenaC: React.FC = () => (
  <AbsoluteFill>
    <OffthreadVideo
      src={staticFile(SRC)}
      startFrom={C_DE}
      muted
      style={cover}
    />
    <Escurecer modo="clarear" de={ESCURECE_DE} ate={ESCURECE_ATE} fim={A_FIM} />
  </AbsoluteFill>
);

const Video: React.FC = () => (
  <AbsoluteFill style={{ backgroundColor: "#000" }}>
    <Sequence from={0} durationInFrames={C_INICIO}>
      <CenaA />
    </Sequence>
    <Sequence from={C_INICIO} durationInFrames={C_QUADROS}>
      <CenaC />
    </Sequence>
    {/* Texto fixo do início ao fim */}
    <TextoEsfera linhas={LINHAS} />
  </AbsoluteFill>
);

export const TesteLuzDeVelas: React.FC = () => (
  <Composition
    id="ReelTesteLuzDeVelas"
    component={Video}
    durationInFrames={DURACAO}
    fps={FPS}
    width={1080}
    height={1920}
  />
);
