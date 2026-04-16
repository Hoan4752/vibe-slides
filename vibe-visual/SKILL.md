---
name: vibe-visual
description: >
  Create minimalist concept visuals in the Visualize Value style (Jack Butcher) —
  pure black OR white canvas, thin SVG strokes, one powerful idea per image.
  Trigger when Hoan says: "visualize this", "làm vibe visual", "VV style",
  "minimal concept visual", "vẽ ý tưởng này bằng hình đơn giản",
  "Jack Butcher style", hoặc muốn minh họa abstract concept/principle.
  Also trigger from vibe-slides (concept illustration panel) và vibe-design
  khi cần visual không có text nhiều.

  Library: đọc LIBRARY.md để tra 170 VV visuals theo theme.
---

# vibe-visual — Minimal Concept Visuals

Tạo visual theo ngôn ngữ thiết kế Visualize Value:
**một ý tưởng — một hình — tối giản tuyệt đối — mạnh như đòn**.

Xem `LIBRARY.md` để tra 170 visual theo theme → pattern.

---

## BƯỚC 1: Tra LIBRARY.md trước

Trước khi build bất cứ thứ gì:
1. Đọc `LIBRARY.md` → tìm concept gần nhất với yêu cầu
2. Xác định PATTERN phù hợp
3. Mô tả concept → hỏi Hoan confirm → build

---

## Design DNA — Bất Biến

### Palette (chọn 1 trong 2 mode)

```css
/* DARK MODE (mặc định) */
--vv-bg:     #000000;   /* pure black */
--vv-stroke: #ffffff;   /* pure white */
--vv-text:   #ffffff;
--vv-dim:    #888888;   /* secondary elements: P7 truth line */
--vv-fill:   #ffffff;   /* intentional fill only: P5 wedge, P9 arrowheads */

/* LIGHT MODE (embed vibe-slides light theme, hoặc khi Hoan yêu cầu) */
--vv-bg:     #ffffff;
--vv-stroke: #000000;
--vv-text:   #000000;
--vv-dim:    #777777;
--vv-fill:   #000000;
```

**Rule:** Chỉ cần swap `--vv-bg` và `--vv-stroke` để convert dark ↔ light. Geometry không thay đổi.

### Typography

```css
font-family: 'Courier New', monospace;
font-size:   11–13px;
text-transform: uppercase;
letter-spacing: 0.12–0.20em;
font-weight: 400;
fill: var(--vv-text);
```

Tuyệt đối KHÔNG: font > 14px, bold, serif/sans-serif, nhiều font weights.

### Canvas

```
Canvas:       1080×1080px | 1080×1350px (portrait)
SVG viewBox:  "0 0 1080 1080"
Stroke width: 1–1.5px (mỏng là đặc trưng)
Negative space: ≥ 60% canvas
```

### Hard Rules
1. ONE concept per visual
2. No fills trừ P5 wedge, P9 arrowheads
3. No gradient, shadow, blur
4. Text ≤ 8 từ/dòng, max 2 dòng
5. 1 visual = 1 pattern thuần
6. SVG dùng CSS vars (`stroke="var(--vv-stroke)"`)

---

## 12 Pattern Templates

### P1 — Shape Progression
**Concept:** Evolution, iteration, mastery, redefinition
**Structure:** 5–8 polygons trải ngang, tăng dần số cạnh.

```javascript
// Helper: polygon points
function polygonPoints(cx, cy, r, sides) {
  return Array.from({length: sides}, (_, i) => {
    const a = (i * 2 * Math.PI / sides) - Math.PI / 2;
    return `${(cx + r * Math.cos(a)).toFixed(1)},${(cy + r * Math.sin(a)).toFixed(1)}`;
  }).join(' ');
}
// 7 shapes at x=160,280,400,520,640,760,880 y=500 r=42
// n = 3(triangle), 4(diamond), 5, 6, 7, 8, chaos/target
```

```svg
<polygon points="[use helper]" fill="none" stroke="var(--vv-stroke)" stroke-width="1.2"/>
<!-- 2 optional text lines (top + bottom) -->
<text x="540" y="360" text-anchor="middle" fill="var(--vv-text)"
  font-family="monospace" font-size="12" letter-spacing="4">BECOME THE BEST IN THE WORLD AT WHAT YOU DO.</text>
<text x="540" y="700" text-anchor="middle" fill="var(--vv-text)"
  font-family="monospace" font-size="12" letter-spacing="4">KEEP REDEFINING WHAT YOU DO UNTIL THIS IS TRUE.</text>
```

