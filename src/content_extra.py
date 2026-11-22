"""Content for the pages that are new in the multi-page site (ru / en)."""

NAV = {
    'ru': [('clients/', 'Заказчикам'), ('members/', 'Участникам'), ('team/', 'Как работает команда'),
           ('guides/', 'Проводникам'), ('investors/', 'Инвесторам'), ('principles/', 'Принципы'), ('book/', 'Книга')],
    'en': [('clients/', 'Clients'), ('members/', 'Members'), ('team/', 'How a team works'),
           ('guides/', 'Referrers'), ('investors/', 'Investors'), ('principles/', 'Principles'), ('book/', 'Book')],
}

TITLE = {'ru': 'Команда последнего поколения', 'en': 'Last Generation Team'}

PAGE_TITLES = {
    'ru': {'index': 'Команда последнего поколения', 'clients': 'Заказчикам — Команда последнего поколения',
           'members': 'Участникам — Команда последнего поколения', 'team': 'Как работает команда — Команда последнего поколения',
           'guides': 'Проводникам — Команда последнего поколения', 'principles': 'Принципы — Команда последнего поколения',
           'investors': 'Инвесторам — Команда последнего поколения', 'book': 'Книга — Команда последнего поколения'},
    'en': {'index': 'Last Generation Team', 'clients': 'Clients — Last Generation Team',
           'members': 'Members — Last Generation Team', 'team': 'How a team works — Last Generation Team',
           'guides': 'Referrers — Last Generation Team', 'principles': 'Principles — Last Generation Team',
           'investors': 'Investors — Last Generation Team', 'book': 'Book — Last Generation Team'},
}

DESC = {
    'ru': {'clients': 'Слаженная работа по этапам до результата: небольшая команда специалистов, диагностика по фиксированной цене, оплата по этапам. Дубай и удалённо.',
           'members': 'Работа в команде, а не в одиночку: задачи со смыслом, равная доля дохода, путь от участника до наставника.',
           'team': 'Ритм недели и шестинедельного цикла, договор команды и то, как процесс улучшает сам себя.',
           'guides': 'Познакомьте нас с заказчиком и получите 5% от первого проекта.',
           'principles': 'На чём держится команда, какие задачи мы берём и как делятся деньги.',
           'investors': 'Путь инвестора: сначала участие, деньги — после доказательств.',
           'book': 'Книга «Команда последнего поколения. Как связка тростника» — скоро.'},
    'en': {'clients': 'Coordinated work, stage by stage, to the result: a small team of specialists, a fixed-price diagnostic, payment per stage. Dubai and remote.',
           'members': 'Work in a team, not alone: meaningful projects, an equal share of income, a path from member to mentor.',
           'team': 'The weekly rhythm, the six-week cycle, the team agreement and how the process improves itself.',
           'guides': 'Introduce us to a client and receive 5% of the first project.',
           'principles': 'What holds the team together, which tasks we take on and how the money is shared.',
           'investors': 'The investor path: participation first, money after proof.',
           'book': 'The book “Last Generation Team. Like a bundle of reeds” — coming soon.'},
}

HOME_MORE = {
'ru': '''<section>
  <div class="head"><h2>Как это устроено</h2></div>
  <ol class="steps">
    <li><span class="num">1</span><div><h3>Задача</h3><p class="when">Заказчик приносит задачу или её находит участник круга. Проверяем её ситом.</p></div></li>
    <li><span class="num">2</span><div><h3>Команда</h3><p class="when">Под задачу собираем небольшую команду из людей, проверенных делом.</p></div></li>
    <li><span class="num">3</span><div><h3>Работа по этапам</h3><p class="when">Каждый этап заказчик видит и принимает. За результат отвечает вся команда.</p></div></li>
    <li><span class="num">4</span><div><h3>Рост</h3><p class="when">Сильные решения могут вырасти в продукт, а команда — стать его совладельцами.</p></div></li>
  </ol>
  <p class="more"><a href="{L}team/">Как работает команда →</a> · <a href="{L}principles/">Принципы →</a></p>
</section>''',
'en': '''<section>
  <div class="head"><h2>How it works</h2></div>
  <ol class="steps">
    <li><span class="num">1</span><div><h3>Task</h3><p class="when">A client brings a task, or a circle member finds one. We run it through our filter.</p></div></li>
    <li><span class="num">2</span><div><h3>Team</h3><p class="when">We form a small team of people who have proven themselves in practice.</p></div></li>
    <li><span class="num">3</span><div><h3>Staged delivery</h3><p class="when">The client sees and accepts every stage. The whole team is accountable.</p></div></li>
    <li><span class="num">4</span><div><h3>Growth</h3><p class="when">Strong solutions can grow into a product, and the team can become its co-owners.</p></div></li>
  </ol>
  <p class="more"><a href="{L}team/">How a team works →</a> · <a href="{L}principles/">Principles →</a></p>
</section>'''}

LADDER = {
'ru': '''<section>
  <div class="head">
    <h2>Приходят за деньгами. Остаются за командой</h2>
    <p class="lead">Мотивация растёт вместе с человеком: от заработка и опыта — к признанию и желанию отдавать.</p>
  </div>
  <ol class="ladder">
    <li><span class="num">1</span><div><h3>Участник</h3><p class="when">мотив: деньги и опыт</p></div></li>
    <li><span class="num">2</span><div><h3>Член команды</h3><p class="when">мотив: доля в проекте и благодарность заказчика</p></div></li>
    <li><span class="num">3</span><div><h3>Ядро</h3><p class="when">мотив: признание за вклад в общее</p></div></li>
    <li><span class="num">4</span><div><h3>Наставник</h3><p class="when">мотив: отдача и рост других</p></div></li>
  </ol>
  <p class="rule"><b>Основа на каждом уровне:</b> справедливая оплата: доход команды делится поровну.</p>
</section>''',
'en': '''<section>
  <div class="head">
    <h2>People come for the money. They stay for the team</h2>
    <p class="lead">Motivation grows with the person: from income and experience to recognition and the wish to give back.</p>
  </div>
  <ol class="ladder">
    <li><span class="num">1</span><div><h3>Member</h3><p class="when">motive: income and experience</p></div></li>
    <li><span class="num">2</span><div><h3>Team member</h3><p class="when">motive: a share in the project and the client’s gratitude</p></div></li>
    <li><span class="num">3</span><div><h3>Core</h3><p class="when">motive: recognition for contributing to the whole</p></div></li>
    <li><span class="num">4</span><div><h3>Mentor</h3><p class="when">motive: giving back and helping others grow</p></div></li>
  </ol>
  <p class="rule"><b>The base at every level:</b> fair pay: team income is shared equally.</p>
</section>'''}

