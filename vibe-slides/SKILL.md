---
name: vibe-slides
description: Build editorial-style HTML slide decks inspired by D-Squared design language. Use when Hoan asks for "slide", "slide deck", "vibe slide", "html slide", "slide template", "workshop slide", or wants to vibe-code a presentation. NOT for .pptx (use pptx skill). Produces a single self-contained HTML file with keyboard nav, chapter sidebar, dark/light theme toggle, and 3 transition styles.
---

# vibe-slides

Build editorial HTML slide decks — single-file, keyboard-navigated, sidebar chapter nav, theme-toggleable. Design language mượn từ D-Squared (Newsreader serif + Figtree sans + Azeret Mono, warm gold accent, noise overlay, subtle transitions).

## When to trigger

- "Làm slide cho workshop / talk / pitch / share"
- "HTML slide deck", "vibe slide", "D-Squared style"
- "Slide template kiểu dark mode"
- Hoan đang build workshop-planner/ content

**Không dùng khi:** user muốn .pptx thật (dùng `pptx` skill) hoặc cần slide animated kiểu video (dùng `web-artifacts-builder`).

## Output contract

1 file HTML duy nhất, self-contained (fonts từ Google Fonts CDN, CSS + JS inline). Save vào:
- `html-files/` nếu là demo/test
- `workshop-planner/deliverables/` hoặc `workshop-planner/drafts/` nếu là slide workshop thật
- Naming: `YYYY-MM-DD_slide-[slug].html`

File HTML phải có:
- Theme toggle button (dark/light) top-right, persist in memory (React state / JS variable — NO localStorage, artifact environment blocks it)
- Sidebar chapter nav (1 trong 3 variants — xem section Sidebars)
- Slide counter top-right `01 / 17`
- Keyboard nav: ← → ↑ ↓ chuyển slide
- Slide transition (1 trong 3 variants — xem section Transitions)
- Noise texture overlay (SVG data URI, opacity 0.025)

## Design tokens (source of truth)

### Dark theme (default)
```css
--bg: #0B0B0F;
--bg-raised: #131318;
--bg-surface: #1A1A21;
--text: #E8E2D8;
--text-dim: #7A7580;
--text-muted: #4A4650;
--border: #2A2830;
--accent-1: #C4956A;  /* warm gold (primary) */
--accent-2: #6AABB5;  /* teal */
--accent-3: #8DAA7E;  /* sage */
--accent-4: #B87D7D;  /* coral */
--accent-5: #9B8AC4;  /* violet */
```

### Light theme
```css
--bg: #FAF7F0;
--bg-raised: #F2EDE2;
--bg-surface: #E8E2D2;
--text: #1A1A1F;
--text-dim: #5A5560;
--text-muted: #8A8590;
--border: #D4CEBE;
--accent-1: #8B5A2B;  /* deeper gold for contrast */
--accent-2: #2E7A85;
--accent-3: #4A7A3B;
--accent-4: #8B3D3D;
--accent-5: #5B4A84;
```

### Typography
```css
/* Google Fonts import */
@import url('https://fonts.googleapis.com/css2?family=Newsreader:ital,wght@0,300;0,400;1,400&family=Figtree:wght@300;400;500;600&family=Azeret+Mono:wght@300;400;500&display=swap');

/* Usage */
.slide-title    { font-family: 'Newsreader', serif; font-size: 52px; font-weight: 400; line-height: 1.15; letter-spacing: -0.01em; }
.slide-title em { font-style: italic; color: var(--slide-accent); }
.section-num    { font-family: 'Newsreader', serif; font-size: 13px; text-transform: uppercase; letter-spacing: 0.15em; }
.body-text      { font-family: 'Figtree', sans-serif; font-size: 18px; font-weight: 300; }
.mono-label     { font-family: 'Azeret Mono', monospace; font-size: 10px; letter-spacing: 0.08em; text-transform: uppercase; }
```

**Rule:** Titles = serif (Newsreader), với 1 từ italic màu accent. Body = sans (Figtree). Labels/data/code = mono (Azeret Mono).

## Sidebar variants (pick 1 per deck)

### Variant A — Dot-line nav (D-Squared Skills style)
Vertical line with dots + progress line that fills as you advance. Minimal.
```html
<nav class="chapter-nav" id="chapterNav">
  <div class="nav-line"></div>
  <div class="nav-line-progress" id="navProgress"></div>
  <!-- nav-items injected by JS -->
</nav>
```
CSS: nav-dot 7px, active 9px + glow (box-shadow). Label uppercase Figtree 11px. Progress line = var(--slide-accent).
**Best for:** decks 5-15 slides, focus on flow.

### Variant B — Number-label nav (SPAR / Three Layers style)
Big chapter number + title. Accent bar (2px) on active chapter.
```html
<nav class="chapter-nav">
  <div class="chapter-item active" data-chapter="0" onclick="goToSlide(0)">
    <div class="chapter-number">01</div>
    <div class="chapter-title">The Problem</div>
  </div>
  ...
</nav>
```
CSS: chapter-number Newsreader 28px, chapter-title Figtree 14px uppercase. Active: number → accent color, left bar 2px.
**Best for:** decks with clear chapter structure (4-8 chapters).

### Variant C — Letter monogram nav (SPAR letter style)
Big single letter per chapter (for mnemonic frameworks like SPAR, STAR, RACI).
```html
<nav class="chapter-nav">
  <div class="spar-letter-item active" data-chapter="sharpen">
    <span class="ch-letter">S</span>
    <span class="ch-label">Sharpen</span>
  </div>
  ...
</nav>
```
CSS: ch-letter Newsreader 40px italic. Expands label on active. Each letter gets own accent color.
**Best for:** framework decks where each chapter = 1 letter of mnemonic.

## Transition variants (pick 1 per deck)

### Transition 1 — Fade-up (default, recommended)
```css
.slide {
  opacity: 0; transform: translateY(20px);
  transition: opacity 0.5s cubic-bezier(0.4, 0, 0.2, 1),
              transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}
.slide.active { opacity: 1; transform: translateY(0); }
```
**Feel:** gentle, editorial, matches Newsreader typeface.

### Transition 2 — Slide-horizontal
```css
.slide {
  opacity: 0; transform: translateX(40px);
  transition: opacity 0.45s cubic-bezier(0.22, 1, 0.36, 1),
              transform 0.45s cubic-bezier(0.22, 1, 0.36, 1);
}
.slide.active { opacity: 1; transform: translateX(0); }
.slide.prev { transform: translateX(-40px); }
```
**Feel:** directional, deck-like. Good for linear narratives.

### Transition 3 — Staggered elements
Slide itself fades, but children elements animate in sequence.
```css
.slide .anim { opacity: 0; transform: translateY(12px); transition: all 0.5s ease; }
.slide.active .anim { opacity: 1; transform: translateY(0); }
.slide.active .anim-1 { transition-delay: 0.1s; }
.slide.active .anim-2 { transition-delay: 0.25s; }
.slide.active .anim-3 { transition-delay: 0.4s; }
.slide.active .anim-4 { transition-delay: 0.55s; }
```
**Feel:** narrative, reveal 1 element at a time. Best for bullet reveals or sequential frameworks.

## Component library (slide types)

Claude nên remix từ bộ component này thay vì tự chế:

1. **Title slide** — `.slide-title` + `.slide-subtitle` center
2. **Section number + title** — `.section-num` above `.slide-title` (editorial feel)
3. **Full-width SVG** — `.full-svg svg` cho chart/diagram
4. **Context bar** — `.context-bar` visual split filled vs remaining
5. **File tree** — `.file-tree` Azeret Mono với `.highlight` + `.dim`
6. **Dual column** — `.dual-column` 2 card side-by-side (.col-card)
7. **Prompt block** — `.prompt-block` code-style box với "PROMPT" badge
8. **Decision grid** — `.decision-grid` 2x2 compare/contrast
9. **Route cards** — `.route-visual` → 2 path cards with accent
10. **Recap cards** — step-through recap với dots indicator
11. **Formula row** — `.formula-pill` + `.formula-op` + `.formula-result` (pill → ÷ → pill)
12. **Gauge** — horizontal bar với sweet-spot marker
13. **Three answers** — numbered list with serif numbers

Full CSS cho từng component: xem `base.html` trong folder này.

## Workflow khi được gọi

1. **Hỏi Hoan 3 câu nếu chưa có:**
   - Slide deck về chủ đề gì, audience ai, bao nhiêu slide?
   - Sidebar variant A/B/C?
   - Transition 1/2/3?
2. **Draft outline text-only trước** (chapter structure + slide titles) để Hoan approve.
3. **Copy `base.html` → file mới** theo naming convention, fill slides.
4. **Save đúng folder** (html-files/ hoặc workshop-planner/).
5. **Confirm path + preview link cho Hoan.**

## Responsive scale system

Mọi slide deck PHẢI có `--content-scale` để user zoom in/out tại chỗ không reload.

```css
:root { --content-scale: 1; }

.slide-inner {
  width: 100%; max-width: 1000px;
  display: flex; flex-direction: column; align-items: center; gap: 28px;
  transform: scale(var(--content-scale));
  transform-origin: center center;
  transition: transform 0.2s ease;
}

.slide { overflow: hidden; }  /* clip khi scale > 1 */
```

**Scale range:** 0.5 → 1.8, step 0.1. Default: 1.0 khi xem browser, 1.2 khi export PDF.

## Zoom controls

Nằm trong `.nav-btns`, bên trái nút ← →. Pattern chuẩn:

```html
<div class="nav-btns">
  <div class="zoom-controls">
    <button class="zoom-btn" id="zoomOut" title="Zoom out (−)">−</button>
    <span class="zoom-lbl" id="zoomLbl" title="Click to reset zoom">100%</span>
    <button class="zoom-btn" id="zoomIn"  title="Zoom in (+)">+</button>
  </div>
  <span class="nav-hint">◐</span>
  <button class="nav-btn" id="prevBtn">←</button>
  <button class="nav-btn" id="nextBtn">→</button>
</div>
```

```css
.zoom-controls {
  display: flex; align-items: center; gap: 6px;
  padding-right: 12px; margin-right: 4px;
  border-right: 1px solid var(--border);
}
.zoom-btn {
  width: 30px; height: 30px; border-radius: 7px;
  background: var(--bg-raised); border: 1px solid var(--border);
  color: var(--text-dim); font-size: 17px; font-weight: 400;
  cursor: pointer; display: flex; align-items: center; justify-content: center;
  transition: all 0.2s ease; user-select: none;
}
.zoom-btn:hover { color: var(--text); border-color: var(--slide-accent); background: var(--bg-surface); }
.zoom-btn:active { transform: scale(0.90); }
.zoom-lbl {
  font-family: 'Azeret Mono', monospace; font-size: 11px; font-weight: 300;
  color: var(--text-dim); min-width: 38px; text-align: center;
  cursor: pointer; user-select: none;
}
.zoom-lbl:hover { color: var(--slide-accent); }
```

```js
let scale = 1.0;
const SCALE_MIN = 0.5, SCALE_MAX = 1.8, SCALE_STEP = 0.1;

function setScale(v) {
  scale = Math.round(Math.min(SCALE_MAX, Math.max(SCALE_MIN, v)) * 10) / 10;
  document.documentElement.style.setProperty('--content-scale', scale);
  const lbl = document.getElementById('zoomLbl');
  if (lbl) lbl.textContent = Math.round(scale * 100) + '%';
}

// Buttons
document.getElementById('zoomIn') ?.addEventListener('click', () => setScale(scale + SCALE_STEP));
document.getElementById('zoomOut')?.addEventListener('click', () => setScale(scale - SCALE_STEP));
document.getElementById('zoomLbl')?.addEventListener('click', () => setScale(1.0)); // click = reset

// Keyboard: Ctrl/Cmd + = / - / 0
document.addEventListener('keydown', e => {
  if (e.ctrlKey || e.metaKey) {
    if (e.key === '=' || e.key === '+') { e.preventDefault(); setScale(scale + SCALE_STEP); }
    if (e.key === '-')                  { e.preventDefault(); setScale(scale - SCALE_STEP); }
    if (e.key === '0')                  { e.preventDefault(); setScale(1.0); }
  }
});
```

## Background: gradient + noise

Mọi deck PHẢI có cả 2 lớp: radial gradient corners + noise grain overlay.

### Radial gradient (layered, theme-aware)
```css
/* Dark theme — trên body */
body {
  background-image:
    radial-gradient(ellipse 70% 55% at 30% 10%, rgba(196,149,106,0.07) 0%, transparent 100%),
    radial-gradient(ellipse 55% 65% at 78% 88%, rgba(106,171,181,0.05) 0%, transparent 100%);
}
/* Light theme override */
:root[data-theme="light"] body {
  background-image:
    radial-gradient(ellipse 70% 55% at 30% 10%, rgba(139,90,43,0.08) 0%, transparent 100%),
    radial-gradient(ellipse 55% 65% at 78% 88%, rgba(46,122,133,0.05) 0%, transparent 100%);
}
```
Logic: top-left = accent-1 (warm gold), bottom-right = accent-2 (teal). Opacity rất thấp để subtle.

### Noise grain overlay (body::after)
```css
body::after {
  content: ''; position: fixed; inset: 0; pointer-events: none; z-index: 9999;
  opacity: 0.028;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  background-repeat: repeat; background-size: 180px 180px;
}
```

## Export to PDF

Dùng script `export_slides.py` trong `/sessions/.../`:

```python
# Key settings
viewport = {"width": 1920, "height": 1080}
# JS trước khi capture:
await page.evaluate("""
    document.documentElement.style.setProperty('--content-scale', '1.2');
    // hide nav chrome (.chapter-nav, .slide-counter, .nav-btns, .theme-toggle)
""")
# PDF page size: 960×540 points (13.33"×7.5" at 72dpi = 144 DPI effective)
# Dùng reportlab.pdfgen.canvas, embed JPEG quality=92 để gọn file
```

**Output tiêu chuẩn:** ~1.5 MB / 15 trang, text rõ, cân đối 16:9. Scale 1.2 khi export làm font to hơn ~20% so với browser default.

## Hard rules

- Single file HTML. Không chia CSS/JS ra file riêng.
- Fonts từ Google Fonts CDN (không self-host).
- NO localStorage / sessionStorage — dùng JS variable cho theme state.
- Dark theme default. Toggle button top-right 32px, persist trong session.
- Slide title LUÔN có 1 từ italic accent (.slide-title em pattern).
- Noise overlay LUÔN có (0.028 opacity, body::after).
- Radial gradient background LUÔN có (2 lớp, theme-aware).
- Zoom controls LUÔN có trong nav-btns.
- `--content-scale` LUÔN có trong :root.
- Slide count minimum 3, maximum 25 (nếu >25 → split thành 2 deck).
- Không dùng emoji trong slides trừ khi Hoan yêu cầu.