---

### P2 — Comparison Diptych
**Concept:** X vs Y, before/after, duality, contrast
**Structure:** 2 elements trái-phải, labels bên dưới, negative space ở giữa.

```svg
<!-- LEFT: complex/messy (V.1) — center x≈300 -->
<g transform="translate(230, 410)">
  <rect x="0"  y="0"  width="18" height="18" fill="none" stroke="var(--vv-stroke)" stroke-width="1"/>
  <rect x="22" y="8"  width="18" height="18" fill="none" stroke="var(--vv-stroke)" stroke-width="1"/>
  <rect x="8"  y="24" width="18" height="18" fill="none" stroke="var(--vv-stroke)" stroke-width="1"/>
  <rect x="32" y="20" width="18" height="18" fill="none" stroke="var(--vv-stroke)" stroke-width="1"/>
  <rect x="-4" y="30" width="18" height="18" fill="none" stroke="var(--vv-stroke)" stroke-width="1"/>
  <!-- +6 more scattered rects -->
</g>
<!-- RIGHT: clean/simple (V.N) — center x≈750 -->
<rect x="660" y="415" width="175" height="135" fill="none" stroke="var(--vv-stroke)" stroke-width="1.2"/>
<!-- Labels -->
<text x="300" y="640" text-anchor="middle" fill="var(--vv-text)"
  font-family="monospace" font-size="11" letter-spacing="3">V.1</text>
<text x="747" y="640" text-anchor="middle" fill="var(--vv-text)"
  font-family="monospace" font-size="11" letter-spacing="3">V.674</text>
```

---

### P3 — Growth Curves
**Concept:** Linear vs exponential, compound, learning curve
**Structure:** Zigzag = linear. Smooth curve = exponential. 1 hoặc 2 curves.

```svg
<!-- Portrait layout: LEFT=jagged, RIGHT=exponential -->
<polyline
  points="150,820 200,790 200,760 255,730 255,700 310,670 310,640 365,610 365,580 420,555"
  fill="none" stroke="var(--vv-stroke)" stroke-width="1.3"/>
<path d="M 580,860 C 600,858 640,845 700,800 S 820,680 900,520 T 950,280"
  fill="none" stroke="var(--vv-stroke)" stroke-width="1.3"/>
```

---

### P4 — Grid Matrix
**Concept:** Systems, complexity, sequences, hierarchy
**Structure:** Grid of cells, hoặc sequence của boxes + arrows.

```svg
<!-- Sequence variant (P4b): THOUGHT → SAID → HEARD → UNDERSTOOD -->
<rect x="80"  y="490" width="160" height="58" fill="none" stroke="var(--vv-stroke)" stroke-width="1"/>
<line x1="242" y1="519" x2="282" y2="519" stroke="var(--vv-stroke)" stroke-width="1"/>
<polygon points="279,514 291,519 279,524" fill="var(--vv-fill)" stroke="none"/>
<text x="160" y="523" text-anchor="middle" fill="var(--vv-text)"
  font-family="monospace" font-size="10" letter-spacing="2">THOUGHT</text>
<!-- Repeat for SAID (x=294), HEARD (x=508), UNDERSTOOD (x=722) -->
```

---

### P5 — Ratio Pie
**Concept:** Execution gap, said vs done, 80:20, proportion
**Structure:** Circle outline + tiny filled wedge + legend.

```svg
<circle cx="540" cy="480" r="200" fill="none" stroke="var(--vv-stroke)" stroke-width="1.3"/>
<!-- 5% wedge (18°): from top clockwise -->
<!-- End point: x=540+200*sin(18°)≈601.6, y=480-200*cos(18°)≈290.4 -->
<path d="M 540,480 L 540,280 A 200,200 0 0,1 601.6,290.4 Z"
  fill="var(--vv-fill)" stroke="none"/>
<!-- Legend -->
<circle cx="677" cy="715" r="5" fill="none" stroke="var(--vv-stroke)" stroke-width="1"/>
<text x="690" y="720" fill="var(--vv-text)" font-family="monospace" font-size="12" letter-spacing="3">SAID</text>
<circle cx="677" cy="741" r="5" fill="var(--vv-fill)" stroke="none"/>
<text x="690" y="746" fill="var(--vv-text)" font-family="monospace" font-size="12" letter-spacing="3">DONE</text>
```

