"""German content for the multi-page site; merged into the dicts of content_extra."""
from content_extra import NAV, TITLE, PAGE_TITLES, DESC, HOME_MORE, LADDER, TEAM, INVESTORS, BOOK

NAV['de'] = [('clients/', 'Auftraggeber'), ('members/', 'Mitglieder'), ('team/', 'So arbeitet ein Team'),
             ('guides/', 'Vermittler'), ('investors/', 'Investoren'), ('principles/', 'Prinzipien'), ('book/', 'Buch')]
TITLE['de'] = 'Team der letzten Generation'
PAGE_TITLES['de'] = {'index': 'Team der letzten Generation', 'clients': 'Auftraggeber — Team der letzten Generation',
                     'members': 'Mitglieder — Team der letzten Generation', 'team': 'So arbeitet ein Team — Team der letzten Generation',
                     'guides': 'Vermittler — Team der letzten Generation', 'principles': 'Prinzipien — Team der letzten Generation',
                     'investors': 'Investoren — Team der letzten Generation', 'book': 'Buch — Team der letzten Generation'}
DESC['de'] = {
    'clients': 'Abgestimmte Arbeit in Etappen bis zum Ergebnis: ein kleines Team von Fachleuten, Diagnose zum Festpreis, Bezahlung pro Etappe. Dubai und remote.',
    'members': 'Im Team arbeiten, nicht allein: sinnvolle Aufgaben, gleicher Anteil am Einkommen, ein Weg vom Mitglied zum Mentor.',
    'team': 'Der Wochenrhythmus, der sechswöchige Zyklus, die Teamvereinbarung und wie sich der Prozess selbst verbessert.',
    'guides': 'Stellen Sie uns einen Auftraggeber vor und erhalten Sie 5 % des ersten Projekts.',
    'principles': 'Was das Team zusammenhält, welche Aufgaben wir übernehmen und wie das Geld geteilt wird.',
    'investors': 'Der Weg für Investoren: zuerst Beteiligung, Geld erst nach Beweisen.',
    'book': 'Das Buch „Team der letzten Generation. Wie ein Bündel Schilfrohr“ – bald.'}

HOME_MORE['de'] = '''<section>
  <div class="head"><h2>So funktioniert es</h2></div>
  <ol class="steps">
    <li><span class="num">1</span><div><h3>Aufgabe</h3><p class="when">Ein Auftraggeber bringt eine Aufgabe, oder ein Mitglied des Kreises findet sie. Wir prüfen sie mit unserem Filter.</p></div></li>
    <li><span class="num">2</span><div><h3>Team</h3><p class="when">Für die Aufgabe stellen wir ein kleines Team aus Menschen zusammen, die sich in der Praxis bewährt haben.</p></div></li>
    <li><span class="num">3</span><div><h3>Arbeit in Etappen</h3><p class="when">Jede Etappe sieht und nimmt der Auftraggeber ab. Für das Ergebnis steht das ganze Team ein.</p></div></li>
    <li><span class="num">4</span><div><h3>Wachstum</h3><p class="when">Starke Lösungen können zu einem Produkt werden – und das Team zu seinen Miteigentümern.</p></div></li>
  </ol>
  <p class="more"><a href="{L}team/">So arbeitet ein Team →</a> · <a href="{L}principles/">Prinzipien →</a></p>
</section>'''

LADDER['de'] = '''<section>
  <div class="head">
    <h2>Man kommt wegen des Geldes. Man bleibt wegen des Teams</h2>
    <p class="lead">Die Motivation wächst mit dem Menschen: vom Verdienst und der Erfahrung hin zu Anerkennung und dem Wunsch, etwas zurückzugeben.</p>
  </div>
  <ol class="ladder">
    <li><span class="num">1</span><div><h3>Mitglied</h3><p>Bezahlte Probeeinsätze, Erfahrung sammeln</p><p class="when">Motiv: Geld und Erfahrung</p></div></li>
    <li><span class="num">2</span><div><h3>Teammitglied</h3><p>Fest in einem Team von etwa fünf Menschen, Anteil nach Beitrag, Stimme im Team</p><p class="when">Motiv: Anteil am Projekt und Dank des Auftraggebers</p></div></li>
    <li><span class="num">3</span><div><h3>Brückenbauer</h3><p>Hilft anderen Teams, verbindet sie und leitet Austauschrunden – von den anderen bestätigt, ohne Macht über Teams</p><p class="when">Motiv: Anerkennung für den Beitrag zum Ganzen</p></div></li>
    <li><span class="num">4</span><div><h3>Mentor</h3><p>Begleitet neue Teams und gibt Erfahrung weiter</p><p class="when">Motiv: zurückgeben und andere wachsen lassen</p></div></li>
  </ol>
  <p class="rule"><b>Und das Team wächst mit:</b> Projektteam → feste Fünf → Gründerteam. Ein Team, das über mehrere Etappen gut zusammenarbeitet, bleibt zusammen – und kann das Startup tragen, das aus seiner Lösung entsteht, mit Anteilen nach Beitrag.</p>
  <p class="rule"><b>Die Basis auf jeder Stufe:</b> faire Bezahlung: Das Einkommen des Teams wird zu gleichen Teilen geteilt.</p>
</section>'''

