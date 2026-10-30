#!/usr/bin/env python3
"""Builds the full static site. Run:  python3 _source/build.py   (from the site folder)
Header, footer, WhatsApp buttons are defined ONCE here and written into every page."""
import os, json, urllib.parse, datetime

# ---------- SETTINGS (change here, then re-run the script) ----------
# --- GitHub Pages hosting ---
CUSTOM_DOMAIN = ""                  # custom domain ho to likho, e.g. "shaifalimathtutor.com" (warna khaali chhodo)
GITHUB_USER = "YOUR-GITHUB-USERNAME"  # <-- apna GitHub username
REPO = "shaifalimathtutor"          # <-- repository ka naam
if CUSTOM_DOMAIN:
    SITE_URL, BASE_PATH = f"https://{CUSTOM_DOMAIN}", ""
else:
    SITE_URL, BASE_PATH = f"https://{GITHUB_USER}.github.io/{REPO}", f"/{REPO}"
BRAND = "Shaifali Jain Math Tutoring"
# Phone / email / Facebook / Web3Forms key are read from js/config.js (single place to edit)
import re
_cfg_txt = open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "js", "config.js"), encoding="utf-8").read()
CFG = json.loads(re.search(r"\{.*\}", _cfg_txt, re.S).group(0))
PHONE_INTL = CFG["phone"]
PHONE_SHOW = CFG["phoneDisplay"]
EMAIL = CFG["email"]
FACEBOOK = CFG["facebook"]
W3F_KEY = CFG["web3formsKey"]
HERO_IMG = "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=600&q=80"
ABOUT_IMG = "https://images.unsplash.com/photo-1580894732444-8ecded7900cd?w=500&q=80"
TODAY = datetime.date.today().isoformat()
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def wa(text):
    return f"https://wa.me/{PHONE_INTL}?text=" + urllib.parse.quote(text)
WA_GENERAL = wa("Hi Shaifali, I'd like to know more about your online math classes.")

WA_ICON = '<svg viewBox="0 0 32 32" width="26" height="26" aria-hidden="true"><path fill="#fff" d="M16 3C8.8 3 3 8.7 3 15.8c0 2.5.7 4.8 2 6.8L3 29l6.6-1.9a13 13 0 0 0 6.4 1.7c7.2 0 13-5.7 13-12.8S23.200 3 16 3z"/><path fill="#25d366" d="M12 9.500c-.4 0-.9.200-1.200.700-.5.700-.8 1.500-.4 2.600.7 2.300 3.900 5.600 6.600 6.500 1.300.4 2.300.2 3-.5.400-.4.600-.9.500-1.200l-.1-.3-2.200-1.100c-.3-.1-.6 0-.8.200l-.8 1c-1.500-.6-2.800-1.900-3.400-3.300l.9-.9c.2-.2.300-.5.200-.8l-.9-2.100c-.1-.4-.4-.7-.4-.7z"/></svg>'

NAV = [("index.html", "Home"), ("about.html", "About"), ("services.html", "Services"),
       ("pricing.html", "Pricing"), ("testimonials.html", "Testimonials"),
       ("blog/index.html", "Blog"), ("faq.html", "FAQ"), ("contact.html", "Contact")]

