"""German wording, revised 2026-11-19: positive, forward-looking, about cooperation; no comparisons that
blame others; consistent terms (Teamleitung, E-Mail, €); fixed grammar.

Applied to the rendered German pages after content_v4.fix_text, because the German texts come from several
sources (krug_de.html via tr_de.py, content_de.py, content_v4.py). Every pair must match at least once:
check() fails the build otherwise, so a later text change cannot silently leave an old phrase behind.
"""
import re

PAIRS = [
    # ---------- home: hero ----------
    ('„Ein Bündel Schilfrohr zerbricht man nicht auf einmal – einzeln aber bricht jeden Halm sogar ein Kind.“',
     '„Ein Bündel Schilfrohr zerbricht niemand auf einmal. Einen einzelnen Halm bricht schon ein Kind.“'),
    ('<p class="hb-tag">Wie man gemeinsam mehr erreicht als allein – und tut, was die Welt braucht</p>',
     '<p class="hb-tag">Gemeinsam mehr erreichen – für Unternehmen, für ihre Branche und für die Gesellschaft</p>'),
    ('Kleine Teams von Fachleuten lösen Aufgaben, die Menschen brauchen und für die sie zahlen. Wir arbeiten in Etappen, stehen füreinander ein und machen aus den besten Lösungen Produkte – gemeinsam mit unseren Auftraggebern.',
     'Kleine, eingespielte Teams aus Fachleuten und KI entwickeln Software für Unternehmen – Etappe für Etappe, mit klarer Abnahme. Die besten Lösungen wachsen zu Produkten, die einer ganzen Branche dienen und allen gehören, die sie aufgebaut haben.'),
    ('80 % an das Team · 20 % Garantie von AMALOR · Vermittler: 5 % des ersten Projekts',
     '80 % für das Team · 20 % Garantie von AMALOR · 5 % des ersten Projekts für den Vermittler'),
    ('<span>erhält das Team, das die Arbeit gemacht hat</span>', '<span>für das Team, das die Lösung baut</span>'),
    # ---------- home: shared ownership ----------
    ('<h2>Wer mitbesitzt, liefert das beste Ergebnis</h2>', '<h2>Gemeinsam Eigentümer, gemeinsam am Erfolg beteiligt</h2>'),
    ('Bei einem klassischen Softwaredienstleister bezahlen Sie den ganzen Apparat, und die Entwickler arbeiten für ihren Arbeitgeber, nicht für Ihr Ergebnis. Bei uns gehen 80 % Ihres Budgets an die Menschen, die Ihre Lösung bauen, und als Partner-Auftraggeber werden Sie und das Team gemeinsam Miteigentümer.',
     '80 % Ihres Budgets gehen direkt an die Menschen, die Ihre Lösung bauen. Als Partner-Auftraggeber werden Sie gemeinsam mit dem Team Miteigentümer – so wollen alle vom ersten Tag an dasselbe: eine Lösung, die lange trägt.'),
    ('<li><b>Bezahlung nur für Ergebnisse</b>', '<li><b>Bezahlung nach Abnahme</b>'),
    ('<li><b>Kleiner Einstieg</b><span>Kostenloses Gespräch,', '<li><b>Überschaubarer Einstieg</b><span>Ein kostenloses Gespräch,'),
    ('<li><b>Kein Lock-in</b><span>Nach Bezahlung gehören Ihnen Code, Dokumentation und Rechte. Ihre Daten verlassen nie Ihre Systeme.</span>',
     '<li><b>Volle Freiheit</b><span>Nach Bezahlung gehören Ihnen Code, Dokumentation und Rechte. Ihre Daten bleiben in Ihren Systemen.</span>'),
    ('>Warum das besser funktioniert →</a>', '>Was Sie gewinnen →</a>'),
    # ---------- home: how it works ----------
    ('Wir prüfen sie mit unserem Filter.', 'Gemeinsam prüfen wir, ob sie Menschen wirklich nützt.'),
    # ---------- FAQ (home and clients) ----------
    ('Wir übernehmen Aufgaben, die unseren Filter bestehen: Menschen brauchen sie und sind bereit, dafür zu zahlen.',
     'Wir übernehmen Aufgaben, die Menschen wirklich brauchen und die für das Unternehmen einen klaren Wert haben.'),
    ('Sie können aber jederzeit zu einem anderen Anbieter wechseln.', 'Sie bleiben dabei frei und können die Betreuung jederzeit selbst übernehmen oder weitergeben.'),
    ('<summary>Darf die Lösung an unsere Wettbewerber verkauft werden?</summary><p>Nur wenn Sie Partner-Auftraggeber werden, und dann verdienen Sie an jedem Verkauf mit.',
     '<summary>Wird die Lösung auch anderen Unternehmen angeboten?</summary><p>Nur wenn Sie Partner-Auftraggeber werden – dann verdienen Sie an jeder Lizenz mit.'),
    ('Der Team Lead ist Ihr einziger Ansprechpartner, aber jedes Mitglied steht hinter dem Ergebnis.',
     'Die Teamleitung ist Ihre feste Ansprechperson, und jedes Mitglied steht hinter dem Ergebnis.'),
    ('Wird sie nicht abgenommen, bessert das Team auf eigene Kosten nach.', 'Passt etwas noch nicht, bessert das Team auf eigene Kosten nach.'),
    # ---------- forms ----------
    ('>Email</label>', '>E-Mail</label>'),
    ('Weitere Sprachen <span class="hint">in denen', 'Weitere Sprachen, <span class="hint">in denen'),
    ('Wir antworten innerhalb von zwei Werktagen.', 'Wir antworten innerhalb eines Werktags.'),
    ('Wir melden uns innerhalb von zwei Werktagen, um ein Gespräch zu vereinbaren.', 'Wir melden uns innerhalb eines Werktags, um ein Gespräch zu vereinbaren.'),
    ('Auf Wunsch sofort gelöscht.', 'Auf Wunsch sofort gelöscht. <a href="https://www.amalor.ai/datenschutz.html">Datenschutz</a>'),
    # ---------- members ----------
    ('<b>Weg des Wachstums:</b> Mitglied → Team Lead → Mentor → Kern. Es wächst nicht die Macht, sondern die Verantwortung für andere.',
     '<b>Weg des Wachstums:</b> Mitglied → Teammitglied → Kern → Mentor. Mit jedem Schritt wächst die Verantwortung für andere.'),
    ('ihr wählt einen Team Lead – jemanden, der den Rhythmus hält und dem Team dient, statt es zu kommandieren',
     'ihr wählt eine Teamleitung – jemanden, der den Rhythmus hält und dem Team dient'),
    ('<h2>Man kommt wegen des Geldes. Man bleibt wegen des Teams</h2>', '<h2>Man kommt wegen der Aufgabe. Man bleibt wegen der Menschen</h2>'),
    ('<b>Die Basis auf jeder Stufe:</b> faire Bezahlung: Das Einkommen', '<b>Die Basis auf jeder Stufe ist faire Bezahlung:</b> Das Einkommen'),
    # ---------- team ----------
    ('<h3>Teilen statt wuchern</h3>', '<h3>Wachsen durch Teilen</h3>'),
    ('die über ihre Leads verbunden bleiben – statt einer großen Abteilung.', 'die über ihre Teamleitungen verbunden bleiben. So bleibt jedes Team klein und nah beieinander.'),
    ('Rollen und Team Lead werden im Konsens bestätigt', 'Rollen und Teamleitung werden im Konsens bestätigt'),
    ('Rollen, auch der Team Lead, werden', 'Rollen, auch die Teamleitung, werden'),
    # ---------- principles: the sieve ----------
    ('<div><b>Beitrag</b><span>die Welt wird besser</span></div>', '<div><b>Wirkung</b><span>macht das Leben besser</span></div>'),
    # ---------- investors ----------
    ('<h1>Zuerst Beteiligung. Geld erst nach Beweisen</h1>', '<h1>Früh dabei sein. Investieren, wenn es sich bewährt hat</h1>'),
    ('Wir bitten nicht darum, in eine Idee zu investieren. Wir laden ein, früh dabei zu sein – und zu investieren, wenn ein Pilot Ergebnisse zeigt.',
     'Wir laden Sie ein, die Teams von Anfang an zu begleiten – und zu investieren, sobald ein Pilot Ergebnisse zeigt.'),
    ('zeigen dem Investor keinen Pitch, sondern einen Team-Pass mit dem ersten Kunden.', 'zeigen Ihnen einen Team-Pass mit dem ersten Kunden.'),
    ('<h2>Zuerst Nachfrage. Dann Menschen. Geld zuletzt</h2>', '<h2>Zuerst die Nachfrage, dann das Team, dann das Kapital</h2>'),
    ('<b>Kein Auftraggeber – kein Team.</b>', '<b>Jedes Team beginnt mit einem Auftraggeber.</b>'),
    ('Team Lead im Konsens', 'Teamleitung im Konsens'),
    ('<div><span>Team Lead</span>', '<div><span>Teamleitung</span>'),
    ('– keine Suche nach Deals.', '– mit echter Nachfrage von Anfang an.'),
    # ---------- book ----------
    ('<p class="lead">Wie man gemeinsam mehr erreicht als allein – und tut, was die Welt braucht. Ein Buch',
     '<p class="lead">Wie man gemeinsam mehr erreicht als allein – und dabei tut, was die Welt braucht. Ein Buch'),
    # ---------- second pass ----------
    ('<h2>Zwei Wege – Sie entscheiden</h2>', '<h2>Sie wählen den Weg, der zu Ihnen passt</h2>'),
    ('Beide Varianten stehen in jedem Angebot. Sie entscheiden nach der Diagnose, bevor die Umsetzung beginnt.',
     'Beide Wege stehen in jedem Angebot. Sie entscheiden nach der Diagnose, bevor die Umsetzung beginnt.'),
    ('Quellcode-Hinterlegung für den Fall, dass das Startup scheitert;', 'Quellcode-Hinterlegung, damit Sie in jedem Fall weiterarbeiten können;'),
    ('Ein Bündel Schilfrohr zerbricht nicht. Ein Team kann mehr als seine Menschen allein.',
     'Wie ein Bündel Schilfrohr: Zusammen erreicht ein Team mehr als jeder Einzelne für sich.'),
    ('Sinnvolle Aufgaben neben Menschen, auf die du dich verlassen kannst.', 'Sinnvolle Aufgaben mit Menschen, auf die du dich verlassen kannst.'),
    ('Über andere sprechen wir über das Wertvolle.', 'Über andere sprechen wir wertschätzend.'),
    ('Zwei übernehmen die Aufgaben.', 'Zwei andere übernehmen so lange die Aufgaben.'),
    ('Anerkennung für Hilfe an andere ist der wichtigste Grund für Ehre', 'Hilfe für andere ist der wichtigste Grund für Anerkennung'),
    ('Worin besteht sein Problem?', 'Wobei braucht er Unterstützung?'),
    # ---------- decisions 2026-11-19: income by agreed effort, referral cap, roots in the manifesto ----------
    ('für jedes Mitglied eines Viererteams – zu gleichen Teilen', 'für jedes Mitglied eines Viererteams bei gleichem Einsatz'),
    ('Anteil für die Entwicklung, intern zu gleichen Teilen', 'Anteil für die Entwicklung, intern nach Einsatz geteilt'),
    ('<li><b>Einkommen zu gleichen Teilen</b> unter den Teammitgliedern, nicht nach Titel.',
     '<li><b>Einkommen nach vereinbartem Einsatz,</b> nicht nach Titel. Gleicher Einsatz, gleicher Anteil.'),
    ('Das Einkommen des Teams wird zu gleichen Teilen geteilt.', 'Das Einkommen wird nach vereinbartem Einsatz geteilt, nicht nach Titel. Gleicher Einsatz, gleicher Anteil.'),
    ('teilen das Einkommen zu gleichen Teilen und entscheiden, wer dazukommt.',
     'teilen das Einkommen nach vereinbartem Einsatz – Vollzeit, Teilzeit oder nebenbei – und entscheiden, wer dazukommt.'),
    ('an das Team in jedem Projekt, zu gleichen Teilen unter den Mitgliedern', 'an das Team in jedem Projekt, geteilt nach vereinbartem Einsatz'),
    ('Einkommen zu gleichen Teilen, Teamvereinbarung', 'Einkommen nach Einsatz, Teamvereinbarung'),
    ('<li><b>5 % des ersten Projekts</b> des vorgestellten Auftraggebers.</li>', '<li><b>5 % des ersten Projekts</b> des vorgestellten Auftraggebers, bis 2.000 €.</li>'),
    ('<span>an den Vermittler für das erste Projekt</span>', '<span>an den Vermittler für das erste Projekt, bis 2.000 €</span>'),
    ('Dann erhalten Sie die Vermittlungsprämie und einen Anteil für Ihre Arbeit.</p>',
     'Dann erhalten Sie die Vermittlungsprämie und einen Anteil für Ihre Arbeit.</p>\n      <p class="when">Mitarbeitende des Auftraggebers und Berater, die für ihn auswählen, erhalten keine Prämie.</p>'),
]

