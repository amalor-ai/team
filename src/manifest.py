"""Designed manifesto in three languages: manifest/ (ru), en/manifest/, de/manifest/ (web)
+ assets/manifest-ru.pdf, manifest-en.pdf, manifest-de.pdf (print). Texts: src/manifest_text.py.
Run from the repo root: python3 src/manifest.py   (needs Playwright for the PDFs)
"""
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(__file__))
from content_extra import SPHERE_JS
from manifest_text import T, SOURCE_URLS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://team.amalor.ai'
OUT = {'ru': ('manifest', '../'), 'en': ('en/manifest', '../../'), 'de': ('de/manifest', '../../')}
HOME = {'ru': '../', 'en': '../', 'de': '../'}

CSS = r'''
@font-face{font-family:"Manrope";src:url("%FONT%") format("truetype");font-weight:200 800;font-display:swap}
:root{--bg:#FBF7EE;--paper:#FFFDF8;--ink:#0B2F2D;--soft:#4A6563;--line:#E4DAC4;--deep:#083C3A;--brand:#0E6B64;--gold:#C99A45;--gold2:#ECCF90;
--gg:linear-gradient(135deg,#F7E7B0,#E2BF74,#C99A45,#EDCD82)}
*{box-sizing:border-box}
html,body{margin:0;background:var(--bg);color:var(--ink);font-family:"Manrope",system-ui,sans-serif;font-size:17px;line-height:1.6;-webkit-print-color-adjust:exact;print-color-adjust:exact}
a{color:var(--brand)}
h1,h2,h3,h4{margin:0;line-height:1.15;text-wrap:balance}
p{margin:0}
.sheet{position:relative;max-width:900px;margin:0 auto;padding:72px 64px}
.eyebrow{font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:var(--gold);font-weight:700;margin-bottom:14px}
h2{font-size:40px;font-weight:800;letter-spacing:-.02em;margin-bottom:18px}
.lead{font-size:20px;color:var(--soft);max-width:60ch}
/* topbar (web only) */
.topbar{position:sticky;top:0;z-index:5;display:flex;justify-content:space-between;align-items:center;gap:12px;padding:12px 24px;background:rgba(8,60,58,.94);backdrop-filter:blur(6px)}
.topbar a{color:#C9E4E2;text-decoration:none;font-weight:600;font-size:15px}
.topbar .dl{background:var(--gg);color:#1B1405;padding:8px 16px;border-radius:999px}
/* cover */
.cover{background:radial-gradient(ellipse 60% 50% at 50% 42%,rgba(27,156,147,.45),rgba(27,156,147,0) 70%),var(--deep);color:#fff;min-height:100vh;display:flex;flex-direction:column;justify-content:space-between;padding:56px 64px}
.cover .brand{font-size:15px;letter-spacing:.3em;text-transform:uppercase;color:var(--gold2);font-weight:600}
.cover .sphere{display:block;width:min(400px,80%);aspect-ratio:1/1;margin:0 auto -80px;position:relative;z-index:1}.cover .tent{display:block;width:min(560px,96%);height:auto;margin:0 auto}
.cover h1{font-size:64px;font-weight:800;letter-spacing:-.03em;line-height:1}
.cover .kind{font-size:22px;color:var(--gold2);font-weight:600;margin-top:12px;letter-spacing:.04em}
.cover .q{font-style:italic;color:#9DC3BF;font-size:16px;margin-top:22px;max-width:46ch}
@media screen and (min-width:1000px){.cover{padding-left:calc((100% - 900px)/2 + 64px);padding-right:calc((100% - 900px)/2 + 64px)}.cover>div:last-child{margin-top:28px}}
/* intro */
.intro .big{font-size:28px;line-height:1.35;font-weight:600;letter-spacing:-.01em}
.intro .cols{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:28px;color:var(--soft)}
.intro .center{margin-top:34px;padding:26px 30px;border-radius:18px;background:var(--deep);color:#fff;font-size:20px;line-height:1.45}
.intro .center b{color:var(--gold2)}
/* beliefs */
.beliefs ol{list-style:none;margin:28px 0 0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:16px}
.beliefs li{position:relative;background:var(--paper);border:1px solid var(--line);border-radius:16px;padding:22px 22px 22px 70px;break-inside:avoid}
.beliefs li:last-child{grid-column:1/-1}
.beliefs .n{position:absolute;left:20px;top:20px;width:36px;height:36px;border-radius:50%;background:var(--gg);display:grid;place-items:center;font-weight:800;color:#1B1405}
.beliefs h3{font-size:19px;margin-bottom:6px}
.beliefs p{font-size:15px;color:var(--soft)}
/* circles */
.rings{width:100%;height:auto;margin:22px 0 8px}
.rings .rl{font-size:14px;letter-spacing:.2em;font-weight:700;fill:#8C7440;text-anchor:middle}
.rings .core{font-size:26px;font-weight:800;fill:#F7E7B0;text-anchor:middle}
.rings .core-s{font-size:14px;fill:#C9E4E2;text-anchor:middle}
.rings .core-g{font-size:14px;font-weight:700;fill:#ECCF90;text-anchor:middle}
.rings .it text{font-size:15px;fill:#0B2F2D;text-anchor:middle;font-weight:500}
table{width:100%;border-collapse:collapse;font-size:14.5px;margin-top:18px}
th,td{text-align:left;vertical-align:top;padding:11px 12px;border-bottom:1px solid var(--line)}
thead th{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);border-bottom:2px solid var(--gold2)}
tbody th{font-weight:700;width:30%}
tr{break-inside:avoid}
.note{font-size:13px;color:var(--soft);margin-top:12px}
/* honor */
.honor{background:var(--deep);color:#fff}
.honor h2{color:#fff} .honor .lead{color:#C9E4E2}
.split{margin-top:30px;display:flex;flex-direction:column;gap:22px}
.split .case b{display:block;font-size:15px;color:#C9E4E2;margin-bottom:8px;font-weight:600}
.bar{display:flex;gap:4px;height:58px;border-radius:12px;overflow:hidden;font-weight:700}
.bar div{display:flex;align-items:center;justify-content:center;background:rgba(201,228,226,.14);color:#C9E4E2;font-size:15px;white-space:nowrap}
.bar .team{background:var(--gg);color:#0B2F2D;justify-content:flex-start;padding-left:22px;font-size:20px}
.big4{margin-top:36px;display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.big4 div{border-top:1px solid rgba(201,228,226,.25);padding-top:14px}
.big4 h4{color:var(--gold2);font-size:19px;margin-bottom:6px}
.big4 p{font-size:14px;color:#A9CBC7}
/* rhythm */
.rhythm ol{list-style:none;margin:26px 0 0;padding:0;position:relative}
.rhythm ol::before{content:"";position:absolute;left:83px;top:10px;bottom:10px;width:2px;background:var(--line)}
.rhythm li{display:grid;grid-template-columns:100px 1fr;gap:26px;padding:12px 0;break-inside:avoid;position:relative}
.rhythm li::before{content:"";position:absolute;left:77px;top:22px;width:14px;height:14px;border-radius:50%;background:var(--gg);box-shadow:0 0 0 4px var(--bg)}
.rhythm .when{text-align:right;padding-right:28px}
.rhythm .when b{display:block;font-size:17px} .rhythm .when span{font-size:13px;color:var(--soft)}
.rhythm h4{font-size:18px;margin-bottom:2px} .rhythm p{color:var(--soft);font-size:15.5px}
.pact{margin-top:22px;padding:20px 24px;border-left:4px solid var(--gold);background:var(--paper);border-radius:0 14px 14px 0;font-size:15.5px}
/* product path */
.path{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:12px;margin-top:28px;counter-reset:s}
.path div{position:relative;background:var(--paper);border:1px solid var(--line);border-radius:16px;padding:18px}
.path div:last-child{background:var(--gg);border-color:transparent}
.path i{font-style:normal;font-size:12px;letter-spacing:.16em;color:var(--gold);font-weight:800}
.path div:last-child i{color:#5B4314}
.path h4{font-size:19px;margin:6px 0 4px} .path p{font-size:14px;color:var(--soft)} .path div:last-child p{color:#3A2C0C}
.owners{margin-top:22px;display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.owners div{font-size:14.5px;color:var(--soft)} .owners b{display:block;color:var(--ink);font-size:16px}
/* invitation */
.invite{background:radial-gradient(ellipse 60% 60% at 80% 20%,rgba(27,156,147,.4),rgba(27,156,147,0) 70%),var(--deep);color:#fff}
.invite h2{color:#fff}
.inv{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:24px}
.inv div{border:1px solid rgba(236,207,144,.3);border-radius:16px;padding:20px;break-inside:avoid}
.inv h4{color:var(--gold2);font-size:18px;margin-bottom:8px} .inv p{color:#C9E4E2;font-size:15px}
.closing{margin-top:44px;text-align:center}
.closing p{font-size:30px;font-weight:800;line-height:1.25;letter-spacing:-.01em}
.closing span{display:block;margin-top:14px;color:var(--gold2);font-weight:600}
/* sources */
.src p{color:var(--soft)}
.src ul{list-style:none;padding:0;margin:20px 0 0;columns:2;column-gap:28px}
.src li{break-inside:avoid;padding:8px 0;border-bottom:1px solid var(--line);font-size:14.5px}
.src li span{display:block;font-size:12px;color:var(--soft)}
footer.end{text-align:center;font-size:13px;color:var(--soft);padding:26px}
@media (max-width:720px){.sheet,.cover{padding:44px 20px}.cover h1{font-size:42px}h2{font-size:30px}
 .intro .cols,.beliefs ol,.inv{grid-template-columns:1fr}.big4,.path,.owners{grid-template-columns:1fr 1fr}.src ul{columns:1}
 .intro .big{font-size:22px}.rings .it text{font-size:17px}.bar .team{font-size:15px;padding-left:12px}
 table,thead,tbody,tr,th,td{display:block}thead{display:none}tbody th{width:auto;border:0;padding-bottom:0}td{border:0;padding-top:2px}tr{border-bottom:1px solid var(--line);padding:6px 0}}
/* blue thread */
.bar{box-shadow:0 0 0 1.5px #6FB7E6}.topbar .dl{box-shadow:0 0 0 1.5px #6FB7E6}
.big4 div{border:1px solid rgba(111,183,230,.55);border-radius:14px;padding:14px}
.beliefs .n{box-shadow:0 0 0 1.5px #6FB7E6}.path div:last-child{box-shadow:0 0 0 1.5px #6FB7E6}
.intro .center{box-shadow:inset 0 0 0 1.5px #6FB7E6}
@page{size:A4;margin:0}
@media print{.topbar{display:none}.cover,.page{height:297mm;overflow:hidden}.page{break-before:page}.sheet{max-width:none;padding:22mm 20mm}
 footer.end{display:none}.beliefs ol{gap:10px;margin-top:18px}.beliefs li{padding:14px 16px 14px 60px}.beliefs .n{left:16px;top:14px;width:32px;height:32px}
 .beliefs h3{font-size:16.5px}.beliefs p{font-size:13.5px;line-height:1.5}.intro .big{font-size:32px}.intro .cols{font-size:18px}
 .path{margin-top:36px}.path{gap:8px}.path div{padding:12px;min-height:170px}.path h4{font-size:14.5px;hyphens:auto}.path p{font-size:12px}.owners{margin-top:34px}.product .lead{font-size:21px}}
'''