# ---------- BLOG CONTENT ----------
POSTS = [
 dict(slug="how-to-choose-online-math-tutor", date="2026-10-05",
  title="How to Choose the Right Online Math Tutor for Your Child",
  desc="Not sure how to pick an online math tutor? Here are 6 practical things parents should check before booking the first class.",
  body="""
<p>Searching for an online math tutor can feel overwhelming. There are many options, and every tutor promises better marks. These six checks will help you decide with confidence.</p>
<h2>1. Check that the tutor knows your curriculum</h2>
<p>CBSE, ICSE, American Common Core, UK GCSE and Australian syllabi all order topics differently and test in different ways. A tutor who has taught your board will know what the school expects and how exam questions are framed.</p>
<h2>2. Look for one-on-one attention</h2>
<p>In a group class, a child who is confused often stays quiet. In a one-on-one lesson, the tutor sees exactly where the student gets stuck and can change the explanation on the spot.</p>
<h2>3. Ask how the first class works</h2>
<p>A good tutor starts by understanding the child: current grade, weak topics, school marks and goals. If a tutor jumps straight into teaching without asking questions, that is a warning sign.</p>
<h2>4. See how progress is tracked</h2>
<p>You should know what is improving and what still needs work. Ask about practice tests, homework review and regular updates for parents.</p>
<h2>5. Make sure timings suit you</h2>
<p>Families living abroad need a tutor who can work across time zones. Flexible scheduling means fewer missed classes.</p>
<h2>6. Take a free consultation first</h2>
<p>Talk to the tutor before you commit. Notice whether your child feels comfortable asking questions. Comfort matters as much as skill.</p>
<p>If you would like to talk about your child's needs, you can <a href="../contact.html">book a free consultation</a> or <a href="../services.html">see the subjects I teach</a>.</p>"""),
 dict(slug="signs-your-child-is-afraid-of-math", date="2026-10-12",
  title="6 Signs Your Child Is Afraid of Math (and How to Help)",
  desc="Math anxiety is common and fixable. Learn the warning signs and simple ways parents can rebuild a child's confidence in math.",
  body="""
<p>Many children say "I'm bad at math" long before they have actually struggled with it. Fear of math usually comes from a few missed basics or a bad experience in class. The good news is that it can be fixed.</p>
<h2>Common signs</h2>
<ul>
<li>They avoid or delay math homework.</li>
<li>They say things like "I can't do it" before even trying.</li>
<li>They hurry to finish without checking the answer.</li>
<li>They feel stomach aches or stress before math tests.</li>
<li>They memorise steps but cannot explain why they work.</li>
<li>Marks in math drop while other subjects stay steady.</li>
</ul>
<h2>How parents can help</h2>
<p><strong>Praise effort, not just marks.</strong> Say "I liked how you kept trying" instead of "You got it right."</p>
<p><strong>Go back to the basics.</strong> Gaps in fractions, tables or negative numbers cause trouble in algebra later. Fixing the base fixes the fear.</p>
<p><strong>Make mistakes normal.</strong> Treat a wrong answer as information about what to learn next.</p>
<p><strong>Use real-life math.</strong> Cooking, shopping and travel plans show children that math is useful.</p>
<p><strong>Get patient support.</strong> A tutor who explains the same idea in different ways, without hurry, can change how a child feels about the subject. Read about <a href="../about.html">my teaching approach</a> or <a href="../contact.html">talk to me</a>.</p>"""),
 dict(slug="5-tips-to-make-algebra-easier", date="2026-10-19",
  title="5 Tips to Make Algebra Easier for Grades 8 to 10",
  desc="Algebra confuses many students because letters replace numbers. These 5 simple tips make equations and expressions easier to understand.",
  body="""
<p>Algebra is the first time many students meet letters in math, and that is where confusion begins. These five habits make the topic much easier.</p>
<h2>1. Treat letters as "mystery numbers"</h2>
<p>A variable like x is just a number we don't know yet. Replace x with a real number now and then to see that the rules are the same as in arithmetic.</p>
<h2>2. Do the same thing to both sides</h2>
<p>An equation is like a balanced scale. Whatever you add, subtract, multiply or divide on one side, do on the other side too.</p>
<h2>3. Write every step</h2>
<p>Skipping steps is the biggest cause of small mistakes, especially with negative signs. Neat, line-by-line working also earns method marks in exams.</p>
<h2>4. Check your answer</h2>
<p>Put the answer back into the original equation. If both sides match, you are right. This builds confidence and catches errors.</p>
<h2>5. Practise a little every day</h2>
<p>Twenty focused minutes daily works better than three hours before the test. Start with easy questions and move up slowly.</p>
<p>Stuck on a specific topic? See my <a href="../services.html#algebra">Algebra 1 &amp; 2 classes</a> or <a href="../contact.html">send me your question</a>.</p>"""),
 dict(slug="4-week-math-exam-revision-plan", date="2026-10-26",
  title="A Simple 4-Week Math Exam Revision Plan",
  desc="A realistic 4-week math revision plan for school and board exams: what to study each week, how to practise and how to stay calm.",
  body="""
<p>Good exam results come from steady, planned revision, not last-night cramming. Here is a simple plan you can adapt to any board or grade.</p>
<h2>Week 1: List and diagnose</h2>
<p>Write down every chapter in the syllabus. Mark each one green (confident), yellow (okay) or red (weak). Spend the most time on red topics.</p>
<h2>Week 2: Fix the weak topics</h2>
<p>Revisit the concept first, then solve textbook examples, then try exercise questions. Keep a notebook of formulas and common mistakes.</p>
<h2>Week 3: Practise past papers</h2>
<p>Solve at least two full papers under timed conditions. Check your answers and note why you lost marks: concept, calculation or time.</p>
<h2>Week 4: Revise and relax</h2>
<p>Go through your formula notebook, re-do mistakes from earlier papers and sleep well. Avoid learning new topics in the last two days.</p>
<h2>Exam day tips</h2>
<ul>
<li>Read the whole paper first and start with questions you know.</li>
<li>Show all steps for method marks.</li>
<li>Keep 10 minutes at the end to check.</li>
</ul>
<p>Need help building a plan around your child's exam date? Look at my <a href="../services.html#exam-preparation">exam preparation classes</a> or <a href="../pricing.html">get an instant price on WhatsApp</a>.</p>"""),
 dict(slug="one-on-one-vs-group-math-classes", date="2026-10-29",
  title="One-on-One vs Group Math Classes: Which Is Better?",
  desc="Compare one-on-one online math tutoring with group classes on attention, pace, confidence and results, and see which suits your child.",
  body="""
<p>Parents often ask whether a private tutor or a group class is the better choice. Both have a place, but they do different jobs.</p>
<h2>Where one-on-one tutoring wins</h2>
<ul>
<li><strong>Personal pace:</strong> The lesson slows down or speeds up with your child.</li>
<li><strong>Focus on gaps:</strong> Time is spent only on topics that need work.</li>
<li><strong>Safe to ask:</strong> Shy students ask doubts freely when no one else is watching.</li>
<li><strong>Flexible timing:</strong> Classes fit around school, sports and time zones.</li>
</ul>
<h2>Where group classes help</h2>
<p>Group classes can be cheaper and give some peer energy. They work well for students who already understand the basics and need practice, but the pace is fixed for everyone.</p>
<h2>Which should you choose?</h2>
<p>If your child is struggling, has gaps in basics, or is preparing for a board exam, one-on-one is usually more effective. If your child is confident and just needs extra practice, a group class can be enough.</p>
<p>My classes are <a href="../about.html">fully one-on-one</a> and built around the student. <a href="../contact.html">Ask for a free consultation</a> to see if it fits.</p>"""),
]