TEAM['de'] = '''<header class="hero small">
  <div class="stack">
    <p class="eyebrow">So arbeitet ein Team</p>
    <h1>Ein Rhythmus, der Menschen zusammenhält</h1>
    <p class="lead">Etwa drei Stunden Meetings pro Woche – vereinbar mit einem Hauptjob. Jedes Meeting beginnt mit einem Ziel und endet mit einer Entscheidung.</p>
  </div>
</header>
<section>
  <div class="head"><h2>Die Woche</h2></div>
  <div class="week">
    <div><p class="when">Mo · 30 Minuten</p><h3>Kreis</h3><p>Das Ziel in einem Satz. Alle sprechen reihum, etwa eine Minute, ohne Diskussion. Jede Person nennt ihre wichtigste Aufgabe und wo sie Hilfe braucht.</p></div>
    <div><p class="when">Di–Do · ohne Meetings</p><h3>Arbeit und Kundentermine</h3><p>Ein kurzes Update im Chat: was ich gemacht habe, wo ich feststecke. Wer feststeckt, bekommt Hilfe – und alle sehen es.</p></div>
    <div><p class="when">Fr · 45 Minuten</p><h3>Demo und Anerkennungsrunde</h3><p>Was wir von Kunden gelernt und was wir gebaut haben. Jede Person nennt etwas Wertvolles, das jemand anderes getan hat.</p></div>
  </div>
</section>
<section>
  <div class="head">
    <h2>Der Zyklus – 6 Wochen Arbeit und eine Pause</h2>
    <p class="lead">Am Ende jedes Zyklus entscheidet das Team: weitermachen, Kurs ändern oder auseinandergehen.</p>
  </div>
  <div class="cycle" aria-label="Sechs Wochen Arbeit, dann eine große Retrospektive und eine Pause">
    <span>Wo. 1</span><span>Wo. 2</span><span>Wo. 3</span><span>Wo. 4</span><span>Wo. 5</span><span>Wo. 6</span><span class="retro">Retro · 90 Min.</span><span class="pause">Pause 1–2 Wo.</span>
  </div>
  <div class="cols" style="margin-top:20px">
    <div><h3>Die große Retrospektive</h3>
      <ul class="ticks"><li>Was ich von jedem gelernt habe</li><li>Mein Fehler und was ich daraus mache</li><li>Wo ich genommen, wo ich gegeben habe</li><li>Eine Änderung am Prozess</li></ul></div>
    <div><h3>Einmal im Quartal – der große Kreis</h3>
      <ul class="ticks"><li>Rollen und Team Lead werden im Konsens bestätigt – nach dem, was getan wurde, nicht nach Sympathie</li><li>Anerkennung für Hilfe an andere ist der wichtigste Grund für Ehre</li><li>Ein Beitrag in den gemeinsamen Fonds, der neue Teams startet</li></ul></div>
  </div>
</section>
<section>
  <div class="head">
    <h2>Die Teamvereinbarung</h2>
    <p class="lead">Wird am ersten Tag unterschrieben und bei jeder großen Retrospektive neu gelesen.</p>
  </div>
  <ol class="contract">
    <li>Wir stehen gemeinsam für das Ergebnis ein: Steckt einer fest, ist es die Aufgabe aller.</li>
    <li>Über andere sprechen wir über das Wertvolle. Über eigene Fehler spricht jeder selbst.</li>
    <li>Im Meeting sind wir ganz da: ohne Handy und ohne parallele Arbeit.</li>
    <li>Wir entscheiden im Konsens: Eine Entscheidung gilt, wenn es keine begründeten Einwände gibt.</li>
    <li>Im Streit geben wir zuerst die Position des anderen so wieder, dass er zustimmt.</li>
    <li>Hilfe für andere ist sichtbar und zählt mehr als persönliche Erfolge.</li>
    <li>Das Signal „Mir geht es gerade schwer“ ist normal und sicher. Zwei übernehmen die Aufgaben.</li>
    <li>Rollen, auch der Team Lead, werden vom Team einmal im Quartal bestätigt.</li>
  </ol>
</section>
<section>
  <div class="head"><h2>Der Prozess verbessert sich selbst</h2></div>
  <ol class="steps">
    <li><span class="num">1</span><div><h3>Team-Retro</h3><p class="when">muss eine Änderung hervorbringen</p></div></li>
    <li><span class="num">2</span><div><h3>Prüfung im Zyklus</h3><p class="when">haben sich die Gesundheitswerte des Teams verbessert?</p></div></li>
    <li><span class="num">3</span><div><h3>Kreis der Teams</h3><p class="when">monatlich: was bei anderen funktioniert hat</p></div></li>
    <li><span class="num">4</span><div><h3>Gemeinsames Playbook</h3><p class="when">eine neue Version für alle Teams</p></div></li>
  </ol>
  <div class="metrics">
    <div><b>Lerngeschwindigkeit</b><span>wie viele Hypothesen pro Woche mit Kunden geprüft wurden</span></div>
    <div><b>Verlässlichkeit</b><span>Anteil eingehaltener Zusagen</span></div>
    <div><b>Sicherheit</b><span>eine kurze Umfrage pro Zyklus</span></div>
    <div><b>Gleiche Stimme</b><span>wie gleichmäßig in Meetings gesprochen wird</span></div>
  </div>
</section>'''

