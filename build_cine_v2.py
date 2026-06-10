import re
from bs4 import BeautifulSoup

# Read template
with open('subpage/applications/audio-distribuido.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix relative paths
html = html.replace('../../style.css', '../style.css')
html = html.replace('../../assets/', '../assets/')
html = html.replace('../../index.html', '../index.html')
html = html.replace('audio-distribuido.html', 'cine_en_casa.html')

soup = BeautifulSoup(html, 'html.parser')

# Read Example
with open('example/WEB DG Audiosound/01 Home/aplicaciones/residencial-premium/cine-en-casa-dg-audiosound.html', 'r', encoding='utf-8') as f:
    ex_html = f.read()

ex_soup = BeautifulSoup(ex_html, 'html.parser')

# Meta
soup.title.string = ex_soup.title.string
if ex_soup.find('meta', {'name': 'description'}):
    soup.find('meta', {'name': 'description'})['content'] = ex_soup.find('meta', {'name': 'description'})['content']

# HERO
ex_hero = ex_soup.find('section', class_='hero')
hero = soup.find('section', class_='corp-hero-v2')
if hero and ex_hero:
    # Set kicker
    kicker = hero.find(class_='hero-kicker')
    if kicker: kicker.string = "Aplicaciones: Cine en Casa"
    
    # Set H1
    h1 = hero.find('h1')
    ex_h1 = ex_hero.find('h1')
    if h1 and ex_h1:
        h1.clear()
        for c in ex_h1.contents:
            if c.name == 'span':
                new_span = soup.new_tag('span', attrs={'class': 'text-accent'})
                new_span.string = c.string
                h1.append(new_span)
            else:
                h1.append(str(c))
                
    # Subtitle
    sub = hero.find(class_='hero-subtitle')
    ex_ps = ex_hero.find_all('p')
    if sub and len(ex_ps) >= 2:
        sub.clear()
        sub.append(ex_ps[0].text)
        sub.append(soup.new_tag('br'))
        sub.append(soup.new_tag('br'))
        sub.append(ex_ps[1].text)
        
    # Badges
    badges = hero.find_all(class_='hero-badge-item')
    ex_badges = ex_hero.find(class_='hero-badges').find_all('span')
    icons = ["fa-solid fa-video", "fa-solid fa-volume-high", "fa-solid fa-compact-disc", "fa-solid fa-screwdriver-wrench"]
    for i, b in enumerate(badges):
        if i < len(ex_badges):
            b.find('span').string = ex_badges[i].text
            b.find('i')['class'] = icons[i]
            
    # Set the hero image
    slides = hero.find_all(class_='slide')
    ex_img = ex_hero.find('img')
    if ex_img:
        # Use exact src but adjust for subpage directory (add ..)
        # example src is /assets/img/... so it becomes ../assets/img/...
        src = ".." + ex_img['src']
        for s in slides:
            s['style'] = f"background-image: url('{src}');"
            # Just set the first image on all slides to make sure it loads, or only keep 1 slide
            
# Section 2
s2 = soup.find_all('section')[1]
ex_s2 = ex_soup.find_all('section')[1] # the first two-col
if s2 and ex_s2:
    s2.find('h2').clear()
    for c in ex_s2.find('h2').contents:
        if c.name == 'span':
            span = soup.new_tag('span', attrs={'class': 'text-accent'})
            span.string = c.string
            s2.find('h2').append(span)
        else:
            s2.find('h2').append(str(c))
            
    ps = s2.find_all('p', recursive=True)
    ex_ps = ex_s2.find_all('p', recursive=False)
    if len(ps) >= 2 and len(ex_ps) >= 2:
        ps[0].string = ex_ps[0].text
        ps[1].string = ex_ps[1].text
        
    img = s2.find('img')
    ex_img = ex_s2.find('img')
    if img and ex_img: img['src'] = ".." + ex_img['src']

    # Grid
    b_grid = s2.find(class_='benefits-corp-grid')
    ex_items = ex_s2.find_all(class_='benefit-card')
    if b_grid and ex_items:
        cards = b_grid.find_all(class_='benefit-v2-card')
        for i, c in enumerate(cards):
            if i < len(ex_items):
                c.find('h3').string = ex_items[i].find('h3').text
                c.find('p').string = ex_items[i].find('p').text

# Section 3: Antitesis
s3 = soup.find_all('section')[2]
ex_s3 = ex_soup.find_all('section')[2]
if s3 and ex_s3:
    s3.find('h2').clear()
    for c in ex_s3.find('h2').contents:
        if c.name == 'span':
            span = soup.new_tag('span', attrs={'class': 'text-accent'})
            span.string = c.string
            s3.find('h2').append(span)
        else:
            s3.find('h2').append(str(c))
            
    p = s3.find('p')
    ex_ps = ex_s3.find_all('p', recursive=False)
    if p and len(ex_ps) >= 2:
        p.clear()
        p.append(ex_ps[0].text)
        p.append(soup.new_tag('br'))
        p.append(soup.new_tag('br'))
        p.append(ex_ps[1].text)
        
    img = s3.find('img', class_='antithesis-main-img')
    ex_img = ex_s3.find('img')
    if img and ex_img: img['src'] = ".." + ex_img['src']
    
    problems = s3.find_all(class_='antithesis-problem-card')
    ex_probs = ex_s3.find_all(class_='problem-card')
    for i, pc in enumerate(problems):
        if i < len(ex_probs):
            pc.find('h3').string = ex_probs[i].find('h3').text
            pc.find('p').string = ex_probs[i].find('p').text

# Section 4: Soluciones Integrales (Qué incluye)
s4 = soup.find_all('section')[3]
ex_s4 = ex_soup.find_all('section')[4] # Qué incluye la solución
if s4 and ex_s4:
    s4.find('h2').clear()
    ex_h2 = ex_s4.find('h2')
    if ex_h2:
        for c in ex_h2.contents:
            if c.name == 'span':
                span = soup.new_tag('span', attrs={'class': 'text-accent'})
                span.string = c.string
                s4.find('h2').append(span)
            else:
                s4.find('h2').append(str(c))
            
    ps = s4.find('p')
    ex_p = ex_s4.find('p', recursive=False)
    if ps and ex_p: ps.string = ex_p.text
    
    incl = s4.find_all(class_='include-card')
    ex_incl = ex_s4.find_all(class_='feature-card')
    for i, ic in enumerate(incl):
        if i < len(ex_incl):
            ex_h3 = ex_incl[i].find('h3').text
            ex_p_text = ex_incl[i].find('p').text
            ic.find('p').string = ex_p_text
            # keep icon, update text
            i_tag = ic.find('i')
            ic.find('h3').clear()
            if i_tag: ic.find('h3').append(i_tag)
            ic.find('h3').append(" " + ex_h3)

# Section 5: Áreas del Hogar
s5 = soup.find_all('section')[4]
ex_s5 = ex_soup.find_all('section')[5] # Opciones de cine en casa
if s5 and ex_s5:
    s5.find('h2').clear()
    for c in ex_s5.find('h2').contents:
        if c.name == 'span':
            span = soup.new_tag('span', attrs={'class': 'text-accent'})
            span.string = c.string
            s5.find('h2').append(span)
        else:
            s5.find('h2').append(str(c))
            
    ps = s5.find('p')
    ex_p = ex_s5.find('p', recursive=False)
    if ps and ex_p: ps.string = ex_p.text
    
    # We might have more areas in ex_s5. Let's create enough area-cards
    area_grid = s5.find(class_='area-grid')
    ex_areas = ex_s5.find_all(class_='area-card')
    if area_grid and ex_areas:
        area_grid.clear()
        for ex_a in ex_areas:
            new_card = soup.new_tag('div', attrs={'class': 'area-card'})
            img_tag = soup.new_tag('img', src=".." + ex_a.find('img')['src'], alt=ex_a.find('img').get('alt', ''))
            span_tag = soup.new_tag('span')
            span_tag.string = ex_a.find('span').text
            new_card.append(img_tag)
            new_card.append(span_tag)
            area_grid.append(new_card)

# Section 6: Banner (Eventos/Modernizacion)
s6 = soup.find_all('section')[5]
ex_s6 = ex_soup.find_all('section')[8] # Prepárate para vivir tus eventos...
if s6 and ex_s6:
    s6.find('h2').string = ex_s6.find('h2').text
    p = s6.find('p')
    ex_p = ex_s6.find('p')
    if p and ex_p: p.string = ex_p.text
    img = s6.find('img')
    ex_img = ex_s6.find('img')
    if img and ex_img: img['src'] = ".." + ex_img['src']

# Section 7: Proceso
s7 = soup.find_all('section')[6]
ex_s7 = ex_soup.find_all('section')[9] # Proceso claro
if s7 and ex_s7:
    s7.find('h2').clear()
    for c in ex_s7.find('h2').contents:
        if c.name == 'span':
            span = soup.new_tag('span', attrs={'class': 'text-accent'})
            span.string = c.string
            s7.find('h2').append(span)
        else:
            s7.find('h2').append(str(c))
            
    b_items = s7.find_all(class_='process-bento-item')
    ex_steps = ex_s7.find_all(class_='process-step')
    for i, it in enumerate(b_items):
        if i < len(ex_steps):
            it.find('h3').string = ex_steps[i].find('h3').text
            it.find('p').string = ex_steps[i].find('p').text
            
    # if ex_steps has more than 4, add them
    if len(ex_steps) > 4:
        grid = s7.find(class_='benefits-corp-grid') or s7.find(class_='include-grid') # check actual grid class for process
        # Wait, process bento grid is inside something
        grid = b_items[0].parent
        for i in range(4, len(ex_steps)):
            new_item = BeautifulSoup(str(b_items[0]), 'html.parser').div
            new_item.find('h3').string = ex_steps[i].find('h3').text
            new_item.find('p').string = ex_steps[i].find('p').text
            new_item.find(class_='bento-num').string = str(i+1)
            grid.append(new_item)

# Section 8: Split Dark / Gold
s8 = soup.find_all('section')[7]
ex_s8_dark = ex_soup.find_all('section')[10]
ex_s8_gold = ex_soup.find_all('section')[11]
if s8:
    dark = s8.find(class_='dark-panel')
    if dark and ex_s8_dark:
        dark.find('h2').string = ex_s8_dark.find('h2').text
        ps = dark.find_all('p')
        ex_ps = ex_s8_dark.find_all('p')
        for i, p in enumerate(ps):
            if i < len(ex_ps): p.string = ex_ps[i].text
            
    gold = s8.find(class_='gold-panel')
    if gold and ex_s8_gold:
        gold.find('h2').string = ex_s8_gold.find('h2').text
        lis = gold.find_all('li')
        ex_lis = ex_s8_gold.find_all('li')
        for i, li in enumerate(lis):
            if i < len(ex_lis): li.string = ex_lis[i].text

# Section 9: FAQ
s9 = soup.find_all('section')[8]
ex_s9 = ex_soup.find_all('section')[12]
if s9 and ex_s9:
    s9.find('h2').clear()
    for c in ex_s9.find('h2').contents:
        if c.name == 'span':
            span = soup.new_tag('span', attrs={'class': 'text-accent'})
            span.string = c.string
            s9.find('h2').append(span)
        else:
            s9.find('h2').append(str(c))
            
    faqs = s9.find_all(class_='faq-lux-item')
    ex_faqs = ex_s9.find_all(class_='faq-item')
    faq_wrapper = faqs[0].parent
    faq_wrapper.clear()
    
    for ex_faq in ex_faqs:
        new_faq = soup.new_tag('div', attrs={'class': 'faq-lux-item'})
        btn = soup.new_tag('button', attrs={'class': 'faq-lux-btn'})
        span_q = soup.new_tag('span')
        span_q.string = ex_faq.find(class_='faq-question').find_all('span')[0].text
        span_icon = soup.new_tag('span')
        span_icon.string = "+"
        btn.append(span_q)
        btn.append(span_icon)
        
        answer = soup.new_tag('div', attrs={'class': 'faq-lux-answer'})
        p = soup.new_tag('p')
        p.string = ex_faq.find(class_='faq-answer').find('p').text
        answer.append(p)
        
        new_faq.append(btn)
        new_faq.append(answer)
        faq_wrapper.append(new_faq)

with open('subpage/cine_en_casa.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Modificaciones listas con EXACTAMENTE los textos e imágenes del archivo de ejemplo.")