TENT = '''<svg class="tent" viewBox="0 0 600 340" role="img" aria-label="Над открытым шатром висит сеть связей; под ним команда за круглым столом">
<defs>
 <linearGradient id="tg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F7E7B0"/><stop offset=".4" stop-color="#E2BF74"/><stop offset=".75" stop-color="#C99A45"/><stop offset="1" stop-color="#EDCD82"/></linearGradient>
 <linearGradient id="beam" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFF4D2" stop-opacity=".5"/><stop offset=".35" stop-color="#FFF4D2" stop-opacity=".7"/><stop offset="1" stop-color="#FFF4D2" stop-opacity=".9"/></linearGradient>
 <radialGradient id="tl" cx="50%" cy="78%" r="42%"><stop offset="0" stop-color="#FFE9B0" stop-opacity=".6"/><stop offset=".55" stop-color="#ECCF90" stop-opacity=".14"/><stop offset="1" stop-color="#ECCF90" stop-opacity="0"/></radialGradient>
 <linearGradient id="tab" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F7E7B0"/><stop offset="1" stop-color="#C99A45"/></linearGradient>
</defs>
<rect x="80" y="60" width="440" height="270" fill="url(#tl)"/>
<path d="M300 0 L300 250" stroke="url(#beam)" stroke-width="2.2"/><path d="M300 0 L300 250" stroke="#6FB7E6" stroke-width=".9" opacity=".8"/><circle cx="300" cy="248" r="22" fill="#FFF4D2" opacity=".18"/>
<ellipse cx="300" cy="312" rx="230" ry="16" fill="#000" opacity=".2"/>
<g fill="none" stroke="url(#tg)" stroke-linecap="round" stroke-linejoin="round">
 <path d="M168 132 L168 300 M432 132 L432 300" stroke-width="1.6" opacity=".45"/>
 <path d="M70 160 C150 150 230 120 300 64 C370 120 450 150 530 160" stroke-width="3"/>
 <path d="M70 160 C88 172 104 172 118 164 C134 174 150 174 164 166 C180 176 196 176 210 168 C226 177 242 177 256 170 C270 178 286 178 300 171 C314 178 330 178 344 170 C358 177 374 177 390 168 C404 176 420 176 436 166 C450 174 466 174 482 164 C496 172 512 172 530 160" stroke-width="1.8" opacity=".9"/>
 <path d="M300 64 C268 108 236 134 210 150 M300 64 C332 108 364 134 390 150 M300 64 C285 110 270 140 256 160 M300 64 C315 110 330 140 344 160" stroke-width="1" opacity=".5"/>
 <path d="M86 166 L86 304 M514 166 L514 304" stroke-width="2.6"/>
 <path d="M70 160 L34 306 M530 160 L566 306" stroke-width="1" opacity=".5" stroke-dasharray="3 5"/>
</g>
<circle cx="300" cy="62" r="4" fill="url(#tg)"/>
<g fill="url(#tg)">
 <path transform="translate(244 262)" opacity=".85" d="M-18 0 C-21 -28 -15 -50 -5 -60 C0 -67 10 -68 13 -60 C15 -54 11 -50 12 -43 C19 -32 22 -14 20 0 Z"/>
 <path transform="translate(356 262)" opacity=".85" d="M18 0 C21 -28 15 -50 5 -60 C0 -67 -10 -68 -13 -60 C-15 -54 -11 -50 -12 -43 C-19 -32 -22 -14 -20 0 Z"/>
 <path transform="translate(300 252)" opacity=".75" d="M-17 0 C-20 -30 -13 -54 0 -63 C13 -54 20 -30 17 0 Z"/>
</g>
<ellipse cx="300" cy="266" rx="92" ry="20" fill="url(#tab)" opacity=".95"/>
<ellipse cx="300" cy="264" rx="84" ry="15" fill="#FFF4D2" opacity=".35"/>
<path d="M208 268 C210 282 250 290 300 290 C350 290 390 282 392 268" fill="none" stroke="#B98A34" stroke-width="5" opacity=".85"/>
<g fill="url(#tg)">
 <path transform="translate(206 296)" d="M-18 0 C-21 -28 -15 -50 -5 -60 C0 -67 10 -68 13 -60 C15 -54 11 -50 12 -43 C19 -32 22 -14 20 0 Z"/>
 <path transform="translate(394 296)" d="M18 0 C21 -28 15 -50 5 -60 C0 -67 -10 -68 -13 -60 C-15 -54 -11 -50 -12 -43 C-19 -32 -22 -14 -20 0 Z"/>
</g>
<path d="M120 306 L480 306" stroke="url(#tg)" stroke-width="1.2" opacity=".55"/>
</svg>'''