INVESTORS['de'] = '''<header class="hero small">
  <div class="stack">
    <p class="eyebrow">Investoren</p>
    <h1>Zuerst Beteiligung. Geld erst nach Beweisen</h1>
    <p class="lead">Wir bitten nicht darum, in eine Idee zu investieren. Wir laden ein, früh dabei zu sein – und zu investieren, wenn ein Pilot Ergebnisse zeigt. Wir finden ein Problem, für dessen Lösung ein Auftraggeber zahlt, stellen ein Team aus bewährten Menschen zusammen und zeigen dem Investor keinen Pitch, sondern einen Team-Pass mit dem ersten Kunden.</p>
  </div>
</header>
<section>
  <div class="head"><h2>Der Weg für Investoren</h2></div>
  <ol class="ladder">
    <li><span class="num">0</span><div><h3>Mentor und Jury</h3><p class="when">jetzt, vor dem Pilot</p><p>Sie begleiten ein Team, sitzen in der Jury des Demo-Days und geben eine weiche Zusage: „Wenn X eintritt, investiere ich Y.“ Sie sehen die Teams am frühesten – ohne Geld und ohne Risiko.</p></div></li>
    <li><span class="num">1</span><div><h3>Angel-Club</h3><p class="when">nach dem Pilot</p><p>Ein kleines Ticket gemeinsam mit 5–10 Angels. Erstes Ansichts- und Co-Investmentrecht bei jedem Team.</p></div></li>
    <li><span class="num">2</span><div><h3>Fonds und Partner</h3><p class="when">im großen Maßstab</p><p>Beteiligung an einem Fonds neben Programmen aus Dubai und Impact-Investoren. Ein Portfolio von Teams mit bewiesener Zusammenarbeit und echten Kunden.</p></div></li>
  </ol>
</section>
<section>
  <div class="head"><h2>Was der Investor bekommt</h2></div>
  <ul class="prin plain">
    <li><b>Einen Strom geprüfter Teams</b><span>Teams kommen mit Pass und erstem Kunden – keine Suche nach Deals.</span></li>
    <li><b>Geringeres Risiko</b><span>Das Team hat schon zusammengearbeitet, die Nachfrage ist vom Auftraggeber bestätigt – die zwei größten Risiken sind vor dem Ticket geschlossen.</span></li>
    <li><b>Daten</b><span>Jeder Zyklus zeigt, welche Signale ein starkes Team vorhersagen.</span></li>
  </ul>
</section>
<section>
  <div class="head"><h2>Team-Pass</h2><p class="lead">Ein Beispiel dafür, was ein Investor sieht.</p></div>
  <div class="passport">
    <div><span>Auftraggeber</span><b>Absichtserklärung ✓</b></div>
    <div><span>Gemeinsame Zyklen</span><b>2 von 2 abgeschlossen</b></div>
    <div><span>Team Lead</span><b>vom Team bestätigt</b></div>
    <div><span>Kundengespräche</span><b>[Anzahl]</b></div>
    <div><span>Verlässlichkeit</span><b>Anteil eingehaltener Zusagen</b></div>
    <div><span>Beitrag</span><b>Produkt · Technik · Vertrieb</b></div>
  </div>
  <p class="more">Möchten Sie einer der ersten Mentoren werden? Schreiben Sie an <b>hello@amalor.ai</b></p>
</section>'''

