import re
import os
from bs4 import BeautifulSoup

def process_app(example_path, output_filename):
    with open('subpage/applications/audio-distribuido.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Base fixes for paths
    html = html.replace('../../style.css', '../style.css')
    html = html.replace('../../assets/', '../assets/')
    html = html.replace('../../index.html', '../index.html')
    html = html.replace('audio-distribuido.html', output_filename)

    soup = BeautifulSoup(html, 'html.parser')

    with open(example_path, 'r', encoding='utf-8') as f:
        ex_html = f.read()

    ex_soup = BeautifulSoup(ex_html, 'html.parser')

    # Meta
    if ex_soup.title: soup.title.string = ex_soup.title.string
    desc = ex_soup.find('meta', {'name': 'description'})
    if desc:
        soup_desc = soup.find('meta', {'name': 'description'})
        if soup_desc: soup_desc['content'] = desc['content']

    ex_sections = ex_soup.find_all('section')
    if not ex_sections: return

    def get_main_paragraphs(section):
        ps = []
        for p in section.find_all('p'):
            parent_classes = []
            for parent in p.parents:
                if parent.get('class'):
                    parent_classes.extend(parent.get('class'))
            if not any('card' in c for c in parent_classes) and not any('step' in c for c in parent_classes) and not any('item' in c for c in parent_classes):
                ps.append(p)
        return ps

    def fix_img_src(src):
        if src.startswith('/assets/'):
            return ".." + src
        return src

    # HERO
    hero = soup.find('section', class_='corp-hero-v2')
    ex_hero = ex_sections[0]
    if hero and ex_hero:
        kicker = hero.find(class_='hero-kicker')
        ex_kicker = ex_hero.find(class_='eyebrow')
        if kicker and ex_kicker: kicker.string = ex_kicker.text
        
        h1 = hero.find('h1')
        ex_h1 = ex_hero.find('h1')
        if h1 and ex_h1:
            h1.clear()
            for c in ex_h1.contents:
                if c.name == 'span':
                    new_span = soup.new_tag('span', attrs={'class': 'text-accent'})
                    new_span.string = c.text
                    h1.append(new_span)
                else:
                    h1.append(str(c))
                    
        sub = hero.find(class_='hero-subtitle')
        ex_ps = ex_hero.find_all('p', class_='lead')
        if sub and len(ex_ps) >= 2:
            sub.clear()
            sub.append(ex_ps[0].text)
            sub.append(soup.new_tag('br'))
            sub.append(soup.new_tag('br'))
            sub.append(ex_ps[1].text)
        elif sub and len(ex_ps) == 1:
            sub.clear()
            sub.append(ex_ps[0].text)
            
        badges_wrapper = hero.find(class_='hero-badges')
        if badges_wrapper: badges_wrapper.decompose()
                
        slides = hero.find_all(class_='slide')
        ex_img = ex_hero.find('img')
        if ex_img:
            src = fix_img_src(ex_img['src'])
            for i, s in enumerate(slides):
                if i == 0:
                    s['style'] = f"background-image: url('{src}');"
                else:
                    s.decompose()

    # Section 2: Apertura emocional
    s2 = soup.find(class_='section-light')
    ex_s2 = ex_sections[1] if len(ex_sections) > 1 else None
    if s2 and ex_s2:
        h2 = s2.find('h2')
        ex_h2 = ex_s2.find('h2')
        if h2 and ex_h2:
            h2.clear()
            for c in ex_h2.contents:
                if c.name == 'span':
                    span = soup.new_tag('span', attrs={'class': 'text-accent'})
                    span.string = c.text
                    h2.append(span)
                else:
                    h2.append(str(c))
                
        ps = s2.find_all('p', recursive=True)
        soup_main_ps = []
        for p in ps:
            if 'benefit-v2-card' not in str(p.parent): soup_main_ps.append(p)

        ex_ps = get_main_paragraphs(ex_s2)
        if len(soup_main_ps) >= 2 and len(ex_ps) >= 2:
            soup_main_ps[0].string = ex_ps[0].text
            soup_main_ps[1].string = ex_ps[1].text
        elif len(soup_main_ps) >= 1 and len(ex_ps) >= 1:
            soup_main_ps[0].string = ex_ps[0].text
            
        img = s2.find('img')
        ex_img = ex_s2.find('img')
        if img and ex_img: img['src'] = fix_img_src(ex_img['src'])

        b_grid = s2.find(class_='benefits-corp-grid')
        ex_items = ex_s2.find_all(class_='mini-card')
        if b_grid and ex_items:
            cards = b_grid.find_all(class_='benefit-v2-card')
            for i, c in enumerate(cards):
                if i < len(ex_items):
                    c.find('h3').string = ex_items[i].find('h3').text
                    c.find('p').string = ex_items[i].find('p').text

    # Section 3: Antitesis
    s3 = soup.find(class_='lux-dark-section')
    ex_s3 = ex_sections[2] if len(ex_sections) > 2 else None
    if s3 and ex_s3:
        h2 = s3.find('h2')
        ex_h2 = ex_s3.find('h2')
        if h2 and ex_h2:
            h2.clear()
            for c in ex_h2.contents:
                if c.name == 'span':
                    span = soup.new_tag('span', attrs={'class': 'text-accent'})
                    span.string = c.text
                    h2.append(span)
                else:
                    h2.append(str(c))
                
        p = s3.find('p')
        ex_ps = get_main_paragraphs(ex_s3)
        if p and len(ex_ps) >= 2:
            p.clear()
            p.append(ex_ps[0].text)
            p.append(soup.new_tag('br'))
            p.append(soup.new_tag('br'))
            p.append(ex_ps[1].text)
        elif p and len(ex_ps) >= 1:
            p.clear()
            p.append(ex_ps[0].text)
            
        img = s3.find('img', class_='antithesis-main-img')
        ex_img = ex_s3.find('img')
        if img and ex_img: img['src'] = fix_img_src(ex_img['src'])
        
        problems = s3.find_all(class_='antithesis-problem-card')
        ex_probs = ex_s3.find_all(class_='mini-card')
        for i, pc in enumerate(problems):
            if i < len(ex_probs):
                pc.find('h3').string = ex_probs[i].find('h3').text
                pc.find('p').string = ex_probs[i].find('p').text

    # Section 4: Soluciones Integrales (Qué incluye)
    ex_s4 = None
    for s in ex_sections:
        if "Qué incluye" in s.text or "Que incluye" in s.text:
            ex_s4 = s
            break

    s4 = soup.find(id='incluye')
    if s4 and ex_s4:
        h2 = s4.find('h2')
        ex_h2 = ex_s4.find('h2')
        if h2 and ex_h2:
            h2.clear()
            for c in ex_h2.contents:
                if c.name == 'span':
                    span = soup.new_tag('span', attrs={'class': 'text-accent'})
                    span.string = c.text
                    h2.append(span)
                else:
                    h2.append(str(c))
                
        ex_p = get_main_paragraphs(ex_s4)
        soup_p = None
        for p in s4.find_all('p'):
            if 'include-card' not in str(p.parent):
                soup_p = p
                break
        if soup_p and ex_p: soup_p.string = ex_p[0].text
        
        incl = s4.find_all(class_='include-card')
        ex_incl = ex_s4.find_all(class_='included-item')
        
        if len(ex_incl) > len(incl) and len(incl) > 0:
            grid = incl[0].parent
            for i in range(len(incl), len(ex_incl)):
                new_item = BeautifulSoup(str(incl[0]), 'html.parser').div
                grid.append(new_item)
            incl = s4.find_all(class_='include-card')
            
        for i, ic in enumerate(incl):
            if i < len(ex_incl):
                strong_tag = ex_incl[i].find('strong')
                ex_h3 = strong_tag.text if strong_tag else ""
                p_tag = ex_incl[i].find('p')
                ex_p_text = p_tag.text if p_tag else ""
                
                ic.find('p').string = ex_p_text
                i_tag = ic.find('i')
                h3_tag = ic.find('h3')
                if h3_tag:
                    h3_tag.clear()
                    if i_tag: h3_tag.append(i_tag)
                    h3_tag.append(" " + ex_h3)

    # Clean Extra Section
    extra_section = soup.find('section', class_='section-white') 
    if extra_section and not extra_section.find(class_='area-grid'):
        if extra_section.find(class_='benefits-corp-grid'):
            extra_section.decompose()

    # Section 5: Áreas
    ex_s5 = None
    for s in ex_sections:
        if s.find(class_='area-card'):
            ex_s5 = s
            break

    s5 = None
    for s in soup.find_all('section'):
        if s.find(class_='area-grid'):
            s5 = s
            break

    if s5 and ex_s5:
        h2 = s5.find('h2')
        ex_h2 = ex_s5.find('h2')
        if h2 and ex_h2:
            h2.clear()
            for c in ex_h2.contents:
                if c.name == 'span':
                    span = soup.new_tag('span', attrs={'class': 'text-accent'})
                    span.string = c.text
                    h2.append(span)
                else:
                    h2.append(str(c))
                
        ex_p = get_main_paragraphs(ex_s5)
        soup_p = None
        for p in s5.find_all('p'):
            if 'area-card' not in str(p.parent):
                soup_p = p
                break
        if soup_p and ex_p: soup_p.string = ex_p[0].text
        
        area_grid = s5.find(class_='area-grid')
        ex_areas = ex_s5.find_all(class_='area-card')
        if area_grid and ex_areas:
            area_grid.clear()
            for ex_a in ex_areas:
                new_card = soup.new_tag('div', attrs={'class': 'area-card'})
                ex_img_tag = ex_a.find('img')
                ex_span_tag = ex_a.find('span') or ex_a.find('p')
                if ex_img_tag:
                    img_tag = soup.new_tag('img', src=fix_img_src(ex_img_tag['src']), alt=ex_img_tag.get('alt', ''))
                    new_card.append(img_tag)
                if ex_span_tag:
                    span_tag = soup.new_tag('span')
                    span_tag.string = ex_span_tag.text
                    new_card.append(span_tag)
                area_grid.append(new_card)

    # Section 6: Banner
    ex_s6 = None
    for s in ex_sections:
        if s.find(class_='event-img') or s.find(class_='modernization-img'):
            ex_s6 = s
            break

    s6 = None
    for s in soup.find_all('section'):
        if s.find(class_='event-banner') or s.find(class_='modernization-banner'):
            s6 = s
            break

    if s6 and ex_s6:
        if s6.find('h2') and ex_s6.find('h2'): s6.find('h2').string = ex_s6.find('h2').text
        if s6.find('p') and ex_s6.find('p'): s6.find('p').string = ex_s6.find('p').text
        if s6.find('img') and ex_s6.find('img'): s6.find('img')['src'] = fix_img_src(ex_s6.find('img')['src'])

    # Section 7: Proceso
    ex_s7 = None
    for s in ex_sections:
        if s.find(class_='process-step'):
            ex_s7 = s
            break

    s7 = soup.find(id='proceso')
    if s7 and ex_s7:
        h2 = s7.find('h2')
        ex_h2 = ex_s7.find('h2')
        if h2 and ex_h2:
            h2.clear()
            for c in ex_h2.contents:
                if c.name == 'span':
                    span = soup.new_tag('span', attrs={'class': 'text-accent'})
                    span.string = c.text
                    h2.append(span)
                else:
                    h2.append(str(c))
                
        b_items = s7.find_all(class_='process-bento-item')
        ex_steps = ex_s7.find_all(class_='process-step')
        
        if len(ex_steps) > len(b_items) and len(b_items) > 0:
            grid = b_items[0].parent
            for i in range(len(b_items), len(ex_steps)):
                new_item = BeautifulSoup(str(b_items[0]), 'html.parser').div
                grid.append(new_item)
            b_items = s7.find_all(class_='process-bento-item')
            
        for i, it in enumerate(b_items):
            if i < len(ex_steps):
                it.find('h3').string = ex_steps[i].find('h3').text
                it.find('p').string = ex_steps[i].find('p').text
                num = it.find(class_='bento-num')
                if num: num.string = str(i+1)

    # Section 8: Split Dark / Gold
    ex_s8_dark = None
    ex_s8_gold = None
    for s in ex_sections:
        h2 = s.find('h2')
        if h2 and ("No vendemos cajas" in h2.text or "no vendemos cajas" in h2.text.lower()):
            ex_s8_dark = s
        if h2 and ("decisión" in h2.text.lower() or "profesional" in h2.text.lower()):
            ex_s8_gold = s

    s8 = None
    for s in soup.find_all('section'):
        if s.find(class_='dark-panel'):
            s8 = s
            break

    if s8:
        dark = s8.find(class_='dark-panel')
        if dark and ex_s8_dark:
            if dark.find('h2') and ex_s8_dark.find('h2'): dark.find('h2').string = ex_s8_dark.find('h2').text
            ps = dark.find_all('p')
            ex_ps = ex_s8_dark.find_all('p')
            for i, p in enumerate(ps):
                if i < len(ex_ps): p.string = ex_ps[i].text
                
        gold = s8.find(class_='gold-panel')
        if gold and ex_s8_gold:
            if gold.find('h2') and ex_s8_gold.find('h2'): gold.find('h2').string = ex_s8_gold.find('h2').text
            lis = gold.find_all('li')
            ex_lis = ex_s8_gold.find_all('li')
            if len(ex_lis) > len(lis) and len(lis) > 0:
                ul = lis[0].parent
                for i in range(len(lis), len(ex_lis)):
                    new_li = soup.new_tag('li')
                    ul.append(new_li)
                lis = gold.find_all('li')
                
            for i, li in enumerate(lis):
                if i < len(ex_lis): li.string = ex_lis[i].text

    # Section 9: FAQ
    ex_s9 = None
    for s in ex_sections:
        if s.find(class_='faq-item'):
            ex_s9 = s
            break

    s9 = soup.find(id='faq')
    if s9 and ex_s9:
        h2 = s9.find('h2')
        ex_h2 = ex_s9.find('h2')
        if h2 and ex_h2:
            h2.clear()
            for c in ex_h2.contents:
                if c.name == 'span':
                    span = soup.new_tag('span', attrs={'class': 'text-accent'})
                    span.string = c.text
                    h2.append(span)
                else:
                    h2.append(str(c))
                
        faqs = s9.find_all(class_='faq-lux-item')
        ex_faqs = ex_s9.find_all(class_='faq-item')
        if faqs and ex_faqs:
            faq_wrapper = faqs[0].parent
            faq_wrapper.clear()
            
            for ex_faq in ex_faqs:
                new_faq = soup.new_tag('div', attrs={'class': 'faq-lux-item'})
                btn = soup.new_tag('button', attrs={'class': 'faq-lux-btn'})
                span_q = soup.new_tag('span')
                question_text = ""
                q_spans = ex_faq.find(class_='faq-question').find_all('span')
                if q_spans: question_text = q_spans[0].text
                else: question_text = ex_faq.find(class_='faq-question').text
                span_q.string = question_text
                span_icon = soup.new_tag('span')
                span_icon.string = "+"
                btn.append(span_q)
                btn.append(span_icon)
                
                answer = soup.new_tag('div', attrs={'class': 'faq-lux-answer'})
                p = soup.new_tag('p')
                a_p = ex_faq.find(class_='faq-answer').find('p')
                if a_p: p.string = a_p.text
                answer.append(p)
                
                new_faq.append(btn)
                new_faq.append(answer)
                faq_wrapper.append(new_faq)

    with open(f'subpage/applications/{output_filename}', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Created: {output_filename}")

mappings = [
    ("example/WEB DG Audiosound/01 Home/aplicaciones/eventos-creadores-y-produccion/audio-musicos-vocalistas-dg-audiosound.html", "musicos-vocalistas.html"),
    ("example/WEB DG Audiosound/01 Home/aplicaciones/eventos-creadores-y-produccion/audio-profesional-sonidos-dj-dg-audiosound.html", "sonidos-dj.html"),
    ("example/WEB DG Audiosound/01 Home/aplicaciones/eventos-creadores-y-produccion/audio-video-centros-de-culto-dg-audiosound.html", "centros-de-culto.html"),
    ("example/WEB DG Audiosound/01 Home/aplicaciones/eventos-creadores-y-produccion/audio-video-cine-independiente-dg-audiosound.html", "cine-independiente.html"),
    ("example/WEB DG Audiosound/01 Home/aplicaciones/eventos-creadores-y-produccion/audio-video-podcast-dg-audiosound.html", "podcast.html"),
    ("example/WEB DG Audiosound/01 Home/aplicaciones/eventos-creadores-y-produccion/audio-video-streamers-dg-audiosound.html", "streamers.html")
]

for src, out in mappings:
    process_app(src, out)

print("Todas las aplicaciones de eventos fueron creadas con exito.")
