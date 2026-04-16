---
name: visual-prompt-card
description: >
  Build polished NghienAI-branded HTML visual cards styled as macOS terminal windows, Claude chat
  interfaces with annotation labels, concept title cards, thumbnails, or social post covers.
  Use this skill whenever the user wants to visualize text/outline as a styled card, "make this
  look like a terminal", "create a prompt structure visual", "turn this into a visual post",
  "build template 1/2/3", make educational AI/prompt visuals, or create shareable knowledge cards.
  ALWAYS trigger this skill before building any HTML artifact that should look like a terminal
  window, chat screenshot, or concept card — even if the user says "just make a quick visual"
  or doesn't name the skill explicitly.
---

# NghienAI Visual Prompt Card Builder

Produces single-file `.html` artifacts — polished NghienAI visual cards for social media, newsletters, course content, and AI education assets. Five templates available.

---

## NghienAI brand system — default for every template

Use this brand system unless the user explicitly asks for a non-NghienAI style. Source of truth:

- Brand guideline: `/Users/khaihoan/Library/Mobile Documents/com~apple~CloudDocs/Claude AI/Qorder Brain/tools/vibe-slides-pro-nghienai/BRAND_GUIDELINE.md`
- Primary logo: `/Users/khaihoan/Library/Mobile Documents/com~apple~CloudDocs/Claude AI/Qorder Brain/tools/NghienAI_logo_orange.svg`
- Optional logomarks: `tools/NghienAI_logomark_orange.svg`, `tools/NghienAI_logomark_white.svg`

### Brand tokens

```css
:root {
  --neo-pearl: #F7F5ED;
  --deep-dark-blue: #2A3140;
  --neon-coral: #FF623B;
  --tangy-yellow: #FFE032;
  --electric-violet: #8F00FF;
  --turquoise-blue: #088B96;
  --blue-glow: #4850ED;

  --title-font: 'IBM Plex Serif', serif;
  --heading-font: 'IBM Plex Sans', sans-serif;
  --body-font: 'IBM Plex Sans', sans-serif;
  --mono-font: 'IBM Plex Mono', monospace;
}
```

### Required font import

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Serif:wght@400;500;600;700&display=swap" rel="stylesheet">
```

### Typography rules

- `.title` / one main display title only: IBM Plex Serif, `clamp(36px, 4vw, 72px)` or equivalent fixed-canvas px size.
- `h1`, `h2`, `h3`, `.h1`, `.h2`, `.h3`: IBM Plex Sans.
- Body copy and UI controls: IBM Plex Sans.
- Labels, tags, counters, code, and metadata: IBM Plex Mono.
- Serif is never used for secondary headings, labels, pills, captions, or UI.
- Keep `letter-spacing: 0` unless recreating a logo SVG; do not use negative tracking.

### Logo rules

- Use the real SVG file, not a text-only "NGHIÊN AI" box.
- Place one NghienAI logo at top-left for branded cards, sized around `clamp(32px, 3vw, 48px)` on responsive pages or 40-52px tall on fixed canvases.
- Do not add brand-name text beside the logo; the logo already contains the wordmark.
- If another brand/product logo is part of the content, keep it visually separate from the NghienAI logo and inside its own safe area.

### Visual language

- Default background: `--neo-pearl`.
- Primary text: `--deep-dark-blue`.
- Primary accent: `--neon-coral`.
- Secondary accents: tangy yellow, turquoise, electric violet, blue glow.
- Use human-made rough edges only on shapes, boxes, chips, circles, triangles, stars, and halftone accents. Never apply rough filters to text or logos.
- Use wrapper patterns for rough shapes so inner text remains sharp.
- Prefer halftone bands, stepped panels, handmade dots, cursor/selection handles, and editorial asymmetry over generic gradients.

---

## Step 1 — Identify template, gather inputs, and get approval

**MANDATORY: Always ask → always preview → always wait for approval before building.**

1. Ask the user to determine which template and gather missing inputs.
2. After gathering inputs, send a **written content outline** in plain text — showing title, subtitle, all terminal content, and any detail blocks exactly as they will appear.
3. Wait for explicit confirmation ("ok", "build it", "go ahead") before writing any HTML file.
4. Only after approval: build and save the file.

Never skip the preview step, even for small changes or tweaks.

- **Template 1 — Terminal Window**: macOS terminal on NghienAI neo-pearl halftone/grid background. Best for outlines, rules, step-by-step instructions.
- **Template 2 — Chat Annotator**: Claude chat box with color-coded annotation pills + SVG connector lines. Best for prompt structure breakdowns.
- **Template 3 — Concept Card**: Large expressive title + subtitle + terminal window. Best for educational explainers, newsletter visuals.
- **Template 4 — Horizontal Brand Thumbnail**: Fixed landscape canvas (16:9 or 5:2). Two-column layout — text left, optional subject/product asset right. Best for YouTube thumbnails, FB post covers, LinkedIn banners. Features NghienAI logo chrome, cascade pills, cursor decoration, human-made shapes, and IBM Plex typography.
- **Template 5 — Background Photo Card**: Fixed 1:1 square canvas (1080×1080px). Uses a NghienAI neo-pearl/halftone background or embedded workspace image. Content layered on top: context tag, real NghienAI logo, large title, inline icon or icon grid, cascade pills, cursor decoration. Best for FB post thumbnails, carousels, social story slides.

**Template 1 inputs:**
- `window_title` — filename in titlebar (e.g. `claude.md`)
- `badge_text` / `badge_color` — optional pill label (default color `#6c5ce7`)
- `content` — text body; `**bold**` = accent highlight, `` `code` `` = inline code
- `accent_color` — default `#FF623B`
- `window_count` — 1, 2, or 3 side-by-side windows
- `window_number` — optional corner label `01`, `02`, etc.