TEAM = {
'ru': '''<header class="hero small">
  <div class="stack">
    <p class="eyebrow">Как работает команда</p>
    <h1>Ритм, который держит людей вместе</h1>
    <p class="lead">Около трёх часов встреч в неделю — совместимо с основной работой. Каждая встреча начинается с цели и заканчивается решением.</p>
  </div>
</header>
<section>
  <div class="head"><h2>Неделя</h2></div>
  <div class="week">
    <div><p class="when">Пн · 30 минут</p><h3>Круг</h3><p>Цель одной фразой. Все говорят по очереди, около минуты, без споров. Каждый называет главную задачу и где нужна помощь.</p></div>
    <div><p class="when">Вт–Чт · без встреч</p><h3>Работа и выходы к клиентам</h3><p>Короткий отчёт в чате: что сделал, где застрял. Застрявшему помогают — и это видно всем.</p></div>
    <div><p class="when">Пт · 45 минут</p><h3>Демо и раунд признания</h3><p>Что узнали у клиентов, что сделали. Каждый называет ценное, что сделал кто-то другой.</p></div>
  </div>
</section>
<section>
  <div class="head">
    <h2>Цикл — 6 недель работы и пауза</h2>
    <p class="lead">В конце цикла команда решает: продолжаем, меняем курс или расходимся.</p>
  </div>
  <div class="cycle" aria-label="Шесть недель работы, затем большая ретроспектива и пауза">
    <span>Нед. 1</span><span>Нед. 2</span><span>Нед. 3</span><span>Нед. 4</span><span>Нед. 5</span><span>Нед. 6</span><span class="retro">Ретро · 90 мин</span><span class="pause">Пауза 1–2 нед.</span>
  </div>
  <div class="cols" style="margin-top:20px">
    <div><h3>Большая ретро</h3>
      <ul class="ticks"><li>Чему я научился у каждого</li><li>Моя ошибка и что я с ней сделаю</li><li>Где тянул на себя, где отдавал</li><li>Одно изменение процесса</li></ul></div>
    <div><h3>Раз в квартал — большой круг</h3>
      <ul class="ticks"><li>Роли и Team Lead подтверждаются по согласию — по сделанному, а не по симпатии</li><li>Признание за помощь другим — главный повод для почёта</li><li>Взнос в общий фонд, который запускает новые команды</li></ul></div>
  </div>
</section>
<section>
  <div class="head">
    <h2>Договор команды</h2>
    <p class="lead">Подписывается в первый день и перечитывается на каждой большой ретро.</p>
  </div>
  <ol class="contract">
    <li>Отвечаем за результат вместе: застрял один — это задача всех.</li>
    <li>О товарищах говорим ценное. О своих ошибках каждый говорит сам.</li>
    <li>На встрече присутствуем полностью: без телефонов и параллельной работы.</li>
    <li>Решаем по согласию: решение проходит, если нет обоснованных возражений.</li>
    <li>В споре сначала пересказываем позицию другого так, чтобы он согласился.</li>
    <li>Помощь другим видна и ценится выше личных достижений.</li>
    <li>Сигнал «мне тяжело» — нормальный и безопасный. Двое подхватят задачи.</li>
    <li>Роли, включая Team Lead, команда подтверждает раз в квартал.</li>
  </ol>
</section>
<section>
  <div class="head"><h2>Процесс улучшает сам себя</h2></div>
  <ol class="steps">
    <li><span class="num">1</span><div><h3>Ретро команды</h3><p class="when">обязана дать одно изменение</p></div></li>
    <li><span class="num">2</span><div><h3>Проверка циклом</h3><p class="when">стало лучше по показателям здоровья команды?</p></div></li>
    <li><span class="num">3</span><div><h3>Круг команд</h3><p class="when">раз в месяц: что сработало у других</p></div></li>
    <li><span class="num">4</span><div><h3>Общий плейбук</h3><p class="when">новая версия для всех команд</p></div></li>
  </ol>
  <div class="metrics">
    <div><b>Скорость обучения</b><span>сколько гипотез проверено у клиентов за неделю</span></div>
    <div><b>Надёжность</b><span>доля выполненных обещаний</span></div>
    <div><b>Безопасность</b><span>короткий опрос раз в цикл</span></div>
    <div><b>Равенство голоса</b><span>насколько равномерно говорят на встречах</span></div>
  </div>
</section>''',
'en': '''<header class="hero small">
  <div class="stack">
    <p class="eyebrow">How a team works</p>
    <h1>A rhythm that keeps people together</h1>
    <p class="lead">About three hours of meetings a week — compatible with a main job. Every meeting starts with a goal and ends with a decision.</p>
  </div>
</header>
<section>
  <div class="head"><h2>The week</h2></div>
  <div class="week">
    <div><p class="when">Mon · 30 minutes</p><h3>Circle</h3><p>The goal in one sentence. Everyone speaks in turn for about a minute, no debate. Each person names their main task and where they need help.</p></div>
    <div><p class="when">Tue–Thu · no meetings</p><h3>Work and client visits</h3><p>A short update in chat: what I did, where I am stuck. Whoever is stuck gets help — and everyone sees it.</p></div>
    <div><p class="when">Fri · 45 minutes</p><h3>Demo and recognition round</h3><p>What we learned from clients and what we built. Everyone names something valuable another person did.</p></div>
  </div>
</section>
<section>
  <div class="head">
    <h2>The cycle — 6 weeks of work and a pause</h2>
    <p class="lead">At the end of each cycle the team decides: continue, change course or part ways.</p>
  </div>
  <div class="cycle" aria-label="Six weeks of work, then a big retrospective and a pause">
    <span>Wk 1</span><span>Wk 2</span><span>Wk 3</span><span>Wk 4</span><span>Wk 5</span><span>Wk 6</span><span class="retro">Retro · 90 min</span><span class="pause">Pause 1–2 wks</span>
  </div>
  <div class="cols" style="margin-top:20px">
    <div><h3>The big retrospective</h3>
      <ul class="ticks"><li>What I learned from each person</li><li>My mistake and what I will do about it</li><li>Where I took, where I gave</li><li>One change to the process</li></ul></div>
    <div><h3>Once a quarter — the big circle</h3>
      <ul class="ticks"><li>Roles and the Team Lead are confirmed by consent — by what was done, not by sympathy</li><li>Recognition for helping others is the main reason for honour</li><li>A contribution to the common fund that launches new teams</li></ul></div>
  </div>
</section>
<section>
  <div class="head">
    <h2>The team agreement</h2>
    <p class="lead">Signed on day one and re-read at every big retrospective.</p>
  </div>
  <ol class="contract">
    <li>We own the result together: if one is stuck, it is everyone’s task.</li>
    <li>About teammates we speak of what is valuable. About our own mistakes each speaks for themselves.</li>
    <li>At meetings we are fully present: no phones, no parallel work.</li>
    <li>We decide by consent: a decision passes if there are no reasoned objections.</li>
    <li>In a disagreement we first restate the other’s position until they agree.</li>
    <li>Helping others is visible and valued above personal achievements.</li>
    <li>Saying “this is hard for me” is normal and safe. Two people will pick up the tasks.</li>
    <li>Roles, including the Team Lead, are confirmed by the team every quarter.</li>
  </ol>
</section>
<section>
  <div class="head"><h2>The process improves itself</h2></div>
  <ol class="steps">
    <li><span class="num">1</span><div><h3>Team retro</h3><p class="when">must produce one change</p></div></li>
    <li><span class="num">2</span><div><h3>Checked by the cycle</h3><p class="when">did the team’s health indicators improve?</p></div></li>
    <li><span class="num">3</span><div><h3>Circle of teams</h3><p class="when">monthly: what worked for others</p></div></li>
    <li><span class="num">4</span><div><h3>Shared playbook</h3><p class="when">a new version for all teams</p></div></li>
  </ol>
  <div class="metrics">
    <div><b>Learning speed</b><span>hypotheses tested with clients per week</span></div>
    <div><b>Reliability</b><span>share of promises kept</span></div>
    <div><b>Safety</b><span>a short survey once per cycle</span></div>
    <div><b>Equal voice</b><span>how evenly people speak in meetings</span></div>
  </div>
</section>'''}

