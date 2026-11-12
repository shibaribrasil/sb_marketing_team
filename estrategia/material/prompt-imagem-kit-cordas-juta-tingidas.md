# Prompt final: kit shibari iniciante, cordas de juta tingidas (post de 13/11/2026, slot P22)

**Status:** escrito, NÃO gerado. Só roda com o "sim" do Hugo (regra de 10/11/2026: ajuste = prompt completo novo do zero, sem editar imagem de IA, teto de 2 rodadas).
**Modelo:** `gemini-3.1-flash-image`, 4:5, 4K. Custo: ~US$ 0,15 por imagem; 3 chamadas com o mesmo prompt = ~US$ 0,45. Se a corda sair acetinada de novo, o `gemini-3-pro-image` custa ~US$ 0,24 por imagem em 4K.
**Quem roda:** `fotografo` (chamar com `model: opus`, `effort: medium`), com o auxiliar de várias referências (o `gerar_imagem_ia.py` só aceita 1).

## O que cada erro das rodadas anteriores virou neste prompt

| Problema apontado pelo Hugo | Onde está resolvido |
|---|---|
| Corda rígida, uniforme, arrumadinha | Seção ROPE TEXTURE AND HANG (assimetria, gravidade) e DO NOT |
| Tecido não encosta nas cordas | Seção WEIGHT, CONTACT AND LIGHT (tecido deforma, enruga e sobe contra a corda) |
| Duas pontas com nós separadas, laço artificial, terceira linha | Seção ANATOMY (exata) |
| Fiapos grossos, como ruído | ROPE TEXTURE (só penugem curta) e DO NOT |
| Corda "lavada", sem textura | Referências reais da corda como autoridade absoluta + texto de fibra e sulco |
| Tesoura sem as características, lavada | SCISSORS: gravações em relevo "143°C AUTOCLAVE 290°F" e etiqueta "STAINLESS", lâmina escovada, plástico preto fundo |
| Sem peso, sem sombreamento, objetos "colados" no tecido | WEIGHT, CONTACT AND LIGHT (sombra de contato, projetada e oclusão nas dobras) |
| Perda de qualidade a cada geração | Geração do zero, sem nenhuma imagem de IA como referência |
| Respiro das bordas | FRAMING (objetos menores, 55% da largura) e, se mesmo assim faltar, estender o linho como na ia-013 |

## Referências a preparar (todas reais; nenhuma imagem de IA)

Rotuladas no envio como no texto do prompt.

- **IMAGE 1** (corda inteira): `01_PRODUTOS\900119_corda-de-juta-tratada-colorida-6mm-x-8m\fornecedor\100278_caramelo_variante.webp`, recorte x 780-3020, y 380-1612, com o "11.KHAKI" e a marca KNOTITUDE apagados em cópia temporária (nunca no original).
- **IMAGE 1B, 1C, 1D** (recortes ampliados da mesma foto): banda (x 1380-2100, y 790-1510), alças (x 860-1440, y 440-1020), nós e franjas (x 1960-2400, y 1726-2140, ampliado 2x).
- **IMAGE 2** (tesoura inteira, vista de cima, a mesma do kit): `01_PRODUTOS\600001_kit-shibari-iniciante\foto\bruto\IMG_0840.JPG`, recorte x 200-2520, y 2230-3300. É a foto que mostra as gravações.
- **IMAGE 2B** (recorte ampliado do cabo grande e da etiqueta junto ao pivô, para o relevo "143°C AUTOCLAVE 290°F" e "STAINLESS"): da mesma IMG_0840, região do pivô e dos cabos.
- **IMAGE 2C** (forma limpa da lâmina e da ponta romba curva): `01_PRODUTOS\900022_tesoura-de-seguranca\foto\bruto\IMG_0796.JPG` recortada. Não usar IMG_0798 (tem mão) nem a IMG_0797 inteira (perspectiva oblíqua).
- **IMAGE 3** (só caimento da juta): `01_PRODUTOS\900003_corda-de-juta-tratada-6mm-x-8m\foto\bruto\IMG_9630.jpg`.
- **IMAGE 4 (opcional, decidir com o Hugo)**: recorte apertado de `600001_kit-shibari-iniciante\foto\bruto\IMG_6932.JPG` (ou 6933), só na junção da corda e da tesoura com a superfície, para mostrar como a sombra real do kit cai. Recortar fora as folhas, o vaso e a mesa de madeira. Serve só de referência de peso e sombra.

