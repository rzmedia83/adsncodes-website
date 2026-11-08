#!/usr/bin/env python3
"""Weekly release helper for adsncodes.com, safe to run from a fresh clone.

Usage (from the repo root, with tools/hkeys.sh written from a fresh Hostinger upload key):
    python3 tools/release.py            # build, upload what changed, print URLs for IndexNow
    python3 tools/release.py --dry-run  # build and list what would be uploaded

Scheduled pages carry a 'publish' date (Dubai time) in site2/extra_services.py or site2/articles_data.py.
The build leaves them out until that date, so on release day a normal build adds them, links them from
their parent pages, the sitemap and llms.txt. This script uploads only files whose content changed.
"""
import hashlib, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, 'site2')
DRY = '--dry-run' in sys.argv


def sh(cmd, cwd=ROOT):
    return subprocess.run(cmd, cwd=cwd, shell=True, check=True, capture_output=True, text=True).stdout


sh('python3 build.py', cwd=SITE)
changed = [l[3:].strip() for l in sh('git status --porcelain site2').splitlines()]
changed = [c for c in changed if c.endswith(('.html', 'sitemap.xml', 'llms.txt', 'robots.txt'))]
# Keep only real content changes, not files that differ only in build noise
files = sorted({c.split('site2/', 1)[1] for c in changed if c.startswith('site2/') and not os.path.basename(c).startswith('_')})

cv = hashlib.md5(open(os.path.join(SITE, 'assets/site.css'), 'rb').read()).hexdigest()[:8]
jv = hashlib.md5(open(os.path.join(SITE, 'assets/site.js'), 'rb').read()).hexdigest()[:8]
out = os.path.join(ROOT, 'prod_release')
os.makedirs(os.path.join(out, 'ar'), exist_ok=True)
urls = []
for f in files:
    src = open(os.path.join(SITE, f), encoding='utf-8').read()
    if f.endswith('.html'):
        src = re.sub(r'<meta name="claude:[^"]*" content="[^"]*">\n?', '', src)
        src = src.replace('href="assets/site.css"', f'href="assets/site.css?v={cv}"').replace('src="assets/site.js"', f'src="assets/site.js?v={jv}"')
        src = re.sub(r'<video\b[^>]*>', lambda m: re.sub(r'\sposter="', ' data-lposter="', m.group(0)) if ('data-src=' in m.group(0) and 'sr-v' not in m.group(0)) else m.group(0), src)
        urls.append('https://adsncodes.com/' + ('' if f == 'index.html' else f))
    open(os.path.join(out, f), 'w', encoding='utf-8').write(src)
    print(('WOULD UPLOAD ' if DRY else 'UPLOAD ') + f)
    if not DRY:
        print(sh(f'bash tools/up.sh "{os.path.join(out, f)}" "{f}"').strip())
print('URLS ' + ' '.join(urls))