**Wedge angle:** θ = percentage × 360. End: x=cx+r×sin(θ°), y=cy-r×cos(θ°). large-arc-flag=0 nếu θ≤180.

---

### P6 — Bar Chart + Gap
**Concept:** Growth requires discomfort, compounding, hidden cost
**Structure:** Bars tăng dần (solid) + dotted extension dưới baseline (pain/cost).

```svg
<!-- Baseline y=620. Bars x=240..770, heights tăng dần -->
<line x1="240" y1="620" x2="240" y2="605" stroke="var(--vv-stroke)" stroke-width="1.5"/>
<!-- ... more bars increasing ... -->
<line x1="770" y1="620" x2="770" y2="365" stroke="var(--vv-stroke)" stroke-width="1.5"/>
<!-- Dotted below (pain): -->
<line x1="240" y1="620" x2="240" y2="650" stroke="var(--vv-stroke)" stroke-width="1" stroke-dasharray="3,4"/>
<line x1="770" y1="620" x2="770" y2="790" stroke="var(--vv-stroke)" stroke-width="1" stroke-dasharray="3,4"/>
<!-- Caption: -->
<text x="540" y="900" text-anchor="middle" fill="var(--vv-text)"
  font-family="monospace" font-size="12" letter-spacing="4">IF IT DOESN'T HURT, IT'S NOT GROWTH.</text>
<line x1="732" y1="905" x2="852" y2="905" stroke="var(--vv-stroke)" stroke-width="0.8"/>
```

---

### P7 — Signal vs Noise
**Concept:** Truth vs trend, fundamentals vs hype, signal vs noise
**Structure:** Dim diagonal = TRUTH. White sine wave oscillating around it = TREND.

```svg
<!-- Diagonal (dim/gray) -->
<line x1="180" y1="800" x2="900" y2="240" stroke="var(--vv-dim)" stroke-width="0.9"/>
<!-- Sine wave (white, thicker) ~4 oscillations crossing diagonal -->
<path d="M 180,800 C 220,770 245,690 285,710 S 345,800 385,765
         S 445,665 485,685 S 545,775 585,735
         S 645,625 685,645 S 745,730 785,685 L 900,580"
  fill="none" stroke="var(--vv-stroke)" stroke-width="1.3"/>
<!-- Legend -->
<line x1="660" y1="875" x2="695" y2="875" stroke="var(--vv-dim)"    stroke-width="0.9"/>
<text x="702" y="879" fill="var(--vv-text)" font-family="monospace" font-size="11" letter-spacing="3">TRUTH</text>
<line x1="660" y1="898" x2="695" y2="898" stroke="var(--vv-stroke)" stroke-width="1.3"/>
<text x="702" y="902" fill="var(--vv-text)" font-family="monospace" font-size="11" letter-spacing="3">TREND</text>
```

---

### P8 — Spatial Scale Contrast
**Concept:** Small now vs large potential, leverage, "you are here"
**Structure:** Tiny element (grid) bottom-left. Large element (rect/L-shape) top-right.

```svg
<!-- Small: row of 8 squares, bottom-left -->
<g transform="translate(110, 500)">
  <rect x="0"   y="0" width="24" height="24" fill="none" stroke="var(--vv-stroke)" stroke-width="1"/>
  <rect x="28"  y="0" width="24" height="24" fill="none" stroke="var(--vv-stroke)" stroke-width="1"/>
  <rect x="56"  y="0" width="24" height="24" fill="none" stroke="var(--vv-stroke)" stroke-width="1"/>
  <rect x="84"  y="0" width="24" height="24" fill="none" stroke="var(--vv-stroke)" stroke-width="1"/>
  <rect x="112" y="0" width="24" height="24" fill="none" stroke="var(--vv-stroke)" stroke-width="1"/>
  <rect x="140" y="0" width="24" height="24" fill="none" stroke="var(--vv-stroke)" stroke-width="1"/>
  <rect x="168" y="0" width="24" height="24" fill="none" stroke="var(--vv-stroke)" stroke-width="1"/>
  <rect x="196" y="0" width="24" height="24" fill="none" stroke="var(--vv-stroke)" stroke-width="1"/>
</g>
<!-- Large: L-shape, top-right -->
<path d="M 560,40 L 560,530 L 1040,530" fill="none" stroke="var(--vv-stroke)" stroke-width="1.2"/>
```