INVESTORS = {
'ru': '''<header class="hero small">
  <div class="stack">
    <p class="eyebrow">Инвесторам</p>
    <h1>Сначала участие. Деньги — после доказательств</h1>
    <p class="lead">Мы не просим вкладывать в идею. Мы зовём войти рано — и вложить, когда пилот покажет результат. Мы находим задачу, за которую заказчик готов платить, собираем под неё команду из людей, проверенных делом, и показываем инвестору не питч, а паспорт команды с первым клиентом.</p>
  </div>
</header>
<section>
  <div class="head"><h2>Путь инвестора</h2></div>
  <ol class="ladder">
    <li><span class="num">0</span><div><h3>Наставник и жюри</h3><p class="when">сейчас, до пилота</p><p>Ведёте команду, судите демо-день, даёте мягкое обещание «если будет X — вложу Y». Получаете самый ранний взгляд на команды — без денег и без риска.</p></div></li>
    <li><span class="num">1</span><div><h3>Клуб ангелов</h3><p class="when">после пилота</p><p>Небольшой чек вместе с 5–10 ангелами. Право первого взгляда и соинвестирования в каждую команду.</p></div></li>
    <li><span class="num">2</span><div><h3>Фонд и партнёры</h3><p class="when">масштаб</p><p>Участие в фонде рядом с программами Дубая и impact-инвесторами. Портфель команд с доказанной совместной работой и реальными клиентами.</p></div></li>
  </ol>
</section>
<section>
  <div class="head"><h2>Что получает инвестор</h2></div>
  <ul class="prin plain">
    <li><b>Поток проверенных команд</b><span>Команды приходят с паспортом и первым клиентом — не нужно искать сделки.</span></li>
    <li><b>Сниженный риск</b><span>Команда уже работала вместе, спрос подтверждён заказчиком — два главных риска закрыты до чека.</span></li>
    <li><b>Данные</b><span>С каждым циклом видно, какие сигналы предсказывают сильную команду.</span></li>
  </ul>
</section>
<section>
  <div class="head"><h2>Паспорт команды</h2><p class="lead">Пример того, что видит инвестор.</p></div>
  <div class="passport">
    <div><span>Заказчик</span><b>письмо о намерениях ✓</b></div>
    <div><span>Совместные циклы</span><b>2 из 2 пройдены</b></div>
    <div><span>Team Lead</span><b>подтверждён командой</b></div>
    <div><span>Разговоры с клиентами</span><b>[число]</b></div>
    <div><span>Надёжность</span><b>доля выполненных обещаний</b></div>
    <div><span>Вклад</span><b>продукт · технологии · продажи</b></div>
  </div>
  <p class="more">Хотите стать одним из первых наставников? Напишите: <b>hello@amalor.ai</b></p>
</section>''',
'en': '''<header class="hero small">
  <div class="stack">
    <p class="eyebrow">Investors</p>
    <h1>Participation first. Money after proof</h1>
    <p class="lead">We do not ask you to invest in an idea. We invite you in early — and to invest once a pilot shows results. We find a problem a client will pay to solve, form a team of people proven in practice and show the investor not a pitch but a team passport with a first client.</p>
  </div>
</header>
<section>
  <div class="head"><h2>The investor path</h2></div>
  <ol class="ladder">
    <li><span class="num">0</span><div><h3>Mentor and jury</h3><p class="when">now, before the pilot</p><p>Guide a team, judge the demo day, give a soft commitment: “if X happens, I will invest Y”. You get the earliest look at teams — no money, no risk.</p></div></li>
    <li><span class="num">1</span><div><h3>Angel club</h3><p class="when">after the pilot</p><p>A small ticket together with 5–10 angels. First look and co-investment rights in every team.</p></div></li>
    <li><span class="num">2</span><div><h3>Fund and partners</h3><p class="when">at scale</p><p>A stake in a fund alongside Dubai programmes and impact investors. A portfolio of teams with proven collaboration and real clients.</p></div></li>
  </ol>
</section>
<section>
  <div class="head"><h2>What the investor gets</h2></div>
  <ul class="prin plain">
    <li><b>A flow of proven teams</b><span>Teams arrive with a passport and a first client — no deal hunting.</span></li>
    <li><b>Lower risk</b><span>The team has already worked together and demand is confirmed by a client — the two biggest risks are closed before the ticket.</span></li>
    <li><b>Data</b><span>Every cycle shows which signals predict a strong team.</span></li>
  </ul>
</section>
<section>
  <div class="head"><h2>Team passport</h2><p class="lead">An example of what an investor sees.</p></div>
  <div class="passport">
    <div><span>Client</span><b>letter of intent ✓</b></div>
    <div><span>Joint cycles</span><b>2 of 2 completed</b></div>
    <div><span>Team Lead</span><b>confirmed by the team</b></div>
    <div><span>Client conversations</span><b>[number]</b></div>
    <div><span>Reliability</span><b>share of promises kept</b></div>
    <div><span>Contribution</span><b>product · technology · sales</b></div>
  </div>
  <p class="more">Want to be one of the first mentors? Write to <b>hello@amalor.ai</b></p>
</section>'''}

BOOK = {
'ru': '''<section class="book">
  <img src="{R}assets/book-cover-ru.jpg" width="659" height="988" alt="Обложка книги «Команда последнего поколения. Как связка тростника»">
  <div class="stack">
    <p class="eyebrow">Книга · скоро</p>
    <h1>Команда последнего поколения</h1>
    <p class="sub">Как связка тростника</p>
    <p class="lead">Как вместе получить больше, чем в одиночку, — и делать то, что нужно миру. Книга о том, как небольшая команда выбирает задачи, самоорганизуется и растёт — от первого заказа до сети команд.</p>
    <p class="when">Книга готовится к выходу. Оставьте анкету участника — пришлём, когда выйдет.</p>
    <div><a class="btn" href="{L}members/#join">Записаться</a></div>
  </div>
</section>''',
'en': '''<section class="book">
  <img src="{R}assets/book-cover-en.jpg" width="659" height="988" alt="Cover of the book “Last Generation Team. Like a bundle of reeds”">
  <div class="stack">
    <p class="eyebrow">Book · coming soon</p>
    <h1>Last Generation Team</h1>
    <p class="sub">Like a bundle of reeds</p>
    <p class="lead">How to achieve more together than alone — and do what the world needs. A book about how a small team chooses its tasks, organises itself and grows — from the first order to a network of teams.</p>
    <p class="when">The book is in preparation. Sign up as a member and we will let you know when it is out.</p>
    <div><a class="btn" href="{L}members/#join">Sign up</a></div>
  </div>
</section>'''}