# label positions on the rings: (x, y) of the first line; a second line goes 20 px lower
RING_POS = [(210, 305), (548, 305), (380, 438), (128, 196), (632, 196), (88, 296), (672, 305), (128, 414), (632, 414), (380, 530)]


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;')


def circles(t):
    items = ''
    for (x, y), label in zip(RING_POS, t['ring_items']):
        for k, line in enumerate(label.split('|')):
            items += f'<text x="{x}" y="{y + 20 * k}">{esc(line)}</text>'
    return f'''<svg viewBox="0 0 760 600" class="rings" role="img" aria-label="{t['rings_aria']}">
<ellipse cx="380" cy="300" rx="350" ry="270" fill="#EFE7D3" stroke="#C9B48A" stroke-dasharray="3 6"/>
<ellipse cx="380" cy="300" rx="225" ry="178" fill="#F7F1E3" stroke="#C9B48A"/>
<ellipse cx="380" cy="300" rx="112" ry="88" fill="#0B3F3C" stroke="#C99A45" stroke-width="3"/>
<text x="380" y="62" class="rl">{t['rl_out']}</text>
<text x="380" y="150" class="rl">{t['rl_mid']}</text>
<text x="380" y="292" class="core">{t['core']}</text>
<text x="380" y="316" class="core-s">{t['core_s']}</text>
<text x="380" y="338" class="core-g">{t['core_g']}</text>
<g class="it">{items}</g>
</svg>'''


