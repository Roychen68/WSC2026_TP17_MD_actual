import { readFile, writeFile } from 'node:fs/promises';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const template = await readFile(resolve(root, 'source/shared.html.tpl'), 'utf8');
const themes = ['simple', 'elegant', 'cyber', 'colorful'];

for (const theme of themes) {
  const html = template.replace('@@CSS_FILE@@', `css_only_${theme}.css`);
  await writeFile(resolve(root, `student/css_only_${theme}.html`), html);
}

console.log(`Generated ${themes.length} locked HTML files.`);

