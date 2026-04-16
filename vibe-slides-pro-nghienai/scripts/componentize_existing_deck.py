#!/usr/bin/env python3
import argparse
import re
import shutil
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlparse


PART_ACCENTS = {
    'P01': 'coral',
    'P02': 'teal',
    'P03': 'blue',
    'P04': 'violet',
    'P05': 'yellow'
}


def read_text(path):
    return path.read_text(encoding='utf-8')


def write_text(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + '\n', encoding='utf-8')


def slugify(value, fallback):
    normalized = unicodedata.normalize('NFKD', value)
    ascii_value = normalized.encode('ascii', 'ignore').decode('ascii')
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', ascii_value.lower()).strip('-')
    return slug or fallback


def get_attr(tag, name):
    match = re.search(rf'\b{name}=(["\'])(.*?)\1', tag, re.I | re.S)
    return match.group(2) if match else ''


def set_attr(tag, name, value):
    if re.search(rf'\b{name}=(["\']).*?\1', tag, re.I | re.S):
        return re.sub(rf'\b{name}=(["\']).*?\1', f'{name}="{value}"', tag, count=1, flags=re.I | re.S)
    return tag[:-1] + f' {name}="{value}">'


def add_class(tag, class_name):
    class_match = re.search(r'\bclass=(["\'])(.*?)\1', tag, re.I | re.S)
    if not class_match:
        return tag[:-1] + f' class="{class_name}">'

    classes = class_match.group(2).split()
    if class_name not in classes:
        classes.append(class_name)
    class_value = ' '.join(classes)
    start, end = class_match.span(2)
    return tag[:start] + class_value + tag[end:]


def find_first_style(html):
    match = re.search(r'<style\b[^>]*>(.*?)</style>', html, re.I | re.S)
    if not match:
        raise RuntimeError('No <style> block found.')
    return match


def find_last_script(html):
    matches = list(re.finditer(r'<script\b[^>]*>(.*?)</script>', html, re.I | re.S))
    if not matches:
        raise RuntimeError('No <script> block found.')
    return matches[-1]


def find_matching_div(html, open_start):
    tag_pattern = re.compile(r'<(/?)div\b[^>]*>', re.I)
    first = tag_pattern.search(html, open_start)
    if not first or first.start() != open_start:
        raise RuntimeError('Expected a <div> at the provided start.')

    depth = 0
    inner_start = first.end()
    for match in tag_pattern.finditer(html, open_start):
        if match.group(1):
            depth -= 1
            if depth == 0:
                return inner_start, match.start(), match.end()
        else:
            depth += 1

    raise RuntimeError('Could not find matching </div>.')


def find_slides_container(html):
    match = re.search(r'<div\b[^>]*\bid=(["\'])slides\1[^>]*>', html, re.I | re.S)
    if not match:
        raise RuntimeError('No <div id="slides"> container found.')
    inner_start, inner_end, close_end = find_matching_div(html, match.start())
    return match, inner_start, inner_end, close_end


def tag_has_slide_class(tag):
    class_value = get_attr(tag, 'class')
    return 'slide' in class_value.split()


def extract_slide_blocks(slides_inner):
    tag_pattern = re.compile(r'<(/?)div\b[^>]*>', re.I)
    slides = []
    cursor = 0
    depth = 0
    pending_start = None

    for match in tag_pattern.finditer(slides_inner):
        closing = bool(match.group(1))
        if not closing:
            if depth == 0 and tag_has_slide_class(match.group(0)):
                pending_start = match.start()
            depth += 1
        else:
            depth -= 1
            if depth == 0 and pending_start is not None:
                leading = slides_inner[cursor:pending_start]
                block = slides_inner[pending_start:match.end()]
                slides.append((leading, block))
                cursor = match.end()
                pending_start = None

    trailing = slides_inner[cursor:]
    if not slides:
        raise RuntimeError('No top-level slide blocks found inside #slides.')
    return slides, trailing


def split_css(css):
    split_match = re.search(r'\n\s*\*,\s*\n\s*\*::before', css)
    if not split_match:
        return '/* Tokens were not detected separately in the original deck. */\n', css.strip()

    split_at = split_match.start()
    tokens = css[:split_at].strip()
    framework = css[split_at:].strip()
    return tokens, framework


def local_asset_path(src, original_dir):
    if not src or src.startswith(('data:', 'http://', 'https://', '#')):
        return None
    if src.startswith('file://'):
        parsed = urlparse(src)
        return Path(unquote(parsed.path))
    return (original_dir / unquote(src)).resolve()


def unique_asset_name(assets_dir, name):
    return Path(name).name