def build_html(lang, for_pdf=False):
    t = T[lang]
    out, up = OUT[lang]
    beliefs = ''.join(f'<li><span class="n">{i+1}</span><h3>{esc(a)}</h3><p>{esc(d)}</p></li>' for i, (a, d) in enumerate(t['beliefs']))
    support = ''.join(f'<tr><th>{esc(a)}</th><td>{esc(b)}</td><td>{esc(c)}</td></tr>' for a, b, c in t['support'])
    rhythm = ''.join(f'<li><div class="when"><b>{w}</b><span>{d}</span></div><div><h4>{esc(a)}</h4><p>{esc(p)}</p></div></li>' for w, d, a, p in t['rhythm'])
    sources = ''.join(f'<li><b>{esc(a)}</b>, <a href="{u}">{esc(b)}</a><span>{t["principle"]} {n}</span></li>'
                      for (a, b), (u, n) in zip(t['sources'], SOURCE_URLS))
    big4 = ''.join(f'<div><h4>{a}</h4><p>{b}</p></div>' for a, b in t['big4'])
    path = ''.join(f'<div><i>{i+1:02d}</i><h4>{a}</h4><p>{b}</p></div>' for i, (a, b) in enumerate(t['path']))
    owners = ''.join(f'<div><b>{a}</b>{b}</div>' for a, b in t['owners'])
    invite = ''.join(f'<div><h4>{a}</h4><p>{b}</p></div>' for a, b in t['invite'])
    alts = ''.join(f'<link rel="alternate" hreflang="{l}" href="{BASE}/{OUT[l][0]}/">' for l in OUT)
    web_bar = '' if for_pdf else (f'<nav class="topbar"><a href="{HOME[lang]}" class="home">{t["home"]}</a>'
                                  f'<a class="dl" href="{up}assets/manifest-{lang}.pdf" download>{t["pdf"]}</a></nav>')
    return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t['title']}</title>