**Template 2 inputs:**
- `page_title` — large heading above
- `panel_count` — 1, 2, or 4 panels (see multi-panel section below)
- `chat_content` — full message text, paragraphs separated by blank lines
- `annotations` — list of `{label, color?, paragraph_index}`
- `model_label` — chat footer label (e.g. `Opus 4.6`)
- `show_connector_lines` — default true; SVG bezier curves from paragraph → pill

**Template 3 inputs:**
- `main_title` — headline; `**text**` for accent color
- `subtitle` — smaller italic text below title
- `window_title` — terminal window label
- `content` — terminal content (`**bold**` / `` `code` `` syntax)
- `accent_color` — default `#FF623B`
- `font_style` — default `nghienai` (IBM Plex Serif for `.title`, IBM Plex Sans for all other text). Only use a non-brand font if the user explicitly asks.

---

## Template 1 — Terminal Window HTML

```
Page: background #F7F5ED, subtle halftone/grid 30px rgba(42,49,64,0.06), min-height 100vh, flex center, padding 60px 40px
Font: IBM Plex Sans for page; IBM Plex Mono for terminal content
Brand chrome: one NghienAI orange logo top-left, no adjacent brand-name text

Window:
  background: #2A3140
  border-radius: 8px
  box-shadow: 0 24px 70px rgba(42,49,64,0.24), 0 0 0 1px rgba(42,49,64,0.10)
  width: 660px (single); auto flex (multi)
  overflow: hidden

Titlebar:
  background: rgba(255,255,255,0.04)
  border-bottom: 1px solid rgba(255,255,255,0.06)
  padding: 13px 18px, display flex, align-items center, gap 8px

Traffic lights: 12×12px circles
  red: #ff5f56   yellow: #ffbd2d   green: #28c93f

Window title: rgba(247,245,237,0.55), 13px, margin 0 auto
Badge: background badge_color, white text, padding 3px 10px, border-radius 4px, 11px

Content:
  padding: 24px 28px
  color: rgba(247,245,237,0.84)
  font-size: 14px, line-height: 1.75

Window number: position absolute top-right, rgba(255,255,255,0.12), 28px
```

Content parsing: `**text**` → accent span | `` `text` `` → code span | blank line → margin-top 14px | `<br>` for line breaks

Multi-window: flex row, gap 20px, page padding 80px 60px.

---

## Template 2 — Chat Annotator HTML

### Layout

```
Page: #F7F5ED background with subtle halftone/grid accents
Wrapper: max-width 960px, margin auto, padding 60px 40px
Brand chrome: one NghienAI orange logo top-left, no adjacent brand-name text

Page title: 30px bold, IBM Plex Sans, text-align center, margin-bottom 36px, color #2A3140

Content layout: position relative (needed for SVG overlay)
  display flex, gap 32px, align-items flex-start

Chat box (left, flex 1):
  background white
  border: 1.5px solid rgba(42,49,64,0.18)
  border-radius: 8px, overflow hidden

Chat content: padding 24px 24px 16px, font-size 13.5px, line-height 1.78, color #2A3140
Each <p data-para="N">: margin-bottom 13px, padding 4px 6px, border-radius 4px

Chat footer: background rgba(42,49,64,0.06), padding 10px 16px, flex space-between
  Left: "+ Q ↗"   Right: "{model_label} ∨ →" as pill

Annotations (right, min-width 148px):
  display flex, flex-direction column, gap 8px, padding-top 4px
  Each pill: padding 9px 16px, border-radius 6px, font-size 12.5px bold, text-align center
```

### Default color palette
```
1: #FF623B   2: #088B96   3: #4850ED   4: #8F00FF
5: #FFE032 (dark text)   6: #2A3140   7: #FF8A6A   8: #0FB7C5
```

### SVG Connector Lines (ALWAYS implement this)

The connector lines link each annotation pill to its corresponding paragraph. This is the key visual feature that makes the annotations meaningful.

**Implementation:**

1. Add an SVG element as the FIRST child of `.layout` (so it renders behind content):
```html
<svg id="connectors" style="position:absolute;top:0;left:0;width:100%;height:100%;pointer-events:none;overflow:visible;z-index:0;"></svg>
```
Make `.layout` position:relative.