def rewrite_local_images(content, original_dir, assets_dir, asset_prefix='./assets'):
    img_pattern = re.compile(r'<img\b[^>]*>', re.I | re.S)

    def replace_img(match):
        tag = match.group(0)
        src_match = re.search(r'\bsrc=(["\'])(.*?)\1', tag, re.I | re.S)
        if not src_match:
            return tag

        src = src_match.group(2)
        asset_path = local_asset_path(src, original_dir)
        if not asset_path or not asset_path.exists():
            return tag

        assets_dir.mkdir(parents=True, exist_ok=True)
        asset_name = unique_asset_name(assets_dir, asset_path.name)
        target = assets_dir / asset_name
        shutil.copy2(asset_path, target)

        next_tag = tag[:src_match.start(2)] + f'{asset_prefix}/{asset_name}' + tag[src_match.end(2):]
        if not re.search(r'\bdata-inline-asset\b', next_tag, re.I):
            next_tag = next_tag[:-1] + ' data-inline-asset>'
        return next_tag

    return img_pattern.sub(replace_img, content)


def transform_slide(block, index, section_file):
    tag_match = re.search(r'<div\b[^>]*>', block, re.I | re.S)
    if not tag_match:
        raise RuntimeError(f'Slide {index} has no opening <div>.')

    tag = tag_match.group(0)
    label = get_attr(tag, 'data-label') or f'Slide {index:02d}'
    part = get_attr(tag, 'data-part')
    slug = slugify(label, f'slide-{index:02d}')
    accent = PART_ACCENTS.get(part, 'coral')

    next_tag = tag
    next_tag = add_class(next_tag, f'slide--{slug}')
    next_tag = set_attr(next_tag, 'data-slide-id', slug)
    next_tag = set_attr(next_tag, 'data-nav', label)
    next_tag = set_attr(next_tag, 'data-accent', accent)

    next_block = block[:tag_match.start()] + next_tag + block[tag_match.end():]
    contract = f'''<!--
SECTION: {slug}
Purpose: Slide {index:02d} - {label}.
Owns: HTML inside div[data-slide-id="{slug}"].
Depends on: shared framework CSS, deck runtime, data-part/data-label navigation.
Do not change: .slide, data-slide-id, data-part, data-label, data-nav, data-accent without checking CSS/JS.
CSS namespace: .slide--{slug} or .slide[data-slide-id="{slug}"].
Edit file: {section_file}
-->
'''
    return slug, label, part, contract + next_block.strip()


def include_line(section_file):
    return f'      <!-- @include {section_file} -->'


def build_edit_map(deck_slug, output_file, sections):
    section_rows = '\n'.join(
        f'- Slide {item["index"]:02d} `{item["label"]}`: `src/{item["file"]}`'
        for item in sections
    )
    style_rows = '\n'.join(
        f'- Slide {item["index"]:02d} custom styling namespace: `.slide--{item["slug"]}` in `src/styles/20-slide-overrides.css`'
        for item in sections
    )

    return f'''# Edit Map

## Output
- Final deck: `{output_file}`
- Source folder: `work/{deck_slug}/src`
- Do not hand-edit the final output unless this is an emergency hotfix. Edit `src/` and rebuild.

## Slide Content
{section_rows}

## Visual Styling
- Original design system and shared slide components: `src/styles/10-framework.css`
- Theme tokens copied from the original deck: `src/styles/00-tokens.css`
- Future slide-specific overrides: `src/styles/20-slide-overrides.css`
{style_rows}

## Behavior
- Runtime/navigation/zoom/theme/sidebar logic: `src/scripts/deck-runtime.js`
- Config placeholder for future refactors: `src/scripts/deck-config.js`

## Assets
- Local images copied into `src/assets/` and marked with `data-inline-asset` so the build can inline them.

## Rebuild
```bash
python3 tools/vibe-slides-pro-nghienai/scripts/build_single_html.py work/{deck_slug}/src/deck.html {output_file}
```

## Editing Rule
For text changes, edit only the relevant `src/sections/[nn-slug].html` file. For one-slide visual changes, add namespaced CSS to `src/styles/20-slide-overrides.css`.
'''


def file_map_comment(deck_slug, sections):
    section_lines = '\n'.join(
        f'- sections/{Path(item["file"]).name}: slide {item["index"]:02d}, {item["label"]}'
        for item in sections
    )
    return f'''<!--
FILE MAP
- styles/00-tokens.css: original theme tokens and font variables
- styles/10-framework.css: original deck layout, shared components, navigation, responsive rules
- styles/20-slide-overrides.css: future slide-specific namespaced CSS
{section_lines}
- scripts/deck-config.js: future config extraction placeholder
- scripts/deck-runtime.js: original navigation, zoom, theme, sidebar, reveal, and generated SVG logic

EDIT CONTRACTS
- Work in work/{deck_slug}/src, then rebuild to output.
- Preserve .slide, data-slide-id, data-part, data-label, data-nav, data-accent, and control IDs.
- Scope new slide-specific CSS to .slide--[slug] or .slide[data-slide-id="[slug]"].
-->
'''


