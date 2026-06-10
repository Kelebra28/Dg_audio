import re
from bs4 import BeautifulSoup

# Template
with open('subpage/soluciones/residencial-premium.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix relative paths since it is saved in the same directory, we just rename
html = html.replace('residencial-premium.html', 'eventos-y-produccion.html')

soup = BeautifulSoup(html, 'html.parser')

# Example
with open('example/WEB DG Audiosound/01 Home/soluciones/eventos-creadores-produccion-dg-audiosound.html', 'r', encoding='utf-8') as f:
    ex_html = f.read()

ex_soup = BeautifulSoup(ex_html, 'html.parser')

# Meta
if ex_soup.title: soup.title.string = ex_soup.title.string
desc = ex_soup.find('meta', {'name': 'description'})
if desc:
    soup_desc = soup.find('meta', {'name': 'description'})
    if soup_desc: soup_desc['content'] = desc['content']

ex_sections = ex_soup.find_all('section')
if not ex_sections: exit()

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
        return "../" + src
    return src.replace('/assets/', '../../assets/')

# HERO
hero = soup.find('section', class_='corp-hero-v2') or soup.find('section', class_='hero')
ex_hero = ex_sections[0]
if hero and ex_hero:
    kicker = hero.find(class_='hero-kicker') or hero.find(class_='eyebrow')
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
                
    sub = hero.find(class_='hero-subtitle') or hero.find('p', class_='lead')
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
        
    slides = hero.find_all(class_='slide')
    ex_img = ex_hero.find('img')
    if ex_img:
        src = fix_img_src(ex_img['src'])
        if slides:
            for i, s in enumerate(slides):
                if i == 0:
                    s['style'] = f"background-image: url('{src}');"
                else:
                    s.decompose()
        else:
            img_tag = hero.find('img')
            if img_tag: img_tag['src'] = src

# App grid!
app_grid_section = soup.find(id='aplicaciones')
ex_app_grid_section = ex_soup.find(id='aplicaciones')
if app_grid_section and ex_app_grid_section:
    h2 = app_grid_section.find('h2')
    ex_h2 = ex_app_grid_section.find('h2')
    if h2 and ex_h2: h2.string = ex_h2.text

    apps = app_grid_section.find_all(class_='app-corp-card')
    ex_apps = ex_app_grid_section.find_all(class_='card') or ex_app_grid_section.find_all(class_='application-card')
    
    if len(ex_apps) > len(apps) and len(apps) > 0:
        grid = apps[0].parent
        for i in range(len(apps), len(ex_apps)):
            new_item = BeautifulSoup(str(apps[0]), 'html.parser').div
            grid.append(new_item)
        apps = app_grid_section.find_all(class_='app-corp-card')
        
    urls = [
        "../applications/podcast.html",
        "../applications/streamers.html",
        "../applications/sonidos-dj.html",
        "../applications/centros-de-culto.html",
        "../applications/cine-independiente.html",
        "../applications/musicos-vocalistas.html"
    ]

    for i, a in enumerate(apps):
        if i < len(ex_apps):
            ex_a = ex_apps[i]
            h3_tag = ex_a.find('h3')
            p_tag = ex_a.find('p')
            if h3_tag and a.find('h3'): a.find('h3').string = h3_tag.text
            if p_tag and a.find('p'): a.find('p').string = p_tag.text
            
            img = a.find('img')
            ex_img = ex_a.find('img')
            if img and ex_img: img['src'] = fix_img_src(ex_img['src'])
            
            if i < len(urls):
                a['href'] = urls[i]
                link_btn = a.find(class_='app-link-text')
                if link_btn: link_btn.string = "Ver aplicación"

# Save the file
with open('subpage/soluciones/eventos-y-produccion.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Categoría de eventos generada con éxito.")