2. Run after DOM renders (`window.addEventListener('load', drawLines)`):
```javascript
function drawLines() {
  const svg = document.getElementById('connectors');
  const layout = svg.parentElement;
  const layoutRect = layout.getBoundingClientRect();

  document.querySelectorAll('.pill[data-target]').forEach(pill => {
    const target = pill.dataset.target;
    const para = document.querySelector(`p[data-para="${target}"]`);
    if (!para) return;

    const pRect = para.getBoundingClientRect();
    const pillRect = pill.getBoundingClientRect();

    // Start: right-center of paragraph | End: left-center of pill
    const x1 = pRect.right - layoutRect.left;
    const y1 = pRect.top + pRect.height / 2 - layoutRect.top;
    const x2 = pillRect.left - layoutRect.left;
    const y2 = pillRect.top + pillRect.height / 2 - layoutRect.top;

    // Smooth cubic bezier: horizontal handles at 40% of the gap
    const cx = (x1 + x2) / 2;
    const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    path.setAttribute('d', `M ${x1} ${y1} C ${cx} ${y1}, ${cx} ${y2}, ${x2} ${y2}`);
    path.setAttribute('fill', 'none');
    path.setAttribute('stroke', pill.dataset.linecolor || '#aaa');
    path.setAttribute('stroke-width', '1.5');
    path.setAttribute('stroke-dasharray', '5,3');
    path.setAttribute('opacity', '0.35');
    svg.appendChild(path);
  });
}
window.addEventListener('load', drawLines);
```

3. Store each pill's color in `data-linecolor` attribute:
```html
<div class="pill" style="background:#FF623B" data-target="1" data-linecolor="#FF623B">Nhiệm vụ</div>
```

4. Also implement hover: on pill mouseenter, highlight target paragraph (rgba color, 0.12 opacity) and increase line opacity to 0.7. On mouseleave, reset.

### Multi-panel variant (2 or 4 panels)

When `panel_count` is 2 or 4:
- Each panel is a self-contained chat box + its own annotation column
- Layout for 2 panels: two side-by-side units in a flex row (each unit = chat + annotations)
- Layout for 4 panels: 2×2 grid using `display: grid; grid-template-columns: 1fr 1fr`
- Each panel unit is `position: relative` for its own SVG connector layer
- Reduce font sizes slightly (13px → 12px, pills 12px → 11px) for 4-panel layout
- Page max-width increases: 1100px for 2-panel, 1200px for 4-panel

---

## Template 3 — Concept Card HTML

```
Page: background #F7F5ED (clean or subtle halftone)
Max-width: 760px, margin auto, padding 64px 52px
Brand chrome: one NghienAI orange logo top-left, no adjacent brand-name text

Font loading: import IBM Plex from Google Fonts:
  title only → IBM Plex Serif
  headings/body → IBM Plex Sans
  labels/code → IBM Plex Mono

Main title:
  font-family: IBM Plex Serif
  font-size: 42px, font-weight: 700, line-height: 1.15, color: #2A3140
  Accent spans: color {accent_color}
  margin-bottom: 8px

Subtitle:
  font-family: IBM Plex Sans
  font-size: 16px, color: rgba(42,49,64,0.64), font-style: italic, margin-bottom: 32px

Terminal window: same dark style as T1, full width
  accent_color for bold highlights

FOOTER: only the universal credit line (no newsletter/tagline row)
```

**IMPORTANT — Footer for Template 3:** Remove any source/tagline bottom row. Only include the universal credit line.

---

## Template 4 — Horizontal Brand Thumbnail HTML

### Canvas sizes

```
16:9 → width: 1200px, height: 675px   (YouTube thumbnail, FB post image)
5:2  → width: 1250px, height: 500px   (LinkedIn banner, Facebook cover)

Always fixed px — never %, never vw/vh inside canvas.
Responsive: use transform: scale(n) on .scale-wrap where n = min(vw-48, vh-72) / canvas_width
```

### Grid system

```
Left column (text):   x=0      → x=696px  (58% of 1200px canvas)
Right column (asset): x=696px  → x=1200px (42% = 504px wide)

Safe padding:
  Top/bottom: 52px
  Left edge:  58px
  Right edge: 44px

Right column safe area (usable space for brand assets):
  X: 716px → 1156px  (440px usable width)
  Y: 52px  → 623px   (571px usable height, 16:9)
  X: 716px → 1206px  (490px usable width, 5:2)
  Y: 40px  → 460px   (420px usable height, 5:2)
```

### Z-index layer order

```
z-index 2  — Background decorative shapes, halftone bands
z-index 5  — Decorative illustrations, icons (can bleed outside safe area)
z-index 6  — Eye / accent elements
z-index 8  — NghienAI logo top-left (MUST stay inside safe area — never bleed)
z-index 9  — Subject/product logo in right column, when relevant
z-index 10 — Left column text content
z-index 20 — Photo / avatar clip
z-index 30 — Footer credit
```

### NghienAI logo and subject asset rules