def componentize(source, work_dir, output_file):
    source = source.resolve()
    original_dir = source.parent
    src_dir = work_dir / 'src'
    styles_dir = src_dir / 'styles'
    sections_dir = src_dir / 'sections'
    scripts_dir = src_dir / 'scripts'
    assets_dir = src_dir / 'assets'
    deck_slug = work_dir.name

    html = read_text(source)

    style_match = find_first_style(html)
    css = style_match.group(1)
    tokens_css, framework_css = split_css(css)

    script_match = find_last_script(html)
    script_content = script_match.group(1).strip()

    slides_match, slides_inner_start, slides_inner_end, _ = find_slides_container(html)
    slides_inner = html[slides_inner_start:slides_inner_end]
    slide_blocks, _ = extract_slide_blocks(slides_inner)

    section_records = []
    include_lines = []
    for index, (_, block) in enumerate(slide_blocks, start=1):
        original_label = get_attr(re.search(r'<div\b[^>]*>', block, re.I | re.S).group(0), 'data-label') or f'Slide {index:02d}'
        slug = slugify(original_label, f'slide-{index:02d}')
        section_file = f'sections/{index:02d}-{slug}.html'
        slug, label, part, transformed = transform_slide(block, index, section_file)
        transformed = rewrite_local_images(transformed, original_dir, assets_dir, '../assets')
        write_text(src_dir / section_file, transformed)
        include_lines.append(include_line(section_file))
        section_records.append({
            'index': index,
            'slug': slug,
            'label': label,
            'part': part,
            'file': section_file
        })

    write_text(styles_dir / '00-tokens.css', f'/* REGION: CSS_TOKENS START */\n{tokens_css}\n/* REGION: CSS_TOKENS END */')
    write_text(styles_dir / '10-framework.css', f'/* REGION: CSS_FRAMEWORK START */\n{framework_css}\n/* REGION: CSS_FRAMEWORK END */')
    write_text(styles_dir / '20-slide-overrides.css', build_slide_overrides(section_records))
    write_text(scripts_dir / 'deck-config.js', build_deck_config_placeholder(section_records))
    write_text(scripts_dir / 'deck-runtime.js', f'// REGION: JS_RUNTIME START\n{script_content}\n// REGION: JS_RUNTIME END')

    links = '\n'.join([
        '  <link rel="stylesheet" href="./styles/00-tokens.css" data-inline>',
        '  <link rel="stylesheet" href="./styles/10-framework.css" data-inline>',
        '  <link rel="stylesheet" href="./styles/20-slide-overrides.css" data-inline>'
    ])
    deck_html = html[:style_match.start()] + links + html[style_match.end():script_match.start()] + '  <script src="./scripts/deck-config.js" data-inline></script>\n  <script src="./scripts/deck-runtime.js" data-inline></script>' + html[script_match.end():]
    _, deck_slides_inner_start, deck_slides_inner_end, _ = find_slides_container(deck_html)
    slides_inner_replacement = '\n' + '\n'.join(include_lines) + '\n'
    deck_html = deck_html[:deck_slides_inner_start] + slides_inner_replacement + deck_html[deck_slides_inner_end:]
    deck_html = rewrite_local_images(deck_html, original_dir, assets_dir, './assets')
    deck_html = file_map_comment(deck_slug, section_records) + deck_html

    write_text(src_dir / 'deck.html', deck_html)
    write_text(work_dir / 'EDIT_MAP.md', build_edit_map(deck_slug, output_file, section_records))

    return section_records


def build_slide_overrides(sections):
    blocks = ['/* REGION: SLIDE_OVERRIDES START', '   Add future one-slide CSS here. Keep every selector namespaced.', '*/']
    for item in sections:
        blocks.append(f'''
/* SLIDE {item["index"]:02d}: {item["label"]}
   Namespace: .slide--{item["slug"]} or .slide[data-slide-id="{item["slug"]}"]
*/
'''.rstrip())
    blocks.append('/* REGION: SLIDE_OVERRIDES END */')
    return '\n'.join(blocks)


def build_deck_config_placeholder(sections):
    items = ',\n'.join(
        f'    {{ index: {item["index"] - 1}, id: "{item["slug"]}", part: "{item["part"]}", label: "{item["label"]}" }}'
        for item in sections
    )
    return f'''// REGION: JS_CONFIG START
// Placeholder for future config extraction. The original runtime is preserved in deck-runtime.js.
window.deckSourceMap = {{
  slides: [
{items}
  ]
}};
// REGION: JS_CONFIG END
'''


def main():
    parser = argparse.ArgumentParser(description='Convert an existing single-file deck into componentized source files.')
    parser.add_argument('source', help='Existing single-file HTML deck')
    parser.add_argument('--work-dir', required=True, help='Target work/[deck-slug] folder')
    parser.add_argument('--output', required=True, help='Generated output HTML path used in EDIT_MAP')
    args = parser.parse_args()

    source = Path(args.source)
    work_dir = Path(args.work_dir)
    output_file = args.output
    sections = componentize(source, work_dir, output_file)
    print(f'Componentized {source} into {work_dir}/src ({len(sections)} slides).')


if __name__ == '__main__':
    main()