# ---------- LAYOUT ----------
def head(title, desc, path, depth, extra="", noindex=False, og_type="website"):
    p = "../" * depth
    url = f"{SITE_URL}/{path}" if path != "index.html" else f"{SITE_URL}/"
    robots = '<meta name="robots" content="noindex, follow">' if noindex else '<meta name="robots" content="index, follow, max-image-preview:large">'
    canon = "" if noindex else f'<link rel="canonical" href="{url}">'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}
{canon}
<meta name="author" content="Shaifali Jain">
<meta name="theme-color" content="#3f51b5">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="en_IN">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E%F0%9F%93%90%3C/text%3E%3C/svg%3E">
<link rel="stylesheet" href="{p}css/style.css">
{extra}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
'''

def header(active, depth):
    p = "../" * depth
    items = "".join(
        f'<li><a href="{p}{h}"{" class=active aria-current=page" if h == active else ""}>{t}</a></li>' for h, t in NAV)
    return f'''<header class="site-header">
  <div class="topbar"><div class="topbar-in">
    <a data-c="tel" href="tel:+{PHONE_INTL}">&#128222; Call: <span data-c="phone-text">{PHONE_SHOW}</span></a>
    <a class="tb-mail" data-c="mail" href="mailto:{EMAIL}">&#9993; <span data-c="email-text">{EMAIL}</span></a>
  </div></div>
  <div class="navbar">
    <a class="logo" href="{p}index.html">Shaifali <span>Jain</span> Math Tutoring</a>
    <button class="menu-toggle" id="menuToggle" aria-label="Open menu" aria-expanded="false" aria-controls="navMenu">&#9776;</button>
    <nav aria-label="Main">
      <ul id="navMenu">{items}
        <li class="nav-wa"><a class="wa-btn" href="{WA_GENERAL}" target="_blank" rel="noopener">{WA_ICON.replace('width="26" height="26"','width="20" height="20"')} WhatsApp</a></li>
      </ul>
    </nav>
  </div>
</header>
'''

def footer(depth):
    p = "../" * depth
    links = "".join(f'<li><a href="{p}{h}">{t}</a></li>' for h, t in NAV)
    return f'''
<footer class="site-footer">
  <div class="container footer-grid">
    <div>
      <h3>{BRAND}</h3>
      <p>One-on-one online math lessons for students across timezones and curricula: CBSE, ICSE, American, UK and Australian.</p>
      <p><a class="wa-btn" href="{WA_GENERAL}" target="_blank" rel="noopener">{WA_ICON.replace('width="26" height="26"','width="20" height="20"')} Chat on WhatsApp</a></p>
    </div>
    <div><h3>Quick Links</h3><ul>{links}</ul></div>
    <div>
      <h3>Contact</h3>
      <ul>
        <li><a data-c="tel" href="tel:+{PHONE_INTL}">&#128222; <span data-c="phone-text">{PHONE_SHOW}</span></a></li>
        <li><a href="{WA_GENERAL}" target="_blank" rel="noopener">&#128172; WhatsApp</a></li>
        <li><a data-c="mail" href="mailto:{EMAIL}">&#9993; <span data-c="email-text">{EMAIL}</span></a></li>
        <li><a data-c="fb" href="{FACEBOOK}" target="_blank" rel="noopener me">Facebook</a></li>
      </ul>
    </div>
  </div>
  <div class="container footer-bottom">
    <p>&copy; 2026 {BRAND}. All rights reserved. <a href="{p}privacy-policy.html">Privacy Policy</a> &middot; <a href="{p}terms.html">Terms</a></p>
  </div>
</footer>
<div class="footer-bar" role="complementary" aria-label="Contact">
  <a class="fb-call" data-c="tel" href="tel:+{PHONE_INTL}">&#128222; <span data-c="phone-text">{PHONE_SHOW}</span></a>
  <a class="fb-wa" href="{WA_GENERAL}" target="_blank" rel="noopener">{WA_ICON.replace('width="26" height="26"','width="22" height="22"')} Chat on WhatsApp</a>
</div>
<script src="{p}js/config.js" defer></script>
<script src="{p}js/main.js" defer></script>
</body>
</html>
'''

def crumbs(items, depth):
    """items: list of (label, href or None)"""
    p = "../" * depth
    out = [f'<a href="{p}index.html">Home</a>']
    for l, h in items:
        out.append(f'<a href="{p}{h}">{l}</a>' if h else f'<span aria-current="page">{l}</span>')
    return '<nav class="breadcrumb" aria-label="Breadcrumb">' + " &rsaquo; ".join(out) + "</nav>"

def jsonld(obj):
    return f'<script type="application/ld+json">{json.dumps(obj, ensure_ascii=False)}</script>'

def bc_schema(items):
    lst = [{"@type": "ListItem", "position": i + 1, "name": n, "item": f"{SITE_URL}/{u}" if u else SITE_URL + "/"}
           for i, (n, u) in enumerate(items)]
    return jsonld({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": lst})

def page_hero(h1, lead, bc_html):
    return f'<section class="page-hero"><div class="container">{bc_html}<h1>{h1}</h1><p>{lead}</p></div></section>'

def cta_band(depth, text="Ready to make math easier for your child?"):
    p = "../" * depth
    return f'''<section class="cta-band"><div class="container">
  <h2>{text}</h2><p>Book a free consultation. No pressure, just a friendly conversation about your child's needs.</p>
  <a class="btn" href="{p}contact.html">Book a Free Consultation</a>
  <a class="btn btn-wa" href="{WA_GENERAL}" target="_blank" rel="noopener">Chat on WhatsApp</a>