```
CRITICAL: The NghienAI logo is brand chrome, not the subject asset.
Use the real logo file:
/Users/khaihoan/Library/Mobile Documents/com~apple~CloudDocs/Claude AI/Qorder Brain/tools/NghienAI_logo_orange.svg

Place exactly one NghienAI logo at top-left:
  .nghienai-logo {
    position: absolute;
    left: 58px;
    top: 44px;
    height: 44px;
    width: auto;
    z-index: 8;
  }

Do not create a text-only "NGHIÊN AI" box and do not add brand-name text beside the logo.

If the visual is about another product/brand, its logo belongs in the right column safe area.
That subject logo must be fully contained. Never position it using raw right: Xpx — always use a wrapper with explicit width.

Logo wrapper pattern:
  .subject-logo-wrap {
    position: absolute;
    right: 44px;                    /* safe_padding_right */
    top: 50%;
    transform: translateY(-50%);
    width: min(440px, 85% of right_col_safe_width);  /* = 374px max for 16:9 */
    overflow: hidden;               /* hard clip — logo never escapes */
    z-index: 9;
  }
  .subject-logo-wrap svg, .subject-logo-wrap img {
    width: 100%;
    height: auto;
    display: block;
  }

Logo sizing by aspect ratio:
  Wide logo (AR > 3:1, e.g. "Lovable" wordmark 911:155 ≈ 5.9:1):
    → Use max-height: 72px; width: auto; max-width: 100%
    → Height constraint gives better visual weight than width constraint
  Square/icon logo (AR 1:1 to 2:1):
    → Use width: min(220px, 50% of right_col_safe_width)
  Tall logo (AR < 1:1):
    → Use max-height: 200px; width: auto

Decorative elements (loa, icons, illustrations):
  → Can bleed: right: -60px to -180px, opacity 0.5–0.85
  → Always lower z-index than the subject logo (z-index 5)
  → Reduce size when a subject logo is present (max 60% of right column width)
```

### Left column rules

```
Badge/label:   margin-bottom 18px, pill shape, coral bg, IBM Plex Mono
Title H1:      font-size 68–88px auto-fit (ALWAYS use JS autoFitTitle — Vietnamese diacritics)
               IBM Plex Serif only when this is the one `.title`; otherwise IBM Plex Sans
               font-weight 700, line-height 1.08, max 2 lines, letter-spacing 0
Subtitle:      font-size 18–20px, italic, color rgba(42,49,64,0.68), margin-bottom 24px, max-width 580px
Tags/pills:    font-size 13px, flex wrap, gap 8–10px, max 3 rows
               Use brand accent colors (see palette below)

Tag palette:
  p1 #FF623B  p2 #088B96  p3 #4850ED  p4 #8F00FF
  p5 #FFE032  p6 #2A3140  p7 #FF8A6A  p8 #0FB7C5
```

### Typography & color defaults

```
Title font:    'IBM Plex Serif' only for `.title`
Primary font:  'IBM Plex Sans' — headings, body, subtitle
Mono font:     'IBM Plex Mono' — badge, pills, footer, metadata
Background:   #F7F5ED (neo pearl)
Accent:       #FF623B (neon coral)
Text:         #2A3140 (deep dark blue)
Muted:        rgba(42,49,64,0.68)
```

### T4 updated design elements (2026-04-05)

**Pills — cascade style (replace old uniform pastel tags):**
```
Pills display in staggered rows — offset alternating left/right by ~12px.
Each pill has solid vivid background, bold text, border radius <= 8px unless the pill is intentionally an organic-chip shape.
Cascade palette: #FF623B | #088B96 | #4850ED | #8F00FF | #FFE032 | #2A3140
Max 6 pills, 2–3 per row. Gap 10px.
```

**Cursor + selection handles decoration:**
```
Add selection-handles UI overlay (4 corner handles + 4 edge handles as 8px filled squares)
with a rectangle outline — same visual as NghienAI brand identity.
Position near the title or inline icon area. Color: #2A3140. z-index: 6.
Also add a macOS-style cursor SVG (pointer arrow) nearby at z-index 6.
```

**Font update:**
```
Title font-size: scale up 10–15% from previous spec (88px base for 16:9).
Use font-weight 700 or 800 with letter-spacing: 0.
If mixing type styles, only the main `.title` line may use IBM Plex Serif; all support text remains IBM Plex Sans/Mono.
```

### T4 inputs

- `canvas_ratio` — `16:9` (default) or `5:2`
- `badge_text` — label pill top-left (e.g. `Lovable for Marketers`)
- `badge_icon_svg` — optional small SVG icon inside badge
- `title_lines` — array of 1–2 strings; wrap accent words in `**text**`
- `subtitle` — italic line below title
- `cascade_pills` — array of `{text, color?}` for cascade pill rows (max 6)
- `nghienai_logo_path` — default `/Users/khaihoan/Library/Mobile Documents/com~apple~CloudDocs/Claude AI/Qorder Brain/tools/NghienAI_logo_orange.svg`
- `subject_logo_svg` — optional inline SVG string of the product/subject logo
- `subject_logo_ar` — aspect ratio hint: `wide` / `square` / `tall` (default `wide`)
- `decorative_asset` — optional: `megaphone` | `rocket` | `none`
- `show_cursor_deco` — default `true` — renders cursor + selection handles
- `photo_src` — optional base64 PNG, bottom-left avatar clip
- `accent_color` — default `#FF623B`
- `bg_color` — default `#F7F5ED`