EXTRA_CSS = '''
/* multi-page additions */
.menu{display:flex;flex-wrap:wrap;gap:4px 16px;padding-block:0 14px}
.menu a{color:#C9E4E2;text-decoration:none;font-size:14px;font-weight:500;padding:4px 0;border-bottom:2px solid transparent}
.menu a:hover,.menu a[aria-current]{color:#FFFFFF;border-bottom-color:#E2BF74}
.brandbar{flex-wrap:wrap}
.brandbar .menu{flex-basis:100%}
.hero.small{padding-block:48px 24px}
.hero.small h1{font-size:clamp(30px,5vw,46px)}
.more{margin-top:20px;font-weight:600}
.ladder{list-style:none;margin:8px 0 0;padding:0;display:grid;gap:12px}
.ladder li{display:grid;grid-template-columns:40px 1fr;gap:14px;padding:16px;border:1px solid var(--line);border-radius:12px;background:var(--surface)}
.ladder li:nth-child(2){margin-left:24px}.ladder li:nth-child(3){margin-left:48px}.ladder li:nth-child(4){margin-left:72px}
@media (max-width:560px){.ladder li{margin-left:0!important}}
.ladder p:not(.when){margin-top:6px;color:var(--muted);font-size:15px}
.rule{margin-top:16px;border-left:3px solid var(--gold);padding:10px 14px;background:var(--gold-soft);border-radius:0 8px 8px 0;font-size:15px}
.week{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px}
.week>div{padding:16px;border:1px solid var(--line);border-radius:12px;background:var(--surface)}
.week h3{margin:4px 0 6px}.week p:not(.when){color:var(--muted);font-size:15px}
.cycle{display:flex;flex-wrap:wrap;gap:6px}
.cycle span{flex:1 1 80px;text-align:center;padding:10px 6px;border-radius:8px;background:var(--teal-soft);color:var(--brand);font-size:14px;font-weight:600}
.cycle .retro{flex-basis:130px;background:var(--gold-soft);color:var(--gold)}
.cycle .pause{flex-basis:130px;background:transparent;border:1px dashed var(--line);color:var(--muted)}
.contract{margin:8px 0 0;padding-left:22px;display:grid;gap:10px}
.contract li::marker{color:var(--gold);font-weight:700}
.metrics{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:10px;margin-top:20px}
.metrics div{display:flex;flex-direction:column;padding:12px;border-radius:10px;background:var(--gold-soft)}
.metrics span{font-size:14px;color:var(--muted)}
.bar .b-guide{min-width:66px;flex-shrink:0;justify-content:center;padding-left:6px;padding-right:6px}
.cards3.two{grid-template-columns:repeat(2,minmax(0,1fr))}@media (max-width:700px){.cards3.two{grid-template-columns:1fr}}.cards3 .card.us{border-color:#D9B66A;background:#FBF3E2}.cards3 .card .ticks{margin:8px 0 0}
.prin.four{grid-template-columns:repeat(4,minmax(0,1fr))}@media (max-width:860px){.prin.four{grid-template-columns:repeat(2,minmax(0,1fr))}}@media (max-width:560px){.prin.four{grid-template-columns:1fr}}
.prin.plain li{background:var(--surface)}
.passport{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px;padding:18px;border:1px solid var(--line);border-radius:14px;background:var(--surface)}
.passport div{display:flex;flex-direction:column}
.passport span{font-size:13px;color:var(--muted)}
.book{display:grid;grid-template-columns:minmax(0,300px) 1fr;gap:36px;align-items:center;border-top:0}
.book img{width:100%;height:auto;border-radius:6px;box-shadow:0 18px 40px rgba(8,60,58,.25)}
@media (max-width:640px){.book{grid-template-columns:1fr}.book img{max-width:260px}}
footer .menu{padding:0}
footer .fl{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;align-items:flex-start}
'''

# ---- product path: a client's task can become a product with co-owners ----
PRODUCT_HOME = {
'ru': '''<section id="product">
  <div class="head">
    <h2>От задачи — к продукту</h2>
    <p class="lead">Иногда задача одной компании — это задача целой отрасли. Тогда решение становится продуктом, а у продукта появляются совладельцы: команда, которая его создала, и заказчик, который его вырастил.</p>
  </div>
  <ol class="flow">
    <li><b>Задача</b><span>одного заказчика</span></li>
    <li><b>Решение</b><span>по этапам, с приёмкой</span></li>
    <li><b>Нужно многим</b><span>проверяем у других компаний</span></li>
    <li><b>Продукт</b><span>лицензии для отрасли</span></li>
  </ol>
  <div class="owners">
    <div><b>Команда</b><span>доля за создание, внутри поровну</span></div>
    <div><b>Заказчик-партнёр</b><span>доля и бесплатная лицензия для себя</span></div>
    <div><b>Организатор</b><span>доля за сборку и запуск</span></div>
    <div><b>Инвесторы</b><span>входят, когда продукт доказал спрос</span></div>
  </div>
  <p class="more"><a href="{L}clients/#product-client">Для заказчиков →</a> · <a href="{L}investors/">Для инвесторов →</a></p>
</section>''',
'en': '''<section id="product">
  <div class="head">
    <h2>From a task to a product</h2>
    <p class="lead">Sometimes one company’s problem is a whole industry’s problem. Then the solution becomes a product — and the product gets co-owners: the team that built it and the client who helped it grow.</p>
  </div>
  <ol class="flow">
    <li><b>Task</b><span>of one client</span></li>
    <li><b>Solution</b><span>in stages, with acceptance</span></li>
    <li><b>Needed by many</b><span>validated with other companies</span></li>
    <li><b>Product</b><span>licences for the industry</span></li>
  </ol>
  <div class="owners">
    <div><b>Team</b><span>a share for building it, split equally inside</span></div>
    <div><b>Partner client</b><span>a share and a free licence for its own use</span></div>
    <div><b>Organiser</b><span>a share for assembling and launching</span></div>
    <div><b>Investors</b><span>join once the product has proven demand</span></div>
  </div>
  <p class="more"><a href="{L}clients/#product-client">For clients →</a> · <a href="{L}investors/">For investors →</a></p>
</section>'''}

PRODUCT_CLIENT = {
'ru': '''<section id="product-client">
  <div class="head">
    <h2>Ваш кейс может стать продуктом</h2>
    <p class="lead">Вы решаете свою задачу — и можете зарабатывать на том, что она нужна другим. Если после решения видно, что та же боль есть у других компаний, вы выбираете, как дальше.</p>
  </div>
  <div class="tbl"><table>
    <thead><tr><th></th><th>Обычный заказ</th><th class="us">Заказчик-партнёр</th></tr></thead>
    <tbody>
      <tr><td>Что получаете</td><td>готовое решение для своей компании</td><td class="us">решение для себя и долю в продукте для других</td></tr>
      <tr><td>Права</td><td>решение ваше, используете как хотите</td><td class="us">бессрочная бесплатная лицензия для своей компании и доля от лицензий для других</td></tr>
      <tr><td>Что вкладываете</td><td>оплату этапов</td><td class="us">оплату этапов, знание отрасли, участие в доработке и рекомендации как первый клиент</td></tr>
      <tr><td>Риск</td><td>—</td><td class="us">если продукт не вырастет, у вас всё равно остаётся работающее решение</td></tr>
    </tbody>
  </table></div>
  <p class="when" style="margin-top:12px">Размер доли зависит от вклада и записывается в договоре до начала работы над продуктом.</p>
</section>''',
'en': '''<section id="product-client">
  <div class="head">
    <h2>Your case can become a product</h2>
    <p class="lead">You solve your own problem — and can earn from the fact that others need it too. If, once it is solved, other companies clearly have the same pain, you choose what happens next.</p>
  </div>
  <div class="tbl"><table>
    <thead><tr><th></th><th>Standard order</th><th class="us">Partner client</th></tr></thead>
    <tbody>
      <tr><td>What you get</td><td>a working solution for your company</td><td class="us">a solution for yourself and a share in the product for others</td></tr>
      <tr><td>Rights</td><td>the solution is yours to use as you wish</td><td class="us">a perpetual free licence for your company and a share of licence revenue from others</td></tr>
      <tr><td>What you contribute</td><td>payment per stage</td><td class="us">payment per stage, industry knowledge, help refining it, and references as the first client</td></tr>
      <tr><td>Risk</td><td>—</td><td class="us">if the product does not grow, you still keep a working solution</td></tr>
    </tbody>
  </table></div>
  <p class="when" style="margin-top:12px">The size of the share depends on contribution and is written into the contract before work on the product starts.</p>
</section>'''}

PRODUCT_MEMBER = {
'ru': '<p class="more"><a href="{L}#product">Как проект вырастает в продукт с совладельцами →</a></p>',
'en': '<p class="more"><a href="{L}#product">How a project grows into a product with co-owners →</a></p>'}

