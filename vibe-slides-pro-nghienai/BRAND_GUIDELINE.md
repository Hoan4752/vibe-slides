# NghienAI Brand Guideline for Slide Design

Brand guideline cho hệ thống slide HTML của NghienAI - vibe-slides-pro-nghienai.

---

## 0. Source Workflow & Edit Map

Với deck có nhiều slide hoặc có khả năng sửa nhiều lần, làm việc trong source folder rồi build ra một file HTML cuối.

```text
work/[deck-slug]/
  EDIT_MAP.md
  src/
    deck.html
    sections/
    styles/
    scripts/
output/YYYY-MM-DD_slide-[slug].html
```

Quy tắc chỉnh sửa:

- Sửa nội dung slide trong `src/sections/[nn-slug].html`
- Sửa style riêng của một slide trong `src/styles/[nn-slug].css`
- Sửa token/layout chung trong `src/styles/00-tokens.css` hoặc `src/styles/10-framework.css`
- Sửa logo, sidebar, zoom, keyboard nav trong `src/scripts/deck-config.js` hoặc `src/scripts/deck-runtime.js`
- Không sửa trực tiếp file `output/*.html` trừ hotfix rất nhỏ; sửa source rồi build lại

Build về một HTML cuối:

```bash
python3 tools/vibe-slides-pro-nghienai/scripts/build_single_html.py work/[deck-slug]/src/deck.html output/YYYY-MM-DD_slide-[slug].html
```

Mỗi slide cần contract comment, `data-slide-id`, `data-nav`, `data-accent`, và CSS namespace như `.slide--intro`.

---

## 1. Layout & Navigation

### Sidebar Navigation
- **Vị trí**: Bên trái slide
- **Thành phần**: Chapter dots + labels
- **Line indicator**: Đường thẳng đứng nối các dots
- **Active state**: Dot to hơn + màu accent

### Click Navigation
- **Click zone trái** (15%): Lùi slide
- **Click zone phải** (15%): Tiến slide
- Không hiển thị hint text trên slide

### Controls Bar
- **Vị trí**: Góc dưới cùng bên phải
- **Thành phần**:
  - Zoom: `-` | `100%` | `+`
  - Divider
  - Navigation: `←` | `→`

### Loại bỏ
- Progress bar (đã có sidebar)
- Hint text
- Brand name text bên cạnh logo

---

## 2. Branding

### Logo
- **Vị trí**: Góc trái trên cùng
- **Số lượng**: Chỉ 1 logo
- **Size**: `clamp(32px, 3vw, 48px)`
- **File**: `NghienAI_logo_orange.svg`

### Slide Counter
- **Vị trí**: Góc phải trên cùng
- **Format**: `1 / 5`
- **Font**: IBM Plex Mono

---

## 3. Typography System

### Font Families
```css
--title-font: 'IBM Plex Serif', serif;     /* Chỉ cho main title */
--heading-font: 'IBM Plex Sans', sans-serif; /* Tất cả headings */
--body-font: 'IBM Plex Sans', sans-serif;    /* Body text */
--mono-font: 'IBM Plex Mono', monospace;     /* Labels, tags, code */
```

### Hierarchy

| Element | Font | Size |
|---------|------|------|
| `.title` (main only) | IBM Plex Serif | clamp(36px, 4vw, 72px) |
| `h1, .h1` | IBM Plex Sans | clamp(32px, 3.5vw, 56px) |
| `h2, .h2` | IBM Plex Sans | clamp(26px, 2.6vw, 44px) |
| `h3, .h3` | IBM Plex Sans | clamp(22px, 2vw, 32px) |
| `.body` | IBM Plex Sans | clamp(15px, 1.35vw, 20px) |
| `.kicker` | IBM Plex Mono | clamp(12px, 0.95vw, 15px) |
| `.tag` | IBM Plex Mono | clamp(11px, 0.85vw, 14px) |

### Quy tắc quan trọng
- **Serif CHỈ dùng cho `.title`** (main title duy nhất)
- **Tất cả headings khác** (h1, h2, h3) dùng Sans-serif
- **Body và UI elements** dùng Sans-serif hoặc Mono

---

## 4. Color System

### Brand Colors
```css
--neo-pearl: #F7F5ED;        /* Background chính */
--deep-dark-blue: #2A3140;   /* Text chính */
--neon-coral: #FF623B;       /* Accent chính (cam) */
--tangy-yellow: #FFE032;     /* Accent phụ */
--electric-violet: #8F00FF;  /* Accent phụ */
--turquoise-blue: #088B96;   /* Accent phụ */
--blue-glow: #4850ED;        /* Accent phụ */
```

### Usage
- **Background**: `--neo-pearl`
- **Primary text**: `--deep-dark-blue`
- **Primary accent**: `--neon-coral`
- **Secondary accents**: Yellow, Turquoise, Violet, Blue

---

## 5. Human-made Shapes

### Nguyên tắc
- **Chỉ apply rough edge lên viền shape**, không vào text bên trong
- Dùng **wrapper pattern** để tách filter khỏi content

### Implementation Pattern