</div></section>'''

def write(path, html):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)

def build_page(path, title, desc, active, body, extra="", noindex=False, og_type="website"):
    depth = path.count("/")
    write(path, head(title, desc, path, depth, extra, noindex, og_type) + header(active, depth)
          + '<main id="main">\n' + body + "\n</main>" + footer(depth))

ORG = {"@context": "https://schema.org", "@type": "EducationalOrganization", "name": BRAND,
       "url": SITE_URL + "/", "telephone": "+" + PHONE_INTL, "email": EMAIL, "sameAs": [FACEBOOK],
       "areaServed": "Worldwide", "description": "One-on-one online math tutoring for CBSE, ICSE, American, UK and Australian curricula.",
       "founder": {"@type": "Person", "name": "Shaifali Jain", "jobTitle": "Online Math Tutor"}}

# ---------- SHARED SNIPPETS ----------
TESTIMONIALS = [
 ("Shaifali ma'am explains every concept so clearly. My daughter actually looks forward to her math classes now.", "A Happy Parent"),
 ("I went from dreading algebra to scoring well in my exams. The one-on-one attention made all the difference.", "A Grateful Student"),
 ("Patient, structured, and genuinely caring about progress. Highly recommend for any student struggling with math.", "A Satisfied Parent"),
]
def tcards(n=None):
    return "".join(f'<figure class="testimonial-card"><div class="stars" aria-label="5 out of 5 stars">★★★★★</div><blockquote><p>“{q}”</p></blockquote><figcaption class="testimonial-name">— {a}</figcaption></figure>'
                   for q, a in TESTIMONIALS[:n])

SERVICES = [
 ("foundational-math", "➕", "Foundational Math", "Building strong basics in arithmetic, fractions, decimals and number sense for younger students.",
  "Strong basics are the base of every later topic. We work on tables, fractions, decimals, percentages, ratios and word problems until they feel easy and natural."),
 ("algebra", "📐", "Algebra 1 & 2", "Step-by-step guidance through equations, functions, and problem-solving techniques.",
  "From linear equations and inequalities to quadratics, polynomials and functions, I break each idea into small steps and connect it to what students already know."),
 ("geometry", "📏", "Geometry", "Making shapes, proofs, and spatial reasoning easy to visualize and understand.",
  "Angles, triangles, circles, area, volume, coordinate geometry and proofs. I use a digital whiteboard so students can see every construction as it is drawn."),
 ("trigonometry", "📊", "Trigonometry", "Clear explanations of ratios, identities, and applications for exam success.",
  "Trigonometric ratios, identities, heights and distances, and the unit circle, explained with diagrams and plenty of exam-style practice."),
 ("exam-preparation", "📝", "Exam Preparation", "Focused revision, practice papers, and strategies to boost exam confidence.",
  "Chapter-wise revision, timed practice papers, error analysis and exam-writing technique for school tests, CBSE/ICSE boards, GCSE and US high-school exams."),
 ("homework-help", "🏠", "Homework Help", "Ongoing support to keep up with school assignments and clear doubts quickly.",
  "Regular help with school assignments and doubt clearing so small confusions never grow into big gaps."),
]

# ---------- PAGES ----------
def home():
    cards = "".join(f'<a class="service-card" href="services.html#{i}"><div class="service-icon" aria-hidden="true">{ic}</div><h3>{t}</h3><p>{s}</p></a>' for i, ic, t, s, _ in SERVICES)
    blog = "".join(blog_card(p, 0) for p in POSTS[-3:][::-1])
    body = f'''
<section class="hero" id="home"><div class="container">
  <div class="hero-text">
    <h1>Online Math Tutoring with Shaifali Jain</h1>
    <p>One-on-one online math lessons for Grades 1 to 12, built around your child's pace, curriculum and goals. CBSE, ICSE, American, UK and Australian syllabi.</p>
    <a href="contact.html" class="btn">Book a Free Consultation</a>
    <a href="{WA_GENERAL}" class="btn btn-wa" target="_blank" rel="noopener">Chat on WhatsApp</a>
  </div>
  <div class="hero-img"><img src="{HERO_IMG}" alt="Student learning math in an online one-on-one class" width="600" height="400" fetchpriority="high"></div>
</div></section>

<section class="trust"><div class="container trust-grid">
  <div><strong>1-on-1</strong><span>Personal attention</span></div>
  <div><strong>4 curricula</strong><span>CBSE/ICSE, US, UK, AU</span></div>
  <div><strong>Any timezone</strong><span>Flexible scheduling</span></div>
  <div><strong>Free</strong><span>First consultation</span></div>
</div></section>

<section><div class="container">
  <div class="section-title"><h2>Does This Sound Familiar?</h2>
  <p>Many parents and students reach out with the same worries. If any of these sound familiar, you're in the right place.</p></div>
  <div class="questions">
    <div class="question-card">Is your child struggling to keep up with math concepts in class?</div>
    <div class="question-card">Do new topics like algebra or geometry feel confusing rather than exciting?</div>
    <div class="question-card">Have regular classroom lessons not given the one-on-one attention needed?</div>
    <div class="question-card">Are you searching for someone who can bridge the gap between basics and advanced math?</div>
  </div>
  <p class="center-note">I help build your child's confidence, strengthen fundamentals and improve grades, while making math genuinely enjoyable to learn.</p>
</div></section>

<section class="bg-light"><div class="container about-flex">
  <div class="about-img"><img src="{ABOUT_IMG}" alt="Shaifali Jain, online math tutor" width="500" height="600" loading="lazy"></div>
  <div class="about-text">
    <h2>Meet Your Math Tutor</h2>
    <p>I'm Shaifali Jain, a dedicated and passionate math educator who loves helping students who find math intimidating. My goal is simple: build a strong foundation, real confidence, and a genuine enjoyment of mathematics.</p>
    <p>Every lesson is one-on-one, planned around the student and delivered live on a digital whiteboard.</p>
    <a href="about.html" class="btn">More About Me</a>
  </div>
</div></section>

<section><div class="container">
  <div class="section-title"><h2>Math Subjects I Teach</h2><p>Personalized online math tutoring for every level, wherever you are in the world.</p></div>
  <div class="services-grid">{cards}</div>
</div></section>

<section class="bg-light"><div class="container">
  <div class="section-title"><h2>My Teaching Approach</h2><p>A four-step method designed to build real understanding, not just memorization.</p></div>
  {steps()}
</div></section>

