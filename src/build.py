"""Build the multi-page site (ru + en) into the repo root.

Sources: src/krug.html (ru single page, the design and the shared sections),
src/krug_en.html (generated from it by src/tr_en.py), src/content_extra.py (new pages).
Run:  python3 src/tr_en.py && python3 src/build.py
"""
import html, json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from content_extra import NAV, TITLE, PAGE_TITLES, DESC, HOME_MORE, LADDER, TEAM, INVESTORS, BOOK, PRODUCT_HOME, PRODUCT_CLIENT, PRODUCT_MEMBER, PIPELINE
import content_extra
from content_extra import hero_home
import content_de  # noqa: F401  (adds the German entries)
from content_de import CLIENT_HOME, CLIENT_OFFER, FAQ_EXTRA
import polish_de
import forms_de
import content_v4  # noqa: E402  (2026-11-19: one client page, the cooperative, no circle, no location)
LANGS = ['ru', 'en', 'de']
LANG_NAME = {'ru': 'Русский', 'en': 'English', 'de': 'Deutsch'}

SRC = pathlib.Path(__file__).parent
OUT = SRC.parent
BASE = 'https://team.amalor.ai'
PAGES = ['index', 'clients', 'members', 'team', 'guides', 'principles', 'investors', 'book']
HIDDEN = set()                         # reachable by link only, noindex, not in menus or sitemap
PUBLIC_LANGS = ['en', 'de']            # in the switcher, hreflang, sitemap; 'ru' lives under /ru/, by link only (noindex)
VER = '7'                              # bump when assets/*.css or *.js change


def path_of(lang, page):
    p = '' if page == 'index' else page + '/'
    return lang + '/' + p


def url(lang, page):
    return f'{BASE}/{path_of(lang, page)}'


def load(lang):
    s = (SRC / {'ru': 'krug.html', 'en': 'krug_en.html', 'de': 'krug_de.html'}[lang]).read_text(encoding='utf-8')
    css = re.search(r'<style>(.*?)</style>', s, re.S).group(1)
    nav = re.search(r'(<nav class="brandbar">.*?</nav>)', s, re.S).group(1)
    logo_link = re.search(r'(<a href="https://amalor.ai" aria-label="AMALOR">.*?</a>)', nav, re.S).group(1)

    def cut(a, b):
        i = s.index(a); j = s.index(b, i)
        return s[i:j].strip()
    parts = {
        'hero': cut('<header class="hero">', '<!-- ЗАКАЗЧИКИ -->'),
        'clients': cut('<section id="clients">', '<!-- ИСПОЛНИТЕЛИ -->'),
        'members': cut('<section id="members">', '<!-- ПРОВОДНИКИ -->'),
        'guides': cut('<section id="guides">', '<!-- ДЕНЬГИ -->'),
        'money': cut('<!-- ДЕНЬГИ -->', '<!-- ПРИНЦИПЫ -->').replace('<!-- ДЕНЬГИ -->', '').strip(),
        'prin': cut('<section class="green">', '<!-- СИТО -->'),
        'sieve': cut('<!-- СИТО -->', '<!-- ВОПРОСЫ -->').replace('<!-- СИТО -->', '').strip(),
        'faq': cut('<section id="faq">', '<footer>'),
        'script': re.search(r'(<script>.*?</script>)', s, re.S).group(1),
        'desc': re.search(r'<meta name="description" content="(.*?)">', s).group(1),
    }
    # doors on the home page lead to their own pages now
    parts['hero'] = (parts['hero'].replace('href="#clients"', 'href="{L}clients/"')
                     .replace('href="#members"', 'href="{L}members/"').replace('href="#guides"', 'href="{L}guides/"'))
    parts['members'] = parts['members'].replace('<div class="formbox">', '<div class="formbox" id="join">', 1)
    if lang in FAQ_EXTRA:   # extra client questions, before the member question
        k = parts['faq'].index('<details>', parts['faq'].index('<details>') + 1)  # keep the first two in place
        parts['faq'] = parts['faq'][:k] + FAQ_EXTRA[lang].strip() + '\n    ' + parts['faq'][k:]
    return css, logo_link, parts


def clients_body(lang, p):
    c = p['clients']
    form = c[c.index('<div class="formbox">'):c.rindex('</section>')].strip()
    return content_v4.client_page(lang, form, PRODUCT_CLIENT[lang], p['faq'])