BOOK['de'] = '''<section class="book">
  <img src="{R}assets/book-cover-de.jpg?v=20261120" width="659" height="993" alt="Cover des Buches „Team der letzten Generation. Wie ein Bündel Schilfrohr“">
  <div class="stack">
    <p class="eyebrow">Buch · bald</p>
    <h1>Team der letzten Generation</h1>
    <p class="sub">Wie ein Bündel Schilfrohr</p>
    <p class="lead">Wie man gemeinsam mehr erreicht als allein – und tut, was die Welt braucht. Ein Buch darüber, wie ein kleines Team seine Aufgaben wählt, sich selbst organisiert und wächst – vom ersten Auftrag bis zu einem Netzwerk von Teams.</p>
    <p class="when">Melde dich als Mitglied an, und wir sagen Bescheid, wenn es erscheint.</p>
    <div><a class="btn" href="{L}members/#join">Anmelden</a></div>
  </div>
</section>'''

from content_extra import PRODUCT_HOME, PRODUCT_CLIENT, PRODUCT_MEMBER, PIPELINE

PRODUCT_HOME['de'] = '''<section id="product">
  <div class="head">
    <h2>Von der Aufgabe zum Produkt</h2>
    <p class="lead">Manchmal ist die Aufgabe eines Unternehmens die Aufgabe einer ganzen Branche. Dann wird die Lösung zum Produkt – und das Produkt bekommt Miteigentümer: das Team, das es gebaut hat, und den Auftraggeber, der es mitgestaltet hat.</p>
  </div>
  <ol class="flow">
    <li><b>Aufgabe</b><span>eines Auftraggebers</span></li>
    <li><b>Lösung</b><span>in Etappen, mit Abnahme</span></li>
    <li><b>Von vielen gebraucht</b><span>bei anderen Unternehmen geprüft</span></li>
    <li><b>Produkt</b><span>Lizenzen für die Branche</span></li>
  </ol>
  <div class="owners">
    <div><b>Team</b><span>Anteil für die Entwicklung, intern zu gleichen Teilen</span></div>
    <div><b>Partner-Auftraggeber</b><span>ein Anteil und eine kostenlose Lizenz für sich</span></div>
    <div><b>Organisator</b><span>ein Anteil für Aufbau und Start</span></div>
    <div><b>Investoren</b><span>steigen ein, wenn das Produkt Nachfrage bewiesen hat</span></div>
  </div>
  <p class="more"><a href="{L}clients/#product-client">Für Auftraggeber →</a> · <a href="{L}investors/">Für Investoren →</a></p>
</section>'''

PRODUCT_CLIENT['de'] = '''<section id="product-client">
  <div class="head">
    <h2>Ihr Fall kann zum Produkt werden</h2>
    <p class="lead">Sie lösen Ihre eigene Aufgabe – und können daran verdienen, dass andere sie auch brauchen. Zeigt sich nach der Lösung, dass andere Unternehmen dasselbe Problem haben, entscheiden Sie, wie es weitergeht.</p>
  </div>
  <div class="tbl"><table>
    <thead><tr><th></th><th>Normaler Auftrag</th><th class="us">Partner-Auftraggeber</th></tr></thead>
    <tbody>
      <tr><td>Was Sie bekommen</td><td>eine fertige Lösung für Ihr Unternehmen</td><td class="us">eine Lösung für sich und einen Anteil am Produkt für andere</td></tr>
      <tr><td>Rechte</td><td>die Lösung gehört Ihnen, Sie nutzen sie frei</td><td class="us">eine unbefristete kostenlose Lizenz für Ihr Unternehmen und ein Anteil an den Lizenzerlösen von anderen</td></tr>
      <tr><td>Was Sie einbringen</td><td>Bezahlung der Etappen</td><td class="us">Bezahlung der Etappen, Branchenwissen, Mitarbeit an der Weiterentwicklung und Empfehlungen als erster Kunde</td></tr>
      <tr><td>Risiko</td><td>—</td><td class="us">wächst das Produkt nicht, bleibt Ihnen trotzdem eine funktionierende Lösung</td></tr>
    </tbody>
  </table></div>
  <p class="when" style="margin-top:12px">Die Höhe des Anteils richtet sich nach dem Beitrag und wird vertraglich festgelegt, bevor die Arbeit am Produkt beginnt.</p>
</section>'''