<section><div class="container">
  <div class="section-title"><h2>What Parents &amp; Students Say</h2></div>
  <div class="testimonial-grid">{tcards()}</div>
  <p class="center-note"><a class="btn" href="testimonials.html#share-feedback">Share Your Feedback</a></p>
</div></section>

<section class="bg-light"><div class="container">
  <div class="section-title"><h2>From the Math Blog</h2><p>Practical tips for students and parents.</p></div>
  <div class="blog-grid">{blog}</div>
  <p class="center-note"><a class="btn" href="blog/index.html">Read All Articles</a></p>
</div></section>
{cta_band(0)}'''
    build_page("index.html", "Online Math Tutor | One-on-One Math Classes by Shaifali Jain",
               "Online one-on-one math tutoring by Shaifali Jain for CBSE, ICSE, American, UK and Australian curricula. Algebra, geometry, trigonometry and exam prep. Free consultation.",
               "index.html", body, jsonld(ORG))

def steps():
    s = [("Understand the Need", "Before the first class, I talk with parents and students to understand exactly where extra attention is needed and set clear learning goals."),
         ("I Do", "I introduce new concepts using interactive strategies that activate prior knowledge and spark curiosity."),
         ("We Do", "We work through examples together, building confidence step by step until the concept feels natural."),
         ("You Do", "Students show their understanding independently through guided practice, quizzes and homework.")]
    return '<ol class="steps">' + "".join(f'<li class="step"><div class="step-number">{i+1}</div><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(s)) + "</ol>"

def blog_card(p, depth):
    pre = "" if depth == 0 else "../"
    d = datetime.date.fromisoformat(p["date"]).strftime("%d %b %Y")
    return f'<article class="blog-card"><time datetime="{p["date"]}">{d}</time><h3><a href="{pre}blog/{p["slug"]}.html">{p["title"]}</a></h3><p>{p["desc"]}</p><a class="read-more" href="{pre}blog/{p["slug"]}.html">Read article</a></article>'

def about():
    bc = [("About", None)]
    body = page_hero("About Shaifali Jain", "A patient, structured and caring online math tutor for students worldwide.", crumbs(bc, 0)) + f'''
<section><div class="container about-flex">
  <div class="about-img"><img src="{ABOUT_IMG}" alt="Shaifali Jain, online math tutor" width="500" height="600" loading="lazy"></div>
  <div class="about-text">
    <p>My name is Shaifali Jain, and I am a dedicated and passionate math educator with experience teaching students across different grades and curricula. Helping students who find math intimidating is what I love doing most.</p>
    <p>My goal is simple: to help every student build a strong foundation, gain real confidence, and enjoy learning mathematics rather than fearing it. I believe every student can master math with the right guidance, patience and encouragement.</p>
    <h2>Curricula I Teach</h2>
    <ul class="curriculum-list">
      <li>Indian Curriculum (CBSE / ICSE, Grades 6–10)</li>
      <li>American Curriculum (Pre-Algebra, Algebra 1 &amp; 2, Geometry)</li>
      <li>UK Curriculum (KS2, KS3, GCSE)</li>
      <li>Australian Curriculum &amp; general homework help</li>
    </ul>
    <h2>How My Classes Work</h2>
    <p>Lessons are live, one-on-one video sessions on a digital whiteboard. You only need a laptop or tablet, a stable internet connection and a notebook. Timings are flexible across time zones.</p>
    <a href="contact.html" class="btn">Get in Touch</a>
  </div>
</div></section>
<section class="bg-light"><div class="container">
  <div class="section-title"><h2>My Teaching Approach</h2><p>A four-step method designed to build real understanding, not just memorization.</p></div>
  {steps()}
  <p class="center-note">Explore the <a href="services.html">subjects I teach</a> or read <a href="blog/index.html">tips on the blog</a>.</p>
</div></section>
{cta_band(0)}'''
    build_page("about.html", "About Shaifali Jain | Online Math Tutor for CBSE, ICSE, US & UK",
               "Meet Shaifali Jain, an online math tutor teaching CBSE, ICSE, American, UK and Australian curricula with patient one-on-one lessons.",
               "about.html", body, bc_schema([("Home", ""), ("About", "about.html")]))

def services():
    bc = [("Services", None)]
    sec = "".join(f'''<section id="{i}" class="{'bg-light' if n % 2 == 0 else ''}"><div class="container service-detail">
      <div class="service-icon" aria-hidden="true">{ic}</div><div><h2>{t}</h2><p>{long}</p>
      <a class="btn" href="{wa(f'Hi Shaifali, I want to know more about {t} classes.')}" target="_blank" rel="noopener">Ask About {t}</a></div></div></section>'''
                  for n, (i, ic, t, s, long) in enumerate(SERVICES))
    body = page_hero("Online Math Tutoring Services", "Personalized one-on-one lessons for every level, from foundational math to board exam preparation.", crumbs(bc, 0)) + sec + f'''
<section><div class="container">
  <div class="section-title"><h2>Curricula Covered</h2></div>
  <div class="services-grid">
    <div class="service-card"><h3>CBSE / ICSE</h3><p>Grades 6 to 10 including board exam preparation.</p></div>
    <div class="service-card"><h3>American</h3><p>Pre-Algebra, Algebra 1 &amp; 2, Geometry.</p></div>
    <div class="service-card"><h3>UK</h3><p>KS2, KS3 and GCSE Mathematics.</p></div>
    <div class="service-card"><h3>Australian</h3><p>Primary and secondary math with homework support.</p></div>
  </div>
  <p class="center-note">Not sure which plan is right? <a href="pricing.html">See pricing options</a> or <a href="blog/how-to-choose-online-math-tutor.html">read how to choose a math tutor</a>.</p>