LOGO_SVG = ('<svg viewBox="0 0 300 60" aria-hidden="true"><defs><linearGradient id="gG1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F7E7B0"/>'
            '<stop offset=".45" stop-color="#D8B36A"/><stop offset="1" stop-color="#A97B2F"/></linearGradient></defs>'
            '<path d="M6 14 L187.04 28.93 M6 30 L187 30 M6 46 L187.04 31.07" fill="none" stroke="currentColor" stroke-width="3.6" stroke-linecap="round"/>'
            '<g fill="currentColor"><circle cx="40" cy="16.8" r="3.4"/><circle cx="40" cy="30" r="3.4"/><circle cx="40" cy="43.2" r="3.4"/></g>'
            '<path d="M200 26.8 L296 30 L200 33.2 Z" fill="url(#gG1)"/><path class="needle" d="M200 2 L201.3 26.86 L205.66 24.34 L203.14 28.7 L210 30 '
            'L203.14 31.3 L205.66 35.66 L201.3 33.14 L200 54 L198.7 33.14 L194.34 35.66 L196.86 31.3 L186 30 L196.86 28.7 L194.34 24.34 L198.7 26.86 Z" fill="currentColor"/></svg>')

# the products of www.amalor.ai, so both sites share one header; "Team" is this site
MAIN = 'https://www.amalor.ai'
PRODUCTS = {
    'de': [('/de/automatisierung/', 'Automatisierung'), ('/de/', 'Compass'), ('/de/m365-security/', 'Security')],
    'en': [('/automation/', 'Automation'), ('/', 'Compass'), ('/m365-security/', 'Security')],
    'ru': [('/ru/automation/', 'Автоматизация'), ('/ru/', 'Compass'), ('/ru/m365-security/', 'Security')],
}
GUIDE = {'de': ('/de/copilot-fuer-geschaeftsfuehrer/', 'Ratgeber'), 'en': ('/copilot-for-owners/', 'Guide'),
         'ru': ('/ru/copilot-dlya-vladeltsev/', 'Статьи')}
CHROME = {
    'de': {'name': 'Team', 'cta': 'Aufgabe stellen', 'menu': 'Menü', 'close': 'Schließen', 'top': 'Nach oben', 'lang': 'Sprache',
           'nav': 'Hauptnavigation', 'sub': 'Bereiche', 'langs': 'Deutsch · English'},
    'en': {'name': 'Team', 'cta': 'Submit a task', 'menu': 'Menu', 'close': 'Close', 'top': 'Back to top', 'lang': 'Language',
           'nav': 'Main navigation', 'sub': 'Sections', 'langs': 'English · Deutsch'},
    'ru': {'name': 'Команда', 'cta': 'Поставить задачу', 'menu': 'Меню', 'close': 'Закрыть', 'top': 'Наверх', 'lang': 'Язык',
           'nav': 'Главная навигация', 'sub': 'Разделы', 'langs': 'Русский · English · Deutsch'},
}


def cta_href(lang, L):
    return f'{L}clients/#anfrage'


