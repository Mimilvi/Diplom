"""Generates index.html (RU) and en.html (EN) from one template.
Content comes from the original repository github.com/Mimilvi/Diplom."""
from pathlib import Path

ICONS = {
    "cloud": '<path d="M7 18h10a4 4 0 000-8 6 6 0 00-11.6 1.5A3.5 3.5 0 007 18z"/><path d="M12 13v5M9.5 15.5L12 18l2.5-2.5"/>',
    "mic": '<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0014 0M12 18v3"/>',
    "eye": '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    "box": '<path d="M12 2l9 5v10l-9 5-9-5V7z"/><path d="M12 22V12M21 7l-9 5-9-5"/>',
    "home": '<path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>',
    "spark": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5L18 18M6 18l2.5-2.5M15.5 8.5L18 6"/>',
    "hand": '<circle cx="12" cy="5" r="2"/><path d="M12 7v6M8 21l4-8 4 8M7 10h10"/>',
    "android": '<path d="M6 11a6 6 0 0112 0z"/><path d="M8 4.5l1.3 2.2M16 4.5l-1.3 2.2"/><circle cx="10" cy="8.6" r=".5"/><circle cx="14" cy="8.6" r=".5"/><rect x="6" y="12.5" width="12" height="7.5" rx="1.5"/><path d="M4 13v5M20 13v5M10 20v2M14 20v2"/>',
    "apple": '<path d="M16 13c0-2.5 2-3.2 2-3.2A4.4 4.4 0 0014.5 8c-1.5 0-2 .8-2.9.8S9.9 8 8.6 8C6.5 8 4.5 9.8 4.5 13c0 3.5 2.6 8 4.5 8 1 0 1.4-.6 2.7-.6s1.6.6 2.7.6c1.4 0 2.8-2.4 3.4-4-2.3-1-1.8-4-1.8-4z"/><path d="M12.5 5.5C13 4 14.4 3 15.5 3c.2 1.5-.8 3.2-2.5 3.5"/>',
}

def icon(name):
    return f'<svg viewBox="0 0 24 24">{ICONS[name]}</svg>'