</div></section>
{cta_band(0)}'''
    build_page("services.html", "Online Math Tutoring Services | Algebra, Geometry, Trigonometry, Exam Prep",
               "One-on-one online math classes in foundational math, algebra, geometry, trigonometry, exam preparation and homework help for all major curricula.",
               "services.html", body, bc_schema([("Home", ""), ("Services", "services.html")]))

def pricing():
    bc = [("Pricing", None)]
    plans = [("Single Session", "Single Session", ["60-minute one-on-one class", "Flexible scheduling", "Great for trying it out"]),
             ("Monthly Plan", "Monthly Plan", ["8 sessions per month", "Homework &amp; doubt support", "Progress tracking"]),
             ("Exam Crash Course", "Exam Crash Course", ["Focused revision sessions", "Practice papers included", "Ideal before exams"])]
    cards = ""
    for i, (t, key, feats) in enumerate(plans):
        link = wa(f"Hi Shaifali, please share the price for the {key}. My child's grade/curriculum is: ")
        cards += f'''<div class="price-card{' featured' if i == 1 else ''}"><h3>{t}</h3>
        <ul>{"".join(f"<li>{f}</li>" for f in feats)}</ul>
        <a class="btn btn-wa" href="{link}" target="_blank" rel="noopener">Get Instant Price</a></div>'''
    body = page_hero("Pricing", "Fees depend on grade, curriculum and number of sessions. Tap the button to get your price instantly on WhatsApp.", crumbs(bc, 0)) + f'''
<section><div class="container">
  <div class="pricing-grid">{cards}</div>
  <p class="center-note">Prefer a call? Dial <a data-c="tel" href="tel:+{PHONE_INTL}"><span data-c="phone-text">{PHONE_SHOW}</span></a> or <a href="contact.html">send a message</a>.</p>
</div></section>
<section class="bg-light"><div class="container narrow">
  <h2>What affects the price?</h2>
  <ul class="curriculum-list"><li>Your child's grade and curriculum</li><li>Number of sessions per week</li><li>One-time exam preparation or ongoing support</li></ul>
  <p>Share these details on WhatsApp and I will send the exact fees along with suggested timings. Read the <a href="faq.html">FAQ</a> for cancellation and homework policies.</p>
</div></section>'''
    build_page("pricing.html", "Math Tutoring Fees | Get Instant Price on WhatsApp",
               "Get an instant price for one-on-one online math tutoring: single session, monthly plan or exam crash course. Message Shaifali Jain on WhatsApp.",
               "pricing.html", body, bc_schema([("Home", ""), ("Pricing", "pricing.html")]))

def form_open(kind, subject, depth=0, redirect="thank-you.html"):
    return f'''<form class="js-form" action="https://api.web3forms.com/submit" method="POST" data-redirect="{redirect}">
  <input type="hidden" name="access_key" value="{W3F_KEY}">
  <input type="hidden" name="subject" value="{subject}">
  <input type="hidden" name="from_name" value="{BRAND} Website">
  <input type="hidden" name="form_type" value="{kind}">
  <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">'''

def testimonials():
    bc = [("Testimonials", None)]
    body = page_hero("Testimonials", "What parents and students say about learning math together.", crumbs(bc, 0)) + f'''
<section><div class="container"><div class="testimonial-grid">{tcards()}</div></div></section>
<section class="bg-light" id="share-feedback"><div class="container narrow">
  <div class="section-title"><h2>Share Your Feedback</h2>
  <p>Are you a student or parent? Tell us about your experience. Reviews are checked and then added to this page.</p></div>
  <div class="form-card">
  {form_open("testimonial", "New Testimonial from Website", redirect="thank-you.html?type=feedback")}
    <label for="t-name">Your name</label><input id="t-name" name="name" type="text" required autocomplete="name">
    <label for="t-role">I am a</label>
    <select id="t-role" name="role" required><option value="">Select</option><option>Student</option><option>Parent</option></select>
    <label for="t-grade">Grade / curriculum (optional)</label><input id="t-grade" name="grade" type="text" placeholder="e.g. Grade 9 CBSE">
    <fieldset class="rating"><legend>Your rating</legend>
      <input type="radio" id="r5" name="rating" value="5" required><label for="r5" title="5 stars">★</label>
      <input type="radio" id="r4" name="rating" value="4"><label for="r4" title="4 stars">★</label>
      <input type="radio" id="r3" name="rating" value="3"><label for="r3" title="3 stars">★</label>
      <input type="radio" id="r2" name="rating" value="2"><label for="r2" title="2 stars">★</label>
      <input type="radio" id="r1" name="rating" value="1"><label for="r1" title="1 star">★</label>
    </fieldset>
    <label for="t-msg">Your feedback</label><textarea id="t-msg" name="message" required placeholder="How did the classes help?"></textarea>
    <label class="check"><input type="checkbox" name="consent" value="yes" required> I allow my name and feedback to be shown on this website.</label>
    <button type="submit" class="btn">Submit Feedback</button>
    <p class="form-status" role="status" aria-live="polite"></p>
  </form></div>
</div></section>'''
    build_page("testimonials.html", "Student & Parent Reviews | Shaifali Jain Math Tutoring",
               "Read feedback from parents and students about Shaifali Jain's online math classes, and share your own experience.",
               "testimonials.html", body, bc_schema([("Home", ""), ("Testimonials", "testimonials.html")]))