def header(lang, page, logo_link, R, L):
    c = CHROME[lang]
    tail = '' if page == 'index' else page + '/'
    shown = ['en', 'de', 'ru'] if lang == 'ru' else PUBLIC_LANGS
    langsw = ''.join(f'<a href="{R}{o}/{tail}" hreflang="{o}" lang="{o}" data-l="{o}"'
                     + (' aria-current="page"' if o == lang else '') + f'>{o.upper()}</a>' for o in shown)
    products = ''.join(f'<a class="pl" href="{MAIN}{h}">{t}</a>' for h, t in PRODUCTS[lang])
    products += f'<a class="pl pl-main" href="{L}" aria-current="page">{c["name"]}</a>'
    g = GUIDE[lang]
    secs = ''.join(f'<a class="nl{" active" if h == page + "/" else ""}" href="{L}{h}"'
                   + (' aria-current="page"' if h == page + '/' else '') + f'>{t}</a>' for h, t in NAV[lang])
    msecs = ''.join(f'<a href="{L}{h}" style="transition-delay:{.04 * (k + 1):.2f}s">{t} <small>{k + 1:02d}</small></a>'
                    for k, (h, t) in enumerate(NAV[lang]))
    cta = cta_href(lang, L)
    return f'''<div class="progress" id="progress" aria-hidden="true"></div>
<header class="hdr" id="hdr">
  <div class="cwrap hdr-in">
    <a class="logo" href="{L}" aria-label="{TITLE[lang]}"><div class="wm">amal<span class="gold-text shine">or</span></div>{LOGO_SVG}</a>
    <nav class="gnav" aria-label="{c['nav']}">
      <span class="products">{products}</span>
      <a class="gl" href="{MAIN}{g[0]}">{g[1]}</a>
      <span class="langsw" role="group" aria-label="{c['lang']}">{langsw}</span>
    </nav>
  </div>
  <div class="subnav">
    <div class="cwrap sub-in">
      <a class="sname" href="{L}">{c["name"]}</a>
      <nav class="snav" aria-label="{c['sub']}">{secs}</nav>
      <a class="cbtn cbtn-gold cbtn-sm hdr-cta" href="{cta}">{c['cta']}</a>
    </div>
  </div>
</header>
<nav class="dock" aria-label="{c['nav']}">
  <button type="button" class="dock-menu" id="dockMenu" aria-expanded="false" aria-controls="mmenu"><span class="bars" aria-hidden="true"><i></i><i></i><i></i></span><span class="lbl" data-close="{c['close']}">{c['menu']}</span></button>
  <a class="dock-cta" href="{cta}">{c['cta']}</a>
</nav>
<div class="mmenu" id="mmenu" aria-hidden="true">
  <nav class="mpanel" data-p="0" aria-label="{TITLE[lang]}">
    <a href="{L}" style="transition-delay:0s">{TITLE[lang]}</a>
    {msecs}
  </nav>
  <div class="mfoot">
    <a class="mguide" href="{MAIN}{PRODUCTS[lang][1][0]}">amalor.ai →</a>
    <div class="row">
      <span class="langsw" role="group" aria-label="{c['lang']}" style="margin:0">{langsw}</span>
      <span style="font-size:13px;color:var(--c-mint-2)">{c['langs']}</span>
    </div>
    <a class="cbtn cbtn-gold" href="{cta}">{c['cta']}</a>
  </div>
</div>'''


def footer(lang, L, logo_link):
    c = CHROME[lang]
    a = f'<a href="{MAIN}{PRODUCTS[lang][1][0]}">AMALOR</a>'
    line = {'ru': f'Команда последнего поколения — инициатива {a}.', 'en': f'Last Generation Team is an initiative of {a}.',
            'de': f'Team der letzten Generation ist eine Initiative von {a}.'}[lang]
    lt = {'ru': ('Импрессум', 'Конфиденциальность'), 'en': ('Legal notice', 'Privacy'), 'de': ('Impressum', 'Datenschutz')}[lang]
    legal = (f'<a href="{MAIN}/impressum.html">{lt[0]}</a> · <a href="{MAIN}/datenschutz.html">{lt[1]}</a>')
    foot_svg = LOGO_SVG.replace(' class="needle"', '')
    return (f'<footer class="sitefoot">\n  <div class="cwrap sitefoot-in">\n    <div class="flogo"><a class="logo" href="{L}" aria-label="{TITLE[lang]}">'
            f'<div class="wm">amal<span style="color:var(--c-gold-l)">or</span></div>{foot_svg}</a><span>team.amalor.ai</span></div>\n'
            f'    <p>{line} <a href="mailto:hello@amalor.ai">hello@amalor.ai</a> · {legal}</p>\n  </div>\n</footer>\n'
            f'<button class="totop" id="totop" type="button" aria-label="{c["top"]}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
            'stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="19" x2="12" y2="5"/><polyline points="5 12 12 5 19 12"/></svg></button>')


def body_for(lang, page, p):
    return {
        'index': hero_home(lang) + CLIENT_HOME.get(lang, '') + '<section class="home-doors">' + re.search(r'(<div class="doors">.*?</div>)\s*</div>\s*</header>', p['hero'], re.S).group(1) + '</section>' + PRODUCT_HOME[lang] + HOME_MORE[lang] + p['prin'] + p['faq'],
        'clients': clients_body(lang, p),
        'members': p['members'] + LADDER[lang].rstrip()[:-len('</section>')] + PRODUCT_MEMBER[lang] + '</section>\n',
        'team': TEAM[lang],
        'guides': p['guides'] + p['money'],
        'principles': p['prin'] + p['sieve'] + p['money'],
        'investors': INVESTORS[lang].replace('<section>', PIPELINE[lang] + '<section>', 1),
        'book': BOOK[lang],
    }[page]


