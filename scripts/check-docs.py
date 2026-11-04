#!/usr/bin/env python3
"""Check public documentation links and the nine README language entry points."""
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
READMES = ['README.md', 'README.zh-CN.md'] + [
    f'docs/i18n/README.{code}.md' for code in ('zh-TW', 'ja', 'ko', 'pt-BR', 'es', 'fr', 'ar')
]

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []

    def handle_starttag(self, tag, attrs):
        self.targets += [value for key, value in attrs if key in ('href', 'src') and value]

errors = []
count = 0
for document in ROOT.rglob('*.md'):
    if '.git' in document.parts:
        continue
    content = document.read_text(encoding='utf-8')
    visible = re.sub(r'```.*?```', '', content, flags=re.S)
    parser = Links()
    parser.feed(visible)
    targets = re.findall(r'\]\(([^\s)]+)\)', visible) + parser.targets
    for target in targets:
        url = urlsplit(target)
        if url.scheme or url.netloc or not url.path:
            continue
        count += 1
        path = (document.parent / unquote(url.path)).resolve()
        if not path.is_relative_to(ROOT) or not path.is_file():
            errors.append(f'{document.relative_to(ROOT)}: missing local target {target}')
for relative in READMES:
    document = ROOT / relative
    if not document.is_file():
        errors.append(f'Missing translation: {relative}')
        continue
    content = document.read_text(encoding='utf-8')
    parser = Links()
    parser.feed(content)
    linked = {(document.parent / target).resolve() for target in parser.targets if target.endswith('.md')}
    expected = {ROOT / name for name in READMES} - {document}
    if not expected.issubset(linked):
        errors.append(f'{relative}: incomplete language navigation')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS {len(READMES)} language pages and {count} local links')