FAQS = [
 ("How does online math tutoring work?", "Classes are conducted over video call using a digital whiteboard. All you need is a laptop or tablet, a stable internet connection, and a quiet space to learn."),
 ("What devices or supplies are needed?", "A laptop, tablet or computer with a camera and microphone, along with a notebook and pen for practice. A stylus is helpful but not required."),
 ("Which grade levels do you teach?", "I teach students from primary grades through high school, across CBSE/ICSE, American, UK and Australian curricula."),
 ("How often are sessions held?", "Session frequency is flexible, from once a week to daily sessions, based on the student's needs and goals, decided together during the consultation."),
 ("What is the homework policy?", "Homework is assigned after most sessions to reinforce concepts. It is reviewed at the start of the next class to track progress and clear doubts."),
 ("What is the cancellation policy?", "Please provide at least 24 hours' notice to reschedule or cancel a session so the time slot can be offered to another student."),
 ("How much do the classes cost?", "Fees depend on grade, curriculum and number of sessions. Tap Get Instant Price on the Pricing page and the price is shared on WhatsApp."),
 ("Do you offer a free consultation?", "Yes. The first consultation is free so we can understand your child's needs and see if we are a good match."),
 ("Can you teach students in other time zones?", "Yes. Timings are flexible, and I teach students in India and abroad."),
]
def faq():
    bc = [("FAQ", None)]
    items = "".join(f'<details class="faq-item"><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQS)
    schema = jsonld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]})
    body = page_hero("Frequently Asked Questions", "Quick answers about classes, scheduling, homework and fees.", crumbs(bc, 0)) + f'''
<section><div class="container narrow">{items}
<p class="center-note">Still have a question? <a href="contact.html">Contact me</a> or <a href="{WA_GENERAL}" target="_blank" rel="noopener">message on WhatsApp</a>.</p></div></section>'''
    build_page("faq.html", "Online Math Tutoring FAQ | Classes, Fees, Homework & Timings",
               "Answers to common questions about online math tutoring with Shaifali Jain: how classes work, devices needed, grades, timings, homework and cancellation.",
               "faq.html", body, schema + bc_schema([("Home", ""), ("FAQ", "faq.html")]))

def contact():
    bc = [("Contact", None)]
    body = page_hero("Contact Me", "Have questions or ready to book a free consultation? Reach out below.", crumbs(bc, 0)) + f'''
<section><div class="container contact-flex">
  <div class="contact-info">
    <h2>Get in Touch</h2>
    <p>&#9993; Email: <a data-c="mail" href="mailto:{EMAIL}"><span data-c="email-text">{EMAIL}</span></a></p>
    <p>&#128222; Phone: <a data-c="tel" href="tel:+{PHONE_INTL}"><span data-c="phone-text">{PHONE_SHOW}</span></a></p>
    <p>&#128172; WhatsApp: <a href="{WA_GENERAL}" target="_blank" rel="noopener"><span data-c="phone-text">{PHONE_SHOW}</span></a></p>
    <p>&#127760; Facebook: <a data-c="fb" href="{FACEBOOK}" target="_blank" rel="noopener me">Our Facebook Page</a></p>
    <p>&#128338; Available: Mon–Sat, flexible across timezones</p>
    <a class="btn btn-wa" href="{WA_GENERAL}" target="_blank" rel="noopener">Chat on WhatsApp</a>
  </div>
  <div class="form-card">
  {form_open("contact", "New Enquiry from Website")}
    <label for="c-name">Your name</label><input id="c-name" name="name" type="text" required autocomplete="name">
    <label for="c-email">Your email</label><input id="c-email" name="email" type="email" required autocomplete="email">
    <label for="c-phone">Phone / WhatsApp</label><input id="c-phone" name="phone" type="tel" autocomplete="tel">
    <label for="c-msg">Tell me about your child's math needs</label><textarea id="c-msg" name="message" required placeholder="Grade, curriculum and topics to work on"></textarea>
    <button type="submit" class="btn">Send Message</button>
    <p class="form-status" role="status" aria-live="polite"></p>
  </form></div>
</div></section>'''
    build_page("contact.html", "Contact Shaifali Jain | Book a Free Math Consultation",
               f"Contact Shaifali Jain for online math tutoring. Call or WhatsApp {PHONE_SHOW}, email {EMAIL}, or send a message to book a free consultation.",
               "contact.html", body,
               jsonld({"@context": "https://schema.org", "@type": "ContactPage", "name": "Contact", "url": SITE_URL + "/contact.html"}) + bc_schema([("Home", ""), ("Contact", "contact.html")]))

def thankyou():
    body = f'''
<section class="thanks"><div class="container narrow center">
  <div class="tick" aria-hidden="true">✓</div>
  <h1 id="ty-title">Thank you! Your message has been sent.</h1>
  <p id="ty-text">I have received your details and will reply on WhatsApp, call or email within 24 hours. In a hurry? Message me directly.</p>
  <p><a class="btn btn-wa" href="{WA_GENERAL}" target="_blank" rel="noopener">Chat on WhatsApp</a>
  <a class="btn" href="index.html">Back to Home</a></p>
  <p class="center-note">While you wait, explore <a href="services.html">my services</a>, <a href="blog/index.html">the math blog</a> or <a href="faq.html">the FAQ</a>.</p>
</div></section>'''
    build_page("thank-you.html", "Thank You | Shaifali Jain Math Tutoring", "Thank you for contacting Shaifali Jain Math Tutoring.", "", body, noindex=True)

def blog_index():
    bc = [("Blog", None)]
    cards = "".join(blog_card(p, 1) for p in POSTS[::-1])
    body = page_hero("Math Blog", "Tips, study plans and guides for students and parents.", crumbs(bc, 1), ) + f'<section><div class="container"><div class="blog-grid">{cards}</div></div></section>' + cta_band(1)
    body = body.replace('href="index.html"', 'href="../index.html"')
    build_page("blog/index.html", "Math Blog | Study Tips for Students & Parents",
               "Read practical online math tutoring tips: algebra help, exam revision plans, choosing a tutor and building confidence in math.",
               "blog/index.html", body, bc_schema([("Home", ""), ("Blog", "blog/index.html")]))