## Light/dark theme toggle pattern

```html
<button class="theme-toggle" id="themeToggle" aria-label="Toggle theme">◐</button>
```

```js
let currentTheme = 'dark';
document.getElementById('themeToggle').addEventListener('click', () => {
  currentTheme = currentTheme === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', currentTheme);
});
```

```css
:root[data-theme="light"] { /* override --bg, --text, --accent-* ở đây */ }
```

## ⚡ VV Concept Slide (Visualize Value embed)

Khi 1 slide trong deck cần **concept illustration panel** — pure black, white strokes, abstract geometry — dùng pattern từ `tools/vibe-value/SKILL.md` và embed inline.

**Trigger:** Hoan nói "slide này cần hình minh họa", "vẽ concept cho slide", "VV illustration cho slide này".

**Cách embed VV visual vào slide:**

```html
<!-- Slide type: "concept-visual" -->
<div class="slide" id="slide-N">
  <div class="slide-inner">

    <!-- Top: title text (optional, dùng khi cần label slide) -->
    <div class="section-num">CONCEPT</div>
    <h2 class="slide-title">The <em>Principle</em></h2>

    <!-- Bottom: VV visual panel -->
    <div class="vv-panel" style="
      width: 100%;
      max-width: 600px;
      aspect-ratio: 1 / 1;
      background: #000;
      border-radius: 8px;
      overflow: hidden;
      margin: 0 auto;
    ">
      <!-- Paste SVG từ vibe-value ở đây, viewBox="0 0 1080 1080" -->
      <svg viewBox="0 0 1080 1080" xmlns="http://www.w3.org/2000/svg"
        style="width:100%; height:100%; display:block;">
        <rect width="1080" height="1080" fill="#000"/>
        <!-- [VV pattern elements] -->
      </svg>
    </div>

  </div>
</div>
```

**Rules khi dùng VV slide:**
- VV panel không được co lại dưới 400px — nếu slide nhỏ, bỏ title/section-num
- VV visual luôn `background:#000` ngay cả trong light theme
- Không resize SVG bằng width/height attribute — chỉ dùng CSS
- VV panel đặt center, max-width 600px, aspect-ratio 1:1

**Workflow:** Đọc `tools/vibe-visual/SKILL.md` → tra concept trong `LIBRARY.md` → chọn pattern → build SVG → paste vào slide. Không viết SVG từ đầu mà không đọc pattern templates. Light theme: dùng `stroke="#000000"` hardcoded thay vì CSS vars.

---

---

# ═══════════════════════════════════════
# v3 SYSTEM UPGRADES (2026-04-14)
# ═══════════════════════════════════════
# Áp dụng cho MỌI deck mới từ v3 trở đi.
# Các section dưới ĐÈ LÊN v2 nếu có xung đột.

---

## [v3-1] Responsive System — Fluid Scale

**Vấn đề với v2:** `transform: scale()` không reflow layout — mobile bị cắt, sidebar không co.

**v3 approach:** Dùng CSS `clamp()` + `ResizeObserver` auto-scale + sidebar collapse on mobile.

### Layout structure (bắt buộc)

```html
<body>
  <nav class="chapter-nav" id="chapterNav">...</nav>
  <main class="deck-main" id="deckMain">
    <div class="slides-area" id="slidesArea">
      <div class="slide active" id="slide-0">
        <div class="slide-inner">...</div>
      </div>
      <!-- more slides -->
    </div>
    <div class="nav-btns">...</div>
  </main>
</body>
```

### CSS — Responsive core

```css
/* ── Layout shell ── */
body {
  display: flex;
  height: 100vh;
  overflow: hidden;
  transition: gap 0.3s ease;
}

.chapter-nav {
  flex-shrink: 0;
  height: 100vh;
  overflow-y: auto;
  overflow-x: hidden;
  transition: width 0.3s ease;
  /* width controlled by sidebar mode — see [v3-2] */
}

.deck-main {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  min-width: 0; /* critical: allows flex child to shrink below content size */
}

.slides-area {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(12px, 2vw, 40px);
  overflow: hidden;
}

/* ── Slide container: aspect-ratio 16:9, scales to fill available space ── */
.slide {
  width: 100%;
  max-width: min(calc(100% - 0px), calc((100vh - 80px) * 16 / 9));
  aspect-ratio: 16 / 9;
  position: relative;
  flex-shrink: 0;
}

/* ── Fluid typography via clamp() ── */
/* clamp(min, preferred, max) — preferred in vw units */
:root {
  --fs-title:    clamp(28px, 3.8vw, 56px);
  --fs-subtitle: clamp(14px, 1.6vw, 22px);
  --fs-body:     clamp(13px, 1.4vw, 18px);
  --fs-mono:     clamp(10px, 0.9vw, 13px);
  --fs-section:  clamp(10px, 0.8vw, 13px);
  --gap-inner:   clamp(16px, 2vw, 32px);
}

.slide-title    { font-size: var(--fs-title);    line-height: 1.12; }
.slide-subtitle { font-size: var(--fs-subtitle); }
.body-text      { font-size: var(--fs-body);     }
.mono-label     { font-size: var(--fs-mono);     }
.section-num    { font-size: var(--fs-section);  }
.slide-inner    { gap: var(--gap-inner);         }

/* ── Remove old --content-scale (deprecated in v3) ── */
/* Do NOT use transform: scale() for responsive. Use clamp() instead. */
/* --content-scale is ONLY kept for manual zoom controls (Ctrl+=/- buttons) */
```

### JavaScript — Auto-scale on resize

```javascript
// Resize observer: recalculate slide max-width on window resize
const resizeObs = new ResizeObserver(() => updateSlideSize());
resizeObs.observe(document.getElementById('deckMain'));

function updateSlideSize() {
  const main    = document.getElementById('deckMain');
  const navW    = document.getElementById('chapterNav').offsetWidth;
  const winH    = window.innerHeight;
  const availW  = main.offsetWidth - 80;  // padding
  const availH  = winH - 80;             // nav-btns height
  // Maintain 16:9 — pick the constraining dimension
  const byWidth  = availW;
  const byHeight = availH * 16 / 9;
  const slideW   = Math.min(byWidth, byHeight);
  document.querySelectorAll('.slide').forEach(s => {
    s.style.maxWidth = slideW + 'px';
  });
}
window.addEventListener('load', updateSlideSize);
```

### Mobile breakpoints

```css
/* ── Mobile: sidebar becomes top bar ── */
@media (max-width: 640px) {
  body { flex-direction: column; }

  .chapter-nav {
    width: 100% !important;  /* override all sidebar mode widths */
    height: 48px !important;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    overflow-x: auto;
    overflow-y: hidden;
    padding: 0 16px;
    border-right: none;
    border-bottom: 1px solid var(--border);
  }

  /* In minimal mode on mobile: dots show horizontally */
  .nav-dot-item { flex-direction: column; gap: 0; }
  .nav-label    { display: none; }
  .nav-line, .nav-line-progress { display: none; }

  /* In full mode on mobile: show chapter titles as pills horizontally */
  .chapter-item { flex-direction: row; gap: 8px; white-space: nowrap; }
  .chapter-number { font-size: 12px; }
  .chapter-title  { font-size: 11px; }

  .deck-main { flex: 1; }

  /* Slide fills remaining height */
  .slide {
    max-width: 100vw !important;
    width: 100%;
  }

  /* Nav buttons on mobile: fixed bottom */
  .nav-btns {
    position: fixed;
    bottom: 0; left: 0; right: 0;
    background: var(--bg);
    border-top: 1px solid var(--border);
    padding: 8px 16px;
    z-index: 100;
  }
}

/* ── Tablet: sidebar compact ── */
@media (max-width: 900px) and (min-width: 641px) {
  /* Force minimal sidebar mode on tablet if in full mode */
  .chapter-nav.mode-full {
    width: 56px !important;
  }
  .chapter-nav.mode-full .chapter-title  { display: none; }
  .chapter-nav.mode-full .chapter-number { font-size: 12px; }
}
```