PRODUCT_MEMBER['de'] = '<p class="more"><a href="{L}#product">Wie ein Projekt zu einem Produkt mit Miteigentümern wird →</a></p>'

PIPELINE['de'] = '''<section>
  <div class="head">
    <h2>Zuerst Nachfrage. Dann Menschen. Geld zuletzt</h2>
    <p class="lead">Der erste Pilot liegt noch vor uns. Jetzt laden wir Mentoren ein, die die Teams von Anfang an sehen wollen.</p>
  </div>
  <ol class="steps">
    <li><span class="num">1</span><div><h3>Nachfrage finden</h3><p class="when">Aufgaben von Auftraggebern und Mitgliedern, Ausschreibungen, Kundenbeschwerden, neue Regeln</p></div></li>
    <li><span class="num">2</span><div><h3>Nachfrage prüfen</h3><p class="when">10–20 Gespräche und ein Auftraggeber, der für einen Pilot zahlt</p></div></li>
    <li><span class="num">3</span><div><h3>Probearbeit</h3><p class="when">1–2 Wochen in gemischten Paaren an einer echten Aufgabe</p></div></li>
    <li><span class="num">4</span><div><h3>Team bilden</h3><p class="when">Kern aus 3–5 Personen, Fachleute aus dem Kreis nach Bedarf, Einkommen zu gleichen Teilen, Teamvereinbarung, Team Lead im Konsens</p></div></li>
    <li><span class="num">5</span><div><h3>Lösung mit dem Auftraggeber</h3><p class="when">erste Nutzer und erstes Geld – vor jeder Finanzierungsrunde</p></div></li>
    <li><span class="num">6</span><div><h3>Team-Pass</h3><p class="when">Geschichte der Zusammenarbeit, Rollen, Kundengespräche, Kennzahlen</p></div></li>
    <li><span class="num">7</span><div><h3>Demo für Investoren</h3><p class="when">ein Team, das bewiesen hat, dass es funktioniert, mit einem Partner-Auftraggeber an der Seite</p></div></li>
  </ol>
  <p class="rule"><b>Kein Auftraggeber – kein Team.</b> Passt es menschlich nicht, stellen wir aus demselben Kreis neu zusammen.</p>
</section>'''

from content_extra import HERO_HOME
HERO_HOME['de'] = dict(quote='„Ein Bündel Schilfrohr zerbricht man nicht auf einmal – einzeln aber bricht jeden Halm sogar ein Kind.“',
    title='Team der letzten Generation', sub='Wie ein Bündel Schilfrohr',
    tag='Wie man gemeinsam mehr erreicht als allein – und tut, was die Welt braucht',
    lead='Kleine Teams von Fachleuten lösen Aufgaben, die Menschen brauchen und für die sie zahlen. Wir arbeiten in Etappen, stehen füreinander ein und machen aus den besten Lösungen Produkte – gemeinsam mit unseren Auftraggebern.',
    b1=('Ich habe eine Aufgabe', 'clients/'), b2=('Ins Team', 'members/'),
    ex='Beispiel: ein Projekt über 100.000 $', bar=[('Team 80 %',80),('Garantie 20 %',20)], legend='80 % an das Team · 20 % Garantie von AMALOR · Vermittler: 5 % des ersten Projekts',
    facts=[('80.000 $', 'erhält das Team, das die Arbeit gemacht hat'), ('20.000 $', 'für jedes Mitglied eines Viererteams – zu gleichen Teilen'), ('20.000 $', 'Garantie von AMALOR – so viel wie jedes Mitglied: Vertrag, Auswahl und Ersatz der Leute, Methode, Qualität'), ('0 $', 'zahlt der Auftraggeber für eine nicht abgenommene Etappe')])