PIPELINE = {
'ru': '''<section>
  <div class="head">
    <h2>Сначала спрос. Потом люди. Деньги — последними</h2>
    <p class="lead">Первый пилот впереди. Сейчас мы зовём наставников, которые хотят увидеть команды с самого начала.</p>
  </div>
  <ol class="steps">
    <li><span class="num">1</span><div><h3>Поиск спроса</h3><p class="when">задачи от заказчиков и участников, тендеры, жалобы клиентов, новые правила</p></div></li>
    <li><span class="num">2</span><div><h3>Проверка спроса</h3><p class="when">10–20 разговоров и заказчик, готовый платить за пилот</p></div></li>
    <li><span class="num">3</span><div><h3>Пробная работа</h3><p class="when">1–2 недели в смешанных парах на реальной задаче</p></div></li>
    <li><span class="num">4</span><div><h3>Сборка команды</h3><p class="when">ядро 3–5 человек, специалисты из круга под задачу, доход поровну, договор команды, Team Lead по согласию</p></div></li>
    <li><span class="num">5</span><div><h3>Решение с заказчиком</h3><p class="when">первые пользователи и первые деньги — до раунда</p></div></li>
    <li><span class="num">6</span><div><h3>Паспорт команды</h3><p class="when">история совместной работы, роли, разговоры с клиентами, показатели</p></div></li>
    <li><span class="num">7</span><div><h3>Демо инвесторам</h3><p class="when">команда, которая уже доказала, что работает, и заказчик-партнёр рядом</p></div></li>
  </ol>
  <p class="rule"><b>Нет заказчика — команду не собираем.</b> Не сработались — пересобираем из того же круга.</p>
</section>''',
'en': '''<section>
  <div class="head">
    <h2>Demand first. Then people. Money last</h2>
    <p class="lead">The first pilot is ahead. Right now we invite mentors who want to see the teams from the very beginning.</p>
  </div>
  <ol class="steps">
    <li><span class="num">1</span><div><h3>Finding demand</h3><p class="when">tasks from clients and members, tenders, customer complaints, new regulations</p></div></li>
    <li><span class="num">2</span><div><h3>Validating demand</h3><p class="when">10–20 conversations and a client ready to pay for a pilot</p></div></li>
    <li><span class="num">3</span><div><h3>Trial work</h3><p class="when">1–2 weeks in mixed pairs on a real task</p></div></li>
    <li><span class="num">4</span><div><h3>Forming the team</h3><p class="when">a core of 3–5 people, specialists from the circle as needed, income shared equally, a team agreement, a Team Lead by consent</p></div></li>
    <li><span class="num">5</span><div><h3>Solution with the client</h3><p class="when">first users and first revenue — before any round</p></div></li>
    <li><span class="num">6</span><div><h3>Team passport</h3><p class="when">history of working together, roles, client conversations, indicators</p></div></li>
    <li><span class="num">7</span><div><h3>Investor demo</h3><p class="when">a team that has already proven it works, with a partner client alongside</p></div></li>
  </ol>
  <p class="rule"><b>No client — no team.</b> If people do not click, we regroup from the same circle.</p>
</section>'''}

EXTRA_CSS += '''
.flow{list-style:none;margin:8px 0 0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;counter-reset:f}
.flow li{position:relative;padding:14px;border-radius:12px;background:var(--teal-soft);display:flex;flex-direction:column;gap:2px}
.flow li:last-child{background:var(--gold-soft)}
.flow b{font-family:var(--display)}.flow span{font-size:14px;color:var(--muted)}
.owners{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:10px;margin-top:14px}
.owners div{padding:12px 14px;border:1px solid var(--line);border-radius:12px;background:var(--surface);display:flex;flex-direction:column}
.owners span{font-size:14px;color:var(--muted)}
.tbl{overflow-x:auto}
table{border-collapse:collapse;width:100%;min-width:520px;font-size:15px}
th,td{text-align:left;padding:12px 14px;border-bottom:1px solid var(--line);vertical-align:top}
thead th{font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);font-weight:600}
td:first-child{color:var(--muted)}
td.us,th.us{background:var(--gold-soft)}
th.us{color:var(--gold)}
'''

# ---- home hero in the colours of the book cover ----
NET_SVG = '''<svg class="net" viewBox="150 160 500 520" aria-hidden="true"><defs><linearGradient id="hg" x1="150" y1="160" x2="650" y2="680" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#F7E7B0"/><stop offset="0.32" stop-color="#E2BF74"/><stop offset="0.64" stop-color="#B98A34"/><stop offset="1" stop-color="#EDCD82"/></linearGradient></defs><g fill="none" stroke="url(#hg)" stroke-width="1.5" stroke-opacity="0.6" stroke-linejoin="round"><polygon points="400,190 535,234 619,349 619,491 535,606 400,650 265,606 181,491 181,349 265,234"/><polygon points="400,190 619,349 535,606 265,606 181,349"/><polygon points="535,234 619,491 400,650 181,491 265,234"/><polygon points="400,190 619,491 265,606 181,349 535,234 400,650 181,491 619,349 535,606 265,234"/><polygon points="400,190 535,606 181,349 619,349 265,606"/><polygon points="535,234 400,650 265,234 619,491 181,491"/><line x1="400" y1="190" x2="400" y2="650"/><line x1="535" y1="234" x2="265" y2="606"/><line x1="619" y1="349" x2="181" y2="491"/><line x1="619" y1="491" x2="181" y2="349"/><line x1="535" y1="606" x2="265" y2="234"/></g><g fill="url(#hg)"><circle cx="400" cy="190" r="15"/><circle cx="535" cy="234" r="15"/><circle cx="619" cy="349" r="15"/><circle cx="619" cy="491" r="15"/><circle cx="535" cy="606" r="15"/><circle cx="400" cy="650" r="15"/><circle cx="265" cy="606" r="15"/><circle cx="181" cy="491" r="15"/><circle cx="181" cy="349" r="15"/><circle cx="265" cy="234" r="15"/></g><circle cx="400" cy="420" r="5" fill="#F7E7B0"/></svg>'''

HERO_HOME = {
'ru': dict(quote='«Связку тростника не сломать разом, а по одной тростинке её переломит и ребёнок»',
           title='Команда последнего поколения', sub='Как связка тростника',
           tag='Как вместе получить больше, чем в одиночку, — и делать то, что нужно миру',
           lead='Небольшие команды специалистов решают задачи, которые нужны людям и за которые готовы платить. Работаем по этапам, отвечаем друг за друга, а лучшие решения выращиваем в продукты — вместе с заказчиками.',
           b1=('Есть задача', 'clients/'), b2=('Хочу в команду', 'members/'),
           ex='Пример: проект на $100 000', bar=[('Команде 80%',80),('Гарантия 20%',20)], legend='80% — команде · 20% — гарантия AMALOR · проводнику — 5% первого проекта',
           facts=[('$80 000', 'получает команда, которая сделала работу'), ('$20 000', 'каждому в команде из четырёх — поровну'), ('$20 000', 'гарантия AMALOR — столько же, сколько каждому: договор, подбор и замена людей, метод, качество'), ('$0', 'заказчик платит за этап, который не принял')]),
'en': dict(quote='“A bundle of reeds cannot be broken at once, yet a child can break the reeds one by one”',
           title='Last Generation Team', sub='Like a bundle of reeds',
           tag='How to achieve more together than alone — and do what the world needs',
           lead='Small teams of specialists solve problems people need solved and will pay for. We work in stages, answer for each other, and grow the best solutions into products — together with our clients.',
           b1=('I have a task', 'clients/'), b2=('Join a team', 'members/'),
           ex='Example: a $100,000 project', bar=[('Team 80%',80),('Guarantee 20%',20)], legend='80% to the team · 20% AMALOR guarantee · referrer: 5% of the first project',
           facts=[('$80,000', 'goes to the team that did the work'), ('$20,000', 'to each member of a team of four — equally'), ('$20,000', 'the AMALOR guarantee — the same as each member: contract, selecting and replacing people, method, quality'), ('$0', 'the client pays for a stage they did not accept')]),
}