---

### P9 — Speech Bubble Grid ← KEY PATTERN
**Concept:** Conflicting opinions, decision by committee, social noise, many perspectives
**Structure:** 3×3 grid of 9 speech bubbles. Each bubble has an inner arrow pointing in a different direction. Together = chaos of opinions.

```svg
<!-- 3×3 positions: x=175,355,535 | y=320,500,680 -->
<!-- Each bubble: 60×42 rect + tail triangle + inner directional arrow -->

<!-- BUBBLE MACRO at (bx, by) with direction (dx,dy normalized): -->
<!-- Rect: x=bx-30, y=by-21, w=60, h=42 -->
<!-- Tail: triangle pointing down from bottom-center -->
<!-- Arrow inside: line from center outward in direction + arrowhead -->

<!-- Example: Bubble at (175,320) — arrow pointing UP ↑ -->
<g transform="translate(145,299)">
  <rect x="0" y="0" width="60" height="42"
    fill="none" stroke="var(--vv-stroke)" stroke-width="1.2" rx="2"/>
  <polygon points="24,42 36,42 30,54"
    fill="none" stroke="var(--vv-stroke)" stroke-width="1.2" stroke-linejoin="round"/>
  <!-- Arrow ↑ inside: line up + arrowhead at top -->
  <line x1="30" y1="32" x2="30" y2="14" stroke="var(--vv-stroke)" stroke-width="1.1"/>
  <polygon points="25,18 30,10 35,18" fill="var(--vv-fill)" stroke="none"/>
</g>

<!-- 9 bubbles with arrows in directions: ↑ ↖ ↗ ← ↙ ↘ ↓ ↙ → -->
<!-- Positions: (175,320) (355,320) (535,320) -->
<!--            (175,500) (355,500) (535,500) -->
<!--            (175,680) (355,680) (535,680) -->
```

**Full 9-direction arrow vectors (center of bubble = cx=30, cy=21):**
```
↑  : line (30,31)→(30,13), head at (25,17)(30,9)(35,17)
↖  : line (30,30)→(18,14), head at (14,20)(13,10)(23,11)
↗  : line (30,30)→(42,14), head at (37,20)(47,10)(37,11)
←  : line (30,21)→(13,21), head at (17,16)(9,21)(17,26)
↙  : line (30,12)→(18,28), head at (13,22)(10,32)(20,28)
↘  : line (30,12)→(42,28), head at (47,22)(50,32)(40,28)
↓  : line (30,11)→(30,29), head at (25,25)(30,33)(35,25)
←₂ : same as ← (or use slightly offset angle)
→  : line (30,21)→(47,21), head at (43,16)(51,21)(43,26)
```

---

### P10 — Venn / Overlap
**Concept:** Intersection, both/and, ikigai, shared understanding
**Structure:** 2–4 intersecting circles. Overlap zone = key concept.

```svg
<!-- 2-circle Venn: left circle (cx=400,cy=540,r=170), right (cx=680,cy=540,r=170) -->
<circle cx="400" cy="540" r="170" fill="none" stroke="var(--vv-stroke)" stroke-width="1.2"/>
<circle cx="680" cy="540" r="170" fill="none" stroke="var(--vv-stroke)" stroke-width="1.2"/>
<text x="290" y="545" text-anchor="middle" fill="var(--vv-text)"
  font-family="monospace" font-size="12" letter-spacing="2">A</text>
<text x="790" y="545" text-anchor="middle" fill="var(--vv-text)"
  font-family="monospace" font-size="12" letter-spacing="2">B</text>
<text x="540" y="545" text-anchor="middle" fill="var(--vv-text)"
  font-family="monospace" font-size="10" letter-spacing="2">A∩B</text>
```

---

### P11 — Single Symbol
**Concept:** Action, singular truth, awareness
**Examples:**

