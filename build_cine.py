import re
from bs4 import BeautifulSoup

# Read template
with open('subpage/applications/audio-distribuido.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix relative paths since cine_en_casa.html is one level up
html = html.replace('../../style.css', '../style.css')
html = html.replace('../../assets/', '../assets/')
html = html.replace('../../index.html', '../index.html')
# Keep canonical URL and specific og: tags correct
html = html.replace('audio-distribuido.html', 'cine_en_casa.html')

soup = BeautifulSoup(html, 'html.parser')

# Title & Meta
soup.title.string = "Cine en Casa Profesional | DG Audiosound"
desc = soup.find('meta', {'name': 'description'})
if desc: desc['content'] = "Diseño e instalación de cine en casa premium en CDMX y México. Audio envolvente, proyectores 4K, pantallas y Dolby Atmos."
kw = soup.find('meta', {'name': 'keywords'})
if kw: kw['content'] = "cine en casa, home theater, proyector 4k, audio envolvente, dolby atmos, pantalla de proyeccion"

# Hero Section
hero = soup.find('section', class_='corp-hero-v2')
if hero:
    kicker = hero.find(class_='hero-kicker')
    if kicker: kicker.string = "Aplicaciones: Cine en Casa"
    h1 = hero.find('h1')
    if h1:
        h1.clear()
        h1.append("Cine en casa premium para disfrutar películas, deportes y conciertos con ")
        span = soup.new_tag('span', attrs={'class': 'text-accent'})
        span.string = "sonido envolvente."
        h1.append(span)
    sub = hero.find(class_='hero-subtitle')
    if sub:
        sub.clear()
        sub.append("Diseñamos e instalamos sistemas de cine en casa a la medida con proyectores 4K, pantallas de gran formato, audio envolvente, subwoofers, receptores AV y soluciones compatibles con Dolby Atmos.")
        sub.append(soup.new_tag('br'))
        sub.append(soup.new_tag('br'))
        sub.append("En DG Audiosound no solo vendemos equipos: analizamos tu espacio, tus hábitos de uso y tu presupuesto para integrar una experiencia cómoda, estética y fácil de usar.")
    
    # Badges
    badges = hero.find_all(class_='hero-badge-item')
    texts = ["Proyectores 4K", "Audio envolvente", "Dolby Atmos", "Instalación Pro"]
    icons = ["fa-solid fa-video", "fa-solid fa-volume-high", "fa-solid fa-compact-disc", "fa-solid fa-screwdriver-wrench"]
    for i, b in enumerate(badges):
        if i < len(texts):
            b.find('span').string = texts[i]
            b.find('i')['class'] = icons[i]

    # Backgrounds
    slides = hero.find_all(class_='slide')
    bg_images = [
        "../assets/Imagenes/soluciones/Residencial premium/cine-en-casa-premium-dg-audiosound-hero.webp",
        "../assets/Imagenes/soluciones/Residencial premium/sala-cine-en-casa-proyector-4k-dg-audiosound.webp",
        "../assets/Imagenes/soluciones/Residencial premium/cuarto-dedicado-cine-en-casa-dg-audiosound.webp"
    ]
    for i, s in enumerate(slides):
        if i < len(bg_images):
            s['style'] = f"background-image: url('{bg_images[i]}');"

# Section 2: Apertura emocional (two-col)
s2 = soup.find_all('section')[1]
if s2:
    s2.find('h2').clear()
    s2.find('h2').append("Tu sala puede convertirse en el lugar ")
    span = soup.new_tag('span', attrs={'class': 'text-accent'})
    span.string = "favorito"
    s2.find('h2').append(span)
    s2.find('h2').append(" de tu casa.")
    
    ps = s2.find_all('p', recursive=True)
    if len(ps) >= 2:
        ps[0].string = "Un cine en casa bien diseñado transforma la forma en que vives una película, un partido, un concierto o una noche familiar. La diferencia no está solo en tener una pantalla grande, sino en lograr que imagen, sonido, comodidad y operación funcionen como una experiencia completa."
        ps[1].string = "Por eso analizamos el espacio antes de recomendar equipos. La distancia de visualización, la iluminación, la acústica, el tamaño de pantalla, la ubicación de bocinas y la forma de uso influyen directamente en el resultado final."
    
    img = s2.find('img')
    if img: img['src'] = "../assets/Imagenes/soluciones/Residencial premium/sala-cine-en-casa-proyector-4k-dg-audiosound.webp"
    
    # Benefits Corp Grid
    b_grid = s2.find(class_='benefits-corp-grid')
    if b_grid:
        cards = b_grid.find_all(class_='benefit-v2-card')
        b_texts = [
            ("Experiencia premium", "Imagen, sonido y confort diseñados para que cada función se sienta especial.", "fa-solid fa-star"),
            ("Uso diario", "Soluciones prácticas para películas, series, deportes, conciertos y videojuegos.", "fa-solid fa-calendar-day"),
            ("Escalable", "Podemos iniciar con una solución funcional y crecer hacia sistemas más avanzados.", "fa-solid fa-arrow-trend-up"),
            ("A la medida", "Cada recomendación se ajusta al espacio, presupuesto y expectativa del cliente.", "fa-solid fa-ruler-combined")
        ]
        for i, c in enumerate(cards):
            if i < len(b_texts):
                c.find('h3').string = b_texts[i][0]
                c.find('p').string = b_texts[i][1]
                c.find('i')['class'] = b_texts[i][2]

# Section 3: Antítesis (Problema puntual)
s3 = soup.find_all('section')[2]
if s3:
    s3.find('h2').clear()
    s3.find('h2').append("Comprar equipos ")
    span = soup.new_tag('span', attrs={'class': 'text-accent'})
    span.string = "sin diseño"
    s3.find('h2').append(span)
    s3.find('h2').append(" puede terminar en una experiencia costosa y poco funcional.")
    
    p = s3.find('p', class_='hero-subtitle')
    if not p: p = s3.find('p')
    if p:
        p.clear()
        p.append("Muchas personas compran una pantalla, proyector, barra de sonido o bocinas sin revisar si realmente son adecuados para su espacio. El resultado puede ser una imagen demasiado pequeña, exceso de brillo, audio sin impacto, cables visibles o un sistema difícil de usar.")
        p.append(soup.new_tag('br'))
        p.append(soup.new_tag('br'))
        p.append("Un cine en casa necesita planeación. Antes de invertir, conviene definir el tamaño de imagen, el tipo de pantalla, la ubicación de bocinas, la potencia necesaria, la conectividad y la forma en que la familia lo va a operar todos los días.")
    
    img = s3.find('img', class_='antithesis-main-img')
    if img: img['src'] = "../assets/Imagenes/soluciones/Residencial premium/problema-audio-video-residencial-dg-audiosound.webp"
    
    problems = s3.find_all(class_='antithesis-problem-card')
    p_texts = [
        ("Audio sin inmersión", "Bocinas mal ubicadas o sin subwoofer pueden quitar emoción y claridad.", "fa-solid fa-volume-xmark"),
        ("Imagen incorrecta", "El tamaño, brillo o tipo de pantalla puede no corresponder al espacio.", "fa-solid fa-tv"),
        ("Luz y reflejos", "La iluminación afecta directamente el desempeño de proyectores y pantallas.", "fa-solid fa-lightbulb"),
        ("Equipos aislados", "Sin integración, el sistema puede volverse complicado y poco práctico.", "fa-solid fa-plug-circle-xmark")
    ]
    for i, p_c in enumerate(problems):
        if i < len(p_texts):
            p_c.find('h3').string = p_texts[i][0]
            p_c.find('p').string = p_texts[i][1]
            p_c.find('i')['class'] = p_texts[i][2]

# Section 4: Soluciones Integrales (Qué hacemos / Incluye)
s4 = soup.find_all('section')[3]
if s4:
    s4.find('h2').clear()
    s4.find('h2').append("Diseñamos soluciones de cine en casa completas, ")
    span = soup.new_tag('span', attrs={'class': 'text-accent'})
    span.string = "estéticas y fáciles de disfrutar"
    s4.find('h2').append(span)
    s4.find('h2').append(".")
    
    ps = s4.find('p')
    if ps: ps.string = "Integramos audio, video, conectividad y configuración para que tu sala, cuarto dedicado o family room tenga una experiencia superior sin complicaciones técnicas innecesarias."
    
    incl = s4.find_all(class_='include-card')
    i_texts = [
        ("Audio envolvente", "Sistemas 5.1, 7.1, Dolby Atmos, barras premium, subwoofers y bocinas según el espacio.", "fa-solid fa-volume-high"),
        ("Video premium", "Proyectores 4K, pantallas de proyección, televisores premium y soportes adecuados.", "fa-solid fa-film"),
        ("Integración estética", "Cuidamos instalación, cableado, ubicación de equipos y apariencia final.", "fa-solid fa-palette"),
        ("Asesoría del espacio", "Revisamos medidas, fotos, iluminación, mobiliario y distancia visual.", "fa-solid fa-ruler-combined"),
        ("Control y Config", "Configuración básica para que sea fácil de usar para todos en casa.", "fa-solid fa-sliders"),
        ("Instalación Profesional", "Montaje, conexión, organización de equipos y pruebas exhaustivas.", "fa-solid fa-check-double")
    ]
    for i, ic in enumerate(incl):
        if i < len(i_texts):
            # The h3 contains the icon and text
            h3 = ic.find('h3')
            h3.clear()
            i_tag = soup.new_tag('i', attrs={'class': i_texts[i][2]})
            h3.append(i_tag)
            h3.append(" " + i_texts[i][0])
            ic.find('p').string = i_texts[i][1]

# Section 5: Áreas del Hogar
s5 = soup.find_all('section')[4]
if s5:
    s5.find('h2').clear()
    s5.find('h2').append("Opciones de cine en casa según tu espacio, ")
    span = soup.new_tag('span', attrs={'class': 'text-accent'})
    span.string = "objetivo y presupuesto"
    s5.find('h2').append(span)
    
    ps = s5.find('p')
    if ps: ps.string = "Podemos desarrollar desde una mejora de sala con sonido premium hasta una sala dedicada con proyección, audio envolvente y configuración avanzada."
    
    areas = s5.find_all(class_='area-card')
    a_texts = [
        ("Sala de TV mejorada", "../assets/Imagenes/soluciones/Residencial premium/barra-sonido-premium-cine-en-casa-dg-audiosound.webp"),
        ("Home theater 5.1 / 7.1", "../assets/Imagenes/soluciones/Residencial premium/audio-envolvente-51-cine-en-casa-dg-audiosound.webp"),
        ("Dolby Atmos residencial", "../assets/Imagenes/soluciones/Residencial premium/dolby-atmos-cine-en-casa-dg-audiosound.webp"),
        ("Proyección 4K", "../assets/Imagenes/soluciones/Residencial premium/proyector-4k-cine-en-casa-dg-audiosound.webp"),
        ("Cuarto dedicado", "../assets/Imagenes/soluciones/Residencial premium/cuarto-dedicado-cine-en-casa-dg-audiosound.webp"),
        ("Instalación e integración", "../assets/Imagenes/soluciones/Residencial premium/cableado-instalacion-cine-en-casa-dg-audiosound.webp")
    ]
    for i, a in enumerate(areas):
        if i < len(a_texts):
            a.find('span').string = a_texts[i][0]
            a.find('img')['src'] = a_texts[i][1]

# Section 6: Banner (Eventos/Modernizacion)
s6 = soup.find_all('section')[5]
if s6:
    s6.find('h2').string = "Prepárate para vivir tus eventos favoritos con una experiencia superior."
    p = s6.find('p')
    if p: p.string = "Un sistema de cine en casa no solo es para películas. También puede transformar partidos, conciertos, Fórmula 1, videojuegos y reuniones familiares en una experiencia más emocionante y cómoda."
    img = s6.find('img')
    if img: img['src'] = "../assets/Imagenes/soluciones/Eventos creadores y produccion/eventos-creadores-produccion-streaming.webp"
    btn = s6.find('a', class_='btn')
    if btn: 
        btn.clear()
        btn.append("Preparar mi sala")

# Section 7: Proceso
s7 = soup.find_all('section')[6]
if s7:
    s7.find('h2').clear()
    s7.find('h2').append("Un proceso claro para una ")
    span = soup.new_tag('span', attrs={'class': 'text-accent'})
    span.string = "solución profesional"
    s7.find('h2').append(span)

    b_items = s7.find_all(class_='process-bento-item')
    proc = [
        ("Nos contactas", "Nos escribes por WhatsApp y nos cuentas qué experiencia quieres lograr.", "fa-solid fa-comment-dots"),
        ("Revisamos tu espacio", "Solicitamos medidas, fotos, iluminación, muebles y ubicación deseada.", "fa-solid fa-magnifying-glass"),
        ("Definimos alcance", "Recomendamos tipo de pantalla, audio, proyector, cableado y accesorios.", "fa-solid fa-list-check"),
        ("Propuesta clara", "Te entregamos alcance, equipos, tiempos e inversión.", "fa-solid fa-file-signature")
    ]
    for i, it in enumerate(b_items):
        if i < len(proc):
            it.find('h3').string = proc[i][0]
            it.find('p').string = proc[i][1]
            icon = it.find(class_='bento-header').find('i')
            if icon: icon['class'] = proc[i][2]

# Section 8: Split Dark / Gold
s8 = soup.find_all('section')[7]
if s8:
    dark = s8.find(class_='dark-panel')
    if dark:
        dark.find('h2').string = "No vendemos cajas: diseñamos experiencias de audio y video."
        ps = dark.find_all('p')
        if len(ps) >= 2:
            ps[0].string = "La recomendación correcta depende del espacio, no solo de la ficha técnica. Un proyector puede ser excelente, pero no ser el ideal si el tiro, la luz o el tamaño de pantalla no corresponden. Una bocina puede ser poderosa, pero perder impacto si se coloca mal."
            ps[1].string = "En DG Audiosound buscamos que tu inversión sea coherente, funcional y preparada para que realmente disfrutes el sistema en tu día a día."

    gold = s8.find(class_='gold-panel')
    if gold:
        gold.find('h2').string = "Una decisión profesional para tu hogar"
        lis = gold.find_all('li')
        g_texts = ["Asesoría personalizada", "Propuesta formal", "Equipos originales", "Instalación profesional", "Integración estética", "Capacitación básica"]
        for i, li in enumerate(lis):
            if i < len(g_texts): li.string = g_texts[i]

# Section 9: FAQ
s9 = soup.find_all('section')[8]
if s9:
    s9.find('h2').clear()
    s9.find('h2').append("Preguntas ")
    span = soup.new_tag('span', attrs={'class': 'text-accent'})
    span.string = "frecuentes"
    s9.find('h2').append(span)

    faqs = s9.find_all(class_='faq-lux-item')
    f_data = [
        ("¿Qué incluye un proyecto de cine en casa?", "Puede incluir asesoría, análisis del espacio, selección de proyector o pantalla, sistema de audio envolvente, subwoofer, receptor AV, cableado, soportes, instalación, configuración, pruebas y capacitación básica de uso."),
        ("¿Puedo instalar un cine en casa en una sala normal?", "Sí. Un cine en casa puede diseñarse para sala, family room, cuarto dedicado, departamento o área social. La solución se adapta al tamaño, iluminación, distribución y presupuesto del espacio."),
        ("¿Qué es mejor: proyector o pantalla de TV?", "Depende del tamaño de imagen deseado, iluminación, distancia de visualización y uso. Un proyector permite mayor impacto visual; una pantalla de TV puede ser mejor para espacios con mucha luz o uso cotidiano intensivo."),
        ("¿Manejan sistemas Dolby Atmos?", "Sí. DG Audiosound puede proponer sistemas compatibles con Dolby Atmos cuando el espacio, presupuesto y equipos lo permiten. También podemos sugerir soluciones 5.1, 7.1 o barras premium según el proyecto.")
    ]
    for i, f_it in enumerate(faqs):
        if i < len(f_data):
            f_it.find(class_='faq-lux-btn').find('span').string = f_data[i][0]
            f_it.find(class_='faq-lux-answer').find('p').string = f_data[i][1]


# Finally, write to cine_en_casa.html
with open('subpage/cine_en_casa.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Modificaciones aplicadas con éxito a cine_en_casa.html")