<meta name="description" content="{t['desc']}">
<link rel="canonical" href="{BASE}/{out}/">{alts}
<link rel="icon" href="{up}assets/favicon.svg">
<style>{CSS.replace('%FONT%', up + 'assets/fonts/Manrope.ttf')}</style></head><body>
{web_bar}
<section class="cover">
  <div class="brand">amalor</div>
  <canvas id="sphere" class="sphere" aria-hidden="true"></canvas>{TENT}
  <div><h1>{t['h1']}</h1><div class="kind">{t['kind']}</div>
  <p class="q">{t['quote']}</p></div>
</section>

<section class="sheet intro page">
  <div class="eyebrow">{t['intro_eb']}</div>
  <p class="big">{t['intro_big']}</p>
  <div class="cols"><p>{t['intro_c1']}</p>
  <p>{t['intro_c2']}</p></div>
  <div class="center">{t['intro_center']}</div>
</section>

<section class="sheet beliefs page">
  <div class="eyebrow">{t['bel_eb']}</div>
  <h2>{t['bel_h2']}</h2>
  <p class="lead">{t['bel_lead']}</p>
  <ol>{beliefs}</ol>
</section>

<section class="sheet circles page">
  <div class="eyebrow">{t['rings_eb']}</div>
  <h2>{t['rings_h2']}</h2>
  <p class="lead">{t['rings_lead']}</p>
  {circles(t)}
