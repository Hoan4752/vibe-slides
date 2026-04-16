---
name: vibe-slides-pro
description: Build professional HTML slide decks with light theme, click navigation, and watermark branding. Use when creating presentation slides for Khai Hoan | Nghien AI content, workshop slides, pitch decks, or any professional presentation requiring clean editorial design with watermark.
---

# vibe-slides-pro

Build professional HTML slide decks — single-file, click-navigated, keyboard-supported, with watermark branding. Light theme default, editorial design language inspired by D-Squared and AI Agents Presentation style.

## When to trigger

- "Làm slide cho workshop / talk / pitch / share"
- "HTML slide deck", "vibe slide", "presentation slide"
- "Slide có watermark Khai Hoan | Nghien AI"
- "Slide kiểu light theme"
- Hoan đang build content presentation

**Không dùng khi:** user muốn .pptx thật (dùng `pptx` skill) hoặc cần slide animated kiểu video.

## Output contract

1 file HTML duy nhất, self-contained (fonts từ Google Fonts CDN, CSS + JS inline). Save vào:
- `html-files/` nếu là demo/test
- `workshop-planner/deliverables/` hoặc `workshop-planner/drafts/` nếu là slide workshop thật
- Naming: `YYYY-MM-DD_slide-[slug].html`

File HTML phải có:
- **Light theme default** (không có dark theme toggle)
- **Watermark** "Khai Hoan | Nghien AI" bên cạnh slide counter (CHỈ 1 watermark ở top-right)
- **Click to navigate**: Click anywhere trên slide để next
- **Button navigation**: ← → buttons ở bottom-right
- **Zoom controls**: + − buttons ở bottom-right (cùng row với nav buttons)
- **Keyboard nav**: ← → ↑ ↓ chuyển slide, Ctrl/Cmd + +/- để zoom
- **Chapter sidebar**: Dot-line nav bên trái với label, mỗi chapter có accent color riêng
- **Slide counter**: `15 / 20 | Khai Hoan | Nghien AI` ở top-right
- **Staggered animation**: Elements fade in sequence (anim-1, anim-2...)
- **SVG diagrams**: Inline SVG cho charts, diagrams, illustrations
- **Responsive**: Mobile-friendly với sidebar collapse, touch swipe support

## Design tokens (source of truth)

### Light theme (default)
```css
--bg: #FAFAF8;
--bg-subtle: #F5F3EF;
--bg-surface: #FFFFFF;
--text: #1A1A1F;
--text-dim: #5A5560;
--text-muted: #8A8590;
--border: #E4E0D6;
--accent-1: #C7956D;  /* warm gold (primary) */
--accent-2: #6AADA7;  /* teal */
--accent-3: #B87A8A;  /* rose */
--accent-4: #8AAB72;  /* sage */
--accent-5: #C7B88A;  /* sand */
```

### Typography
```css
/* Google Fonts import */
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,300;0,400;0,600;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600&family=Fira+Code:wght@300;400;500&display=swap');

/* Usage */
.slide-title    { font-family: 'Fraunces', serif; font-size: clamp(32px, 4vw, 52px); font-weight: 300; line-height: 1.15; }
.slide-title em { font-style: italic; font-weight: 600; color: var(--slide-accent); }
.section-label  { font-family: 'Fira Code', monospace; font-size: 11px; text-transform: uppercase; letter-spacing: 0.12em; }
.body-text      { font-family: 'Plus Jakarta Sans', sans-serif; font-size: clamp(14px, 1.4vw, 18px); font-weight: 400; }
.mono-text      { font-family: 'Fira Code', monospace; font-size: clamp(10px, 0.9vw, 13px); }
```

**Rule:** Titles = serif (Fraunces), với 1 từ italic màu accent. Body = sans (Plus Jakarta Sans). Labels/data/code = mono (Fira Code).

## Sidebar navigation

Pattern từ AI Agents Presentation — vertical dot-line nav với chapter labels:

```html
<nav class="chapter-nav" id="chapterNav">
  <div class="nav-line"></div>
  <div class="nav-line-progress" id="navProgress"></div>
  <!-- nav items injected by JS -->
</nav>
```