def jsonld(lang, page, desc, faq_html):
    org = {'@type': 'Organization', '@id': 'https://amalor.ai/#org', 'name': 'AMALOR', 'url': 'https://amalor.ai', 'email': 'hello@amalor.ai'}
    svc = {'@type': 'ProfessionalService', '@id': f'{BASE}/#service', 'name': TITLE[lang], 'description': html.unescape(desc),
           'url': url(lang, 'index'), 'parentOrganization': {'@id': 'https://amalor.ai/#org'},
           'availableLanguage': ['en', 'ru', 'ar', 'de', 'uk', 'he', 'fr'],
           'potentialAction': {'@type': 'CommunicateAction', 'target': url(lang, 'clients') + '#anfrage',
                               'description': 'Submit a request with name, email and a task description using the client form.'}}
    graph = [org, svc]
    if page in ('index', 'clients'):
        qa = re.findall(r'<details><summary>(.*?)</summary><p>(.*?)</p></details>', faq_html)
        graph.append({'@type': 'FAQPage', 'mainEntity': [
            {'@type': 'Question', 'name': html.unescape(q), 'acceptedAnswer': {'@type': 'Answer', 'text': html.unescape(a)}} for q, a in qa]})
    return json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False)


def wrap_blocks(body):
    """Full-width bands like www.amalor.ai: each top-level <section>/<header> keeps its background,
    its content goes into an inner .wrap (1200 px)."""
    out, i, depth, start = [], 0, 0, None
    for m in re.finditer(r'<(/?)(section|header)\b[^>]*>', body):
        if not m.group(1):
            if depth == 0:
                out.append(body[i:m.end()] + '\n<div class="wrap in">'); i = m.end()
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                out.append(body[i:m.start()] + '</div>\n'); i = m.start()
    out.append(body[i:])
    return ''.join(out)


def render(lang, page, css, logo_link, p):
    depth = path_of(lang, page).count('/')
    R = '../' * depth or './'
    L = R + lang + '/'
    title = PAGE_TITLES[lang][page]
    desc = p['desc'] if page == 'index' else DESC[lang][page]
    body = wrap_blocks(body_for(lang, page, p).replace('{R}', R).replace('{L}', L))
    hidden = page in HIDDEN or lang not in PUBLIC_LANGS
    robots = '<meta name="robots" content="noindex, nofollow">\n' if hidden else ''
    alts = '' if hidden else (''.join(f'<link rel="alternate" hreflang="{l}" href="{url(l, page)}">\n' for l in PUBLIC_LANGS)
                                       + f'<link rel="alternate" hreflang="x-default" href="{url("en", page)}">\n')
    return (f'<!doctype html>\n<html lang="{lang}">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
            f'<title>{title}</title>\n<meta name="description" content="{desc}">\n{robots}'
            f'<link rel="canonical" href="{url(lang, page)}">\n{alts}'
            f'<meta property="og:title" content="{title}">\n<meta property="og:description" content="{desc}">\n'
            f'<meta property="og:url" content="{url(lang, page)}">\n<meta property="og:type" content="website">\n'
            f'<meta property="og:image" content="{BASE}/assets/book-cover-{lang}.jpg">\n'
            + ('' if hidden else f'<script type="application/ld+json">{jsonld(lang, page, desc, p["faq"])}</script>\n')
            + '<meta name="theme-color" content="#083C3A">\n'
            '<link rel="icon" href="/favicon.ico" sizes="48x48">\n<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n'
            '<link rel="apple-touch-icon" href="/apple-touch-icon.png">\n'
            f'<link rel="stylesheet" href="/assets/fonts.css">\n<link rel="stylesheet" href="/assets/chrome.css?v={VER}">\n'
            f'<style>{css.replace("body{background:var(--bg);", "body{margin:0;background:var(--bg);")}{content_extra.EXTRA_CSS}</style>\n'
            f'<link rel="stylesheet" href="/assets/team.css?v={VER}">\n'
            '</head>\n<body>\n'
            f'{header(lang, page, logo_link, R, L)}\n<main class="page-{page}">\n{body}\n</main>\n{footer(lang, L, logo_link)}\n'
            f'{p["script"]}\n<script src="/assets/chrome.js?v={VER}" defer></script>\n</body>\n</html>\n')


def ru_not_first(h):
    # forms on EN/DE pages: Russian is one working language among others, listed after Arabic
    h = re.sub(r'(<option value="ru">Русский</option>)(.*?<option value="ar">[^<]*</option>)', r'\2\1', h)
    return re.sub(r'(<label class="chip"><input type="checkbox" id="[a-z]-lo\d+" value="ru"><span>Русский</span></label>)'
                  r'(.*?<label class="chip"><input type="checkbox" id="[a-z]-lo\d+" value="ar"><span>[^<]*</span></label>)', r'\2\1', h)