```svg
<!-- Arrow: Movement, Direction, Shoot -->
<line x1="280" y1="540" x2="760" y2="540" stroke="var(--vv-stroke)" stroke-width="1.3"/>
<polygon points="740,525 782,540 740,555" fill="var(--vv-fill)" stroke="none"/>

<!-- Target: You are here, Focus, Shoot -->
<circle cx="540" cy="490" r="190" fill="none" stroke="var(--vv-stroke)" stroke-width="1.2"/>
<circle cx="540" cy="490" r="110" fill="none" stroke="var(--vv-stroke)" stroke-width="1.2"/>
<circle cx="540" cy="490" r="22"  fill="var(--vv-fill)" stroke="none"/>

<!-- Eye: Vision, Perspective, Observer -->
<path d="M 180,490 Q 540,270 900,490 Q 540,710 180,490 Z"
  fill="none" stroke="var(--vv-stroke)" stroke-width="1.2"/>
<circle cx="540" cy="490" r="72" fill="none" stroke="var(--vv-stroke)" stroke-width="1.2"/>
<circle cx="540" cy="490" r="22" fill="var(--vv-fill)" stroke="none"/>

<!-- Pyramid: Hierarchy, Observer/Expert/Practitioner -->
<polygon points="540,250 200,750 880,750" fill="none" stroke="var(--vv-stroke)" stroke-width="1.2"/>
<line x1="340" y1="500" x2="740" y2="500" stroke="var(--vv-stroke)" stroke-width="0.8"/>
<line x1="420" y1="625" x2="660" y2="625" stroke="var(--vv-stroke)" stroke-width="0.8"/>
```

---

### P12 — Typography-led
**Concept:** Long quotes requiring text emphasis
**Structure:** Text IS the visual. Size contrast creates hierarchy.

```svg
<!-- Large word dim (background texture) + small word prominent -->
<text x="540" y="450" text-anchor="middle" fill="var(--vv-text)"
  font-family="monospace" font-size="100" letter-spacing="6" opacity="0.12">SAID</text>
<text x="540" y="610" text-anchor="middle" fill="var(--vv-text)"
  font-family="monospace" font-size="56" letter-spacing="5">DONE</text>
<!-- Attribution -->
<text x="540" y="700" text-anchor="middle" fill="var(--vv-text)"
  font-family="monospace" font-size="11" letter-spacing="2" opacity="0.5">— ATTRIBUTION</text>
```

---