---

## [v3-2] Sidebar Mode Switch

3 modes cycle bằng nút nhỏ trên sidebar. Mode persist trong session memory (no localStorage).

### CSS — 3 sidebar mode widths + visibility

```css
/* ── Mode: MINIMAL — dots only, no text, 44px wide ── */
.chapter-nav.mode-minimal {
  width: 44px;
  padding: 20px 0;
  align-items: center;
}
.chapter-nav.mode-minimal .chapter-title  { display: none; }
.chapter-nav.mode-minimal .chapter-number { display: none; }
.chapter-nav.mode-minimal .spar-label     { display: none; }
.chapter-nav.mode-minimal .nav-label      { display: none; }
/* Only dots/circles remain */

/* ── Mode: COMPACT — numbers only, 64px wide ── */
.chapter-nav.mode-compact {
  width: 64px;
  padding: 20px 8px;
  align-items: center;
}
.chapter-nav.mode-compact .chapter-title { display: none; }
.chapter-nav.mode-compact .nav-label     { display: none; }
/* Chapter number + active indicator remain */

/* ── Mode: FULL — numbers + titles, 200px wide (default) ── */
.chapter-nav.mode-full {
  width: 200px;
  padding: 20px 0 20px 24px;
}
/* All elements visible */

/* ── Mode toggle button: positioned at bottom of sidebar ── */
.sidebar-mode-btn {
  position: absolute;
  bottom: 16px;
  left: 50%;
  transform: translateX(-50%);
  width: 28px; height: 28px;
  border-radius: 50%;
  background: var(--bg-raised);
  border: 1px solid var(--border);
  color: var(--text-dim);
  font-size: 13px;
  cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  transition: all 0.2s ease;
  z-index: 10;
}
.sidebar-mode-btn:hover { color: var(--text); border-color: var(--slide-accent); }

/* Sidebar must be position: relative for absolute child */
.chapter-nav { position: relative; }
```

### HTML — mode toggle button inside nav

```html
<nav class="chapter-nav mode-full" id="chapterNav">
  <!-- ...existing nav items... -->
  <button class="sidebar-mode-btn" id="sidebarModeBtn" title="Sidebar mode">⊟</button>
</nav>
```

### JavaScript — cycle through 3 modes

```javascript
const SIDEBAR_MODES = ['mode-full', 'mode-compact', 'mode-minimal'];
const SIDEBAR_ICONS = { 'mode-full': '⊟', 'mode-compact': '≡', 'mode-minimal': '·' };
let sidebarModeIdx = 0; // 0=full, 1=compact, 2=minimal

function cycleSidebarMode() {
  const nav = document.getElementById('chapterNav');
  const btn = document.getElementById('sidebarModeBtn');
  // Remove current mode class
  nav.classList.remove(...SIDEBAR_MODES);
  // Advance to next mode
  sidebarModeIdx = (sidebarModeIdx + 1) % SIDEBAR_MODES.length;
  const newMode = SIDEBAR_MODES[sidebarModeIdx];
  nav.classList.add(newMode);
  btn.textContent = SIDEBAR_ICONS[newMode];
  // Recalculate slide size after sidebar width changes
  setTimeout(updateSlideSize, 320); // after CSS transition
}

document.getElementById('sidebarModeBtn')
  ?.addEventListener('click', cycleSidebarMode);
```

**Behavior summary:**
| Mode | Width | Shows | Icon |
|------|-------|-------|------|
| Full (default) | 200px | Number + full title | ⊟ |
| Compact | 64px | Number only | ≡ |
| Minimal | 44px | Active dot only | · |

Mobile override: trên `< 640px`, sidebar luôn collapse thành top bar bất kể mode.

---

## [v3-3] Optical Centering

Content nhìn có vẻ "thấp" khi đặt ở center toán học (50%). Mắt người cảm nhận tâm thị giác ở ~45% — cần bù lại bằng offset nhẹ lên trên.

### 3 kỹ thuật (chọn theo content type)

#### Technique A — Content Offset (mặc định, áp dụng hầu hết slides)
```css
.slide-inner {
  /* Đẩy content lên ~5% so với center toán học */
  /* Thay vì padding: 0, dùng asymmetric padding */
  padding-top:    0;
  padding-bottom: 8%;  /* bottom padding > top → content shifts up */
  /* Hoặc dùng translate: */
  /* transform: translateY(-4%); */
}
```
**Dùng cho:** Title slides, single-concept slides, quote slides.

#### Technique B — Asymmetric Balance (content-heavy slides)
```css
/* Áp dụng khi có 2 columns hoặc mixed content weight */
.slide-inner {
  align-items: flex-start;   /* không center ngang */
  padding-left: 8%;          /* golden ratio left margin */
  padding-right: 5%;
  padding-top: 0;
  padding-bottom: 10%;       /* optical center correction */
}

/* Heavy element (image, chart) → gets less top margin */
/* Light element (text, list) → gets more top margin */
.col-heavy { margin-top: 0; }
.col-light { margin-top: 4%; }
```
**Dùng cho:** Dual column slides, slides với SVG chart bên cạnh text.

#### Technique C — Layout Compensation (element weight balancing)
```css
/* Dùng khi 1 element visual nặng hơn element kia */
/* Ví dụ: icon/SVG bên trái + text nhẹ hơn bên phải */
.slide-inner {
  display: grid;
  grid-template-columns: 1fr 1.2fr; /* right column slightly wider = compensate visual weight */
  align-items: center;
  padding-bottom: 8%; /* optical center */
  gap: clamp(20px, 3vw, 48px);
}

/* VV visual panel: cần compensation vì màu đen nặng hơn chữ */
.vv-panel-wrapper {
  /* Shift VV panel slightly up to counteract visual weight */
  margin-top: -3%;
}
```
**Dùng cho:** Slides với VV visual panel, icon + text combos, chart + annotation.

### Rule of thumb
```
Slide chỉ có text     → Technique A (padding-bottom: 8%)
Text + chart/SVG      → Technique B (asymmetric balance)
VV panel + text       → Technique C (grid compensation)
Title / quote only    → Technique A (translateY -4%)
```

### Quick implementation cho mọi slide (minimum effort)
```css
/* Thêm vào mọi .slide-inner — override sau nếu cần tech B/C */
.slide-inner {
  width: 100%; max-width: 900px;
  margin: 0 auto;
  display: flex; flex-direction: column;
  align-items: center;
  gap: var(--gap-inner);
  padding-bottom: 8%; /* ← Optical center: Technique A */
}
```

---

## [v3-4] AI-Friendly HTML Indexing

Mỗi HTML deck cần một **DECK INDEX** comment ở đầu file và **slide markers** trên mỗi slide. Mục đích: AI (hoặc Hoan) có thể đọc index → locate slide → edit chính xác mà không cần đọc toàn file.

### Cấu trúc deck index (đặt ngay sau `<body>`)