### Capture for T4

Same pattern as T1–T3 but target output is `1920×1080` (16:9) or `2500×1000` (5:2).

```javascript
// T4 capture: scale 1.6 for 16:9 → 1920×1080
const canvas = await html2canvas(frame, { scale: 1.6, ... });
// download filename:
download: 'thumbnail-16x9.png'  // or 'thumbnail-5x2.png'
```

---

## Template 5 — Background Photo Card HTML

### Overview

Fixed 1:1 square canvas (1080×1080px) with NghienAI brand background. Content layered on top.
Best for: Facebook post thumbnails, carousels, social story slides.

```
Canvas: 1080×1080px fixed px
Responsive: transform: scale(n) on .scale-wrap where n = min(vw-32, vh-32) / 1080
Background: #F7F5ED with CSS halftone/grid, or full-cover <img> with object-fit: cover (embedded base64 JPG/PNG)
```

### Workspace assets

Use the real NghienAI assets from the workspace:

- Logo: `/Users/khaihoan/Library/Mobile Documents/com~apple~CloudDocs/Claude AI/Qorder Brain/tools/NghienAI_logo_orange.svg`
- Optional orange logomark: `/Users/khaihoan/Library/Mobile Documents/com~apple~CloudDocs/Claude AI/Qorder Brain/tools/NghienAI_logomark_orange.svg`
- Optional white logomark for dark accent blocks: `/Users/khaihoan/Library/Mobile Documents/com~apple~CloudDocs/Claude AI/Qorder Brain/tools/NghienAI_logomark_white.svg`
- Optional clean background image: `/Users/khaihoan/Library/Mobile Documents/com~apple~CloudDocs/Claude AI/Qorder Brain/tools/background empty 2.jpg`
- Optional Hoan/avatar image: `/Users/khaihoan/Library/Mobile Documents/com~apple~CloudDocs/Claude AI/Qorder Brain/tools/Avatar.png`

When using bitmap backgrounds or photos, embed them as data URLs before capture. Do NOT use `file://` URLs because html2canvas cannot reliably capture them.

### Layout layers (z-index order)

```
z-index 1   — Background <img> (full cover, 1080×1080)
z-index 5   — Cursor decoration + selection handles
z-index 8   — NghienAI real logo (top-left)
z-index 8   — context_tag label (top-right or below logo)
z-index 10  — Title block + inline icon
z-index 10  — Cascade pills
z-index 15  — Download circle arrow (bottom-right)
z-index 30  — Capture button (outside canvas)
```

### Fixed chrome elements (always present)

**NghienAI real logo (top-left):**
```css
.nghienai-logo {
  position: absolute;
  top: 40px;
  left: 44px;
  height: 48px;
  width: auto;
  z-index: 8;
}
```

Do not draw a text-only brand box. If selection handles are needed, put them around an icon, shape, or content module, not around the logo itself.

**Human-made selection handles:**
```css
.handle {
  position: absolute;
  width: 9px; height: 9px;
  background: #2A3140;
}
```

**Cursor + selection handles on inline icon:**
```html
<!-- Selection box around inline icon (adjustable position) -->
<div class="selection-box" style="position:absolute; width:120px; height:120px;
  border: 2px solid #2A3140; left: Xpx; top: Ypx; z-index:5;">
  <!-- 8 handle squares at corners + edge midpoints -->
</div>
<!-- Cursor arrow SVG -->
<svg class="cursor-deco" style="position:absolute; left: X+80px; top: Y+90px; z-index:5;" ...>
  <!-- macOS pointer cursor path -->
</svg>
```

**Download circle arrow (bottom-right):**
```html
<div style="position:absolute; bottom:32px; right:36px; width:48px; height:48px;
  border:2px solid #2A3140; border-radius:50%; display:flex; align-items:center;
  justify-content:center; z-index:15;">
  <!-- ↓ arrow SVG -->
</div>
```

### Content layout

```
Context tag (top-left):
  position: absolute, top: 104px, left: 44px OR top: 44px, right: 44px
  font: IBM Plex Mono 600, 13px, letter-spacing 0, text-transform uppercase
  color: #2A3140

Title block (center, slight left offset):
  position: absolute, top: 140px–200px, left: 44px
  max-width: 640px

  Title font: IBM Plex Serif for the one main `.title`; IBM Plex Sans otherwise
  font-size: auto-fit starting at 100px, min 48px
  line-height: 1.05
  color: #2A3140
  letter-spacing: 0

  Inline icon (between title lines):
    <img> or inline SVG, height: 80–100px, vertical-align: middle
    + selection-box overlay + cursor deco nearby

Cascade pills:
  position: absolute, bottom: 120px–200px, right: 40px
  OR: bottom-half of canvas, staggered
  Each pill: border-radius 8px, padding 10px 22px, font-weight 700, font-size 16px
  Stagger: odd pills margin-right 24px, even pills margin-right 0
  Cascade palette: #FF623B | #088B96 | #4850ED | #8F00FF | #FFE032 (top to bottom)
```

