"""Copies the captions and references from the Session 1 outline into the prompter page.

    python3 -I build_prompter.py [outline.html] [prompter.html]

Defaults (inside the Session 1 folder next to this script):
    Session 1/RiskMind Session1 Outline.html  ->  Session 1/RiskMind Session 1 Prompter.html
See README.md.
Each <article class="slide"> in the outline is one scene; each beat row is "<label> · <t>s | Visual | On-screen | Caption | Reference".
A label is a number, or a word for beats before beat 1 (e.g. "Cover", "Course"); a first beat with a word label is
the cover, shown at 0 s before anything plays.
The beats are written into the prompter's <script id="beats"> block; nothing else in the prompter changes.
"""
import html, json, os, re, sys, time

here = os.path.dirname(os.path.abspath(__file__))
session = os.path.join(here, 'Session 1')
outline = sys.argv[1] if len(sys.argv) > 1 else os.path.join(session, 'RiskMind Session1 Outline.html')
prompter = sys.argv[2] if len(sys.argv) > 2 else os.path.join(session, 'RiskMind Session 1 Prompter.html')

for label, path in (('outline', outline), ('prompter', prompter)):
    if not os.path.exists(path):
        sys.exit(f'{label} not found: {path}')
src = open(outline, encoding='utf-8').read()
src = re.sub(r'<img\b[^>]*>', '', src)                      # embedded screenshots


def text(cell):
    cell = re.sub(r'<br\s*/?>', '\n', cell)
    cell = re.sub(r'<[^>]+>', '', cell)
    return html.unescape(cell).strip()


slides = []
for art in re.split(r'<article class="slide"', src)[1:]:
    h = re.search(r'<h3>(.*?)</h3>', art, re.S)
    title, subtitle = '', ''
    if h:
        sub = re.search(r'<span class="subtitle">(.*?)</span>', h.group(1), re.S)
        subtitle = text(sub.group(1)) if sub else ''
        title = text(re.sub(r'<span class="subtitle">.*?</span>', '', h.group(1), flags=re.S))
    beats = []
    for n, t, rest in re.findall(r'<tr><td>([^<·]+?) · ([\d.]+)s</td>(.*?)</tr>', art, re.S):
        tds = re.findall(r'<td>(.*?)</td>', rest, re.S)
        if len(tds) != 4:
            sys.exit(f'beat {n}: expected 4 more cells, found {len(tds)}')
        cap = text(tds[2])
        ref = [r.strip().lstrip('•').strip() for r in text(tds[3]).split('\n')]
        ref = [r for r in ref if r and r != '—']
        beats.append({'n': int(n) if n.strip().isdigit() else n.strip(), 't': float(t), 'caption': '' if cap == '—' else cap, 'ref': ref})
    if beats:
        slides.append({'title': title, 'subtitle': subtitle, 'beats': beats})

data = {'source': os.path.basename(outline),
        'built': time.strftime('%Y-%m-%d %H:%M'),
        'slides': slides}
blob = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')

page = open(prompter, encoding='utf-8').read()
new, k = re.subn(r'(<script id="beats" type="application/json">).*?(</script>)',
                 lambda m: m.group(1) + blob + m.group(2), page, count=1, flags=re.S)
if not k:
    sys.exit('no <script id="beats"> block in the prompter')
open(prompter, 'w', encoding='utf-8').write(new)

labels = [b['n'] for s in slides for b in s['beats']]
nums = [n for n in labels if isinstance(n, int)]
print(f'{len(slides)} scenes, {len(labels)} beats ({", ".join(map(str, labels[:3]))} … {labels[-1]}) -> {os.path.normpath(prompter)}')
if nums != list(range(nums[0], nums[0] + len(nums))):
    print('warning: beat numbers are not consecutive:', nums)
