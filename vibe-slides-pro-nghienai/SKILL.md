---
name: vibe-slides-pro-nghienai
description: Build branded HTML slide decks for NghienAI with IBM Plex typography, the NghienAI color system, responsive 16:9 layout, sidebar navigation, zoom controls, page numbering, human-made orange shapes (box, circle, triangle, star), halftone patterns, image-to-halftone conversion, smart font system (Serif only for main title), and component-first source folders that build into one final HTML file.
---

# vibe-slides-pro-nghienai

Create single-file HTML slide decks that match NghienAI's visual language. This variant features IBM Plex typography, NghienAI brand colors, human-made shapes with rough edges, advanced halftone patterns, image halftone conversion, and a smart font system where Serif is reserved only for the main title.

## When to use

- User asks for HTML slides, presentation decks, workshop slides, or pitch slides
- The deck should feel like NghienAI brand output
- The deck needs click navigation, keyboard navigation, and slide numbering
- The deck benefits from a visible sidebar and zoom controls during presenting
- The deck should include human-made shapes (boxes, circles, triangles, stars) with rough edges
- The deck needs halftone patterns or image-to-halftone conversion
- The deck should optionally show NghienAI name, full logo, or logomark

Do not use this skill when the user explicitly wants `.pptx` or a video-style motion deck.

## Output contract

Produce 1 self-contained HTML file as the final deliverable, but use a component-first source folder for substantial decks or later edits. Read `references/component-workflow.md` when a deck will have more than 3 slides, custom CSS/JS, or likely follow-up revisions.

Final deck must include:

- Responsive centered 16:9 slide stage
- **Smart font system**: IBM Plex Serif ONLY for main `.title`, IBM Plex Sans for all headings (h1, h2, h3) and body
- IBM Plex Mono for labels, metadata, counters, code, and small UI
- Text sizes slightly larger than the original `vibe-slides-pro` baseline
- Click-anywhere navigation, keyboard navigation, and visible prev/next buttons
- Sidebar chapter navigation on the left
- Zoom in, zoom out, and reset zoom controls
- Page numbering in the UI
- Optional NghienAI brand name and SVG logo/logomark
- Clean alignment with centered or justified-center layouts
- **Human-made shapes**: box, circle, triangle, star with rough-edge SVG filters
- **Halftone patterns**: stepped, brick, gradient, human-made variants
- **Image-to-halftone conversion** utility via JavaScript

Save in:

- `output/` for finished decks
- `inbox/` or another user-specified folder for drafts

Suggested naming:

- `YYYY-MM-DD_slide-[slug].html`

## Component-first editing contract

Default to this structure before building the final HTML:

```text
work/[deck-slug]/
  EDIT_MAP.md
  src/
    deck.html
    sections/
      01-intro.html
      02-problem.html
    styles/
      00-tokens.css
      10-layout.css
      01-intro.css
    scripts/
      deck-config.js
      deck-runtime.js
```

Use `base.html` as the visual/runtime source of truth, then split working changes into `src/sections`, `src/styles`, and `src/scripts`. Build back into one HTML with:

```bash
python3 tools/vibe-slides-pro-nghienai/scripts/build_single_html.py work/[deck-slug]/src/deck.html output/YYYY-MM-DD_slide-[slug].html
```

Convert an existing single-file deck into this structure with:

```bash
python3 tools/vibe-slides-pro-nghienai/scripts/componentize_existing_deck.py output/existing-deck.html --work-dir work/[deck-slug] --output output/YYYY-MM-DD_slide-[slug]-componentized.html
```

When the user asks for edits, first identify the component file(s) to touch and say where they live. Edit the source files, rebuild the final HTML, and treat the generated `output/*.html` file as a deliverable, not the primary editing surface.

If the task is a tiny one-off deck, a direct single-file edit is allowed, but keep the file map comments and region contracts from `base.html`.

## Region contract rules

- Every slide section must have `data-slide-id`, `data-nav`, and `data-accent`.
- Every slide source file starts with a comment contract: purpose, owns, depends on, do not change, edit file.
- Deck-specific CSS must be namespaced to `.slide--[slug]` or `.slide[data-slide-id="[slug]"]`.
- Shared framework CSS may use existing base classes such as `.stage`, `.slide`, `.chapter-nav`, `.controls-bar`.
- Do not add broad selectors such as `.card`, `button`, `section h2`, or `.active` for deck-specific styling.
- Treat `id`, `data-*`, `.slide`, `.slide-content`, and navigation/control element IDs as internal APIs.
- Keep a `FILE MAP` comment near the top of each source `deck.html` and a human-readable `EDIT_MAP.md` next to `src/`.