# only on one page: {page: [(old, new)]}
PAGE_PAIRS = {
    'principles': [('<h2>Was das Team zusammenhält</h2>\n  </div>',
                    '<h2>Was das Team zusammenhält</h2>\n    <p class="lead">Die Idee hat ihre Wurzeln in alten Texten über die Verbindung '
                    'zwischen Menschen und wird von heutiger Forschung bestätigt. <a href="../manifest/">Mehr im Manifest →</a></p>\n  </div>')],
}

_MONEY = re.compile(r'(\d[\d.]*) \$')


def apply(page_html, page=''):
    for a, b in PAIRS + PAGE_PAIRS.get(page, []):
        page_html = page_html.replace(a, b)
    # euros on the German pages, outside scripts
    parts = re.split(r'(<script.*?</script>)', page_html, flags=re.S)
    return ''.join(p if p.startswith('<script') else _MONEY.sub(r'\1 €', p) for p in parts)


def check(pages):
    """pages: {page: rendered German page before apply()}. Every pair must be used."""
    unused = [a for a, _ in PAIRS if not any(a in p for p in pages.values())]
    unused += [a for pg, pairs in PAGE_PAIRS.items() for a, _ in pairs if a not in pages.get(pg, '')]
    if unused:
        raise SystemExit('polish_de: phrases not found (text changed?):\n- ' + '\n- '.join(unused))