```html
<!--
╔══════════════════════════════════════════════════════════════════╗
║  DECK INDEX                                                      ║
║  Title   : [Deck Title]                                          ║
║  File    : YYYY-MM-DD_slide-[slug].html                         ║
║  Created : YYYY-MM-DD   Updated: YYYY-MM-DD                     ║
║  Slides  : NN total   Chapters: N                               ║
║  Theme   : dark | Sidebar: full | Transition: fade-up           ║
╠══════════════════════════════════════════════════════════════════╣
║  SLIDE MAP  (format: [##] id | Chapter | "Title" | ~line)       ║
╠══════════════════════════════════════════════════════════════════╣
║  [01] slide-0  | ch:0 Intro     | "Opening Title"      | ~ln150 ║
║  [02] slide-1  | ch:0 Intro     | "The Problem"         | ~ln185 ║
║  [03] slide-2  | ch:1 Context   | "Why This Matters"    | ~ln225 ║
║  [04] slide-3  | ch:1 Context   | "Current State"       | ~ln265 ║
║  [05] slide-4  | ch:2 Solution  | "Section Break"       | ~ln300 ║
║  ...                                                             ║
║  [NN] slide-N  | ch:N Outro     | "Thank You"           | ~ln890 ║
╠══════════════════════════════════════════════════════════════════╣
║  HOW TO EDIT:                                                    ║
║  1. Find slide by searching: <!-- SLIDE [##] -->                 ║
║  2. Each slide ends before the next <!-- SLIDE --> marker       ║
║  3. Update this index after adding/removing/reordering slides   ║
╚══════════════════════════════════════════════════════════════════╝
-->
```

### Slide marker comment (ngay trên mỗi `<div class="slide">`)

```html
<!-- SLIDE [03] ─── ch:1 "Context" ─── "Why This Matters" ───────── -->
<div class="slide" id="slide-2"
  data-slide="2"
  data-chapter="1"
  data-chapter-name="Context"
  data-title="Why This Matters"
  data-type="content">
  <div class="slide-inner">
    <!-- slide content here -->
  </div>
</div>
<!-- END SLIDE [03] ──────────────────────────────────────────────── -->
```

### data-* attributes (machine-readable, không hiển thị)

| Attribute | Values | Purpose |
|-----------|--------|---------|
| `data-slide` | 0-based index | JS navigation |
| `data-chapter` | 0-based chapter | Sidebar grouping |
| `data-chapter-name` | string | Sidebar label |
| `data-title` | string | Index + debug |
| `data-type` | `title` \| `section` \| `content` \| `vv` \| `outro` | Helps AI know layout type |

### JavaScript — Auto-build index từ slides (runtime)

```javascript
// Chạy sau DOM ready — builds a runtime index array
// AI hoặc devtools có thể inspect window.DECK_INDEX
window.DECK_INDEX = Array.from(
  document.querySelectorAll('.slide[data-slide]')
).map(el => ({
  n:       parseInt(el.dataset.slide) + 1,       // 1-based
  id:      el.id,
  chapter: parseInt(el.dataset.chapter ?? 0),
  chName:  el.dataset.chapterName ?? '',
  title:   el.dataset.title ?? '',
  type:    el.dataset.type ?? 'content',
}));
console.table(window.DECK_INDEX); // visible in DevTools
```

### Quy trình cập nhật index khi sửa slide

Khi AI (hoặc Hoan) thêm/xóa/đổi thứ tự slide:
1. Update `data-slide` attribute để giữ đúng index
2. Update `<!-- SLIDE [##] -->` marker tương ứng
3. Update DECK INDEX comment ở đầu file (line numbers ~approximate là ok)
4. Chạy lại `window.DECK_INDEX` trong DevTools để verify

### Workflow cho AI khi được yêu cầu sửa slide cụ thể

```
User: "Sửa slide 5 — đổi title thành X"
AI:   1. Search file cho `<!-- SLIDE [05] -->` → locate block
      2. Find <h2 class="slide-title"> bên trong block đó
      3. Replace text → done
      4. Update DECK INDEX nếu title trong index cũng thay đổi
```

**Không cần đọc toàn bộ file** — chỉ cần: đọc DECK INDEX → jump đến marker → edit block.

---

## [v3] Full Boilerplate Template

Đây là HTML template chuẩn v3 — gộp tất cả 4 cơ chế mới. Dùng làm baseline cho mọi deck từ v3.