## Brand system

### Typography

Use IBM Plex family from Google Fonts:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Serif:wght@400;500;600;700&display=swap" rel="stylesheet">
```

**Smart Font Rules:**

| Element | Font | CSS Class |
|---------|------|-----------|
| Main title only | IBM Plex Serif | `.title` |
| All headings (h1, h2, h3) | IBM Plex Sans | `h1`, `h2`, `h3`, `.h1`, `.h2`, `.h3` |
| Body text | IBM Plex Sans | `.body` |
| Labels, counters, tags, code | IBM Plex Mono | `.kicker`, `.tag`, `.mono` |

Minimum size guidance:

- Labels: 13-16px
- Body text: 16-21px
- Mono helper text: 12-15px
- Headings: increase by roughly 2-3px from base

### Colors

Use these as the NghienAI source-of-truth tokens:

```css
--neo-pearl: #F7F5ED;
--deep-dark-blue: #2A3140;
--neon-coral: #FF623B;
--tangy-yellow: #FFE032;
--electric-violet: #8F00FF;
--turquoise-blue: #088B96;
--blue-glow: #4850ED;
```

Working defaults:

- Background: `--neo-pearl`
- Primary text: `--deep-dark-blue`
- Primary accent: `--neon-coral`
- Secondary accents: yellow, turquoise, blue, violet when useful

## Brand assets

Use the bundled SVG assets in `assets/`:

- `assets/NghienAI_logo_orange.svg`
- `assets/NghienAI_logomark_orange.svg`
- `assets/NghienAI_logomark_white.svg`

Preferred logic:

- Light background: orange full logo or orange logomark
- Dark accent block: white logomark
- If the user asks for minimal branding, show logomark only
- If the user asks for explicit identity, show full logo plus optional presenter name

## Layout rules

- Default to a responsive centered 16:9 stage
- Use `aspect-ratio: 16 / 9`
- Keep the slide itself centered in the viewport both horizontally and vertically
- Prefer `justify-content: center` and `align-items: center` for hero / section slides
- Use grid layouts for split slides, but preserve strong visual center
- Keep generous edge padding so content survives on smaller screens

## Human-made Shapes

Apply rough-edge SVG filter effects to shapes only, **never to text**.

### Available Shapes

```html
<!-- Box with rough edges -->
<div class="human-shape human-box">Content</div>

<!-- Box with outline only -->
<div class="human-shape human-box is-outline">Content</div>

<!-- Circle with rough edges -->
<div class="human-shape human-circle"></div>

<!-- Triangle with rough edges -->
<div class="human-triangle"></div>

<!-- Star with rough edges -->
<div class="human-star"></div>

<!-- Organic chip/tag -->
<span class="organic-chip">Label</span>
```

### Shape Classes

| Class | Description |
|-------|-------------|
| `.human-shape` | Base class for rough filter effect |
| `.human-box` | Rectangle box with coral fill |
| `.human-box.is-outline` | Box with transparent fill, coral border |
| `.human-circle` | Circle shape with coral fill |
| `.human-circle.is-outline` | Circle with transparent fill |
| `.human-triangle` | Triangle pointing up |
| `.human-star` | 5-point star shape |
| `.organic-chip` | Tag/chip with rough edges |

## Halftone Patterns

### Pattern Classes

```html
<!-- Stepped halftone with clipped edge -->
<div class="halftone-panel halftone-stepped"></div>

<!-- Brick pattern halftone -->
<div class="halftone-band halftone-brick"></div>

<!-- Gradient density halftone -->
<div class="halftone-bg halftone-gradient"></div>

<!-- Irregular human-made dots -->
<div class="halftone-bg halftone-human"></div>

<!-- Standard halftone panel -->
<div class="halftone-panel"></div>
```

### Pattern Variants

| Class | Effect |
|-------|--------|
| `.halftone-panel` | Base halftone with stepped clip-path edge |
| `.halftone-band` | Horizontal band with halftone |
| `.halftone-bg` | Full background halftone |
| `.halftone-stepped` | Stair-step clip-path pattern |
| `.halftone-brick` | Brick-layout dot pattern |
| `.halftone-gradient` | Dots denser at edges |
| `.halftone-human` | Irregular dot sizes for hand-made feel |

## Image-to-Halftone Conversion

Convert PNG images to halftone style programmatically:

### JavaScript API

```javascript
// Process an image element and get data URL
const dataUrl = window.halftoneImage.process(imageElement, {
  dotSize: 4,      // Size of halftone dots
  spacing: 6       // Spacing between dots
});