from content_extra import CIRCLES_TXT
CIRCLES_TXT['de'] = dict(core='Bund', team='das Team · macht die Arbeit', purpose='für wen wir arbeiten', support='Kreis der Unterstützung',
    motto='„Alle stehen füreinander ein“', motto_src='',
    path=['Ein Problem, das Menschen wichtig ist', 'Pilot', 'Projekt', 'Startup'],
    path_note='Im Startup hält jedes Mitglied des Kreises einen Anteil nach seinem Beitrag. Den größten Anteil erhalten die, die die Hauptarbeit geleistet haben.',
    man='Manifest (RU)', links='Verbindungen zwischen den Kreisen')

from content_extra import _size_block, TEAM
TEAM['de'] = TEAM['de'].replace('</header>\n', '</header>\n' + _size_block(('Teamgröße','Ein Kern aus 3–5 Menschen','Sie tragen die Verantwortung für das Ergebnis, teilen das Einkommen zu gleichen Teilen und entscheiden, wer dazukommt. In dieser Größe hören alle einander und sehen den Beitrag jedes Einzelnen.','Fachleute für die Aufgabe','Wird für 1–2 Wochen eine Juristin, ein Designer oder eine andere Expertin gebraucht, kommt sie aus dem Kreis dazu. Sie wird für ihren Teil bezahlt und gehört nicht zum Kern.','Teilen statt wuchern','Braucht ein Projekt mehr als fünf Menschen, teilt sich das Team in zwei, die über ihre Leads verbunden bleiben – statt einer großen Abteilung.')), 1)

# --- German client offer (2026-11): what the client gets, two ways to own the result, safety, after the project ---
CLIENT_HOME = {'de': '''<section id="vorteile">
  <div class="head">
    <h2>Wer mitbesitzt, liefert das beste Ergebnis</h2>
    <p class="lead">Bei einem klassischen Softwaredienstleister bezahlen Sie den ganzen Apparat, und die Entwickler arbeiten für ihren Arbeitgeber, nicht für Ihr Ergebnis. Bei uns gehen 80 % Ihres Budgets an die Menschen, die Ihre Lösung bauen, und als Partner-Auftraggeber werden Sie und das Team gemeinsam Miteigentümer.</p>
  </div>
  <ul class="prin plain four">
    <li><b>Bezahlung nur für Ergebnisse</b><span>Jede Etappe hat einen festen Preis. Sie zahlen erst, wenn Sie sie abgenommen haben.</span></li>
    <li><b>Kleiner Einstieg</b><span>Kostenloses Gespräch, dann zwei Wochen Diagnose zum Festpreis. Danach entscheiden Sie.</span></li>
    <li><b>Kein Lock-in</b><span>Nach Bezahlung gehören Ihnen Code, Dokumentation und Rechte. Ihre Daten verlassen nie Ihre Systeme.</span></li>
    <li><b>An der Lösung mitverdienen</b><span>Als Partner-Auftraggeber werden Sie Miteigentümer und verdienen an jeder Lizenz für andere Firmen.</span></li>
  </ul>
  <p class="more"><a href="{L}clients/#warum">Warum das besser funktioniert →</a> · <a href="{L}clients/#vision">Die Vision →</a></p>
</section>'''}