```html
<!DOCTYPE html>
<html lang="vi" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Deck Title]</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,wght@0,300;0,400;1,400&family=Figtree:wght@300;400;500&family=Azeret+Mono:wght@300;400&display=swap" rel="stylesheet">
  <style>
    /* ── DESIGN TOKENS ── */
    :root {
      --bg: #0B0B0F; --bg-raised: #131318; --bg-surface: #1A1A21;
      --text: #E8E2D8; --text-dim: #7A7580; --text-muted: #4A4650;
      --border: #2A2830;
      --accent-1: #C4956A; --accent-2: #6AABB5;
      --slide-accent: var(--accent-1);

      /* v3 fluid type */
      --fs-title:    clamp(28px, 3.8vw, 54px);
      --fs-subtitle: clamp(14px, 1.6vw, 22px);
      --fs-body:     clamp(13px, 1.3vw, 18px);
      --fs-mono:     clamp(10px, 0.85vw, 13px);
      --fs-section:  clamp(10px, 0.8vw, 13px);
      --gap-inner:   clamp(16px, 2vw, 32px);
      --content-scale: 1; /* kept for manual zoom only */
    }
    :root[data-theme="light"] {
      --bg: #FAF7F0; --bg-raised: #F2EDE2; --bg-surface: #E8E2D2;
      --text: #1A1A1F; --text-dim: #5A5560; --text-muted: #8A8590;
      --border: #D4CEBE;
      --accent-1: #8B5A2B; --accent-2: #2E7A85;
    }

    /* ── RESET + BASE ── */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html, body { height: 100%; overflow: hidden; }
    body {
      display: flex;
      background: var(--bg);
      color: var(--text);
      font-family: 'Figtree', sans-serif;
      transition: background 0.3s, color 0.3s;
    }
    body::after { /* noise grain */
      content: ''; position: fixed; inset: 0; pointer-events: none; z-index: 9999;
      opacity: 0.028;
      background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
      background-size: 180px 180px;
    }
    body { /* radial gradient */
      background-image:
        radial-gradient(ellipse 70% 55% at 30% 10%, rgba(196,149,106,0.07) 0%, transparent 100%),
        radial-gradient(ellipse 55% 65% at 78% 88%, rgba(106,171,181,0.05) 0%, transparent 100%);
    }

    /* ── SIDEBAR ── */
    .chapter-nav {
      position: relative;
      width: 200px; /* mode-full default */
      height: 100vh;
      background: var(--bg-raised);
      border-right: 1px solid var(--border);
      display: flex; flex-direction: column;
      padding: 20px 0 20px 24px;
      overflow-y: auto; overflow-x: hidden;
      flex-shrink: 0;
      transition: width 0.3s ease, padding 0.3s ease;
    }
    /* Sidebar modes */
    .chapter-nav.mode-compact { width: 64px; padding: 20px 8px; align-items: center; }
    .chapter-nav.mode-compact .chapter-title { display: none; }
    .chapter-nav.mode-minimal { width: 44px; padding: 20px 0; align-items: center; }
    .chapter-nav.mode-minimal .chapter-title,
    .chapter-nav.mode-minimal .chapter-number { display: none; }
    /* Chapter items */
    .chapter-item {
      display: flex; flex-direction: column; gap: 3px;
      padding: 10px 8px 10px 0; cursor: pointer;
      border-left: 2px solid transparent;
      transition: all 0.2s ease;
    }
    .chapter-item.active { border-left-color: var(--slide-accent); }
    .chapter-number {
      font-family: 'Newsreader', serif; font-size: 22px; color: var(--text-muted);
      transition: color 0.2s;
    }
    .chapter-item.active .chapter-number { color: var(--slide-accent); }
    .chapter-title {
      font-family: 'Figtree', sans-serif; font-size: 11px; font-weight: 500;
      text-transform: uppercase; letter-spacing: 0.1em; color: var(--text-dim);
    }
    .chapter-item.active .chapter-title { color: var(--text); }
    /* Sidebar toggle btn */
    .sidebar-mode-btn {
      position: absolute; bottom: 16px; left: 50%; transform: translateX(-50%);
      width: 26px; height: 26px; border-radius: 50%;
      background: var(--bg-surface); border: 1px solid var(--border);
      color: var(--text-muted); font-size: 12px; cursor: pointer;
      display: flex; align-items: center; justify-content: center;
      transition: all 0.2s ease;
    }
    .sidebar-mode-btn:hover { color: var(--text); border-color: var(--slide-accent); }

    /* ── MAIN AREA ── */
    .deck-main {
      flex: 1; min-width: 0;
      display: flex; flex-direction: column;
      overflow: hidden;
    }
    .slides-area {
      flex: 1;
      display: flex; align-items: center; justify-content: center;
      padding: clamp(10px, 2vw, 36px) clamp(16px, 3vw, 60px);
      overflow: hidden;
    }

    /* ── SLIDE ── */
    .slide {
      position: absolute; inset: 0;
      display: none; align-items: center; justify-content: center;
    }
    .slide.active { display: flex; }
    /* Transitions */
    .slide { opacity: 0; transform: translateY(16px);
      transition: opacity 0.5s cubic-bezier(0.4,0,0.2,1),
                  transform 0.5s cubic-bezier(0.4,0,0.2,1); }
    .slide.active { opacity: 1; transform: translateY(0); }

    .slide-viewport {
      width: 100%; height: 100%;
      display: flex; align-items: center; justify-content: center;
    }

    /* ── SLIDE INNER — Optical Center (Technique A) ── */
    .slide-inner {
      width: 100%; max-width: min(900px, 90%);
      display: flex; flex-direction: column;
      align-items: center; text-align: center;
      gap: var(--gap-inner);
      padding-bottom: 8%; /* OPTICAL CENTER: asymmetric — shifts content up */
      transform: scale(var(--content-scale));
      transform-origin: center center;
    }

    /* ── TYPOGRAPHY ── */
    .slide-title {
      font-family: 'Newsreader', serif;
      font-size: var(--fs-title); font-weight: 400;
      line-height: 1.12; letter-spacing: -0.01em;
      color: var(--text);
    }
    .slide-title em { font-style: italic; color: var(--slide-accent); }
    .slide-subtitle {
      font-family: 'Figtree', sans-serif;
      font-size: var(--fs-subtitle); font-weight: 300;
      color: var(--text-dim); line-height: 1.5;
    }
    .section-num {
      font-family: 'Newsreader', serif;
      font-size: var(--fs-section); text-transform: uppercase;
      letter-spacing: 0.15em; color: var(--slide-accent);
    }
    .body-text {
      font-family: 'Figtree', sans-serif;
      font-size: var(--fs-body); font-weight: 300;
      line-height: 1.65; color: var(--text-dim);
      max-width: 65ch;
    }
    .mono-label {
      font-family: 'Azeret Mono', monospace;
      font-size: var(--fs-mono); letter-spacing: 0.08em;
      text-transform: uppercase; color: var(--text-muted);
    }

    /* ── NAV BUTTONS ── */
    .nav-btns {
      display: flex; align-items: center; justify-content: flex-end;
      gap: 8px; padding: 12px 20px;
      border-top: 1px solid var(--border);
      flex-shrink: 0;
    }
    .slide-counter {
      font-family: 'Azeret Mono', monospace; font-size: 11px;
      color: var(--text-muted); margin-right: auto;
    }
    .nav-btn {
      width: 36px; height: 36px; border-radius: 8px;
      background: var(--bg-raised); border: 1px solid var(--border);
      color: var(--text-dim); font-size: 16px; cursor: pointer;
      display: flex; align-items: center; justify-content: center;
      transition: all 0.2s; user-select: none;
    }
    .nav-btn:hover { color: var(--text); border-color: var(--slide-accent); }
    .theme-toggle {
      width: 34px; height: 34px; border-radius: 8px;
      background: transparent; border: 1px solid var(--border);
      color: var(--text-dim); cursor: pointer; font-size: 16px;
      display: flex; align-items: center; justify-content: center;
      transition: all 0.2s;
    }
    .theme-toggle:hover { color: var(--text); border-color: var(--slide-accent); }
    /* Zoom controls */
    .zoom-controls { display: flex; align-items: center; gap: 4px;
      padding-right: 10px; margin-right: 6px;
      border-right: 1px solid var(--border); }
    .zoom-btn {
      width: 28px; height: 28px; border-radius: 6px;
      background: var(--bg-raised); border: 1px solid var(--border);
      color: var(--text-dim); font-size: 15px; cursor: pointer;
      display: flex; align-items: center; justify-content: center;
      transition: all 0.2s;
    }
    .zoom-btn:hover { color: var(--text); border-color: var(--slide-accent); }
    .zoom-lbl {
      font-family: 'Azeret Mono', monospace; font-size: 10px;
      color: var(--text-dim); min-width: 36px; text-align: center; cursor: pointer;
    }
    .zoom-lbl:hover { color: var(--slide-accent); }

    /* ── MOBILE ── */
    @media (max-width: 640px) {
      body { flex-direction: column; }
      .chapter-nav {
        width: 100% !important; height: 48px !important;
        flex-direction: row; overflow-x: auto; overflow-y: hidden;
        padding: 0 12px; border-right: none;
        border-bottom: 1px solid var(--border);
        align-items: center; gap: 8px;
      }
      .chapter-nav.mode-minimal .chapter-number { display: block; font-size: 14px; }
      .chapter-title { display: none !important; }
      .chapter-item { flex-direction: row; padding: 0 4px; border-left: none;
        border-bottom: 2px solid transparent; }
      .chapter-item.active { border-bottom-color: var(--slide-accent); }
      .sidebar-mode-btn { display: none; }
      .nav-btns { position: fixed; bottom: 0; left: 0; right: 0;
        background: var(--bg); border-top: 1px solid var(--border); z-index: 100; }
      .slides-area { padding-bottom: 60px; }
    }
    @media (max-width: 900px) and (min-width: 641px) {
      .chapter-nav.mode-full { width: 56px !important; padding: 20px 4px; }
      .chapter-nav.mode-full .chapter-title { display: none; }
    }
  </style>
</head>

<body>

<!--
╔═══════════════════════════════════════════════════════════════════╗
║  DECK INDEX                                                       ║
║  Title   : [Deck Title]                                           ║
║  File    : YYYY-MM-DD_slide-[slug].html                          ║
║  Created : YYYY-MM-DD   Updated: YYYY-MM-DD                      ║
║  Slides  : 05 total   Chapters: 3                                ║
║  Theme   : dark | Sidebar: full | Transition: fade-up            ║
╠═══════════════════════════════════════════════════════════════════╣
║  [01] slide-0  | ch:0 Intro    | "Opening Title"       | ~ln 250 ║
║  [02] slide-1  | ch:0 Intro    | "The Problem"          | ~ln 280 ║
║  [03] slide-2  | ch:1 Main     | "Section Break"        | ~ln 310 ║
║  [04] slide-3  | ch:1 Main     | "Key Insight"          | ~ln 345 ║
║  [05] slide-4  | ch:2 Close    | "Thank You"            | ~ln 375 ║
╠═══════════════════════════════════════════════════════════════════╣
║  HOW TO EDIT: search <!-- SLIDE [##] --> to jump to any slide    ║
╚═══════════════════════════════════════════════════════════════════╝
-->

<!-- SIDEBAR -->
<nav class="chapter-nav mode-full" id="chapterNav">
  <div class="chapter-item active" data-chapter="0" onclick="goToSlide(0)">
    <div class="chapter-number">01</div>
    <div class="chapter-title">Intro</div>
  </div>
  <div class="chapter-item" data-chapter="1" onclick="goToChapter(1)">
    <div class="chapter-number">02</div>
    <div class="chapter-title">Main</div>
  </div>
  <div class="chapter-item" data-chapter="2" onclick="goToChapter(2)">
    <div class="chapter-number">03</div>
    <div class="chapter-title">Close</div>
  </div>
  <button class="sidebar-mode-btn" id="sidebarModeBtn" title="Toggle sidebar">⊟</button>
</nav>

<!-- MAIN -->
<main class="deck-main" id="deckMain">
  <div class="slides-area" id="slidesArea">

    <!-- SLIDE [01] ─── ch:0 "Intro" ─── "Opening Title" ──────────── -->
    <div class="slide active" id="slide-0"
      data-slide="0" data-chapter="0" data-chapter-name="Intro"
      data-title="Opening Title" data-type="title">
      <div class="slide-inner">
        <div class="section-num">01 · Intro</div>
        <h1 class="slide-title">[Deck <em>Title</em>]</h1>
        <p class="slide-subtitle">Subtitle or tagline goes here</p>
      </div>
    </div>
    <!-- END SLIDE [01] ────────────────────────────────────────────── -->

    <!-- SLIDE [02] ─── ch:0 "Intro" ─── "The Problem" ────────────── -->
    <div class="slide" id="slide-1"
      data-slide="1" data-chapter="0" data-chapter-name="Intro"
      data-title="The Problem" data-type="content">
      <div class="slide-inner">
        <div class="section-num">02</div>
        <h2 class="slide-title">The <em>Problem</em></h2>
        <p class="body-text">Body text here. Keep it short — one idea per slide.</p>
      </div>
    </div>
    <!-- END SLIDE [02] ────────────────────────────────────────────── -->

    <!-- add more slides following same pattern -->

  </div>

  <!-- NAV BUTTONS -->
  <div class="nav-btns">
    <span class="slide-counter" id="slideCounter">01 / 05</span>
    <div class="zoom-controls">
      <button class="zoom-btn" id="zoomOut">−</button>
      <span class="zoom-lbl" id="zoomLbl">100%</span>
      <button class="zoom-btn" id="zoomIn">+</button>
    </div>
    <button class="theme-toggle" id="themeToggle">◐</button>
    <button class="nav-btn" id="prevBtn">←</button>
    <button class="nav-btn" id="nextBtn">→</button>
  </div>
</main>

<script>
// ── STATE ──
let currentSlide = 0;
let currentTheme = 'dark';
let scale = 1.0;
const SCALE_MIN = 0.5, SCALE_MAX = 2.0, SCALE_STEP = 0.1;
const SIDEBAR_MODES = ['mode-full', 'mode-compact', 'mode-minimal'];
const SIDEBAR_ICONS = {'mode-full':'⊟','mode-compact':'≡','mode-minimal':'·'};
let sidebarModeIdx = 0;

// ── SLIDES ──
const slides = Array.from(document.querySelectorAll('.slide'));
const total  = slides.length;

function goToSlide(n) {
  if (n < 0 || n >= total) return;
  slides[currentSlide].classList.remove('active');
  currentSlide = n;
  slides[currentSlide].classList.add('active');
  document.getElementById('slideCounter').textContent =
    String(currentSlide + 1).padStart(2,'0') + ' / ' + String(total).padStart(2,'0');
  updateChapterNav();
}
function goToChapter(ch) {
  const first = slides.findIndex(s => parseInt(s.dataset.chapter) === ch);
  if (first >= 0) goToSlide(first);
}

// ── NAV ──
document.getElementById('nextBtn').addEventListener('click', () => goToSlide(currentSlide + 1));
document.getElementById('prevBtn').addEventListener('click', () => goToSlide(currentSlide - 1));
document.addEventListener('keydown', e => {
  if (e.key === 'ArrowRight' || e.key === 'ArrowDown') { e.preventDefault(); goToSlide(currentSlide+1); }
  if (e.key === 'ArrowLeft'  || e.key === 'ArrowUp')   { e.preventDefault(); goToSlide(currentSlide-1); }
  if ((e.ctrlKey||e.metaKey) && e.key === '=') { e.preventDefault(); setScale(scale+SCALE_STEP); }
  if ((e.ctrlKey||e.metaKey) && e.key === '-') { e.preventDefault(); setScale(scale-SCALE_STEP); }
  if ((e.ctrlKey||e.metaKey) && e.key === '0') { e.preventDefault(); setScale(1.0); }
});

// ── CHAPTER NAV ──
function updateChapterNav() {
  const currentCh = parseInt(slides[currentSlide].dataset.chapter ?? 0);
  document.querySelectorAll('.chapter-item').forEach(item => {
    const ch = parseInt(item.dataset.chapter ?? -1);
    item.classList.toggle('active', ch === currentCh);
  });
}

// ── SIDEBAR MODE SWITCH ──
function cycleSidebarMode() {
  const nav = document.getElementById('chapterNav');
  const btn = document.getElementById('sidebarModeBtn');
  nav.classList.remove(...SIDEBAR_MODES);
  sidebarModeIdx = (sidebarModeIdx + 1) % SIDEBAR_MODES.length;
  const mode = SIDEBAR_MODES[sidebarModeIdx];
  nav.classList.add(mode);
  btn.textContent = SIDEBAR_ICONS[mode];
  setTimeout(updateSlideSize, 320);
}
document.getElementById('sidebarModeBtn')?.addEventListener('click', cycleSidebarMode);

// ── THEME ──
document.getElementById('themeToggle').addEventListener('click', () => {
  currentTheme = currentTheme === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', currentTheme);
});

// ── ZOOM ──
function setScale(v) {
  scale = Math.round(Math.min(SCALE_MAX, Math.max(SCALE_MIN, v)) * 10) / 10;
  document.documentElement.style.setProperty('--content-scale', scale);
  document.getElementById('zoomLbl').textContent = Math.round(scale*100) + '%';
}
document.getElementById('zoomIn') ?.addEventListener('click', () => setScale(scale+SCALE_STEP));
document.getElementById('zoomOut')?.addEventListener('click', () => setScale(scale-SCALE_STEP));
document.getElementById('zoomLbl')?.addEventListener('click', () => setScale(1.0));

// ── RESPONSIVE: auto-fit slide to viewport ──
function updateSlideSize() {
  const slidesArea = document.getElementById('slidesArea');
  const aW = slidesArea.offsetWidth  - 40;
  const aH = slidesArea.offsetHeight - 40;
  const byW = aW;
  const byH = aH * 16 / 9;
  const w   = Math.min(byW, byH);
  document.querySelectorAll('.slide').forEach(s => {
    s.style.maxWidth  = w + 'px';
    s.style.maxHeight = (w * 9 / 16) + 'px';
  });
}
const resizeObs = new ResizeObserver(updateSlideSize);
resizeObs.observe(document.getElementById('deckMain'));
window.addEventListener('load', updateSlideSize);

// ── DECK INDEX (runtime) ──
window.DECK_INDEX = slides.map(el => ({
  n:      parseInt(el.dataset.slide ?? 0) + 1,
  id:     el.id,
  ch:     parseInt(el.dataset.chapter ?? 0),
  chName: el.dataset.chapterName ?? '',
  title:  el.dataset.title ?? '',
  type:   el.dataset.type ?? 'content',
}));
</script>

</body>
</html>
```