</section>

<section class="sheet circles page">
  <div class="eyebrow">{t['sup_eb']}</div>
  <h2>{t['sup_h2']}</h2>
  <p class="lead">{t['sup_lead']}</p>
  <table><thead><tr><th>{t['sup_head'][0]}</th><th>{t['sup_head'][1]}</th><th>{t['sup_head'][2]}</th></tr></thead><tbody>{support}</tbody></table>
</section>

<section class="sheet honor page">
  <div class="eyebrow">{t['hon_eb']}</div>
  <h2>{t['hon_h2']}</h2>
  <p class="lead">{t['hon_lead']}</p>
  <div class="split">
    <div class="case"><div class="bar"><div class="team" style="flex:80">{t['bar_team']}</div><div style="flex:20">{t['bar_rest']}</div></div></div>
    <p class="note" style="color:#A9CBC7">{t['hon_note']}</p>
  </div>
  <div class="big4">{big4}</div>
</section>

<section class="sheet rhythm page">
  <div class="eyebrow">{t['rh_eb']}</div>
  <h2>{t['rh_h2']}</h2>
  <p class="lead">{t['rh_lead']}</p>
  <ol>{rhythm}</ol>
  <p class="pact">{t['pact']}</p>
</section>

<section class="sheet product page">
  <div class="eyebrow">{t['pr_eb']}</div>
  <h2>{t['pr_h2']}</h2>
  <p class="lead">{t['pr_lead']}</p>
  <div class="path">{path}</div>
  <div class="owners">{owners}</div>
  <p class="note">{t['pr_note']}</p>
</section>

<section class="sheet invite page">
  <div class="eyebrow">{t['inv_eb']}</div>
  <h2>{t['inv_h2']}</h2>
  <div class="inv">{invite}</div>
  <div class="closing"><p>{t['closing']}</p><span>hello@amalor.ai · team.amalor.ai</span></div>
</section>

<section class="sheet src page">
  <div class="eyebrow">{t['src_eb']}</div>
  <h2>{t['src_h2']}</h2>
  <p>{t['src_lead']}</p>
  <ul>{sources}</ul>
</section>
<footer class="end">{t['end']}</footer>
{SPHERE_JS}
</body></html>'''


def main():
    for lang, (out, _) in OUT.items():
        d = os.path.join(ROOT, out)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(build_html(lang, False))
        tmp = os.path.join(d, '_print.html')
        open(tmp, 'w', encoding='utf-8').write(build_html(lang, True))
        pdf = os.path.join(ROOT, 'assets', f'manifest-{lang}.pdf')
        js = f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:794,height:1123}}}});
await p.emulateMedia({{reducedMotion:'reduce'}});await p.goto('file://{tmp}');await p.waitForTimeout(800);
await p.pdf({{path:'{pdf}',format:'A4',printBackground:true,preferCSSPageSize:true}});await b.close()}})()"""
        subprocess.run(['node', '-e', js], check=True)
        os.remove(tmp)
    print('manifest pages + PDFs written (ru, en, de)')


if __name__ == '__main__':
    main()