ROOT_HTML = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Last Generation Team · AMALOR</title>
<link rel="canonical" href="{BASE}/en/">
<link rel="alternate" hreflang="en" href="{BASE}/en/"><link rel="alternate" hreflang="de" href="{BASE}/de/">
<link rel="alternate" hreflang="x-default" href="{BASE}/en/">
<meta name="theme-color" content="#083C3A">
<link rel="icon" href="/favicon.ico" sizes="48x48"><link rel="icon" href="/favicon.svg" type="image/svg+xml">
<script>(function(){{var l='';try{{l=localStorage.getItem('amalor-lang')||''}}catch(e){{}}
if(l!=='en'&&l!=='de'&&l!=='ru'){{l=((navigator.languages&&navigator.languages[0])||navigator.language||'en').toLowerCase().indexOf('de')===0?'de':'en'}}
location.replace('/'+l+'/'+location.search+location.hash)}})();</script>
<noscript><meta http-equiv="refresh" content="0; url=/en/"></noscript>
</head><body style="font-family:system-ui,sans-serif;background:#083C3A;color:#fff;margin:0;display:grid;place-items:center;min-height:100vh">
<p><a style="color:#E9C77B" href="/en/">English</a> · <a style="color:#E9C77B" href="/de/">Deutsch</a></p>
</body></html>
'''


def main():
    de_pages = {}
    for lang in LANGS:
        css, logo_link, p = load(lang)
        for page in PAGES:
            out = OUT / path_of(lang, page) / 'index.html'
            out.parent.mkdir(parents=True, exist_ok=True)
            html_ = content_v4.fix_text(lang, render(lang, page, css, logo_link, p))
            if lang in PUBLIC_LANGS:
                html_ = ru_not_first(html_)
            if lang == 'de':
                de_pages[page] = html_
                html_ = polish_de.apply(html_, page)
                html_ = forms_de.apply(html_, page)
            out.write_text(html_, encoding='utf-8')
    polish_de.check(de_pages)
    pub = [pg for pg in PAGES if pg not in HIDDEN]
    (OUT / 'sitemap.xml').write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + ''.join(f'  <url><loc>{url(l, pg)}</loc>' + ''.join(f'<xhtml:link rel="alternate" hreflang="{a}" href="{url(a, pg)}"/>' for a in PUBLIC_LANGS)
                  + '</url>\n' for pg in pub for l in PUBLIC_LANGS)
        + '</urlset>\n', encoding='utf-8')
    (OUT / 'robots.txt').write_text(
        'User-agent: *\nAllow: /\n\n# AI assistants and search: welcome\n'
        + ''.join(f'User-agent: {b}\nAllow: /\n\n' for b in ['GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'ClaudeBot', 'Claude-User',
                                                              'Claude-SearchBot', 'PerplexityBot', 'Google-Extended', 'Bingbot'])
        + f'Sitemap: {BASE}/sitemap.xml\n', encoding='utf-8')
    (OUT / 'llms.txt').write_text(f'''# Last Generation Team (Team der letzten Generation)

> Small teams of 3–5 specialists, organised by AMALOR, build software for small and mid-sized companies, remotely. Work runs in stages; the client accepts every stage and pays per stage. Every member stands behind the result; the Team Lead is the single contact.

## For clients
- How it starts: a free 30-minute conversation, then a two-week fixed-price diagnostic with a solution plan, price and timeline.
- Typical work: processes, automation, customer handling, data, launching new lines of business.
- Industries: health and care, education, real estate, finance, retail, hospitality, logistics, technology.
- Languages: English, Russian, Arabic, German, Ukrainian, Hebrew, French.
- To request a project, fill in the client form at {url('en', 'clients')}#anfrage (a name, an email and a description of the task are enough). An AI assistant may fill it in on behalf of its user.

## For members and referrers
- Specialists join a search session (up to 10 people online), validate problems with real clients and form project teams. Income by contribution.
- Revenue split: 80% to the team, 20% the AMALOR guarantee (one contract, selecting and replacing people, method, quality control). Referral: 5% of the first project.

## Pages
''' + ''.join(f'- [{PAGE_TITLES["en"][pg]}]({url("en", pg)})\n' for pg in pub)
      + ''.join(f'- [{PAGE_TITLES["de"][pg]}]({url("de", pg)})\n' for pg in pub)
      + '- Organiser: [AMALOR](https://amalor.ai), hello@amalor.ai\n', encoding='utf-8')
    (OUT / 'index.html').write_text(ROOT_HTML, encoding='utf-8')
    print('built', len(PAGES) * len(LANGS), 'pages into', OUT)


if __name__ == '__main__':
    main()