### T5 inputs

- `background_mode` — `"brand-css"` (default), `"empty-image"`, or `"custom-image"`
- `context_tag` — small caps label top-left (e.g. `"FOR MARKETER WITH CASE STUDY"`)
- `title_line1` — first title line (e.g. `"How to Master"`)
- `title_line2` — second title line (e.g. `"Lovable"`)
- `title_font_mix` — `"brand"` default (main `.title` in IBM Plex Serif, support text in Sans)
- `content_mode` — `"pills"` or `"icon_grid"`
- **Pills mode inputs:**
  - `cascade_pills` — array of `{text, color?}`, max 6. Colors auto-assigned from cascade palette if omitted.
- **Icon grid mode inputs:**
  - `icon_grid` — array of `{icon_src, label?}`, 6–9 items (renders as 3×3 grid of rounded-square icons)
  - `icon_grid_caption` — small text below grid (e.g. `"/jackvi810/NghienAI/chia_se"`)
- `inline_icon_src` — optional base64 PNG or SVG data URI — logo/icon placed inline between title lines
- `inline_icon_size` — height in px, default `88`
- `show_cursor_deco` — default `true`
- `accent_text_color` — highlight color for accent words in title, default `#FF623B`

### T5 Capture

Target output: 1080×1080px (1:1 social media)

```javascript
// T5 capture: scale 1.0 since canvas IS 1080×1080
const canvas = await html2canvas(frame, { scale: 1.0, width: 1080, height: 1080, ... });
// filename: 'thumbnail-1x1.png'
```

