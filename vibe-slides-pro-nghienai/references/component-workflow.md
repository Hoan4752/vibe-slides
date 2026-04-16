# Component Workflow

Use this workflow when a NghienAI HTML slide deck is more than a quick one-off, has custom CSS/JS, or will be revised later.

## Goal

Work in small source files, then build one final HTML file. The source folder is the editing surface; the generated `output/*.html` file is the deliverable.

## Required source tree

```text
work/[deck-slug]/
  EDIT_MAP.md
  src/
    deck.html
    sections/
      01-intro.html
      02-context.html
      03-takeaway.html
    styles/
      00-tokens.css
      10-framework.css
      01-intro.css
      02-context.css
      03-takeaway.css
    scripts/
      deck-config.js
      deck-runtime.js
```

`src/deck.html` should contain the shell, file map, and include directives:

```html
<!--
FILE MAP
- styles/00-tokens.css: brand tokens and font variables
- styles/10-framework.css: stage, navigation, controls, shared components
- sections/01-intro.html: opening slide
- scripts/deck-config.js: deckConfig only
- scripts/deck-runtime.js: navigation, zoom, halftone utilities
-->

<link rel="stylesheet" href="./styles/00-tokens.css" data-inline>
<link rel="stylesheet" href="./styles/10-framework.css" data-inline>
<link rel="stylesheet" href="./styles/01-intro.css" data-inline>

<div class="slides" id="slides">
  <!-- @include sections/01-intro.html -->
  <!-- @include sections/02-context.html -->
</div>

<script src="./scripts/deck-config.js" data-inline></script>
<script src="./scripts/deck-runtime.js" data-inline></script>
```

Build with:

```bash
python3 tools/vibe-slides-pro-nghienai/scripts/build_single_html.py work/[deck-slug]/src/deck.html output/YYYY-MM-DD_slide-[slug].html
```

## Convert an Existing Deck

When the user provides an existing single-file HTML deck, convert it first:

```bash
python3 tools/vibe-slides-pro-nghienai/scripts/componentize_existing_deck.py output/existing-deck.html --work-dir work/[deck-slug] --output output/YYYY-MM-DD_slide-[slug]-componentized.html
```

Then build the generated source:

```bash
python3 tools/vibe-slides-pro-nghienai/scripts/build_single_html.py work/[deck-slug]/src/deck.html output/YYYY-MM-DD_slide-[slug]-componentized.html
```

The converter preserves the original visual/runtime code, creates one section file per slide, copies local images into `src/assets/`, marks those images for inlining, adds `data-slide-id` / `data-nav` / `data-accent`, and writes `EDIT_MAP.md`.

## Section contract template

Put this at the top of every file in `src/sections/`:

```html
<!--
SECTION: intro
Purpose: Open the deck and establish the promise.
Owns: HTML inside section[data-slide-id="intro"].
Depends on: .slide, .slide-content, .slide-inner, .title, .kicker, deck runtime.
Do not change: data-slide-id, data-nav, data-accent, .slide, .slide-content.
CSS namespace: .slide--intro or .slide[data-slide-id="intro"].
Edit file: src/sections/01-intro.html
-->
<section class="slide slide--intro align-center active" data-slide-id="intro" data-nav="Intro" data-accent="coral">
  ...
</section>
```

## CSS namespace rules

Deck-specific CSS must be scoped to the slide or component namespace:

```css
.slide--intro .promise-grid { ... }
.slide[data-slide-id="context"] .evidence-row { ... }
```

Avoid broad selectors in deck-specific files:

```css
/* Avoid */
.card { ... }
button { ... }
section h2 { ... }
.active { ... }
```

Shared framework files may define `.stage`, `.slide`, `.chapter-nav`, `.controls-bar`, `.title`, `.kicker`, `.body`, `.tag`, shape utilities, and halftone utilities.

## EDIT_MAP.md template

Create this file beside `src/` so the user knows where to work:

```md
# Edit Map

## Output
- Final deck: output/YYYY-MM-DD_slide-[slug].html
- Do not hand-edit final output unless this is an emergency hotfix. Edit `src/` and rebuild.

## Slide Text
- Slide 1 Intro: src/sections/01-intro.html
- Slide 2 Context: src/sections/02-context.html

## Visual Styling
- Brand/framework styles: src/styles/00-tokens.css, src/styles/10-framework.css
- Slide 1 custom CSS: src/styles/01-intro.css
- Slide 2 custom CSS: src/styles/02-context.css

## Behavior
- Branding and runtime flags: src/scripts/deck-config.js
- Navigation, zoom, sidebar, halftone runtime: src/scripts/deck-runtime.js

## Rebuild
`python3 tools/vibe-slides-pro-nghienai/scripts/build_single_html.py work/[deck-slug]/src/deck.html output/YYYY-MM-DD_slide-[slug].html`
```

## Edit protocol

Before editing, identify the smallest source file that owns the requested change.

For content changes, edit only the matching `src/sections/[nn-slug].html`.

For visual changes on one slide, edit only that slide section plus its matching namespaced CSS file.

For shared layout changes, edit `src/styles/10-framework.css` and verify at least one title slide, one split slide, and one dense content slide.

For runtime changes, edit `src/scripts/deck-runtime.js` and preserve `deckConfig`, sidebar, zoom, keyboard navigation, and click zones.

After editing, rebuild the final HTML and summarize:

- Source files changed
- Generated output file
- Whether any shared framework file changed
- What the user should edit next time for the same type of change

## Single-file fallback

If there is no source folder yet and the user asks for a tiny change, edit the generated HTML directly only inside the matching region markers:

```html
<!-- REGION: SLIDE_INTRO START -->
...
<!-- REGION: SLIDE_INTRO END -->
```

Keep or add a `FILE MAP` comment at the top of the file so future edits can narrow context quickly.