```css
.chapter-nav {
  position: fixed; left: 40px; top: 50%; transform: translateY(-50%);
  z-index: 100; display: flex; flex-direction: column; align-items: flex-start;
}
.nav-item {
  display: flex; align-items: center; gap: 14px; padding: 10px 0;
  cursor: pointer; transition: all 0.4s cubic-bezier(0.22, 1, 0.36, 1);
}
.nav-dot {
  width: 5px; height: 5px; border-radius: 50%; background: var(--text-muted);
  transition: all 0.4s cubic-bezier(0.22, 1, 0.36, 1);
}
.nav-item.active .nav-dot {
  width: 8px; height: 8px; background: var(--accent);
  box-shadow: 0 0 12px var(--accent);
}
.nav-label {
  font-family: 'Plus Jakarta Sans', sans-serif; font-size: 11px; font-weight: 500;
  letter-spacing: 0.08em; text-transform: uppercase; color: var(--text-muted);
  transition: all 0.4s cubic-bezier(0.22, 1, 0.36, 1);
}
.nav-item.active .nav-label { color: var(--accent); }
.nav-line { width: 1px; height: 16px; background: var(--text-muted); margin-left: 6.5px; opacity: 0.4; }
```

**Behavior:**
- Mỗi chapter có `accent` color riêng (truyền qua JS)
- Click nav-item để jump đến slide đầu của chapter
- Progress line fill theo chapter hiện tại

## Slide counter + Watermark

```html
<div class="slide-counter" id="slideCounter">
  <span class="current">1</span> / <span class="total">12</span>
  <span class="watermark">| Khai Hoan | Nghien AI</span>
</div>
```

```css
.slide-counter {
  position: fixed; top: 36px; right: 48px;
  font-family: 'Fira Code', monospace; font-size: 13px;
  color: var(--text-dim); z-index: 100; letter-spacing: 0.05em;
}
.slide-counter .watermark {
  margin-left: 12px;
  color: var(--text-muted);
  opacity: 0.7;
}
```

## Click to navigate

```javascript
// Click anywhere on slide to go next
document.querySelectorAll('.slide').forEach(slide => {
  slide.addEventListener('click', (e) => {
    // Don't navigate if clicking on interactive elements
    if (e.target.closest('a, button, input, textarea, [contenteditable]')) return;
    goToSlide(currentSlide + 1);
  });
});
```

## Navigation buttons + Zoom controls

```html
<div class="nav-btns">
  <button class="nav-btn" id="prevBtn" aria-label="Previous slide">←</button>
  <button class="nav-btn" id="nextBtn" aria-label="Next slide">→</button>
  <div class="zoom-divider"></div>
  <button class="nav-btn zoom-btn" id="zoomOut" aria-label="Zoom out">−</button>
  <span class="zoom-level" id="zoomLevel">100%</span>
  <button class="nav-btn zoom-btn" id="zoomIn" aria-label="Zoom in">+</button>
</div>
```

```css
.nav-btns {
  position: fixed; bottom: 32px; right: 48px;
  display: flex; gap: 8px; z-index: 100; align-items: center;
}
.nav-btn {
  width: 40px; height: 40px; border-radius: 8px;
  background: var(--bg-surface); border: 1px solid var(--border);
  color: var(--text-dim); font-size: 16px; cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  transition: all 0.2s ease;
}
.nav-btn:hover {
  color: var(--text); border-color: var(--slide-accent);
  background: var(--bg-subtle);
}
.nav-btn:disabled { opacity: 0.3; cursor: not-allowed; }
.zoom-divider { width: 1px; height: 24px; background: var(--border); margin: 0 4px; }
.zoom-level {
  font-family: 'Fira Code', monospace; font-size: 11px;
  color: var(--text-muted); min-width: 36px; text-align: center;
  cursor: pointer; user-select: none;
}
.zoom-level:hover { color: var(--slide-accent); }
```

**Zoom JavaScript:**
```javascript
let scale = 1.0;
const SCALE_MIN = 0.5, SCALE_MAX = 2.0, SCALE_STEP = 0.1;

function setScale(v) {
  scale = Math.round(Math.min(SCALE_MAX, Math.max(SCALE_MIN, v)) * 10) / 10;
  document.documentElement.style.setProperty('--slide-scale', scale);
  document.getElementById('zoomLevel').textContent = Math.round(scale * 100) + '%';
}

document.getElementById('zoomIn').addEventListener('click', (e) => {
  e.stopPropagation();
  setScale(scale + SCALE_STEP);
});
document.getElementById('zoomOut').addEventListener('click', (e) => {
  e.stopPropagation();
  setScale(scale - SCALE_STEP);
});
document.getElementById('zoomLevel').addEventListener('click', (e) => {
  e.stopPropagation();
  setScale(1.0);
});

// Keyboard zoom
document.addEventListener('keydown', e => {
  if ((e.ctrlKey || e.metaKey)) {
    if (e.key === '=' || e.key === '+') { e.preventDefault(); setScale(scale + SCALE_STEP); }
    else if (e.key === '-') { e.preventDefault(); setScale(scale - SCALE_STEP); }
    else if (e.key === '0') { e.preventDefault(); setScale(1.0); }
  }
});
```