def blog_posts():
    for i, p in enumerate(POSTS):
        others = [q for q in POSTS if q is not p][:3]
        rel = "".join(f'<li><a href="{q["slug"]}.html">{q["title"]}</a></li>' for q in others)
        url = f'blog/{p["slug"]}.html'
        schema = jsonld({"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"],
                         "description": p["desc"], "datePublished": p["date"], "dateModified": p["date"],
                         "author": {"@type": "Person", "name": "Shaifali Jain"},
                         "publisher": {"@type": "Organization", "name": BRAND},
                         "mainEntityOfPage": f"{SITE_URL}/{url}"}) + bc_schema([("Home", ""), ("Blog", "blog/index.html"), (p["title"], url)])
        d = datetime.date.fromisoformat(p["date"]).strftime("%d %B %Y")
        body = f'''<article class="container narrow article">
  {crumbs([("Blog", "blog/index.html"), (p["title"], None)], 1)}
  <h1>{p["title"]}</h1>
  <p class="meta">By Shaifali Jain &middot; <time datetime="{p["date"]}">{d}</time></p>
  {p["body"]}
  <div class="article-cta"><strong>Need help with math?</strong> <a class="btn btn-wa" href="{WA_GENERAL}" target="_blank" rel="noopener">Chat on WhatsApp</a></div>
  <h2>More articles</h2><ul class="curriculum-list">{rel}</ul>
</article>'''
        build_page(url, f'{p["title"]} | Shaifali Jain Math Blog', p["desc"], "blog/index.html", body, schema, og_type="article")

def legal():
    bc = [("Privacy Policy", None)]
    build_page("privacy-policy.html", "Privacy Policy | Shaifali Jain Math Tutoring", "How Shaifali Jain Math Tutoring collects and uses information submitted through the website forms.", "",
      page_hero("Privacy Policy", f"Last updated: {TODAY}", crumbs(bc, 0)) + f'''<section><div class="container narrow article">
<h2>Information we collect</h2><p>When you use the contact or feedback form, we receive the details you enter: name, email, phone number and message. Forms are delivered to us by Web3Forms, a third-party form service.</p>
<h2>How we use it</h2><p>We use your details only to reply to your enquiry, arrange classes and, if you submit feedback with consent, display it on this website. We do not sell your information.</p>
<h2>WhatsApp</h2><p>If you click a WhatsApp button, you will be taken to WhatsApp and your conversation is subject to WhatsApp's own policy.</p>
<h2>Your choices</h2><p>To ask us to correct or delete your details, email <a data-c="mail" href="mailto:{EMAIL}"><span data-c="email-text">{EMAIL}</span></a>.</p></div></section>''', noindex=False)
    build_page("terms.html", "Terms of Use | Shaifali Jain Math Tutoring", "Terms for using the Shaifali Jain Math Tutoring website and booking online classes.", "",
      page_hero("Terms of Use", f"Last updated: {TODAY}", crumbs([("Terms", None)], 0)) + f'''<section><div class="container narrow article">
<h2>Classes</h2><p>Class timings, fees and number of sessions are agreed with the student or parent before classes begin.</p>
<h2>Cancellation</h2><p>Please give at least 24 hours' notice to reschedule or cancel a session.</p>
<h2>Results</h2><p>Progress depends on the student's effort and consistency. Marks and results cannot be guaranteed.</p>
<h2>Website content</h2><p>Content on this website is for general information and may not be copied without permission.</p>
<h2>Contact</h2><p>Questions? Email <a data-c="mail" href="mailto:{EMAIL}"><span data-c="email-text">{EMAIL}</span></a>.</p></div></section>''')

def notfound():
    html = head("Page Not Found | Shaifali Jain Math Tutoring", "The page you are looking for could not be found.", "404.html", 0, noindex=True)
    html = html.replace('href="css/style.css"', f'href="{BASE_PATH}/css/style.css"')
    hd = header("", 0).replace('href="', f'href="{BASE_PATH}/').replace(f'href="{BASE_PATH}/https', 'href="https').replace(f'href="{BASE_PATH}/tel', 'href="tel')
    ft = footer(0).replace('href="', f'href="{BASE_PATH}/').replace('src="js', f'src="{BASE_PATH}/js').replace(f'href="{BASE_PATH}/https', 'href="https').replace(f'href="{BASE_PATH}/tel', 'href="tel').replace(f'href="{BASE_PATH}/mailto', 'href="mailto')
    body = f'<main id="main"><section class="thanks"><div class="container narrow center"><h1>Page not found</h1><p>Sorry, that page does not exist or has moved.</p><p><a class="btn" href="{BASE_PATH}/index.html">Go to Home</a> <a class="btn btn-wa" href="{BASE_PATH}/contact.html">Contact Me</a></p></div></section></main>'
    write("404.html", html + hd + body + ft)

def seo_files():
    urls = ["index.html", "about.html", "services.html", "pricing.html", "testimonials.html", "faq.html", "contact.html",
            "blog/index.html", "privacy-policy.html", "terms.html"] + [f'blog/{p["slug"]}.html' for p in POSTS]
    x = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        loc = SITE_URL + "/" if u == "index.html" else f"{SITE_URL}/{u}"
        x += f"  <url><loc>{loc}</loc><lastmod>{TODAY}</lastmod></url>\n"
    write("sitemap.xml", x + "</urlset>\n")
    write(".nojekyll", "")
    if CUSTOM_DOMAIN: write("CNAME", CUSTOM_DOMAIN + "\n")
    write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /thank-you.html\n\nSitemap: {SITE_URL}/sitemap.xml\n")

if __name__ == "__main__":
    home(); about(); services(); pricing(); testimonials(); faq(); contact(); thankyou()
    blog_index(); blog_posts(); legal(); notfound(); seo_files()
    print("Site built in", OUT)