## Prompt (enviar em inglês, inteiro)

```text
Create ONE new photograph from scratch (this is a fresh generation, not an edit of any image). A real, editorial product photograph of a shibari starter kit: two hanks of dyed jute rope and one pair of safety scissors, lying on a crumpled raw linen cloth, shot straight from above. Vertical 4:5, 4K. It must look like a real photograph taken with a real camera, not a render and not an illustration.

=== REFERENCE IMAGES AND THE ROLE OF EACH ===
All reference images are real photographs. None of them shows the final scene; the scene is described only in words below.
IMAGE 1 (real studio photo of the actual rope, full hank) + IMAGES 1B, 1C, 1D (enlarged real crops of the same rope: 1B = the wrapped middle band, 1C = the folded loops, 1D = the two overhand knots with their short fibre tassels): the ABSOLUTE AUTHORITY for the rope's texture, fibre, twist, surface fuzz and colour. Copy the rope's material from these exactly, at the same level of detail.
IMAGE 2 (real top-down photo of the actual scissors) + IMAGE 2B (enlarged real crop of the handles with their moulded markings) + IMAGE 2C (clean real photo of the same scissors showing the bent blades and the blunt curved tip): the ABSOLUTE AUTHORITY for the scissors. Reproduce this exact object, including its markings and its materials.
IMAGE 3 (real photo of natural jute hanks): ONLY for how real jute hanks drape, sag and relax. Ignore its golden colour completely.
[IF IMAGE 4 IS USED] IMAGE 4 (real photo of the real kit on a surface): ONLY for how the real rope and scissors press on a surface and how their shadows fall (softness, depth, darkness). Ignore its background, table, plants, colours and light colour.

=== THE SCISSORS (get this right first) ===
Bandage / trauma shears, about 19 cm long, exactly the object in images 2, 2B and 2C.
- Handles: deep, rich black matte plastic with a very slight sheen on the raised edges, with a faint moulded texture, NOT flat grey, NOT washed out. Two open rings: one large oval, one smaller round. The plastic carries tiny MOULDED (raised relief, same black as the plastic, low contrast, not printed, not white) markings exactly as in image 2B: along the flat top of the large handle, near the pivot, the small text "143°C AUTOCLAVE 290°F"; and on the other handle half, next to the pivot, a small rectangular recessed label plate with the word "STAINLESS". These two markings are tiny and subtle (at the size of the finished photograph they are small marks, barely readable), they are part of the real object and must be there as small moulded plates in the right place. Copy their position and size from image 2B. Do NOT enlarge them, do NOT print them in white or as flat ink, and do NOT write any other letters, logos or marks anywhere.
- Blades: brushed stainless steel, satin with fine directional brushing, NOT chrome-mirror and NOT flat pale grey. They reflect a little of the warm beige linen around them, with soft highlights, never pure white. The blade section is bent at an angle to the handle line at the pivot. One round rivet at the pivot, a pressed groove (channel) along each blade, a finely serrated edge on the lower blade. The tip is BLUNT and ROUNDED: the longer blade ends in a small flat curved paddle, as in images 2B and 2C. No sharp point.
- This is NOT thread snips, NOT embroidery scissors, NOT garden shears, NOT a pair with a U-shaped handle or pointed blades.
- The scissors are about two thirds the length of a hank.

=== THE ROPE ===
Two identical hanks of 3-strand twisted jute rope, 6 mm thick, each hank is ONE 8-metre rope. Colour is the measured colour of image 1: ochre-rust caramel, around #A84C09 / #AC4807 / #B14A07 on the band, with natural variation from light orange on the tops of the strands to brown in the grooves. Do not let the shadows of the scene make the rope darker, redder or more brown than image 1: keep its local colour, with its lit parts at the colour of image 1.

=== ANATOMY OF EACH HANK (must be exact) ===
Each hank is a single rope folded into a bundle of loops and held in the middle by several tight turns of the same rope wrapped around the bundle (the band). A hank has exactly TWO rope ends. Both ends come out TOGETHER from inside the band, on the SAME side of the band (the lower end of the band), as two parallel lines running side by side, and hang together to their overhand knots; each knot is followed by a short brush of untwisted fibres (a short tassel, about 2 to 3 cm). On the other side of the band there are only folded loops. No extra loop coming out of the band, no big artificial bow, no third line, no ends coming out on opposite sides. Every hank therefore shows exactly TWO knots; two hanks show four knots in total, all four clearly visible.

THE BAND (a precise description, copy image 1 and image 1B exactly): the band is one tidy, compact cylinder made of 6 to 8 neat helical turns of the same rope, lying side by side and slightly slanted, each turn right next to the previous one, like a coil of thread on a spool, wrapped tightly around the whole bundle. It has ONE single point where a line goes in or comes out: at the lower end of the band, where the two tails leave together. The upper end of the band is simply closed and rounded, with the folded loops of the bundle emerging from it, and NOTHING else: no loose end, no tail, no tuck, no crossing, no pleat, no folded flap, no "ear", no second entry, no visible start or finish of the wrapping rope on that side. The band must not look like rope entering or leaving from both of its ends. The turns of the band are all the same thickness as the rope; they do not overlap in a pile and do not fold over at the ends.

=== FRAMING AND BREATHING ROOM (strict) ===
Wide, calm framing: the camera is far enough away that the whole group (hanks and scissors together) occupies only the central area, about 55% of the frame width and about 50% of the frame height. Every knot, tassel, loop and the whole scissors stay at least 18% of the frame width away from EVERY edge (top, bottom, left, right). Everything outside that central area is plain crumpled linen with nothing on it. Small objects in a lot of linen is correct. The scissors' rings must not come near the right edge.

=== COMPOSITION (single arrangement) ===
Two hanks and one pair of scissors grouped in the middle of a large crumpled linen cloth. Two hanks side by side, both standing roughly upright and tilted a little, nestled against each other: the LEFT hank lies on a diagonal from the upper left to the lower right, its upper part tucked under a large, soft fold of the same linen that comes down from the upper left corner of the frame (the cloth lies OVER the top of that hank and presses on it, with a soft shadow on the rope); the RIGHT hank is taller, almost vertical, leaning very slightly to the right, its loops at the top and its two tails with their knots hanging down at the bottom, in front of the cloth. The two hanks are NOT symmetrical or identical: different heights, different tilt, loops and band not a copy of each other. Both hanks lean on one another where they touch, the right one resting partly on the edge of the left one. The scissors lie to the right of the right hank, a little separated from it, almost vertical (slightly diagonal), tip pointing up, handles at the bottom, the large oval ring on the left and the smaller round ring on the right, resting on a small ripple of the cloth. A single continuous large fold of linen rises from the upper left; the rest of the cloth has smaller soft wrinkles.

=== TEXTURE OF THE ROPE (the main point of the image) ===
Matte, dry, fibrous jute exactly like images 1, 1B, 1C, 1D: deep dark grooves between the strands, each strand clearly showing its individual fibres, tonal variation along every strand, and only a very fine, very short fuzz along the edges. The twist is crisp and visible on every turn of the band and every loop. No sheen, no silky or satin highlights on the rope.
The hanks are relaxed and heavy, not arranged: loops of unequal length that sag, a band that is slightly irregular, turns not all perfectly parallel, a slightly different curve in each loop. They obey gravity and settle into the cloth.

=== WEIGHT, CONTACT AND LIGHT (the objects must really sit ON the cloth) ===
- Light: ONE soft natural window light from the LEFT, slightly from above, a little higher than the horizon. A soft but clearly directional light: the left sides of the rope strands and of the scissors are lit, the right sides are in shade. The same single light direction for every object and every fold in the picture. Warm neutral colour.
- Weight of the rope: each hank is heavy (about 250 g of dense jute). It visibly presses into the linen: the cloth under and around it is dented and compressed, the weave is pushed down at the contact, and small wrinkles radiate outward from the edges of each hank, as when a heavy object rests on a soft cloth. The underside of the loops touches the cloth with no gap.
- Contact shadow: where rope touches linen there is a thin, very dark, soft contact shadow (almost black in the tightest creases, between the loops and under the strands), so there is no light gap and no outline halo between rope and cloth.
- Cast shadow: each hank throws a clear, soft shadow onto the linen toward the RIGHT and slightly DOWN, about one third of the hank's width long, darkest next to the rope and fading out gradually, following the wrinkles of the cloth (it bends over folds, it does not fall flat like a drop-shadow). The shadow colour is a warm deep brown-taupe, not grey and not black. The knots and tassels cast small shadows too.
- Cloth over rope: where the linen fold rises across the base of the left hank, the cloth has a soft shadow on the rope and a shadow line along the fold's edge; the rope under the cloth is darker.
- Scissors: they rest on the cloth with their full weight; a thin dark contact shadow runs along the whole underside edge of the handles and of the blades; the large and the small ring cast shadow inside the rings onto the linen, and through the rings the linen shows; the blades sit very slightly above the cloth, so a thin, darker line of shadow shows under the steel edge; the steel shows a soft reflection of the beige cloth. They never float.
- Overall: gentle depth and shading everywhere, soft occlusion in every fold of the linen and under every object, a natural light falloff. No pale halo or glow around any object. No flat, evenly lit "cut-out" look.

=== SCENE ===
Flat lay, camera exactly 90 degrees overhead, no tilt, no perspective. One single continuous piece of raw, undyed beige linen fills the whole frame, crumpled with soft volume in the folds, visible weave and natural slub irregularities, crisp fibre detail. Restrained palette: beige and nude; the rope is the only strong colour. No flash, no specular highlights, no vignette.

=== REALITY CHECK (before you finish) ===
Compare mentally with the real reference photos. The rope must have as much fibre detail, groove depth and fuzz as images 1, 1B, 1C, 1D. The scissors must show the markings, the steel brushing and the deep black plastic of images 2, 2B, 2C. The objects must look as heavy and as grounded as the objects in a real photograph: pressing into the cloth, with shadows that fall the same way everywhere.

=== DO NOT (errors from earlier attempts) ===
- DO NOT make the rope smooth, washed-out, cotton-like, silky or plastic-like, with flat uniform colour, a faded twist or no grooves.
- DO NOT add long, thick stray fibres or hairs that look like noise, scratches, sewing thread or dirt. No long hairs at all; only the subtle short fuzz of image 1.
- DO NOT make the hanks stiff, symmetric, moulded, arranged into a perfect X, or with identical loops.
- DO NOT make anything look pasted, floating or cut out over the cloth; DO NOT leave a light gap, a halo or a white outline between an object and the cloth.
- DO NOT use hard, flat, grey or black drop-shadows; DO NOT use a different light direction for different objects; DO NOT skip the shadows.
- DO NOT turn the fold into a separate flap of smoother, lighter fabric with a cut hem, like a napkin. ONE single continuous cloth, no hem, no seam, no second piece of fabric.
- DO NOT render the linen smooth, blotchy or satin-like.
- DO NOT separate the two ends of the same hank; DO NOT make a big artificial loop coming out of the band; DO NOT add a loop that looks like a third line; DO NOT let the tails come out of the loops instead of the band; DO NOT show only three knots.
- DO NOT make the band look as if rope enters or leaves it from BOTH ends: no folded "ear", pleat, flap, loose end, tuck or crossing at the upper end of the band; the only line that goes in or out of the band is the pair of tails at its lower end. DO NOT make the band a pile of overlapping turns: it is a neat helical coil of 6 to 8 turns.
- DO NOT draw thread snips, sewing or embroidery scissors, garden shears, scissors with a pointed tip or a U-shaped handle. DO NOT render the scissors plastic grey or washed, DO NOT print the markings in white or as flat ink, DO NOT invent any letters other than the two moulded markings of image 2B.
- DO NOT let anything come closer than 18% of the width to any edge.
- DO NOT make the rope redder or darker than image 1.
- DO NOT include any watermark (no "KNOTITUDE", no "KHAKI"), any other text, hands, people, bed, box, plants, wooden table, or any other object.
```

## Depois de gerar (conferência antes de mostrar ao Hugo)

1. Corda com tanta fibra e sulco quanto a foto real (e sem laço artificial nem terceira linha).
2. Tesoura com "143°C AUTOCLAVE 290°F" e "STAINLESS" legíveis e certas; nenhuma outra letra.
3. Sombra de contato escura, sombra projetada para a direita e para baixo, igual em todos os objetos; sem halo claro.
4. Respiro de 15% ou mais nas quatro bordas (medir). Se faltar só um pouco, estender o linho com trechos reais, como na ia-013, em vez de gerar de novo.
5. Gravar no banco com marca de IA (XMP), sRGB e sem sobrescrever as versões anteriores. Apagar as versões superadas só com o "sim" do Hugo.