## Animation system

Staggered fade-in animation (giống AI Agents Presentation):

```css
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(16px); }
  to { opacity: 1; transform: translateY(0); }
}
.slide.active .anim-1 { animation: fadeInUp 0.6s 0.1s cubic-bezier(0.22, 1, 0.36, 1) both; }
.slide.active .anim-2 { animation: fadeInUp 0.6s 0.25s cubic-bezier(0.22, 1, 0.36, 1) both; }
.slide.active .anim-3 { animation: fadeInUp 0.6s 0.4s cubic-bezier(0.22, 1, 0.36, 1) both; }
.slide.active .anim-4 { animation: fadeInUp 0.6s 0.55s cubic-bezier(0.22, 1, 0.36, 1) both; }
```

## Slide structure

```html
<div class="slide active" data-chapter="0">
  <div class="slide-inner">
    <div class="section-label anim-1" style="color: var(--accent-1);">Chapter 01</div>
    <h1 class="slide-title anim-2">Three forces — <em>all at once</em></h1>
    <div class="hairline anim-3"></div>
    <!-- SVG or content here -->
  </div>
</div>
```

## Chapter configuration

```javascript
const chapters = [
  { name: 'Why Now', color: '#C7956D', slides: [0, 1] },
  { name: 'What\'s Different', color: '#6AADA7', slides: [2, 3, 4, 5] },
  { name: 'When to Use Which', color: '#B87A8A', slides: [6, 7] },
  { name: 'Your First Time', color: '#8AAB72', slides: [8, 9] },
  { name: 'Recap', color: '#C7B88A', slides: [10, 11] }
];
```

## Component library

### Hairline divider
```css
.hairline { width: 60px; height: 1px; background: var(--border); opacity: 0.5; }
```

### SVG Diagrams
Inline SVG với viewBox, sử dụng CSS variables cho colors:
```html
<svg viewBox="0 0 740 300" width="740" height="300">
  <line x1="138" y1="44" x2="358" y2="148" stroke="var(--accent-1)" stroke-width="1.5"/>
  <circle cx="370" cy="152" r="5" fill="var(--accent-1)"/>
</svg>
```

### Recap cards
```css
.recap-grid { display: flex; flex-direction: column; align-items: center; gap: 16px; }
.recap-row { display: flex; gap: 16px; justify-content: center; }
.recap-card {
  display: flex; flex-direction: column; align-items: center; gap: 10px;
  padding: 20px 16px; border-radius: 8px;
  border: 1px solid var(--border); background: var(--bg-subtle);
  width: 190px; text-align: center;
}
```

## Workflow khi được gọi

1. **Hỏi Hoan 3 câu nếu chưa có:**
   - Slide deck về chủ đề gì, audience ai, bao nhiêu slide?
   - Có cần SVG diagrams không? (nếu có → mô tả diagram cần)
   - Chapter structure như thế nào?

2. **Draft outline text-only trước** (chapter structure + slide titles) để Hoan approve.

3. **Copy `base.html` → file mới** theo naming convention, fill slides.

4. **Save đúng folder** (html-files/ hoặc workshop-planner/).  

5. **Confirm path + preview link cho Hoan.**

## Hard rules

- Single file HTML. Không chia CSS/JS ra file riêng.
- Light theme ONLY (không có dark toggle).
- Watermark LUÔN có: "| Khai Hoan | Nghien AI" sau counter ở top-right (KHÔNG có watermark thứ 2 ở slide)
- Click anywhere on slide để next (trừ interactive elements).
- Navigation buttons LUÔN có ở bottom-right.
- Zoom controls (+ − reset) LUÔN có ở bottom-right.
- Sidebar chapter nav LUÔN có với dot-line style.
- Animation staggered LUÔN có (anim-1, anim-2...).
- Mỗi chapter có accent color riêng.
- Fonts từ Google Fonts CDN (không self-host).
- NO localStorage / sessionStorage — dùng JS variable.
- Slide title LUÔN có 1 từ italic accent.
- Slide count minimum 3, maximum 25.
- Responsive: Mobile viewport hỗ trợ, touch swipe gestures.

## Full boilerplate template

Xem `base.html` trong folder này cho complete template với tất cả features.