CLIENT_OFFER = {'de': '''<section id="warum">
  <div class="head">
    <h2>Warum Softwareprojekte so teuer sind – und so oft enttäuschen</h2>
    <p class="lead">Wer Software bei einem Entwicklungsunternehmen bestellt, bezahlt nicht nur die Entwickler, sondern den ganzen Apparat: Vertrieb, Projektmanagement, Verwaltung, Büros und Marge. Und die Menschen, die Ihre Software tatsächlich bauen, sind Angestellte ihres Arbeitgebers, nicht Ihre. Ihr Gehalt ist dasselbe, ob Ihre Lösung ein Erfolg wird oder nicht.</p>
  </div>
  <div class="cards3 two">
    <div class="card"><h3>Klassisch beauftragt</h3><ul class="ticks">
      <li>Ihr Budget finanziert den Apparat des Dienstleisters.</li>
      <li>Die Entwickler arbeiten für ihren Arbeitgeber, nicht für Ihr Ergebnis.</li>
      <li>Oft wird nach Stunden abgerechnet: Mehr Aufwand bringt dem Dienstleister mehr Umsatz.</li>
      <li>Nach dem Projekt zieht das Team zum nächsten Kunden weiter.</li>
    </ul></div>
    <div class="card us"><h3>Mit uns</h3><ul class="ticks">
      <li>80 % Ihres Budgets gehen an die Menschen, die Ihre Lösung bauen.</li>
      <li>Bezahlt wird nur, was Sie abgenommen haben.</li>
      <li>Als Partner-Auftraggeber werden Sie und das Team gemeinsam Miteigentümer der Lösung.</li>
      <li>Das Team bleibt, weil es seine eigene Lösung weiterentwickelt.</li>
    </ul></div>
  </div>
  <p class="rule"><b>Die stärkste Motivation ist Eigentum.</b> Wer an der Lösung beteiligt ist, will, dass sie wirklich funktioniert – nicht nur, dass das Projekt abgerechnet wird. So ist jeder Beteiligte vom ersten Tag an daran interessiert, das beste Ergebnis zu liefern.</p>
</section>
<section id="vorteile">
  <div class="head">
    <h2>Ihre Vorteile</h2>
    <p class="lead">Sie bekommen die Lösung, die Ihre Branchensoftware nicht bietet – ohne eigene Entwicklungsabteilung und ohne das Risiko eines klassischen Softwareprojekts.</p>
  </div>
  <ul class="prin plain four">
    <li><b>Bezahlung nur für abgenommene Ergebnisse</b><span>Keine Stundenabrechnung. Jede Etappe hat einen vorab festgelegten Preis und klare Abnahmekriterien. Passt sie nicht, bessert das Team auf eigene Kosten nach.</span></li>
    <li><b>Kleiner, kalkulierbarer Einstieg</b><span>Ein kostenloses Gespräch, dann zwei Wochen Diagnose zum Festpreis mit Lösungsplan, Preis und Termin. Erst dann entscheiden Sie über die Umsetzung.</span></li>
    <li><b>Ein eingespieltes Team statt Einzelkämpfer</b><span>3–5 Fachleute und KI-Werkzeuge in einem festen Wochenrhythmus. Jeden Freitag gibt es sichtbare Ergebnisse, auf Wunsch als kurze Demo für Sie.</span></li>
    <li><b>Ein Vertrag, ein Ansprechpartner</b><span>Vertrag, Rechnungen und Abstimmung laufen über uns. Für fachliche Fragen sprechen Sie direkt mit dem Team.</span></li>
    <li><b>Ihre Daten bleiben bei Ihnen</b><span>Der Livebetrieb und echte Daten laufen in Ihren Systemen. Entwickelt und getestet wird mit Testdaten.</span></li>
    <li><b>Kein Lock-in</b><span>Nach Bezahlung erhalten Sie Quellcode, Dokumentation und Rechte. Sie können jederzeit den Anbieter wechseln.</span></li>
    <li><b>Kontinuität</b><span>Fällt jemand aus, ersetzt ihn unser Netzwerk. Nach dem Projekt betreut dasselbe Team Ihre Lösung im Wartungsvertrag weiter.</span></li>
    <li><b>Mitverdienen als Option</b><span>Hat Ihre ganze Branche dasselbe Problem, kann aus Ihrer Lösung ein Produkt werden – mit Ihnen als Miteigentümer.</span></li>
  </ul>
</section>
<section id="passt">
  <div class="head">
    <h2>Passt das zu Ihnen?</h2>
    <p class="lead">Am meisten gewinnen Unternehmen, auf die mindestens zwei dieser Punkte zutreffen:</p>
  </div>
  <ul class="ticks">
    <li>Sie arbeiten mit einer Branchensoftware, die nicht zu Ihren Abläufen passt, zu teuer oder zu starr ist.</li>
    <li>Wichtige Arbeit läuft noch über Excel, E-Mail oder Papier und kostet jede Woche Stunden.</li>
    <li>Sie haben schon überlegt, eine eigene Software entwickeln zu lassen, aber das Risiko schreckt ab.</li>
    <li>Andere Firmen Ihrer Branche kämpfen mit demselben Problem.</li>
  </ul>
</section>'''}