## HTML Output Contract

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>vv — [slug]</title>
  <style>
    :root {
      --vv-bg:     #000000;
      --vv-stroke: #ffffff;
      --vv-text:   #ffffff;
      --vv-dim:    #888888;
      --vv-fill:   #ffffff;
    }
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      background: #111;
      display: flex; flex-direction: column;
      align-items: center; justify-content: center;
      min-height: 100vh; gap: 16px;
    }
    #artwork { width: 540px; height: 540px; display: block; background: var(--vv-bg); }
    .controls { display: flex; gap: 10px; align-items: center; }
    button {
      background: #1a1a1a; color: #aaa; border: 1px solid #333;
      padding: 7px 18px; border-radius: 3px; cursor: pointer;
      font-family: monospace; font-size: 10px; letter-spacing: 3px; text-transform: uppercase;
    }
    button:hover { color: #fff; border-color: #666; }
    .info { color: #333; font-family: monospace; font-size: 10px; letter-spacing: 2px; }
  </style>
</head>
<body>
  <svg id="artwork" viewBox="0 0 1080 1080" xmlns="http://www.w3.org/2000/svg">
    <rect width="1080" height="1080" fill="var(--vv-bg)"/>
    <!-- SVG elements: stroke="var(--vv-stroke)" fill="var(--vv-fill)" etc. -->
  </svg>
  <div class="controls">
    <button onclick="toggleTheme()">◑ THEME</button>
    <button onclick="downloadPNG()">DOWNLOAD PNG</button>
  </div>
  <div class="info">1080 × 1080 · DARK · P[X] — [PATTERN NAME]</div>
  <script>
  let isDark = true;
  function toggleTheme() {
    isDark = !isDark;
    const v = isDark
      ? {bg:'#000000',stroke:'#ffffff',text:'#ffffff',fill:'#ffffff'}
      : {bg:'#ffffff',stroke:'#000000',text:'#000000',fill:'#000000'};
    const r = document.documentElement;
    r.style.setProperty('--vv-bg',v.bg); r.style.setProperty('--vv-stroke',v.stroke);
    r.style.setProperty('--vv-text',v.text); r.style.setProperty('--vv-fill',v.fill);
  }
  function downloadPNG() {
    const svg = document.getElementById('artwork');
    const bg=isDark?'#000000':'#ffffff', stroke=isDark?'#ffffff':'#000000',
          fill=isDark?'#ffffff':'#000000';
    const svgStr = svg.outerHTML
      .replace(/var\(--vv-bg\)/g,bg).replace(/var\(--vv-stroke\)/g,stroke)
      .replace(/var\(--vv-text\)/g,stroke).replace(/var\(--vv-fill\)/g,fill)
      .replace(/var\(--vv-dim\)/g,'#888888');
    const canvas=document.createElement('canvas');
    canvas.width=canvas.height=1080;
    const ctx=canvas.getContext('2d'), img=new Image();
    const url=URL.createObjectURL(new Blob([svgStr],{type:'image/svg+xml;charset=utf-8'}));
    img.onload=()=>{
      ctx.fillStyle=bg; ctx.fillRect(0,0,1080,1080);
      ctx.drawImage(img,0,0,1080,1080);
      const a=document.createElement('a');
      a.download='vv-[slug]-'+(isDark?'dark':'light')+'.png';
      a.href=canvas.toDataURL('image/png'); a.click();
      URL.revokeObjectURL(url);
    };
    img.src=url;
  }
  </script>
</body>
</html>
```

---

## Embed trong vibe-slides

```html
<!-- Dark slide: vv-panel với black bg -->
<div class="vv-panel" style="width:100%;max-width:560px;aspect-ratio:1/1;
  background:#000;border-radius:8px;overflow:hidden;margin:0 auto;">
  <svg viewBox="0 0 1080 1080" style="width:100%;height:100%;display:block;">
    <rect width="1080" height="1080" fill="#000"/>
    <!-- hardcode stroke="#ffffff" cho dark slide -->
  </svg>
</div>

<!-- Light slide: vv-panel với white bg + thin border -->
<div class="vv-panel" style="width:100%;max-width:560px;aspect-ratio:1/1;
  background:#ffffff;border-radius:8px;overflow:hidden;margin:0 auto;
  border:1px solid rgba(0,0,0,0.08);">
  <svg viewBox="0 0 1080 1080" style="width:100%;height:100%;display:block;">
    <rect width="1080" height="1080" fill="#ffffff"/>
    <!-- hardcode stroke="#000000" cho light slide -->
  </svg>
</div>
```

**Rule:** Khi embed, hardcode màu thay vì CSS vars.

---

## Workflow

1. **Nhận concept** từ Hoan
2. **Tra LIBRARY.md** → closest match → pattern
3. **Đề xuất:**
   > "Dùng **P[X]** để visualize:
   > → [element chính]: [mô tả]
   > → [element phụ nếu có]
   > → Text: [nếu có]
   > → Theme: dark / light
   > Build không?"
4. **Confirm → build HTML** → save `output/YYYY-MM-DD_vv-[slug].html`

---

## Design Language — 7 Principles

1. **Economy of Elements** — Remove until you can't remove more. If an element can go without breaking meaning → remove it.
2. **Spatial Metaphor > Literal** — Don't draw "compound interest" as text. Draw an exponential curve. Spatial = instant understanding.
3. **Stroke Weight = Importance** — Main: 1.5px. Secondary: 0.8–1px. Labels/annotations: dim (var(--vv-dim)).
4. **White Space IS Element** — The gap between V.1 and V.674 = "the journey". Empty pie = "what wasn't done". Don't fill it.
5. **One Visual Tension** — Each visual has exactly 1 tension. Complex vs simple. Said vs done. Truth vs trend. 2 tensions = 2 visuals.
6. **Typography Last** — Add text only when geometry isn't enough. When added: uppercase, mono, small, wide letter-spacing. Never "explain" a clear geometry with text.
7. **Numbers Sparingly** — "V.1" "V.674" "SAID" "DONE" — max 3 text elements per visual.

---

## Cross-references

- `LIBRARY.md` — 170 visual dictionary (đọc trước khi build)
- `vibe-design/SKILL.md` → section cuối: khi nào dùng vibe-visual thay T1–T5
- `vibe-slides/SKILL.md` → "VV Concept Slide": embed pattern vào slide

---

## Session Log

- 2026-04-14 v1: Created P1–P8 từ phân tích 9 VV images
- 2026-04-14 v2: Renamed vibe-value → vibe-visual. Extracted 170 visuals từ HTML catalog. Added P9 (Speech Bubble Grid), P10 (Venn), P11 (Single Symbol), P12 (Typography). Light theme CSS vars system. Theme toggle + download PNG resolves CSS vars. LIBRARY.md (170 visual dictionary). 7 Design Language principles.