```html
<!-- Box -->
<div class="human-shape-wrapper">
  <div class="human-box">
    <span>Content sắc nét</span>
  </div>
</div>

<!-- Circle -->
<div class="human-circle-wrapper">
  <div class="human-circle"></div>
</div>

<!-- Triangle (SVG) -->
<div class="human-triangle-wrapper">
  <svg viewBox="0 0 120 104" preserveAspectRatio="none">
    <polygon points="60,0 0,104 120,104" fill="#FF623B"/>
  </svg>
</div>

<!-- Star (SVG) -->
<div class="human-star-wrapper">
  <svg viewBox="0 0 100 100" preserveAspectRatio="none">
    <polygon points="50,0 61,35 98,35 68,57 79,91 50,70 21,91 32,57 2,35 39,35" fill="#FF623B"/>
  </svg>
</div>

<!-- Chip/Tag -->
<span class="organic-chip">Label</span>
```

### CSS Classes

| Class | Mô tả |
|-------|-------|
| `.human-shape-wrapper` | Wrapper cho box với rough edge |
| `.human-box` | Box bên trong, content sạch |
| `.human-box.is-outline` | Box viền không fill |
| `.human-circle-wrapper` | Wrapper cho circle |
| `.human-circle` | Circle bên trong |
| `.human-triangle-wrapper` | Wrapper cho triangle SVG |
| `.human-star-wrapper` | Wrapper cho star SVG |
| `.organic-chip` | Tag/chip với rough edge |

### SVG Filters
```html
<filter id="roughFilter">
  <feTurbulence type="fractalNoise" baseFrequency="0.04" numOctaves="3" seed="5"/>
  <feDisplacementMap in="SourceGraphic" in2="noise" scale="3"/>
</filter>
```

---

## 6. Halftone Patterns

### Pattern Classes

| Class | Hiệu ứng |
|-------|----------|
| `.halftone-panel` | Stepped edge + dots |
| `.halftone-band` | Horizontal band pattern |
| `.halftone-bg` | Full background pattern |
| `.halftone-stepped` | Stair-step clip-path |
| `.halftone-brick` | Brick-layout dots |
| `.halftone-gradient` | Gradient density dots |
| `.halftone-human` | Irregular hand-made dots |

### Implementation
```css
.halftone-panel::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image: radial-gradient(
    circle, 
    var(--deep-dark-blue) 0 1px, 
    transparent 1.5px
  );
  background-size: 6px 6px;
  opacity: 0.4;
  pointer-events: none;
}
```

---

## 7. Image-to-Halftone Conversion

### Container
```html
<div class="halftone-image">
  <img src="image.png" alt="Description">
</div>
```

### JavaScript API
```javascript
// Process và trả về data URL
const dataUrl = window.halftoneImage.process(imageElement, {
  dotSize: 4,
  spacing: 6
});

// Apply trực tiếp vào container
window.halftoneImage.applyToElement('.halftone-image', 'image.png', {
  dotSize: 4,
  spacing: 6
});
```

---

## 8. Zoom System

### Behavior
- Scale **nội dung slide** (`.slide-content`), không phải cả page
- Transform origin: center center
- Max zoom: 1.3 (tránh tràn ra ngoài)
- Min zoom: 0.7

### CSS
```css
.slide-content {
  width: 100%;
  height: 100%;
  transform: scale(var(--slide-zoom, 1));
  transform-origin: center center;
  max-width: calc(100% / var(--slide-zoom, 1));
  max-height: calc(100% / var(--slide-zoom, 1));
  margin: auto;
}
```

---

## 9. Responsive Breakpoints

### Sidebar Width
| Breakpoint | Width |
|------------|-------|
| Desktop (>1100px) | 140px |
| Tablet (900-1100px) | 120px |
| Small tablet (720-900px) | 100px |
| Mobile (<720px) | 36px (chỉ dots) |

### Mobile Adjustments
- Ẩn chapter labels, chỉ giữ dots
- Giảm padding slide
- Thu nhỏ controls bar
- Logo height: 28px

---

## 10. Slide Structure Template

```html
<section class="slide align-center active" data-nav="Chapter" data-accent="coral">
  <div class="slide-content">
    <div class="slide-inner">
      <div class="kicker reveal r1">Kicker text</div>
      <h1 class="title reveal r2">Main Title <strong>Highlight</strong></h1>
      <p class="body reveal r3">Body content...</p>
      <div class="meta-row reveal r4">
        <span class="organic-chip">Tag 1</span>
        <span class="tag">Tag 2</span>
      </div>
    </div>
  </div>
</section>
```

### Data Attributes
- `data-nav`: Label cho sidebar
- `data-accent`: Màu accent (coral, blue, violet, teal, yellow, dark)

### Animation Classes
- `.reveal` + `.r1`, `.r2`, `.r3`, `.r4`: Staggered fade-in animation

---

## 11. File Structure

```
vibe-slides-pro-nghienai/
├── SKILL.md              # Skill documentation
├── BRAND_GUIDELINE.md    # File này
├── base.html             # Template cơ bản
└── assets/
    ├── NghienAI_logo_orange.svg
    ├── NghienAI_logomark_orange.svg
    └── NghienAI_logomark_white.svg
```

---

## 12. Hard Rules

1. **Serif chỉ cho `.title`** - tất cả headings khác dùng Sans-serif
2. **Rough edge chỉ cho shapes** - không bao giờ apply lên text
3. **Dùng wrapper pattern** cho human-made shapes
4. **Zoom scale content** không phải page
5. **Chỉ 1 logo** - không text brand name thừa
6. **Sidebar thay thế progress bar**
7. **Click zones** cho navigation, không hint text
8. **Single file output** - self-contained HTML