PRODUCT_CLIENT['de'] = '''<section id="product-client">
  <div class="head">
    <h2>Zwei Wege – Sie entscheiden</h2>
    <p class="lead">Beide Varianten stehen in jedem Angebot. Sie entscheiden nach der Diagnose, bevor die Umsetzung beginnt.</p>
  </div>
  <div class="tbl"><table>
    <thead><tr><th></th><th>Eigene Lösung</th><th class="us">Partner-Auftraggeber</th></tr></thead>
    <tbody>
      <tr><td>Wem gehört die Software</td><td>Ihnen: ausschließliche Rechte nach der letzten Zahlung</td><td class="us">dem gemeinsamen Produkt-Startup; Sie erhalten eine unbefristete kostenlose Lizenz für Ihr Unternehmen</td></tr>
      <tr><td>Preis</td><td>voller Projektpreis</td><td class="us">reduzierter Projektpreis</td></tr>
      <tr><td>Was Sie zusätzlich bekommen</td><td>—</td><td class="us">einen Anteil am Startup und eine Beteiligung an jeder Lizenz, die an andere Firmen verkauft wird</td></tr>
      <tr><td>Schutz</td><td>Code und Dokumentation gehören Ihnen</td><td class="us">Quellcode-Hinterlegung für den Fall, dass das Startup scheitert; auf Wunsch zeitweise Exklusivität gegenüber direkten Wettbewerbern</td></tr>
      <tr><td>Wenn kein Produkt entsteht</td><td>—</td><td class="us">Sie erhalten die vollen Rechte gegen eine vorab vereinbarte Restzahlung</td></tr>
      <tr><td>Nach dem Projekt</td><td>Wartungsvertrag mit demselben Team</td><td class="us">Wartung und Weiterentwicklung durch das Startup</td></tr>
    </tbody>
  </table></div>
  <p class="when" style="margin-top:12px">Allgemeine Bausteine wie Vorlagen und Werkzeuge, die nicht für Ihr Unternehmen spezifisch sind, bleiben bei uns. Sie dürfen sie unbefristet mitnutzen.</p>
</section>
<section id="danach">
  <div class="head">
    <h2>Nach dem Projekt</h2>
    <p class="lead">Software braucht Pflege. Deshalb endet die Zusammenarbeit nicht mit der Übergabe.</p>
  </div>
  <div class="cards3">
    <div class="card"><h3>Wartung zum Monatspreis</h3><p>Updates, Fehlerbehebung und kleine Anpassungen mit vereinbarten Reaktionszeiten.</p></div>
    <div class="card"><h3>Dasselbe Team</h3><p>Die Menschen, die Ihre Lösung gebaut haben, kennen sie am besten und bleiben Ihre Ansprechpartner.</p></div>
    <div class="card"><h3>Weiterentwicklung in Etappen</h3><p>Neue Wünsche werden wie im Projekt umgesetzt: kleine Etappe, fester Preis, Abnahme.</p></div>
  </div>
</section>'''

FAQ_EXTRA = {'de': '''
    <details><summary>Wem gehört die Software?</summary><p>Das entscheiden Sie. Als eigene Lösung gehört sie nach der letzten Zahlung Ihnen, mit Quellcode und Dokumentation. Als Partner-Auftraggeber gehört sie einem gemeinsamen Produkt-Startup, Sie erhalten eine kostenlose Lizenz, einen Anteil und eine Beteiligung an den Lizenzerlösen.</p></details>
    <details><summary>Was passiert mit unseren Daten?</summary><p>Der Livebetrieb und echte Daten bleiben in Ihren Systemen. Das Team arbeitet dort mit Gastzugängen. Entwickelt und getestet wird mit Testdaten.</p></details>
    <details><summary>Was ist, wenn jemand aus dem Team ausfällt?</summary><p>Dann ersetzen wir die Person aus unserem Netzwerk geprüfter Fachleute. Der Vertrag und die Verantwortung für das Ergebnis bleiben bei uns.</p></details>
    <details><summary>Wer betreut die Lösung nach dem Projekt?</summary><p>Auf Wunsch dasselbe Team, in einem Wartungsvertrag mit Monatspreis und vereinbarten Reaktionszeiten. Sie können aber jederzeit zu einem anderen Anbieter wechseln.</p></details>
    <details><summary>Darf die Lösung an unsere Wettbewerber verkauft werden?</summary><p>Nur wenn Sie Partner-Auftraggeber werden, und dann verdienen Sie an jedem Verkauf mit. Auf Wunsch vereinbaren wir eine zeitweise Exklusivität gegenüber direkten Wettbewerbern. Als eigene Lösung wird nichts weiterverkauft.</p></details>'''}
