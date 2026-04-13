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

## Session learnings

- 2026-04-08: Skill created. Base template dùng sidebar variant A + transition 1 làm default. User có thể swap bằng prompt "dùng variant B / transition 3".
- 2026-04-09: Upgrade v2 — thêm zoom controls (+/-/Ctrl+=/0), --content-scale responsive system, radial gradient backgrounds (theme-aware), noise grain opacity 0.028, export_slides.py PDF workflow (1920×1080 → 960×540pt reportlab, scale 1.2). Tất cả là MUST-HAVE default cho mọi deck mới.