T = {
 "ru": dict(
  file="index.html", lang="ru", other_file="en.html", other_label="ENG",
  title="НОКТИС — Голосовая станция с ИИ на базе ESP32-S3-DevKitC-1",
  desc="Голосовая станция с искусственным интеллектом на базе микроконтроллера ESP32-S3-DevKitC-1: облачный и локальный режимы, тренды, применение и загрузка приложения.",
  logo="НОКТИС",
  nav=["Главная", "О проекте", "Тренды", "Применение", "Загрузить", "Контакты"],
  cta_nav="Загрузить", menu="Открыть меню",
  eyebrow="Дипломный проект · ESP32-S3-DevKitC-1",
  h1a="Голосовая станция", h1b="с искусственным интеллектом",
  hero_sub="Создание голосовой станции с ИИ на базе ESP32-S3-DevKitC-1 — это популярный и хорошо документированный проект. В зависимости от ваших целей, вы можете выбрать один из двух основных путей: облачный (мощный, но требующий интернета) или локальный (приватный и быстрый, но с ограничениями).",
  btn1="Загрузить приложение", btn2="Подробнее",
  chip1="Слушаю…", chip2b="ESP32-S3", chip2="Wi‑Fi · Bluetooth LE",
  stats=[("2", "Режима: облако и локально"), ("240", "МГц, двухъядерный CPU"), ("3 м", "Захват голоса"), ("100%", "Своими руками")],
  about_label="О проекте",
  about_h="Своя приватная", about_hg="голосовая станция",
  about_p="Голосовая станция с искусственным интеллектом на базе ESP32-S3-DevKitC-1 — это, по сути, недорогое, гибкое устройство для голосового взаимодействия, которое можно собрать своими руками. Его главная ценность в том, что он позволяет создавать приватные, кастомизируемые и локальные голосовые интерфейсы, не зависящие полностью от коммерческих экосистем вроде Alexa или Google.",
  checks=["Недорогое устройство, которое можно собрать своими руками", "Приватные и кастомизируемые голосовые интерфейсы", "Независимость от коммерческих экосистем вроде Alexa или Google"],
  badge="ESP32-S3", badge_t="Сердце<br>станции",
  trends_label="Направления развития", trends_h="Куда движутся", trends_hg="ИИ-устройства",
  trends_p="Развитие идет по нескольким ключевым направлениям, которые постепенно стирают границы между дешевыми DIY-устройствами и полноценными ИИ-продуктами.",
  trends=[
   ("cloud", "От облака к гибридным и локальным решениям", "Это самый значимый тренд. Первые DIY-проекты полагались на отправку аудио в облако для распознавания и генерации ответа. Сейчас акцент смещается в сторону локальной обработки. Цель — снизить задержку, зависимость от интернета и повысить приватность, обрабатывая простые команды (например, «включи свет») прямо на ESP32. Будущее за гибридными системами, которые используют мощь облачных LLM только для сложных запросов."),
   ("mic", "Качество аудио и распознавания речи", "DIY-проекты часто страдают от шума и плохого распознавания. Для решения этой проблемы появляются специализированные аппаратные решения. Например, ReSpeaker Lite использует отдельный аудиопроцессор XMOS для шумоподавления, эхоподавления и захвата голоса с расстояния до 3 метров. Интеграция таких модулей с ESP32-S3 — это прямой путь к созданию устройств, которые работают так же хорошо, как коммерческие колонки."),
   ("eye", "За пределами «просто ассистента»", "ESP32-S3 способен не только на голос. Благодаря поддержке камер и дисплеев, он может стать основой для мультимодальных устройств, которые видят и показывают. В проекте с роботом-космонавтом использовался OLED-экран для отображения анимации в зависимости от режима работы. В будущем такие устройства смогут не только слышать, но и видеть (например, распознавать лица или жесты), и управлять физическими действиями (роботами, манипуляторами)."),
   ("box", "Простая разработка и низкий порог входа", "Появляется все больше «коробочных» решений и платформ, которые скрывают сложность программирования. ESP Private Agents позволяет генерировать прошивку прямо из веб-интерфейса. Проекты вроде ElatoAI предоставляют готовую серверную инфраструктуру для подключения к десяткам голосовых моделей. Это означает, что в будущем создание собственного ИИ-ассистента станет таким же простым, как настройка умной лампочки."),
  ],
  uses_label="Применение", uses_h="Где станция", uses_hg="приносит пользу",
  uses=[
   ("home", "Умный дом без облака", "Это одно из главных направлений. Вы можете создать голосового ассистента, который будет управлять освещением, климатом или другими устройствами.", 90),
   ("spark", "Кастомные ассистенты", "Вместо того чтобы быть привязанным к одному «характеру» Alexa, вы можете запрограммировать ассистента с уникальной личностью.", 75),
   ("hand", "Устройства для доступности", "Голосовой ассистент может помочь людям с ограниченными возможностями управлять окружением с помощью голоса.", 82),
  ],
  dl_label="Загрузка", dl_h="Приложение для", dl_hg="вашего телефона",
  dl=[("android", "Android", "Загрузка для Android", "Управляйте голосовой станцией со смартфона на Android.", "Загрузить"),
      ("apple", "iOS", "Загрузка для iOS", "Управляйте голосовой станцией с iPhone.", "Загрузить")],
  cta_label="Остались вопросы?", cta_h="Напишите", cta_hg="нам",
  cta_p="Расскажем о проекте, сборке станции и работе приложения.",
  cta_btn="Связаться",
  f_text="Голосовая станция с искусственным интеллектом на базе микроконтроллера ESP32-S3-DevKitC-1.",
  f_nav="Навигация", f_contacts="Контакты", f_social="Мы в соцсетях", f_write="Написать нам",
  f_write_p="Ответим на вопросы о проекте и приложении.",
  subject="Заявка с сайта", rights="Все права защищены.",
 ),
 "en": dict(
  file="en.html", lang="en", other_file="index.html", other_label="РУС",
  title="NOCTIS — AI Voice Station based on ESP32-S3-DevKitC-1",
  desc="An AI-based voice station built on the ESP32-S3-DevKitC-1 microcontroller: cloud and local modes, trends, use cases and app download.",
  logo="NOCTIS",
  nav=["Home", "About", "Trends", "Use Cases", "Download", "Contact"],
  cta_nav="Download", menu="Open menu",
  eyebrow="Diploma project · ESP32-S3-DevKitC-1",
  h1a="AI-powered", h1b="voice station",
  hero_sub="Creating a voice station with AI based on the ESP32-S3-DevKitC-1 is a popular and well-documented project. Depending on your goals, you can choose one of two main paths: cloud-based (powerful, but requires an internet connection) or local (private and fast, but with limitations).",
  btn1="Download the App", btn2="Learn More",
  chip1="Listening…", chip2b="ESP32-S3", chip2="Wi‑Fi · Bluetooth LE",
  stats=[("2", "Modes: cloud & local"), ("240", "MHz dual-core CPU"), ("3 m", "Voice pickup range"), ("100%", "DIY-built")],
  about_label="About the project",
  about_h="Your own private", about_hg="voice station",
  about_p="A voice station with artificial intelligence based on the ESP32-S3-DevKitC-1 is, in essence, an inexpensive, flexible device for voice interaction that you can assemble with your own hands. Its main value lies in the fact that it allows you to create private, customizable, and local voice interfaces that are not entirely dependent on commercial ecosystems like Alexa or Google.",
  checks=["An inexpensive device you can assemble yourself", "Private, customizable voice interfaces", "Independent of commercial ecosystems like Alexa or Google"],
  badge="ESP32-S3", badge_t="The heart<br>of the station",
  trends_label="Key directions", trends_h="Where AI devices", trends_hg="are heading",
  trends_p="Development is proceeding along several key directions, which are gradually blurring the boundaries between inexpensive DIY devices and full-fledged AI products.",
  trends=[
   ("cloud", "From pure cloud to hybrid and local", "This is the most significant trend. The first DIY projects relied on sending audio to the cloud for recognition and response generation. Now the focus is shifting towards local processing. The goal is to reduce latency, dependence on the internet, and improve privacy by processing simple commands (for example, “turn on the light”) directly on the ESP32. The future lies in hybrid systems that use the power of cloud LLMs only for complex requests."),
   ("mic", "Better audio and speech recognition", "DIY projects often suffer from noise and poor recognition. Specialized hardware solutions are emerging to solve this problem. For example, ReSpeaker Lite uses a separate XMOS audio processor for noise reduction, echo cancellation and voice capture from a distance of up to 3 meters. Integrating such modules with the ESP32-S3 is a direct way to create devices that work just as well as commercial speakers."),
   ("eye", "Beyond a “simple assistant”", "ESP32-S3 is capable of more than just voice. Thanks to its support for cameras and displays, it can become the foundation for multimodal devices that see and show. In the project involving a robot astronaut, an OLED screen was used to display animation depending on the operating mode. In the future, such devices will be able not only to hear but also to see (for example, to recognize faces or gestures) and to control physical actions (robots, manipulators)."),
   ("box", "Simpler development, lower entry barrier", "There are an increasing number of “out-of-the-box” solutions and platforms that hide the complexity of programming. ESP Private Agents allows you to generate firmware directly from a web interface. Projects like ElatoAI provide ready-made server infrastructure for connecting to dozens of voice models. This means that in the future, creating your own AI assistant will be as simple as setting up a smart light bulb."),
  ],
  uses_label="Use cases", uses_h="Where the station", uses_hg="makes a difference",
  uses=[
   ("home", "Smart home without the cloud", "This is one of the main directions. You can create a voice assistant that controls lighting, climate or other devices.", 90),
   ("spark", "Custom voice assistants", "Instead of being tied to Alexa’s single “personality”, you can program an assistant with a unique personality.", 75),
   ("hand", "Accessibility devices", "A voice assistant can help people with disabilities control their surroundings using their voice.", 82),
  ],
  dl_label="Download", dl_h="The app for", dl_hg="your phone",
  dl=[("android", "Android", "Download for Android", "Control your voice station from an Android smartphone.", "Download"),
      ("apple", "iOS", "Download for iOS", "Control your voice station from your iPhone.", "Download")],
  cta_label="Have questions?", cta_h="Write", cta_hg="to us",
  cta_p="We’ll tell you about the project, building the station and how the app works.",
  cta_btn="Contact Us",
  f_text="An AI-based voice station built on the ESP32-S3-DevKitC-1 microcontroller.",
  f_nav="Navigation", f_contacts="Contacts", f_social="Social media", f_write="Write to us",
  f_write_p="We’ll answer your questions about the project and the app.",
  subject="Website request", rights="All rights reserved.",
 ),
}