---

## [v3] Updated Workflow

1. **Hỏi Hoan 3 câu:**
   - Deck về gì, audience, bao nhiêu slides?
   - Sidebar mode mặc định (full/compact/minimal)?
   - Optical center technique (A/B/C)?
2. **Draft outline** với DECK INDEX structure → Hoan approve
3. **Dùng Full Boilerplate Template v3** làm baseline
4. **Fill slides** — mỗi slide có `<!-- SLIDE [##] -->` marker + `data-*` attributes
5. **Save** `YYYY-MM-DD_slide-[slug].html`

---

## Session learnings

- 2026-04-08: Skill created. Base template dùng sidebar variant A + transition 1 làm default.
- 2026-04-09: Upgrade v2 — thêm zoom controls, --content-scale system, gradient backgrounds, noise grain, export PDF.
- 2026-04-14: Upgrade v3 — 4 cơ chế mới: [v3-1] Fluid responsive (clamp() + ResizeObserver + mobile breakpoints), [v3-2] Sidebar mode switch (full/compact/minimal, cycle button ⊟≡·), [v3-3] Optical centering (Technique A/B/C, default: padding-bottom 8%), [v3-4] AI-friendly indexing (DECK INDEX comment, slide markers, data-* attributes, runtime DECK_INDEX array). Full boilerplate template v3 tích hợp tất cả.
- 2026-04-15: Upgrade v3.1 — Thêm 2 best practices từ AI 101 deck:
  - [v3-5] Sidebar Chapter Navigation: Thay vì hiển thị tất cả slides, sidebar nhóm slides thành chapters (5-6 chapters), hiển thị vertical line + progress bar + sub-dots cho slides trong chapter. Pattern: `const chapters = [{name:'Title', slides:[0,1]}, ...]` + `buildNav()` function.
  - [v3-6] Font Size Guidelines: Content text tối thiểu 11-12px (không dùng 7-9px), labels tối thiểu 10px, mono text tối thiểu 9px. Dùng clamp() cho fluid scaling.

