# Facebook Multi-Image Format Guide
> Note cho skill visual-prompt-card (SKILL.md read-only, ghi chú tại đây)

## Rule: Khi làm 4 ảnh Facebook, LUÔN hỏi layout trước

Có 3 dạng tỉ lệ phổ biến khi post album 4 ảnh trên Facebook:

### Layout A — 4× Square `1200×1200`
- Tất cả 4 slide đều 1:1
- Dùng khi: info cards đồng đều, tips, steps

### Layout B — 1 Landscape + 3 Square *(khuyên dùng cho hook-first posts)*
- Slide 1: `1920×1280` (3:2) — hero slide, visual to
- Slides 2–4: `1000×1000` (1:1) — content slides
- Dùng khi: slide 1 là hook lớn có ảnh người, layout kiểu NghienAI brand

### Layout C — 1 Portrait + 3 Square
- Slide 1: `1000×2000` (1:2, dọc) — chiếm nhiều feed nhất
- Slides 2–4: `1000×1000` (1:1) — content slides
- Dùng khi: muốn tối đa diện tích trên feed

---

## Implementation Pattern (v2 chuẩn)

- Dùng `data-card-w` / `data-card-h` attributes trên mỗi `.card`
- JS scale: `transform: scale(wrapW / cardW)` — không dùng % font-size hay absolute position với px cứng
- Canvas-wrap switch class `r1x1` ↔ `r3x2` theo từng slide
- Reference file: `html-files/2026-04-09_visual-vibe-code-brand-4cards-v2.html`

## Hướng dẫn ghép ảnh người vào slide (cập nhật 2026-04-09)
- Crop ảnh người: KHÔNG để khoảng trống ở góc dưới — bottom của frame = bottom của chân/body
- CSS anchor: `position:absolute; bottom:0; left:0; width:100%; object-position: bottom left`
- Cho phép ảnh tràn lên trên (max-height: 150-160%) để overlap vào section trên
- Drop shadow: `filter: drop-shadow(-4px 0 12px rgba(0,0,0,.4))` để blend tự nhiên

## Font chuẩn NghienAI (cập nhật 2026-04-09)
- **Body / headline**: `IBM Plex Serif` (serif, "có chân")
- **UI labels / overlines / buttons**: `IBM Plex Sans`
- **Code / monospace / numbers**: `IBM Plex Mono`
- **Không dùng**: Be Vietnam Pro (đã replace), rough displacement filter trên text

## Text distortion — KHÔNG dùng

`filter: url(#rough)` trên các text container → gây méo chữ. Chỉ được dùng trên decorative elements (circles, shapes), KHÔNG BAOGIỜ trên `.card` hoặc text boxes.

---
*Learned: 2026-04-09*