**CRITICAL for T5 capture:** Any background `<img>` must use base64 src (not file:// or http://). html2canvas cannot capture cross-origin images reliably. Always embed bitmap assets at build time.

### T5 quality checklist
- [ ] Background renders as CSS brand background or base64 embedded image?
- [ ] Exactly one real NghienAI logo visible top-left?
- [ ] No text-only "NGHIÊN AI" brand box?
- [ ] Context tag visible and not competing with logo?
- [ ] Title auto-fits within 640px max-width?
- [ ] Inline icon selection box + cursor showing (if content has icon)?
- [ ] Pills cascade stagger (not uniform row)?
- [ ] Download arrow circle bottom-right?
- [ ] Capture outputs 1080×1080px?

---

## Universal footer credit (ALL templates)

Every output must end with:
```html
<div style="font-size:12px;color:rgba(0,0,0,0.28);text-align:center;margin-top:32px;letter-spacing:0.4px;">
  Made by Khai Hoan with Claude · #NghienAI
</div>
```

---

## Capture Button (ALL templates — ALWAYS include)

Every template must include a floating "📷 Capture" button that screenshots the main content as a square PNG and copies it to clipboard.

### Tech stack
- **html2canvas 1.4.1** from cdnjs — captures DOM as canvas, works in static files
- **ClipboardItem API** — copies PNG to clipboard; auto-falls back to download if on `file://`
- **Hidden square frame** — off-screen clone zone ensures clean square output without capturing the button itself

### Structure

Wrap ALL main content (everything except the button) in `<div id="capture-content">`.
Place `<button id="capture-btn">` OUTSIDE and AFTER `#capture-content`, fixed to bottom of screen.

```html
<body>
  <div id="capture-content">
    <!-- page title, layout, footer-credit — everything visual -->
  </div>

  <!-- Hidden square frame: off-screen, used as capture target -->
  <div id="capture-frame"></div>

  <!-- Floating button: outside capture-content so it never appears in screenshot -->
  <button id="capture-btn" onclick="captureCard()">📷 Capture</button>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
  <script>/* capture logic */</script>
</body>
```

### CSS for capture-frame and capture-btn

```css
#capture-frame {
  position: absolute;
  top: -9999px;
  left: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  /* width/height set dynamically by JS */
  box-sizing: border-box;
}
#capture-btn {
  position: fixed;
  bottom: 28px;
  left: 50%;
  transform: translateX(-50%);
  background: #2A3140;
  color: white;
  border: none;
  padding: 13px 28px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  box-shadow: 0 4px 20px rgba(0,0,0,0.25);
  z-index: 9999;
  letter-spacing: 0;
  transition: background 0.15s, transform 0.1s;
  white-space: nowrap;
}
#capture-btn:hover { background: #FF623B; transform: translateX(-50%) scale(1.03); }
#capture-btn:disabled { background: #555; cursor: default; transform: translateX(-50%); }
```

### JavaScript capture logic

```javascript
async function captureCard() {
  const btn = document.getElementById('capture-btn');
  const source = document.getElementById('capture-content');
  const frame = document.getElementById('capture-frame');

  btn.textContent = '⏳ Processing...';
  btn.disabled = true;

  // Wait for fonts and layout
  await document.fonts.ready;
  await new Promise(r => setTimeout(r, 200));

  // Calculate square size: max dimension + generous padding
  const sw = source.scrollWidth;
  const sh = source.scrollHeight;
  const PAD = 80;
  const squareSize = Math.max(sw, sh) + PAD * 2;

  // Style the off-screen frame
  const bgColor = getComputedStyle(document.body).backgroundColor || '#F7F5ED';
  frame.style.width  = squareSize + 'px';
  frame.style.height = squareSize + 'px';
  frame.style.background = bgColor;
  frame.style.padding = PAD + 'px';

  // Clone content into frame
  frame.innerHTML = '';
  const clone = source.cloneNode(true);
  frame.appendChild(clone);

  // If T2: re-draw SVG connector lines on the clone
  redrawConnectors(frame);

  // Give browser a tick to render the clone
  await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));

  const canvas = await html2canvas(frame, {
    scale: 2,
    useCORS: true,
    allowTaint: true,
    backgroundColor: bgColor,
    logging: false,
    width: squareSize,
    height: squareSize
  });

  // Clean up frame
  frame.innerHTML = '';

  // Copy to clipboard or fallback download
  canvas.toBlob(async (blob) => {
    try {
      await navigator.clipboard.write([new ClipboardItem({ 'image/png': blob })]);
      btn.textContent = '✓ Copied!';
    } catch {
      const url = URL.createObjectURL(blob);
      const a = Object.assign(document.createElement('a'), {
        href: url,
        download: 'nghienai-card.png'
      });
      a.click();
      URL.revokeObjectURL(url);
      btn.textContent = '✓ Downloaded!';
    }
    setTimeout(() => { btn.textContent = '📷 Capture'; btn.disabled = false; }, 2000);
  }, 'image/png');
}

// For T2 templates: re-draw SVG bezier lines after cloning
// For T1/T3: this is a no-op (no connectors to redraw)
function redrawConnectors(container) {
  const svg = container.querySelector('#connectors');
  const layout = container.querySelector('.layout');
  if (!svg || !layout) return;

  svg.innerHTML = '';
  const layoutRect = layout.getBoundingClientRect();

  container.querySelectorAll('.pill[data-target]').forEach(pill => {
    const target = pill.dataset.target;
    const para = container.querySelector(`p[data-para="${target}"]`);
    if (!para) return;

    const pRect = para.getBoundingClientRect();
    const pillRect = pill.getBoundingClientRect();

    const x1 = pRect.right  - layoutRect.left;
    const y1 = pRect.top    + pRect.height / 2 - layoutRect.top;
    const x2 = pillRect.left - layoutRect.left;
    const y2 = pillRect.top  + pillRect.height / 2 - layoutRect.top;
    const cx = (x1 + x2) / 2;

    const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    path.setAttribute('d', `M ${x1} ${y1} C ${cx} ${y1}, ${cx} ${y2}, ${x2} ${y2}`);
    path.setAttribute('fill', 'none');
    path.setAttribute('stroke', pill.dataset.linecolor || '#aaa');
    path.setAttribute('stroke-width', '1.5');
    path.setAttribute('stroke-dasharray', '5,3');
    path.setAttribute('opacity', '0.32');
    svg.appendChild(path);
  });
}
```

### Notes
- `#capture-frame` is at `top: -9999px` — in DOM but off-screen, so html2canvas can render it
- Google Fonts: `await document.fonts.ready` ensures text renders correctly before capture
- Background color is read dynamically from `document.body` — works for all template backgrounds
- `redrawConnectors()` is a no-op for T1/T3 (no SVG), so include it in all templates for consistency

---

## Output instructions

1. Single `.html` file, all CSS in `<style>` block. Google Fonts allowed via `<link>` in `<head>`.
2. Filename: `YYYY-MM-DD_visual-[t1|t2|t3|t4|t5]-[short-slug].html`
3. Save finished visuals to `/Users/khaihoan/Library/Mobile Documents/com~apple~CloudDocs/Claude AI/Qorder Brain/output/` unless the user specifies another folder.
4. Provide the absolute file path.

## Quality checklist
- Traffic lights correct colors (red/yellow/green)?
- Connector lines drawn and visible (T2)?
- Hover highlight working (T2)?
- Font loaded correctly (T3)?
- No source/tagline footer row on T3?
- Universal credit line present?
- Capture button present and floating bottom-center?
- `#capture-content` wraps ALL visual content (button is outside)?
- `redrawConnectors()` function present in all templates?
- NghienAI logo uses the real SVG file and appears exactly once?
- No brand-name text added beside the logo?
- IBM Plex fonts loaded and used according to hierarchy?
- Rough-edge filters applied only to shapes/boxes, never to text or logo?
- **(T4)** Subject logo, if any, wrapped in `.subject-logo-wrap` with explicit width + `overflow: hidden`?
- **(T4)** Subject logo uses height constraint if AR > 3:1 (`max-height: 72px; width: auto`)?
- **(T4)** Decorative elements have lower z-index (5) than subject logo (9)?
- **(T4)** Canvas fixed px, `transform: scale()` on `.scale-wrap` for responsive?
- **(T4)** Capture outputs correct resolution (1920×1080 for 16:9, 2500×1000 for 5:2)?
- **(T4)** Pills use cascade stagger style (not uniform row)?
- **(T4)** Cursor + selection handles decoration present?
- **(T5)** Any background `<img>` uses embedded base64 (NOT file:// or http://)?
- **(T5)** No text-only "NGHIÊN AI" brand box?
- **(T5)** Context tag visible and not competing with top-left logo?
- **(T5)** Title auto-fits within 640px column?
- **(T5)** Canvas exactly 1080×1080px, responsive via `transform: scale()`?
- **(T5)** Capture outputs 1080×1080px?

---

## Custom Thumbnail Gotchas (learned 2026-04-03)

### Bug 1 — Vietnamese title overflow (font-size too large)

**Root cause:** Vietnamese diacritics make average char width ~0.64em at heavy weight.
"Hướng Dẫn Toàn Tập:" (19 chars) at 74px ≈ 900px — overflows any reasonable column.
Static `font-size` cannot be pre-calculated safely for multi-diacritic Vietnamese text.

**Fix — JS auto-fit pattern (ALWAYS use for Vietnamese titles):**
```html
<!-- Wrap each title line in .title-line with white-space:nowrap -->
<div class="title" id="main-title">
  <span class="title-line">Line one text</span>
  <span class="title-line"><span class="accent">Line</span> two text</span>
</div>
```
```javascript
// Run AFTER document.fonts.ready — critical for accurate measurement
function autoFitTitle() {
  const titleEl = document.getElementById('main-title');
  const lines   = titleEl.querySelectorAll('.title-line');
  const maxW    = titleEl.parentElement.clientWidth - 16;
  let size = 80;
  titleEl.style.fontSize = size + 'px';
  while (Array.from(lines).some(l => l.scrollWidth > maxW) && size > 28) {
    size -= 1;
    titleEl.style.fontSize = size + 'px';
  }
}
document.fonts.ready.then(autoFitTitle);
```
**Re-run autoFitTitle on capture clone** — clone has different parentElement.clientWidth.

---

### Bug 2 — Photo crop shows wrong area (body instead of head)

**Root cause:** `img { width:100%; height:auto }` renders image SMALLER than container
→ no overflow → no crop → entire person visible at tiny scale.

**Fix — oversized img + top-anchor pattern:**
```css
/* Container: clips overflow, anchored bottom-left */
.photo-clip {
  position: absolute;
  bottom: 0; left: 0;
  width: 200px;
  height: 225px;   /* ~1/3 canvas height */
  overflow: hidden;
  z-index: 20;
}
/* IMG: LARGER than container width, anchored top, centered */
.photo-clip img {
  position: absolute;
  top: 0;                    /* anchor HEAD to top of container */
  left: 50%;
  transform: translateX(-50%); /* center horizontally */
  width: 340px;              /* MUST be > container width to force crop */
  height: auto;              /* 340px for square PNG → clips ~110px at bottom */
  display: block;
}
```
**Rule of thumb:** `img width = container_height / 0.65` to show top ~65% of a square PNG.
Adjust multiplier based on where the face appears in the source PNG.

---

### Rule — Title line breaks

Max 2 lines. Always break at natural punctuation (`:`, `—`, `.`).
Use explicit `<br>` inside `.title-line` structure, never rely on browser wrap.
Line break point cho tiếng Việt: sau dấu `:` hoặc cuối cụm danh từ.

---

### Rule — Responsive canvas + 1920×1080 capture

- Canvas fixed at `1200×675px` internally
- `transform: scale(n)` on `.scale-wrap` where `n = min(vw-48, vh-72) / 1200`
- Capture: clone canvas to off-screen frame, `html2canvas({ scale: 1.6 })` → 1920×1080
- Re-run auto-fit JS on clone before capture

---

## ⚡ Visualize Value Mode (vibe-value skill)

Khi Hoan muốn visual **đơn sắc, abstract, concept-driven** (không phải thumbnail hay card NghienAI) → đây là mode khác hoàn toàn.

**Trigger sang vibe-value skill khi:**
- "Visualize this idea / concept" — một ý tưởng trừu tượng
- "VV style", "Jack Butcher style", "minimal concept"
- "Làm hình đơn giản để minh họa nguyên lý / thông điệp"
- Slide cần 1 panel concept illustration thuần hình học

**Điểm khác biệt:**
| vibe-design (templates T1–T5) | vibe-value |
|-------------------------------|-----------|
| Có text nhiều, layout phức tạp | Tối đa 1 dòng text, ≤ 8 từ |
| Brand-aware (NghienAI) | Không brand, thuần concept |
| Fill màu, gradient, typography đa dạng | Chỉ black + white stroke |
| Social post có context | Principle / idea visualization |

→ **Đọc `tools/vibe-visual/SKILL.md`** trước khi build loại visual này. Tra concept trong `tools/vibe-visual/LIBRARY.md` (170 visuals).