---

## [v3-5] Sidebar Chapter Navigation (AI 101 Pattern)

Thay vì hiển thị tất cả slides trong sidebar (có thể 20+ items), nhóm slides thành 5-6 chapters chính. Sidebar hiển thị:
- Vertical line với progress fill
- Dot cho mỗi chapter
- Sub-dots cho slides trong chapter đang active

### JavaScript Pattern

```javascript
const chapters = [
  { name: 'Title',    slides: [0, 1] },
  { name: 'Part 01',  slides: [2, 3, 4, 5] },
  { name: 'Part 02',  slides: [6, 7, 8] },
  { name: 'Part 03',  slides: [9, 10, 11, 12, 13, 14, 15, 16] },
  { name: 'Part 04',  slides: [17, 18, 19] },
  { name: 'Part 05',  slides: [20, 21, 22] }
];

function buildNav() {
  const nav = document.getElementById('chapterNav');
  chapters.forEach((ch, chIdx) => {
    const item = document.createElement('div');
    item.className = 'nav-item';
    item.dataset.chapter = chIdx;
    
    const subDotsHtml = ch.slides.map((slideIdx) => 
      `<div class="nav-sub-dot" data-slide="${slideIdx}"></div>`
    ).join('');
    
    item.innerHTML = `
      <div class="nav-dot"></div>
      <div class="nav-label">${ch.name}</div>
      <div class="nav-sub-dots">${subDotsHtml}</div>
    `;
    
    item.addEventListener('click', () => goToSlide(ch.slides[0]));
    nav.insertBefore(item, document.getElementById('sidebarModeBtn'));
  });
}
```

### CSS cho Chapter Nav

```css
.nav-line { position: absolute; left: 35px; top: 50px; bottom: 80px; width: 1px; background: var(--border); }
.nav-line-progress { position: absolute; left: 35px; top: 50px; width: 2px; background: var(--accent-1); transition: height .3s ease; }
.nav-item { display: flex; align-items: center; gap: 12px; padding: 10px 0; cursor: pointer; position: relative; z-index: 1; }
.nav-dot { width: 7px; height: 7px; border-radius: 50%; background: var(--text-muted); transition: all .2s ease; }
.nav-item.active .nav-dot { width: 9px; height: 9px; background: var(--accent-1); box-shadow: 0 0 8px rgba(196,149,106,.4); }
.nav-sub-dots { display: flex; gap: 4px; margin-left: 8px; }
.nav-sub-dot { width: 4px; height: 4px; border-radius: 50%; background: var(--text-muted); opacity: .4; transition: all .2s ease; }
.nav-sub-dot.active { opacity: 1; background: var(--accent-1); }
```

**Best for:** Decks 15+ slides với cấu trúc chapter rõ ràng. Giúp navigation không bị quá dài.

---

## [v3-6] Font Size Guidelines

### Minimum readable sizes (đã test trên nhiều deck)

| Element | Min Size | Recommended | Notes |
|---------|----------|-------------|-------|
| Body text | 11px | 13-14px | Nội dung chính |
| Labels, captions | 10px | 11-12px | Mô tả, chú thích |
| Mono text (code, data) | 9px | 10-11px | Font monospace nhìn nhỏ hơn |
| Section numbers | 10px | 11px | Uppercase, letter-spacing |
| Slide numbers | 9px | 10px | Counter ở góc |

### CSS Pattern với clamp()

```css
:root {
  /* Fluid type scale - đảm bảo không nhỏ hơn min ở mọi viewport */
  --fs-body:     clamp(11px, 1.4vw, 16px);  /* min 11px */
  --fs-label:    clamp(10px, 1.1vw, 13px);  /* min 10px */
  --fs-mono:     clamp(10px, 0.9vw, 12px);  /* min 10px (mono nhìn nhỏ hơn) */
  --fs-section:  clamp(10px, 0.8vw, 12px);  /* min 10px */
}

/* Không dùng kích thước cố định nhỏ hơn 10px cho content có nghĩa */
/* Tránh: font-size: 7px, 8px, 9px cho text đọc được */
```

### Anti-patterns (tránh)

```css
/* ❌ Không dùng - quá nhỏ để đọc */
.tc-lbl { font-size: 7px; }   /* → dùng 10-11px */
.ba-cap { font-size: 10px; }  /* → dùng 12-13px */
.plb { font-size: 8px; }      /* → dùng 10px */

/* ✅ Pattern đúng */
.tc-lbl { font-family: var(--mono); font-size: clamp(10px, 0.9vw, 12px); letter-spacing: .2em; text-transform: uppercase; }
.ba-cap { font-size: clamp(12px, 1.2vw, 14px); color: var(--text-dim); }
.plb { font-family: var(--mono); font-size: clamp(10px, 0.85vw, 11px); }
```