// Apply halftone to a container with image URL
window.halftoneImage.applyToElement('.halftone-image', 'path/to/image.png', {
  dotSize: 4,
  spacing: 6
});
```

### HTML Container

```html
<div class="halftone-image human-shape">
  <img src="original.png" alt="Description">
</div>
```

The image will be automatically converted to grayscale with halftone dot overlay.

## Required interactions

- Click on empty slide area to go next
- Arrow keys and PageUp / PageDown navigate
- Prev / next buttons remain visible
- Sidebar remains clickable for direct slide jumps
- Zoom controls remain visible unless the deck explicitly disables them
- Slide counter always visible
- Support touch-friendly navigation zones when possible
- Keyboard zoom: `+` / `-` / `0` for zoom in/out/reset

## Required config surface

Every produced deck should keep a small config object near the top of the script:

```javascript
const deckConfig = {
  showBrandName: true,
  showLogo: true,
  logoVariant: 'full-orange',
  presenterName: 'NghienAI',
  enableClickAdvance: true,
  enableKeyboardNav: true,
  showSlideNumbers: true,
  enableSidebar: true,
  enableZoomControls: true,
  defaultZoom: 1,
  zoomStep: 0.1,
  minZoom: 0.8,
  maxZoom: 1.4
};
```

Accepted logo variants:

- `full-orange`
- `logomark-orange`
- `logomark-white`
- `none`

## Base template

Start from `base.html` in this skill folder. It already includes:

- Brand tokens
- IBM Plex imports
- Responsive 16:9 stage
- Numbered slides
- Sidebar chapter navigation
- Zoom controls with `+`, `-`, and reset
- Click / button / keyboard navigation
- Optional brand row with presenter name and SVG logo
- Centered hero and split layouts
- All human-made shape classes
- All halftone pattern classes
- Image-to-halftone JavaScript utility
- Smart font system (Serif only for `.title`)
- File map comments and region contracts for safe single-file edits

## Workflow

1. Clarify deck topic, audience, and rough slide count if missing.
2. Draft a tight outline before filling visuals.
3. Plan the source split: list slide section files, slide-specific CSS files, and shared JS/config files before editing.
4. Create `work/[deck-slug]/src/` from `base.html`, keeping a `FILE MAP` in `deck.html`.
5. Write an `EDIT_MAP.md` that tells the user which file to edit for slide text, visual styling, runtime config, and generated output.
6. Put each slide in `src/sections/[nn-slug].html` with a contract comment and a namespaced class such as `.slide--problem`.
7. Put deck-specific CSS in `src/styles/[nn-slug].css`, scoped to `.slide--[slug]` or `[data-slide-id="[slug]"]`.
8. Set `deckConfig` branding options based on the user's brief.
9. Build the final HTML with `scripts/build_single_html.py`; deliver the generated `output/YYYY-MM-DD_slide-[slug].html`.
10. Use human-made shapes for decorative elements and accent blocks.
11. Apply halftone patterns for background texture or image treatment.
12. Use `window.halftoneImage.applyToElement()` for photo halftone conversion.
13. **Remember**: Only use `.title` class for the main slide title (uses Serif). Use `h1`, `h2`, `h3` for all other headings (uses Sans-serif).
14. Check that long text still fits at laptop width and smaller screens.
15. For follow-up edits, touch the smallest source component, rebuild, and summarize exactly which source files changed.

## Hard rules

- Stay in light-theme NghienAI brand language unless the user explicitly wants a dark variant
- **Serif font ONLY for `.title` class** - all other headings use Sans-serif
- Keep typography hierarchy obvious and spacious
- Avoid tiny text
- Avoid off-center layouts unless it is a deliberate editorial move
- Keep the sidebar labels short and scannable
- Keep zoom controls functional after edits
- **Use rough-edge / hand-made treatment only for shapes and boxes, never for text itself**
- Keep halftone subtle enough that contrast remains accessible
- Keep all navigation working after edits
- Preserve single-file output for the final generated deck unless the user asks otherwise
- Prefer component source edits over direct output edits when the deck already has a source folder
- Never rename `data-slide-id`, navigation/control IDs, or `data-*` hooks without checking all dependent CSS/JS