IDS = ["home", "about", "trends", "uses", "download", "contact"]

def page(c):
    nav = "\n".join(
        f'          <li><a href="#{i}" class="nav__link{" is-active" if i == "home" else ""}">{n}</a></li>'
        for i, n in zip(IDS, c["nav"]))
    stats = "\n".join(
        f'          <li class="stats__item"><span class="stats__num">{n}</span><span class="stats__label">{l}</span></li>'
        for n, l in c["stats"])
    checks = "\n".join(f"            <li>{x}</li>" for x in c["checks"])
    trends = "\n".join(f'''          <article class="card glass">
            <span class="card__num">0{k}</span>
            <div class="card__icon">{icon(ic)}</div>
            <h3 class="card__title">{t}</h3>
            <p class="card__text">{p}</p>
          </article>''' for k, (ic, t, p) in enumerate(c["trends"], 1))
    uses = "\n".join(f'''          <article class="metric glass">
            <div class="metric__top"><span class="metric__num">0{k}</span><div class="card__icon card__icon--sm">{icon(ic)}</div></div>
            <h3 class="metric__title">{t}</h3>
            <p class="metric__text">{p}</p>
            <div class="progress"><span style="--p: {pr}%"></span></div>
          </article>''' for k, (ic, t, p, pr) in enumerate(c["uses"], 1))
    dl = "\n".join(f'''          <article class="work glass">
            <div class="work__media work__media--{k}" aria-hidden="true">
              <span class="work__tag">{tag}</span>
              <span class="work__icon">{icon(ic)}</span>
            </div>
            <div class="work__body">
              <p class="label label--muted">{c["logo"]} · App</p>
              <h3 class="work__title">{t}</h3>
              <p class="work__text">{p}</p>
              <a href="#download" class="btn btn--primary btn--sm work__btn">{b} <span class="btn__arrow" aria-hidden="true">↓</span></a>
            </div>
          </article>''' for k, (ic, tag, t, p, b) in enumerate(c["dl"], 1))
    fnav = "\n".join(f'          <li><a href="#{i}">{n}</a></li>' for i, n in zip(IDS, c["nav"]))
    other = c["other_file"]
    return f'''<!DOCTYPE html>
<html lang="{c["lang"]}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{c["title"]}</title>
  <meta name="description" content="{c["desc"]}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Montserrat:wght@600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <!-- Global cosmic layers (pure CSS) -->
  <div class="cosmos" aria-hidden="true">
    <span class="stars stars--sm"></span>
    <span class="stars stars--md"></span>
    <span class="stars stars--lg"></span>
    <span class="orb orb--1"></span>
    <span class="orb orb--2"></span>
    <span class="orb orb--3"></span>
  </div>

  <!-- ========== HEADER ========== -->
  <header class="header">
    <div class="container header__inner">
      <a href="#home" class="logo" aria-label="{c["logo"]}">
        <span class="logo__mark" aria-hidden="true"></span>
        {c["logo"]}
      </a>

      <!-- CSS-only mobile menu toggle (replaces the original JS burger) -->
      <input type="checkbox" id="nav-toggle" class="nav-toggle" aria-label="{c["menu"]}">
      <label for="nav-toggle" class="nav-burger" aria-hidden="true"><span></span></label>

      <nav class="nav" aria-label="Primary">
        <ul class="nav__list">
{nav}
        </ul>
        <div class="nav__actions">
          <a href="{other}" class="lang-switch" hreflang="{"en" if c["lang"] == "ru" else "ru"}">{c["other_label"]}</a>
          <a href="#download" class="btn btn--primary btn--sm nav__cta">{c["cta_nav"]}</a>
        </div>
      </nav>
    </div>
  </header>

  <main>
    <!-- ========== HERO ========== -->
    <section class="hero" id="home">
      <div class="container hero__grid">
        <div class="hero__content">
          <p class="label"><span class="label__dot"></span>{c["eyebrow"]}</p>
          <h1 class="hero__title">{c["h1a"]} <span class="text-glow">{c["h1b"]}</span></h1>
          <p class="hero__sub">{c["hero_sub"]}</p>
          <div class="hero__actions">
            <a href="#download" class="btn btn--primary">{c["btn1"]} <span class="btn__arrow" aria-hidden="true">→</span></a>
            <a href="#about" class="btn btn--ghost">{c["btn2"]}</a>
          </div>
        </div>

        <!-- Hero visual: AI "entity" listening, with a CSS voice waveform -->
        <div class="hero__visual" aria-hidden="true">
          <div class="entity">
            <span class="entity__ring entity__ring--1"></span>
            <span class="entity__ring entity__ring--2"></span>
            <span class="entity__fibers"></span>
            <span class="entity__fibers entity__fibers--alt"></span>
            <span class="entity__eye entity__eye--l"></span>
            <span class="entity__eye entity__eye--r"></span>
            <span class="wave"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></span>
          </div>
          <div class="glass chip chip--top"><span class="chip__dot"></span> {c["chip1"]}</div>
          <div class="glass chip chip--bottom"><strong>{c["chip2b"]}</strong> {c["chip2"]}</div>
        </div>
      </div>

      <div class="container">
        <ul class="stats glass">
{stats}
        </ul>
      </div>
    </section>

    <!-- ========== ABOUT ========== -->
    <section class="section about" id="about">
      <div class="container about__grid">
        <div class="about__visual" aria-hidden="true">
          <div class="about__frame glass">
            <span class="about__grid-lines"></span>
            <span class="about__planet"></span>
            <span class="about__streak about__streak--1"></span>
            <span class="about__streak about__streak--2"></span>
            <span class="about__streak about__streak--3"></span>
          </div>
          <div class="about__badge glass">
            <span class="about__badge-num">S3</span>
            <span class="about__badge-text">{c["badge_t"]}</span>
          </div>
        </div>

        <div class="about__content">
          <p class="label">{c["about_label"]}</p>
          <h2 class="section__title">{c["about_h"]} <span class="text-glow">{c["about_hg"]}</span></h2>
          <p class="section__text">{c["about_p"]}</p>
          <ul class="checklist">
{checks}
          </ul>
          <a href="#trends" class="btn btn--ghost">{c["trends_label"]} →</a>
        </div>
      </div>
    </section>

    <!-- ========== TRENDS (services grid) ========== -->
    <section class="section services" id="trends">
      <div class="container">
        <header class="section__head">
          <p class="label">{c["trends_label"]}</p>
          <h2 class="section__title">{c["trends_h"]} <span class="text-glow">{c["trends_hg"]}</span></h2>
          <p class="section__text">{c["trends_p"]}</p>
        </header>
        <div class="services__grid services__grid--2">
{trends}
        </div>
      </div>
    </section>

    <!-- ========== USE CASES (results cards) ========== -->
    <section class="section results" id="uses">
      <div class="container">
        <header class="section__head">
          <p class="label">{c["uses_label"]}</p>
          <h2 class="section__title">{c["uses_h"]} <span class="text-glow">{c["uses_hg"]}</span></h2>
        </header>
        <div class="results__grid results__grid--3">
{uses}
        </div>
      </div>
    </section>

    <!-- ========== DOWNLOAD (featured works cards) ========== -->
    <section class="section works" id="download">
      <div class="container">
        <header class="section__head">
          <p class="label">{c["dl_label"]}</p>
          <h2 class="section__title">{c["dl_h"]} <span class="text-glow">{c["dl_hg"]}</span></h2>
        </header>
        <div class="works__list">
{dl}
        </div>
      </div>
    </section>

    <!-- ========== CTA BANNER ========== -->
    <section class="section cta">
      <div class="container">
        <div class="cta__box">
          <span class="cta__glow" aria-hidden="true"></span>
          <p class="label">{c["cta_label"]}</p>
          <h2 class="cta__title">{c["cta_h"]} <span class="text-glow">{c["cta_hg"]}</span></h2>
          <p class="cta__text">{c["cta_p"]}</p>
          <a href="mailto:info@tams.ru?subject={c["subject"]}" class="btn btn--primary btn--lg">{c["cta_btn"]} <span class="btn__arrow" aria-hidden="true">→</span></a>
        </div>
      </div>
    </section>
  </main>

  <!-- ========== FOOTER ========== -->
  <footer class="footer" id="contact">
    <div class="container footer__grid footer__grid--4">
      <div class="footer__brand">
        <a href="#home" class="logo"><span class="logo__mark" aria-hidden="true"></span>{c["logo"]}</a>
        <p class="footer__text">{c["f_text"]}</p>
      </div>

      <nav class="footer__col" aria-label="{c["f_nav"]}">
        <h4 class="footer__title">{c["f_nav"]}</h4>
        <ul>
{fnav}
        </ul>
      </nav>

      <address class="footer__col">
        <h4 class="footer__title">{c["f_contacts"]}</h4>
        <ul>
          <li><a href="tel:+79991234567">+7 (999) 123-45-67</a></li>
          <li><a href="tel:+74951234567">+7 (495) 123-45-67</a></li>
          <li><a href="mailto:info@tams.ru">info@tams.ru</a></li>
        </ul>
      </address>

      <div class="footer__col footer__news">
        <h4 class="footer__title">{c["f_social"]}</h4>
        <ul class="socials" aria-label="{c["f_social"]}">
          <li><a href="https://mail.google.com/" target="_blank" rel="noopener" aria-label="Email"><img src="assets/img/email.svg" alt=""></a></li>
          <li><a href="https://vk.com" target="_blank" rel="noopener" aria-label="VK"><img src="assets/img/vk.svg" alt=""></a></li>
        </ul>
        <h4 class="footer__title footer__title--gap">{c["f_write"]}</h4>
        <p class="footer__text">{c["f_write_p"]}</p>
        <a href="mailto:info@tams.ru?subject={c["subject"]}" class="btn btn--ghost btn--sm">{c["cta_btn"]}</a>
      </div>
    </div>

    <div class="container footer__bottom">
      <p>© 2026 {c["logo"]}. {c["rights"]}</p>
      <p><a href="index.html" hreflang="ru">РУС</a> · <a href="en.html" hreflang="en">ENG</a></p>
    </div>
  </footer>

</body>
</html>
'''

for c in T.values():
    Path(__file__).with_name(c["file"]).write_text(page(c), encoding="utf-8")
    print("wrote", c["file"])