def hero_home(lang):
    h = HERO_HOME[lang]
    facts = ''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in h['facts'])
    bar = ''.join(f'<div style="flex:{w}">{t}</div>' for t, w in h['bar'])
    return f'''<header class="hero-band">
  <div class="hb-text">
    <p class="hb-quote">{h['quote']}</p>
    <h1>{h['title']}</h1>
    <p class="hb-sub">{h['sub']}</p>
    <p class="hb-tag">{h['tag']}</p>
    <p class="hb-lead">{h['lead']}</p>
    <div class="hb-cta"><a class="btn" href="{{L}}{h['b1'][1]}">{h['b1'][0]}</a><a class="btn ghost" href="{{L}}{h['b2'][1]}">{h['b2'][0]}</a></div>
  </div>
  <div class="hb-art">{NET_SVG}</div>
  <div class="hb-money"><p class="hb-ex">{h['ex']}</p><div class="hb-bar">{bar}</div><p class="hb-legend">{h['legend']}</p><ul class="hb-facts">{facts}</ul></div>
</header>'''

EXTRA_CSS += '''
/* home hero: continues the green header band, like the book cover */
.hero-band{position:relative;display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:24px 40px;align-items:center;
  padding-block:24px 40px;color:#FFFFFF;background:radial-gradient(ellipse 40% 55% at 70% 48%,rgba(27,156,147,.42),rgba(27,156,147,0) 70%),#083C3A;box-shadow:0 0 0 100vmax #083C3A;clip-path:inset(0 -100vmax)}

.hb-text{position:relative;display:flex;flex-direction:column;gap:14px;min-width:0}
.hb-quote{font-style:italic;font-size:15px;color:#9DC3BF;max-width:46ch}
.hero-band h1{color:#FFFFFF;font-size:clamp(38px,6.4vw,66px);line-height:1.02;letter-spacing:-.025em}
.hb-sub{font-size:clamp(20px,2.6vw,26px);font-weight:600;color:#ECCF90}
.hb-tag{font-size:clamp(17px,2vw,20px);color:#C9E4E2;max-width:40ch}
.hb-lead{font-size:16px;color:#A9CBC7;max-width:52ch}
.hb-cta{display:flex;flex-wrap:wrap;gap:12px;margin-top:6px}
.btn.ghost{background:transparent;color:#FFFFFF;border:1px solid rgba(236,207,144,.55);box-shadow:none}
.hb-art{position:relative;display:flex;justify-content:center}
.hb-art .net{width:100%;max-width:420px;height:auto}
.hb-money{grid-column:1/-1;margin-top:8px;padding-top:20px;border-top:1px solid rgba(201,228,226,.18);display:flex;flex-direction:column;gap:14px}
.hb-ex{font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:#9DC3BF;margin:0}
.hb-bar{display:flex;gap:3px;height:40px;border-radius:10px;overflow:hidden;font-size:13px;font-weight:700}
.hb-bar div{display:flex;align-items:center;padding:0 12px;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;background:rgba(201,228,226,.14);color:#C9E4E2}
.hb-bar div:first-child{background:linear-gradient(135deg,#F7E7B0,#E2BF74,#C99A45,#EDCD82);color:#0B2F2D}
.hb-facts{list-style:none;margin:0;padding:0;
  display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px 28px}
.hb-facts li{display:flex;flex-direction:column;gap:2px}
.hb-legend{font-size:14px;color:#A9CBC7;margin:-4px 0 6px}
.hb-facts b{white-space:nowrap;font-family:var(--display);font-size:clamp(22px,2.4vw,32px);color:#ECCF90;line-height:1.1}
.hb-facts span{font-size:14px;color:#A9CBC7}
@media (max-width:760px){.hero-band{grid-template-columns:minmax(0,1fr)}.hero-band h1{font-size:34px}.hb-bar{font-size:11px}.hb-bar div{padding:0 8px}.hb-art{order:-1}.hb-art .net{max-width:220px}.hb-facts{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (prefers-reduced-motion:no-preference){.hb-art .net{animation:hbspin 120s linear infinite}@keyframes hbspin{to{transform:rotate(360deg)}}}
.doors.below{margin-top:0}
section.home-doors{padding-block:40px 20px;border-top:0}
'''

# ---- hero v3: the circles (team in the centre) + path problem → startup + manifesto link ----
CIRCLES_TXT = {
 'ru': dict(core='Связь', team='команда · делает работу', purpose='ради кого работа', support='круг поддержки',
            motto='«Все отвечают друг за друга»', motto_src='',
            path=['Проблема, важная людям', 'Пилот', 'Проект', 'Стартап'],
            path_note='В стартапе у каждого участника круга есть доля по вкладу. Больше всего — у тех, кто сделал основную работу.',
            man='Манифест', links='связи между кругами'),
 'en': dict(core='Bond', team='the team · does the work', purpose='who the work is for', support='circle of support',
            motto='“Everyone is responsible for one another”', motto_src='',
            path=['A problem people care about', 'Pilot', 'Project', 'Startup'],
            path_note='In the startup every member of the circle holds a share according to their contribution. The largest shares go to those who did the core work.',
            man='Manifesto (RU)', links='links between the circles'),
}

def circles_svg(lang):
    t = CIRCLES_TXT[lang]
    import math
    def ring_dots(r, n, size, phase=0):
        return ''.join(f'<circle cx="{300 + r*math.cos(2*math.pi*i/n + phase):.1f}" cy="{300 + r*math.sin(2*math.pi*i/n + phase):.1f}" r="{size}"/>' for i in range(n))
    team = [(300 + 112*math.cos(-math.pi/2 + 2*math.pi*i/5), 300 + 112*math.sin(-math.pi/2 + 2*math.pi*i/5)) for i in range(5)]
    pent = ' '.join(f'{x:.1f},{y:.1f}' for x, y in team)
    star = ' '.join(f'{team[(2*i) % 5][0]:.1f},{team[(2*i) % 5][1]:.1f}' for i in range(5))
    spokes = ''.join(f'<line x1="300" y1="300" x2="{x:.1f}" y2="{y:.1f}"/>' for x, y in team)
    nodes = ''.join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="13"/>' for x, y in team)
    return f'''<svg class="circles" viewBox="0 0 600 600" role="img" aria-label="{t['core']}: {t['team']}, {t['purpose']}, {t['support']}">
<defs>
 <linearGradient id="cgold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F7E7B0"/><stop offset=".35" stop-color="#E2BF74"/><stop offset=".7" stop-color="#C99A45"/><stop offset="1" stop-color="#EDCD82"/></linearGradient>
 <radialGradient id="cglow"><stop offset="0" stop-color="#FFF4D2" stop-opacity=".95"/><stop offset=".45" stop-color="#ECCF90" stop-opacity=".55"/><stop offset="1" stop-color="#ECCF90" stop-opacity="0"/></radialGradient>
 <path id="arc-out" d="M 68 300 A 232 232 0 0 1 532 300"/>
 <path id="arc-mid" d="M 146 300 A 154 154 0 0 1 454 300"/>
 <path id="arc-team" d="M 146 300 A 154 154 0 0 0 454 300"/>
</defs>
<circle cx="300" cy="300" r="270" fill="rgba(201,228,226,.04)" stroke="#ECCF90" stroke-opacity=".28" stroke-dasharray="2 6"/>
<circle cx="300" cy="300" r="190" fill="rgba(201,228,226,.05)" stroke="#ECCF90" stroke-opacity=".4"/>
<g class="orb orb-out" fill="#C9E4E2" fill-opacity=".55">{ring_dots(270, 12, 4.5)}</g>
<g class="orb orb-mid" fill="#ECCF90" fill-opacity=".8">{ring_dots(190, 3, 7, 0.5)}</g>
<text class="ring-label"><textPath href="#arc-out" startOffset="50%" text-anchor="middle">{t['support']}</textPath></text>
<text class="ring-label"><textPath href="#arc-mid" startOffset="50%" text-anchor="middle">{t['purpose']}</textPath></text>
<circle class="core-glow" cx="300" cy="300" r="150" fill="url(#cglow)"/>
<g fill="none" stroke="url(#cgold)" stroke-width="1.6" stroke-linejoin="round"><polygon points="{pent}"/><polygon points="{star}" stroke-opacity=".55"/><g stroke-opacity=".7">{spokes}</g></g>
<g fill="url(#cgold)">{nodes}</g>
<circle cx="300" cy="300" r="52" fill="#0B3F3C" stroke="url(#cgold)" stroke-width="2"/>
<text class="core-word" x="300" y="308" text-anchor="middle">{t['core']}</text>
<text class="ring-label team"><textPath href="#arc-team" startOffset="50%" text-anchor="middle">{t['team']}</textPath></text>
</svg>'''

def hero_home(lang):
    h = HERO_HOME[lang]; t = CIRCLES_TXT[lang]
    facts = ''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in h['facts'])
    bar = ''.join(f'<div style="flex:{w}">{x}</div>' for x, w in h['bar'])
    steps = '<span class="arr" aria-hidden="true">→</span>'.join(f'<li><i>{i+1}</i>{s}</li>' for i, s in enumerate(t['path']))
    return f'''<header class="hero-band">
  <div class="hb-text">
    <p class="hb-quote">{h['quote']}</p>
    <h1>{h['title']}</h1>
    <p class="hb-sub">{h['sub']}</p>
    <p class="hb-tag">{h['tag']}</p>
    <p class="hb-lead">{h['lead']}</p>
    <div class="hb-cta"><a class="btn" href="{{L}}{h['b1'][1]}">{h['b1'][0]}</a><a class="btn ghost" href="{{L}}{h['b2'][1]}">{h['b2'][0]}</a><a class="btn manifest" href="{{L}}manifest/"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M5 4h10a3 3 0 0 1 3 3v13H8a3 3 0 0 1-3-3z M8 20a3 3 0 0 1-3-3 M9 9h6 M9 13h6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>{t['man']}</a></div>
  </div>
  <figure class="hb-art">{circles_svg(lang)}<figcaption><b>{t['motto']}</b>{('<span>'+t['motto_src']+'</span>') if t['motto_src'] else ''}</figcaption></figure>
  <div class="hb-path"><ol>{steps}</ol><p>{t['path_note']}</p></div>
  <div class="hb-money"><p class="hb-ex">{h['ex']}</p><div class="hb-bar">{bar}</div><p class="hb-legend">{h['legend']}</p><ul class="hb-facts">{facts}</ul></div>
</header>'''

EXTRA_CSS += '''
.hb-art{margin:0;flex-direction:column;align-items:center;gap:10px}
.hb-art .circles{width:100%;max-width:560px;height:auto;overflow:visible}
.circles .ring-label{font-size:16px;letter-spacing:.16em;text-transform:uppercase;fill:#9DC3BF;font-weight:600}
.circles .ring-label.team{fill:#ECCF90;font-size:15px;letter-spacing:.12em}
.circles .core-word{font-family:var(--display);font-size:24px;font-weight:700;fill:#F7E7B0}
.hb-art figcaption{display:flex;flex-direction:column;align-items:center;text-align:center;gap:2px}
.hb-art figcaption b{font-size:17px;color:#ECCF90;font-weight:600}
.hb-art figcaption span{font-size:13px;color:#9DC3BF}
.hb-man{display:inline-flex;align-items:center;gap:8px;color:#ECCF90;font-weight:600;text-decoration:none;border-bottom:1px solid rgba(236,207,144,.4);align-self:flex-start;padding-bottom:2px}
.hb-man:hover{border-bottom-color:#ECCF90}
.hb-path{grid-column:1/-1;display:flex;flex-direction:column;gap:10px;padding-top:20px;border-top:1px solid rgba(201,228,226,.18)}
.hb-path ol{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;align-items:center;gap:10px}
.hb-path li{display:flex;align-items:center;gap:10px;padding:10px 16px;border-radius:999px;border:1px solid rgba(236,207,144,.35);background:rgba(201,228,226,.06);color:#FFFFFF;font-weight:600}
.hb-path li:last-of-type{background:linear-gradient(135deg,#F7E7B0,#E2BF74,#C99A45,#EDCD82);color:#0B2F2D;border-color:transparent}
.hb-path li i{font-style:normal;font-size:12px;width:22px;height:22px;border-radius:50%;display:grid;place-items:center;background:rgba(236,207,144,.18);color:#ECCF90}
.hb-path li:last-of-type i{background:rgba(11,47,45,.15);color:#0B2F2D}
.hb-path .arr{color:#ECCF90;opacity:.7}
.hb-path p{margin:0;font-size:15px;color:#C9E4E2;max-width:70ch}
.hb-money{border-top:0;padding-top:4px}
@media (max-width:760px){.hb-art .circles{max-width:360px}.hb-path li{padding:8px 12px;font-size:14px}}
@media (prefers-reduced-motion:no-preference){
 .circles .orb{transform-box:view-box;transform-origin:300px 300px}
 .circles .orb-out{animation:orbspin 160s linear infinite}
 .circles .orb-mid{animation:orbspin 90s linear infinite reverse}
 .circles .core-glow{transform-box:view-box;transform-origin:300px 300px;animation:corepulse 5s ease-in-out infinite}
 @keyframes orbspin{to{transform:rotate(360deg)}}
 @keyframes corepulse{0%,100%{opacity:.75;transform:scale(.94)}50%{opacity:1;transform:scale(1.04)}}
}
'''

# ---- hero v4: a network sphere instead of flat circles ----
SPHERE_JS = r'''<script>
(function(){
var c=document.getElementById('sphere');if(!c||!c.getContext)return;var x=c.getContext('2d');
var still=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
function fib(n,R){var p=[],g=Math.PI*(3-Math.sqrt(5));for(var i=0;i<n;i++){var y=1-(i+.5)/n*2,r=Math.sqrt(1-y*y),t=g*i;p.push([Math.cos(t)*r*R,y*R,Math.sin(t)*r*R]);}return p;}
var S=[{n:10,R:.30,col:[247,231,176],size:5.2,line:.75},{n:26,R:.62,col:[236,207,144],size:3.2,line:.38},{n:64,R:.95,col:[157,195,191],size:2.2,line:.22},{col:[111,183,230],line:.7}];
var P=[],E=[];S.forEach(function(s,k){fib(s.n,s.R).forEach(function(q){P.push({p:q,k:k});});});
function d2(a,b){var dx=a.p[0]-b.p[0],dy=a.p[1]-b.p[1],dz=a.p[2]-b.p[2];return dx*dx+dy*dy+dz*dz;}
function near(i,k,m){return P.map(function(q,j){return [j,q]}).filter(function(e){return e[1].k===k&&e[0]!==i}).sort(function(a,b){return d2(P[i],a[1])-d2(P[i],b[1])}).slice(0,m).map(function(e){return e[0]});}
var seen={};function add(i,j,k){var key=i<j?i+'-'+j:j+'-'+i;if(seen[key])return;seen[key]=1;E.push([i,j,k]);}
P.forEach(function(q,i){if(q.k===0){P.forEach(function(r,j){if(r.k===0&&j>i)add(i,j,0);});}
 else{near(i,q.k,3).forEach(function(j){add(i,j,q.k);});near(i,q.k-1,1).forEach(function(j){add(i,j,3);});}});
var a=0.6,tilt=-.38,W=0,H=0,dpr=1;
function size(){var r=c.getBoundingClientRect();dpr=Math.min(window.devicePixelRatio||1,2);W=r.width;H=r.width;c.width=W*dpr;c.height=H*dpr;c.style.height=H+'px';x.setTransform(dpr,0,0,dpr,0,0);}
function proj(q){var ca=Math.cos(a),sa=Math.sin(a),ct=Math.cos(tilt),st=Math.sin(tilt);var X=q[0]*ca+q[2]*sa,Z=-q[0]*sa+q[2]*ca,Y=q[1]*ct-Z*st;Z=q[1]*st+Z*ct;var f=4/(4+Z),s=W*.355;return [W/2+X*s*f,H/2+Y*s*f,Z,f];}
function frame(){x.clearRect(0,0,W,H);
 var g=x.createRadialGradient(W/2,H/2,0,W/2,H/2,W*.32);g.addColorStop(0,'rgba(255,244,210,.55)');g.addColorStop(.5,'rgba(236,207,144,.16)');g.addColorStop(1,'rgba(236,207,144,0)');x.fillStyle=g;x.fillRect(0,0,W,H);
 var Q=P.map(function(q){return proj(q.p)});
 E.forEach(function(e){var A=Q[e[0]],B=Q[e[1]],s=S[e[2]],dep=(2-(A[2]+B[2])/2)/2;x.strokeStyle='rgba('+s.col.join(',')+','+(s.line*(.35+.65*dep)).toFixed(3)+')';x.lineWidth=e[2]===0?1.3:.8;x.beginPath();x.moveTo(A[0],A[1]);x.lineTo(B[0],B[1]);x.stroke();});
 P.map(function(q,i){return [i,Q[i][2]]}).sort(function(m,n){return n[1]-m[1]}).forEach(function(o){var i=o[0],s=S[P[i].k],q=Q[i],dep=(1-q[2])/2;x.fillStyle='rgba('+s.col.join(',')+','+(.35+.65*dep).toFixed(3)+')';x.beginPath();x.arc(q[0],q[1],s.size*q[3]*(W/520),0,6.2832);x.fill();});
 x.fillStyle='rgba(255,248,225,.95)';x.beginPath();x.arc(W/2,H/2,4*(W/520),0,6.2832);x.fill();}
function loop(){a+=.0016;frame();if(!document.hidden)requestAnimationFrame(loop);else setTimeout(loop,500);}
size();frame();window.addEventListener('resize',function(){size();frame();});if(!still)requestAnimationFrame(loop);
})();
</script>'''

def circles_svg(lang):
    t = CIRCLES_TXT[lang]
    return (f'<canvas id="sphere" class="sphere" role="img" aria-label="{t["team"]}, {t["purpose"]}, {t["support"]}"></canvas>'
            f'<ul class="sphere-key"><li class="k0">{t["team"]}</li><li class="k1">{t["purpose"]}</li><li class="k2">{t["support"]}</li><li class="k3">{t.get("links","")}</li></ul>'
            + SPHERE_JS)

EXTRA_CSS += '''
.hb-art .sphere{display:block;width:100%;max-width:540px;aspect-ratio:1/1}
.sphere-key{list-style:none;margin:-6px 0 6px;padding:0;display:flex;flex-wrap:wrap;justify-content:center;gap:6px 18px;font-size:13px;color:#C9E4E2}
.sphere-key li{display:flex;align-items:center;gap:7px}
.sphere-key li::before{content:"";width:9px;height:9px;border-radius:50%}
.sphere-key .k0::before{background:#F7E7B0;box-shadow:0 0 8px #F7E7B0}
.sphere-key .k1::before{background:#ECCF90;opacity:.8}
.sphere-key .k2::before{background:#9DC3BF;opacity:.8}
@media (max-width:760px){.hb-art .sphere{max-width:340px}}
'''

EXTRA_CSS += '''
/* the blue thread: a thin sky-blue line around gold buttons, key numbers and charts */
:root{--thread:#6FB7E6}
.btn:not(.ghost){box-shadow:0 0 0 1.5px var(--thread),0 6px 20px rgba(201,154,69,.22)}
.bar,.hb-bar{box-shadow:0 0 0 1.5px var(--thread)}
.hb-facts li{border:1px solid rgba(111,183,230,.6);border-radius:14px;padding:14px 16px;min-width:0}
.hero-band .hb-facts b{font-size:clamp(20px,2.1vw,30px)}
.hb-path li:last-of-type{box-shadow:0 0 0 1.5px var(--thread)}
.hb-art figcaption b{border-bottom:1px solid rgba(111,183,230,.6);padding-bottom:4px}
.sphere-key .k3::before{background:#6FB7E6}
'''

EXTRA_CSS += '''
.btn.manifest{gap:10px;background:rgba(111,183,230,.1);color:#DDF0FB;border:1.5px solid var(--thread);box-shadow:none}
.btn.manifest:hover{background:rgba(111,183,230,.22)}
'''

# ---- team size: fixed core, flexible periphery ----
_SIZE = {'ru': ('Размер команды', 'Ядро — 3–5 человек', 'Они несут ответственность за результат, делят доход поровну и решают, кого принимать. Столько людей хорошо слышат друг друга и видят вклад каждого.', 'Специалисты под задачу', 'Когда нужен юрист, дизайнер или другой эксперт на 1–2 недели, его подключают из круга. Он получает оплату за свою часть и в ядро не входит.', 'Делимся, а не разрастаемся', 'Если проекту нужно больше пяти человек, команда делится на две и держит связь через тимлидов — вместо одного большого отдела.'), 'en': ('Team size', 'A core of 3–5 people', 'They are responsible for the result, share income equally and decide who joins. A group this size hears each other well and sees everyone’s contribution.', 'Specialists for the task', 'When a lawyer, designer or other expert is needed for 1–2 weeks, they join from the circle. They are paid for their part and do not join the core.', 'We split rather than sprawl', 'If a project needs more than five people, the team splits into two that stay connected through their leads — instead of one big department.')}
def _size_block(t):
    h,a1,b1,a2,b2,a3,b3=t
    return ('<section>\n  <div class="head"><h2>'+h+'</h2></div>\n  <div class="cards3"><div class="card"><h3>'+a1+'</h3><p>'+b1+'</p></div><div class="card"><h3>'+a2+'</h3><p>'+b2+'</p></div><div class="card"><h3>'+a3+'</h3><p>'+b3+'</p></div></div>\n</section>\n')
for _l, _t in _SIZE.items():
    TEAM[_l] = TEAM[_l].replace('</header>\n', '</header>\n' + _size_block(_t), 1)
EXTRA_CSS += """
.cards3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
.cards3 .card{background:#FFFDF8;border:1px solid #E4DAC4;border-radius:16px;padding:20px}
.cards3 h3{margin:0 0 8px;font-size:18px}.cards3 p{margin:0;color:#4A6563;font-size:15px}
@media (max-width:760px){.cards3{grid-template-columns:1fr}}
"""
