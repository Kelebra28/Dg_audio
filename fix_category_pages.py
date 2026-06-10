import os
import re
from bs4 import BeautifulSoup

def fix_eventos():
    path = 'subpage/soluciones/eventos-y-produccion.html'
    if not os.path.exists(path):
        print("eventos-y-produccion.html does not exist.")
        return

    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Head title & meta
    if soup.title:
        soup.title.string = "Soluciones para Eventos, Creadores y Producción | DG Audiosound"
    desc_tag = soup.find('meta', {'name': 'description'})
    if desc_tag:
        desc_tag['content'] = "Diseñamos soluciones profesionales de audio y video para podcast, streaming, DJ, centros de culto, música en vivo y cine independiente en México."

    # Hero
    hero = soup.find('section', class_='hero-lux')
    if hero:
        kicker = hero.find(class_='hero-kicker') or hero.find(class_='lux-kicker')
        if kicker: kicker.string = "Ingeniería Audiovisual"
        
        title = hero.find(class_='hero-lux-title')
        if title:
            title.clear()
            title.append("Soluciones de audio y video para eventos, ")
            span = soup.new_tag('span', attrs={'class': 'text-accent'})
            span.string = "creadores y producción"
            title.append(span)
            title.append(".")

        subtitle = hero.find(class_='hero-lux-subtitle')
        if subtitle:
            subtitle.string = "Diseñamos soluciones profesionales para proyectos donde el sonido, la imagen, la microfonía, la grabación, la mezcla, la transmisión y la experiencia audiovisual son parte esencial del resultado."

        # Hero backgrounds
        slides = hero.find_all(class_='hero-lux-slide')
        img_hero = '../../assets/Imagenes/soluciones/Eventos creadores y produccion/eventos-creadores-produccion-hero..webp'
        for i, slide in enumerate(slides):
            if i == 0:
                slide['style'] = f"background-image: url('{img_hero}');"
            else:
                slide.decompose()

        # Hero badges
        badges_wrap = hero.find(class_='hero-lux-badges')
        if badges_wrap:
            badges_wrap.clear()
            badges = [
                ("fa-microphone-lines", "Audio Profesional"),
                ("fa-microphone", "Microfonía"),
                ("fa-sliders", "Mezcla y Control"),
                ("fa-video", "Grabación y Streaming")
            ]
            for icon, text in badges:
                b_div = soup.new_tag('div', attrs={'class': 'hero-lux-badge'})
                i_tag = soup.new_tag('i', attrs={'class': f'fa-solid {icon}'})
                span_tag = soup.new_tag('span')
                span_tag.string = text
                b_div.append(i_tag)
                b_div.append(span_tag)
                badges_wrap.append(b_div)

    # Philosophy / Problems Section
    prob_section = soup.find(id='problema')
    if prob_section:
        title = prob_section.find(class_='lux-title')
        if title:
            title.clear()
            title.append("Cuando el audio y el video fallan, la experiencia ")
            strong = soup.new_tag('strong')
            strong.string = "completa pierde impacto"
            title.append(strong)
            
        leads = prob_section.find_all(class_='lux-lead')
        if leads:
            leads[0].string = "En eventos, contenido digital, presentaciones en vivo y espacios de producción, la tecnología no debe improvisarse. Un micrófono incorrecto, una bocina mal seleccionada, una mezcla poco clara o una imagen deficiente pueden afectar la atención del público, la calidad del contenido y la percepción profesional del proyecto."
            
        p_desc = prob_section.find('p', style=lambda value: value and 'color: #555560' in value)
        if p_desc:
            p_desc.string = "En DG Audiosound revisamos el proyecto completo antes de recomendar tecnología. Así evitamos soluciones sobredimensionadas, equipos suficientes, gastos innecesarios y configuraciones que terminan generando más problemas que resultados."

        # Problem cards
        cards = prob_section.find_all(class_='antithesis-problem-card')
        if len(cards) >= 2:
            # Card 1: Audio poco claro
            cards[0].find('h3').string = "Audio poco claro"
            cards[0].find('p').string = "Voces sin presencia, música sin impacto, saturación, ruido, eco o mala cobertura del espacio."
            cards[0].find('i')['class'] = "fa-solid fa-volume-xmark"
            # Card 2: Video limitado
            cards[1].find('h3').string = "Video limitado"
            cards[1].find('p').string = "Imagen pequeña, poca luminosidad, mala conexión, proyección inadecuada o pantallas mal seleccionadas."
            cards[1].find('i')['class'] = "fa-solid fa-triangle-exclamation"

    # Blueprint section
    blueprint = soup.find(id='blueprint')
    if blueprint:
        title = blueprint.find(class_='lux-title')
        if title:
            title.clear()
            title.append("La Anatomía de un ")
            strong = soup.new_tag('strong')
            strong.string = "Ecosistema de Producción"
            title.append(strong)

        lead = blueprint.find(class_='lux-lead')
        if lead:
            lead.string = "Diseñar de forma profesional requiere estructurar planos detallados de ingeniería antes de colocar un solo cable. Conoce cómo estructuramos los sistemas para garantizar calidad."

        img = blueprint.find('img')
        if img:
            img['src'] = "../../assets/Imagenes/soluciones/Eventos creadores y produccion/eventos-creadores-produccion-contexto.webp"

        hotspots = blueprint.find_all(class_='blueprint-hotspot')
        hotspot_labels = [
            "Audio y Captura",
            "Microfonía Inalámbrica",
            "Consolas y Control",
            "Proyección y Video"
        ]
        for i, spot in enumerate(hotspots):
            if i < len(hotspot_labels):
                label_span = spot.find(class_='blueprint-hotspot-label')
                if label_span: label_span.string = hotspot_labels[i]

    # Showcase section background slides
    showcase = soup.find(id='sistemas')
    if showcase:
        slides = showcase.find_all(class_='showcase-slide')
        img_prefix = '../../assets/Imagenes/soluciones/Eventos creadores y produccion/'
        images = [
            'eventos-creadores-produccion-podcast.webp',
            'eventos-creadores-produccion-streaming.webp',
            'eventos-creadores-produccion-sonidos-dj.webp',
            'eventos-creadores-produccion-centros-culto.webp',
            'eventos-creadores-produccion-cine-independiente.webp',
            'eventos-creadores-produccion-musicos-vocalistas.webp'
        ]
        for i, slide in enumerate(slides):
            if i < len(images):
                slide['style'] = f"background-image: url('{img_prefix + images[i]}');"
        
        # Navigation buttons
        nav_btns = showcase.find_all(class_='showcase-nav-btn')
        btn_texts = [
            "01. Podcast",
            "02. Streamers",
            "03. Sonidos y DJ",
            "04. Centros de Culto",
            "05. Cine Independiente",
            "06. Músicos y Vocalistas"
        ]
        for i, btn in enumerate(nav_btns):
            if i < len(btn_texts):
                btn.string = btn_texts[i]

    # Bento Proceso
    proceso = soup.find(id='proceso')
    if proceso:
        title = proceso.find(class_='lux-title')
        if title:
            title.clear()
            title.append("Un Proceso Claro para ")
            strong = soup.new_tag('strong')
            strong.string = "Equipar e Instalar"
            title.append(strong)
            
        subtitle = proceso.find(class_='section-subtitle')
        if subtitle: subtitle.string = "Un proceso estructurado para garantizar resultados excepcionales en cada etapa de tu proyecto."
        
        bento_items = proceso.find_all(class_=['process-bento-item', 'process-lux-item'])
        steps = [
            ("Contacto inicial", "Nos compartes la idea, el tipo de proyecto y el objetivo principal."),
            ("Diagnóstico", "Revisamos uso, espacio, audiencia, fuentes, operation y necesidades técnicas."),
            ("Diseño de solución", "Definimos equipos, familias de producto y configuración sugerida."),
            ("Instalación", "Apoyamos con suministro, instalación, conexión, pruebas y puesta en marcha."),
            ("Capacitación", "Explicamos el uso básico para que el sistema pueda operarse con confianza.")
        ]
        for i, item in enumerate(bento_items):
            if i < len(steps):
                item.find('h3').string = steps[i][0]
                item.find('p').string = steps[i][1]

    # Gateway de aplicaciones cards
    gateway = soup.find(id='aplicaciones')
    if gateway:
        cards = gateway.find_all(class_='gateway-lux-card')
        img_prefix = '../../assets/Imagenes/soluciones/Eventos creadores y produccion/'
        app_data = [
            ("Podcast", "Micrófonos, interfaces, mezcladoras, monitoreo, grabación y video para producir contenido.", "../applications/podcast.html", "eventos-creadores-produccion-podcast.webp"),
            ("Streamers", "Audio, cámaras, iluminación básica, captura y control para transmisiones profesionales.", "../applications/streamers.html", "eventos-creadores-produccion-streaming.webp"),
            ("Sonidos y DJ", "PA, subwoofers, mezcladoras, control, microfonía y accesorios para potencia y claridad.", "../applications/sonidos-dj.html", "eventos-creadores-produccion-sonidos-dj.webp"),
            ("Centros de Culto", "Microfonía, sonido, monitoreo, video y transmisión para ceremonias ordenadas.", "../applications/centros-de-culto.html", "eventos-creadores-produccion-centros-culto.webp"),
            ("Cine Independiente", "Proyección, pantallas, sonido, conectividad y soporte técnico para exhibiciones.", "../applications/cine-independiente.html", "eventos-creadores-produccion-cine-independiente.webp"),
            ("Músicos y vocalistas", "Micrófonos, interfaces, monitoreo, mezcla y grabación para ensayos y producción.", "../applications/musicos-vocalistas.html", "eventos-creadores-produccion-musicos-vocalistas.webp")
        ]
        
        for i, card in enumerate(cards):
            if i < len(app_data):
                title, desc, link, img_name = app_data[i]
                img = card.find('img')
                if img:
                    img['src'] = img_prefix + img_name
                    img['alt'] = f"DG Audiosound {title}"
                card.find('h3').string = title
                card.find('p').string = desc
                card.find('a')['href'] = link

    # Ticker brands
    brands_div = soup.find(class_='brands-ticker')
    if brands_div:
        brands_div.clear()
        brands_list = ["SHURE", "ALLEN & HEATH", "QSC", "NEXO", "ZOOM", "BIAMP", "KRAMER", "OPTOMA", "SHARP", "DBTECHNOLOGIES"] * 3
        for brand in brands_list:
            item = soup.new_tag('div', attrs={'class': 'ticker-item'})
            item.string = brand
            brands_div.append(item)

    # FAQs
    faq_section = soup.find(id='faq')
    if faq_section:
        title = faq_section.find(class_='lux-title')
        if title:
            title.clear()
            title.append("Resolvemos tus ")
            strong = soup.new_tag('strong')
            strong.string = "Dudas Frecuentes"
            title.append(strong)

        faq_items = faq_section.find_all(class_='faq-lux-item')
        faqs = [
            ("¿Qué tipo de soluciones ofrece DG Audiosound para eventos, creadores y producción?", "Ofrecemos soluciones profesionales de audio, video, microfonía, consolas, mezcladoras, bocinas, subwoofers, monitoreo, interfaces, grabación, streaming, proyección, pantallas e iluminación complementaria."),
            ("¿Pueden ayudarme a elegir el equipo correcto para mi proyecto?", "Sí. Analizamos el tipo de proyecto, espacio, uso, audiencia, operación, presupuesto y objetivos para recomendar una solución adecuada, de alta fidelidad, escalable y fácil de operar."),
            ("¿Trabajan con soluciones para podcast y streamers?", "Sí. Podemos integrar micrófonos, interfaces, mezcladoras, monitoreo, cámaras, iluminación básica, captura de video y flujos de audio para podcast, streaming y creación de contenido."),
            ("¿También atienden proyectos para sonidos, DJs y eventos en vivo?", "Sí. Desarrollamos soluciones con sistemas PA, subwoofers, consolas, microfonía, monitoreo, cableado y accesorios para sonidos, DJs, presentaciones y eventos que requieran potencia y claridad."),
            ("¿La solución puede incluir instalación y capacitación?", "Sí. Según el alcance del proyecto, apoyamos con instalación, conexión, configuración, pruebas de operación, puesta en marcha y capacitación básica para que el equipo pueda operarse con total confianza."),
            ("¿Cómo puedo solicitar una cotización?", "Puedes escribirnos por WhatsApp al 55 3727 0177 o llenar el formulario de contacto en esta página. Te pediremos detalles básicos de tu proyecto para preparar una recomendación adecuada.")
        ]
        for i, item in enumerate(faq_items):
            if i < len(faqs):
                item.find('button').find('span').string = faqs[i][0]
                item.find(class_='faq-lux-answer').find('p').string = faqs[i][1]

    # Form options
    form_select = soup.find('select', id='cb-project')
    if form_select:
        form_select.clear()
        options = [
            ("Podcast o grabación", "Podcast o grabación"),
            ("Streaming o creación de contenido", "Streaming o creación de contenido"),
            ("Sonidos y DJ", "Sonidos y DJ"),
            ("Centro de culto", "Centro de culto"),
            ("Cine independiente", "Cine independiente"),
            ("Músicos o vocalistas", "Músicos o vocalistas"),
            ("Otro proyecto de producción", "Otro proyecto de producción")
        ]
        for val, text in options:
            opt = soup.new_tag('option', value=val)
            opt.string = text
            form_select.append(opt)

    # Now let's update JS scripts!
    script_tag = soup.find('script')
    if script_tag and script_tag.string:
        js = script_tag.string
        
        # 1. Replace systemsData array
        new_systems_data = """const systemsData = [
                {
                    title: "Podcast <strong>Profesional</strong>",
                    desc: "Micrófonos, interfaces, mezcladoras, monitoreo, grabación y video para producir contenido con sonido claro y presencia profesional.",
                    specs: [
                        "Micrófonos profesionales e interfaces de audio",
                        "Tratamiento acústico básico y soportes",
                        "Solución lista para grabar y transmitir"
                    ],
                    link: "../applications/podcast.html"
                },
                {
                    title: "Audio y Video para <strong>Streamers</strong>",
                    desc: "Audio, cámaras, iluminación básica, captura, monitoreo y control para transmisiones más limpias, estables y profesionales.",
                    specs: [
                        "Audio optimizado y micrófonos dinámicos",
                        "Cámaras y capturadoras de alta definición",
                        "Iluminación básica de rostro y control"
                    ],
                    link: "../applications/streamers.html"
                },
                {
                    title: "Sonidos y <strong>DJ</strong>",
                    desc: "Sistemas PA, subwoofers, mezcladoras, control, microfonía y accesorios para presentaciones con potencia y claridad.",
                    specs: [
                        "Sistemas de sonido PA y subwoofers activos",
                        "Mezcladoras de audio y consolas de mezcla",
                        "Micrófonos inalámbricos y cableado robusto"
                    ],
                    link: "../applications/sonidos-dj.html"
                },
                {
                    title: "Centros de <strong>Culto</strong>",
                    desc: "Microfonía, sonido, monitoreo, video y operación audiovisual para lograr mensajes claros y experiencias más ordenadas.",
                    specs: [
                        "Microfonía para voz principal y predicación",
                        "Sistemas de sonido y cobertura uniforme",
                        "Solución de transmisión en vivo y video"
                    ],
                    link: "../applications/centros-de-culto.html"
                },
                {
                    title: "Cine <strong>Independiente</strong>",
                    desc: "Proyección, pantallas, sonido, conectividad y soporte audiovisual para exhibiciones, conciertos grabados y contenido especial.",
                    specs: [
                        "Proyección HD y pantallas de gran formato",
                        "Sonido envolvente y cobertura de audio",
                        "Conectividad y soporte técnico para salas"
                    ],
                    link: "../applications/cine-independiente.html"
                },
                {
                    title: "Músicos y <strong>Vocalistas</strong>",
                    desc: "Micrófonos, interfaces, monitoreo, mezcla y grabación para mejorar ensayos, presentaciones, contenido y producción musical.",
                    specs: [
                        "Micrófonos para voz e instrumentos",
                        "Monitoreo personal y audífonos de estudio",
                        "Interfaces y mezcladoras de grabación"
                    ],
                    link: "../applications/musicos-vocalistas.html"
                }
            ];"""
        js = re.sub(r'const systemsData = \[.*?\];', new_systems_data, js, flags=re.DOTALL)

        # 2. Replace blueprintData
        new_bp_data = """const blueprintData = {
                cine: {
                    header: "Audio y Captura",
                    title: "Producción de <strong>Audio</strong>",
                    desc: "Calibramos y seleccionamos micrófonos de condensador y dinámicos junto con interfaces y consolas para capturar audio de alta definición sin saturación ni ruidos.",
                    tech1Title: "Entradas",
                    tech1Desc: "Previos de micro de bajo ruido",
                    tech2Title: "Operación",
                    tech2Desc: "Monitoreo en vivo con audífonos"
                },
                audio: {
                    header: "Sistemas de Microfonía",
                    title: "Microfonía <strong>Inalámbrica Profesional</strong>",
                    desc: "Diseño y asignación de frecuencias para evitar interferencias en escenarios, templos o eventos en vivo. Máxima claridad de voz.",
                    tech1Title: "Estabilidad",
                    tech1Desc: "Análisis de espectro de radiofrecuencia",
                    tech2Title: "Sistemas",
                    tech2Desc: "Micrófonos de diadema, solapa y mano"
                },
                jardin: {
                    header: "Refuerzo Sonoro",
                    title: "Sonido PA <strong>para Eventos y DJ</strong>",
                    desc: "Configuración de sistemas PA y subwoofers para cobertura acústica impecable, con graves con pegada e inteligibilidad del habla para toda tu audiencia.",
                    tech1Title: "Potencia",
                    tech1Desc: "Bocinas amplificadas y subwoofers",
                    tech2Title: "Protección",
                    tech2Desc: "Procesamiento DSP y limitadores"
                },
                hifi: {
                    header: "Producción de Video",
                    title: "Proyección y <strong>Streaming Digital</strong>",
                    desc: "Integración de video multicanal, mezcladoras de video y capturadoras para transmisiones y proyecciones nítidas con sincronización de audio.",
                    tech1Title: "Video",
                    tech1Desc: "Captura 1080p / 4K Ultra HD",
                    tech2Title: "Flujo",
                    tech2Desc: "Mezcladores de video por hardware"
                }
            };"""
        js = re.sub(r'const blueprintData = \{.*?\};', new_bp_data, js, flags=re.DOTALL)
        script_tag.string = js

    with open(path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Eventos category page fully customized.")


def fix_negocios():
    path = 'subpage/soluciones/negocios-y-experiencias.html'
    if not os.path.exists(path):
        print("negocios-y-experiencias.html does not exist.")
        return

    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Head title & meta
    if soup.title:
        soup.title.string = "Soluciones de Audio y Video para Negocios | DG Audiosound"
    desc_tag = soup.find('meta', {'name': 'description'})
    if desc_tag:
        desc_tag['content'] = "Audio ambiental distribuido, video, pantallas y automatización profesional para restaurantes, bares, cafeterías, tiendas, gimnasios y oficinas."

    # Hero
    hero = soup.find('section', class_=['hero-lux', 'hero']) or soup.find('section', class_='corp-hero-v2')
    if hero:
        kicker = hero.find(class_='hero-kicker') or hero.find(class_='lux-kicker')
        if kicker: kicker.string = "Consultoría Comercial"
        
        title = hero.find(class_=['hero-lux-title', 'hero-title']) or hero.find('h1')
        if title:
            title.clear()
            title.append("Soluciones de audio y video para negocios y ")
            span = soup.new_tag('span', attrs={'class': 'text-accent'})
            span.string = "experiencias comerciales"
            title.append(span)
            title.append(".")

        subtitle = hero.find(class_=['hero-lux-subtitle', 'hero-subtitle']) or hero.find('p', class_='lead')
        if subtitle:
            subtitle.string = "Crea la atmósfera perfecta para tus clientes. Diseñamos e integramos audio ambiental distribuido, video de alto impacto y automatización comercial fácil de operar."

        # Hero backgrounds
        slides = hero.find_all(class_='hero-lux-slide') or hero.find_all(class_='slide')
        img_hero = '../../assets/Imagenes/soluciones/Negocios y experiencias comerciales/negocios-experiencias-comerciales-dg-audiosound-hero.webp'
        for i, slide in enumerate(slides):
            if i == 0:
                slide['style'] = f"background-image: url('{img_hero}');"
            else:
                slide.decompose()

        # Hero badges
        badges_wrap = hero.find(class_=['hero-lux-badges', 'hero-badges'])
        if badges_wrap:
            badges_wrap.clear()
            badges = [
                ("fa-volume-high", "Audio Distribuido"),
                ("fa-utensils", "Restaurantes y Bares"),
                ("fa-dumbbell", "Gimnasios y Fitness"),
                ("fa-store", "Retail y Tiendas")
            ]
            for icon, text in badges:
                b_div = soup.new_tag('div', attrs={'class': 'hero-lux-badge'})
                i_tag = soup.new_tag('i', attrs={'class': f'fa-solid {icon}'})
                span_tag = soup.new_tag('span')
                span_tag.string = text
                b_div.append(i_tag)
                b_div.append(span_tag)
                badges_wrap.append(b_div)

    # Philosophy / Problems Section
    prob_section = soup.find(id='problema')
    if prob_section:
        title = prob_section.find(class_='lux-title')
        if title:
            title.clear()
            title.append("El Silencio del Diseño vs el ")
            strong = soup.new_tag('strong')
            strong.string = "Ruido Comercial"
            title.append(strong)
            
        leads = prob_section.find_all(class_=['lux-lead', 'lead'])
        if leads:
            leads[0].string = "En muchos negocios se colocan bocinas y pantallas de forma improvisada, provocando problemas acústicos: zonas con volumen excesivo donde los clientes no pueden hablar y zonas sin cobertura. La experiencia se demerita."
            
        p_desc = prob_section.find('p', style=lambda value: value and 'color: #555560' in value)
        if p_desc:
            p_desc.string = "En DG Audiosound planificamos el audio por zonas y la acústica del espacio para que la música acompañe la experiencia, facilitando el diálogo y mejorando el confort del cliente."

        # Problem cards
        cards = prob_section.find_all(class_='antithesis-problem-card')
        if len(cards) >= 2:
            cards[0].find('h3').string = "Volumen desequilibrado"
            cards[0].find('p').string = "Clientes que no pueden conversar cerca de las bocinas y zonas en silencio completo por falta de cobertura."
            cards[0].find('i')['class'] = "fa-solid fa-volume-high"
            
            cards[1].find('h3').string = "Operación confusa"
            cards[1].find('p').string = "Controles complicados que el personal no sabe usar, provocando interrupciones, ruidos y mala música."
            cards[1].find('i')['class'] = "fa-solid fa-screwdriver-wrench"

    # Blueprint section
    blueprint = soup.find(id='blueprint')
    if blueprint:
        title = blueprint.find(class_='lux-title')
        if title:
            title.clear()
            title.append("Planificación de ")
            strong = soup.new_tag('strong')
            strong.string = "Zonas Comerciales"
            title.append(strong)

        lead = blueprint.find(class_='lux-lead')
        if lead:
            lead.string = "Diseñar de forma profesional requiere estructurar planos técnicos de audio y video comercial. Conoce cómo controlamos múltiples áreas con total sencillez."

        img = blueprint.find('img')
        if img:
            img['src'] = "../../assets/Imagenes/soluciones/Negocios y experiencias comerciales/problema-audio-video-negocios-dg-audiosound.webp"

        hotspots = blueprint.find_all(class_='blueprint-hotspot')
        hotspot_labels = [
            "Audio por Zonas",
            "Música Ambiental",
            "Sistemas de Video",
            "Control Central"
        ]
        for i, spot in enumerate(hotspots):
            if i < len(hotspot_labels):
                label_span = spot.find(class_='blueprint-hotspot-label')
                if label_span: label_span.string = hotspot_labels[i]

    # Showcase section background slides
    showcase = soup.find(id='sistemas')
    if showcase:
        slides = showcase.find_all(class_='showcase-slide')
        img_prefix = '../../assets/Imagenes/soluciones/Negocios y experiencias comerciales/'
        images = [
            'aplicacion-restaurantes-audio-video-dg-audiosound.webp',
            'aplicacion-bares-y-antros-audio-video-dg-audiosound.webp',
            'aplicacion-gimnasios-audio-video-dg-audiosound.webp',
            'aplicacion-cafeterias-audio-video-dg-audiosound.webp',
            'aplicacion-retail-tiendas-audio-video-dg-audiosound.webp',
            'aplicacion-barberia-audio-video-dg-audiosounddiosound.webp'
        ]
        for i, slide in enumerate(slides):
            if i < len(images):
                slide['style'] = f"background-image: url('{img_prefix + images[i]}');"
        
        # Navigation buttons
        nav_btns = showcase.find_all(class_='showcase-nav-btn')
        btn_texts = [
            "01. Restaurantes",
            "02. Bares y Antros",
            "03. Gimnasios",
            "04. Cafeterías",
            "05. Retail",
            "06. Barberías"
        ]
        for i, btn in enumerate(nav_btns):
            if i < len(btn_texts):
                btn.string = btn_texts[i]

    # Bento Proceso
    proceso = soup.find(id='proceso')
    if proceso:
        title = proceso.find(class_='lux-title')
        if title:
            title.clear()
            title.append("Un Proceso Claro para ")
            strong = soup.new_tag('strong')
            strong.string = "Negocios Modernos"
            title.append(strong)
            
        subtitle = proceso.find(class_='section-subtitle')
        if subtitle: subtitle.string = "Planificamos tu sistema de audio para que puedas operarlo desde el primer día con seguridad."
        
        bento_items = proceso.find_all(class_=['process-bento-item', 'process-lux-item'])
        steps = [
            ("Contacto inicial", "Nos escribes por WhatsApp y nos cuentas qué tipo de negocio tienes."),
            ("Diagnóstico", "Revisamos fotos, medidas, zonas, uso, presupuesto y equipos actuales."),
            ("Diseño de solución", "Definimos audio, video, zonas, cableado, pantallas y control."),
            ("Instalación", "Procedemos con el montaje seguro, conexión y pruebas de calibración."),
            ("Capacitación", "Explicamos el uso básico para que tu personal opere el sistema con facilidad.")
        ]
        for i, item in enumerate(bento_items):
            if i < len(steps):
                item.find('h3').string = steps[i][0]
                item.find('p').string = steps[i][1]

    # Gateway de aplicaciones cards
    gateway = soup.find(id='aplicaciones')
    if gateway:
        cards = gateway.find_all(class_='gateway-lux-card')
        img_prefix = '../../assets/Imagenes/soluciones/Negocios y experiencias comerciales/'
        app_data = [
            ("Restaurantes", "Música ambiental, pantallas, terrazas, audio por zonas y confort sonoro.", "../applications/restaurantes.html", "aplicacion-restaurantes-audio-video-dg-audiosound.webp"),
            ("Bares y Antros", "Sistemas de alto impacto para música, DJs, pantallas, subwoofers e iluminación.", "../applications/bares-antros.html", "aplicacion-bares-y-antros-audio-video-dg-audiosound.webp"),
            ("Gimnasios", "Audio potente y distribuido para clases, recepción y áreas de entrenamiento.", "../applications/gimnasios.html", "aplicacion-gimnasios-audio-video-dg-audiosound.webp"),
            ("Cafeterías", "Música ambiental y sonido por zonas para mejorar comodidad y permanencia.", "../applications/cafeterias.html", "aplicacion-cafeterias-audio-video-dg-audiosound.webp"),
            ("Retail y tiendas", "Música, pantallas, señalización digital y branding sonoro comercial.", "../applications/retail.html", "aplicacion-retail-tiendas-audio-video-dg-audiosound.webp"),
            ("Barberías", "Música ambiental, pantallas y sonido con identidad moderna y agradable.", "../applications/barberias.html", "aplicacion-barberia-audio-video-dg-audiosounddiosound.webp")
        ]
        
        for i, card in enumerate(cards):
            if i < len(app_data):
                title, desc, link, img_name = app_data[i]
                img = card.find('img')
                if img:
                    img['src'] = img_prefix + img_name
                    img['alt'] = f"DG Audiosound {title}"
                card.find('h3').string = title
                card.find('p').string = desc
                card.find('a')['href'] = link

    # Ticker brands
    brands_div = soup.find(class_='brands-ticker')
    if brands_div:
        brands_div.clear()
        brands_list = ["SONOS", "BOSE", "YAMAHA", "QSC", "SHURE", "KRAMER", "BIAMP", "OPTOMA", "SHARP", "NEXO"] * 3
        for brand in brands_list:
            item = soup.new_tag('div', attrs={'class': 'ticker-item'})
            item.string = brand
            brands_div.append(item)

    # FAQs
    faq_section = soup.find(id='faq')
    if faq_section:
        title = faq_section.find(class_='lux-title')
        if title:
            title.clear()
            title.append("Resolvemos tus ")
            strong = soup.new_tag('strong')
            strong.string = "Dudas Comerciales"
            title.append(strong)

        faq_items = faq_section.find_all(class_='faq-lux-item')
        faqs = [
            ("¿Qué tipo de soluciones ofrece para negocios?", "Ofrecemos audio ambiental distribuido, sistemas de video comercial, pantallas, proyectores, sonido de alto impacto para eventos, microfonía y automatización comercial."),
            ("¿Cómo garantizan que la música se escuche igual en todo el local?", "Realizamos un cálculo acústico para distribuir bocinas de forma uniforme y a la altura correcta, controlando el volumen por zonas según las necesidades de cada área."),
            ("¿Qué marcas de audio recomiendan para uso comercial?", "Usamos marcas profesionales con alta resistencia de operación 24/7 y excelente fidelidad como Sonos, Yamaha, Bose, QSC, Biamp y dBTechnologies."),
            ("¿Podemos conectar el audio a una tablet o celular fácilmente?", "Sí. Centralizamos el sistema para que puedas reproducir música desde servicios como Spotify, Apple Music o YouTube a través de una aplicación intuitiva en tablet o smartphone."),
            ("¿La solución incluye instalación y capacitación?", "Sí. Nuestro equipo se encarga del cableado oculto, montaje de bocinas, calibración de señal y explicamos de forma práctica a tu personal cómo utilizar el sistema sin errores."),
            ("¿Cómo solicito una cotización comercial?", "Escríbenos por WhatsApp o completa el formulario. Analizaremos medidas, planos, fotos o realizaremos una visita de obra si el proyecto lo requiere.")
        ]
        for i, item in enumerate(faq_items):
            if i < len(faqs):
                item.find('button').find('span').string = faqs[i][0]
                item.find(class_='faq-lux-answer').find('p').string = faqs[i][1]

    # Form options
    form_select = soup.find('select', id='cb-project')
    if form_select:
        form_select.clear()
        options = [
            ("Restaurantes", "Restaurantes"),
            ("Bares y antros", "Bares y antros"),
            ("Gimnasios o fitness", "Gimnasios o fitness"),
            ("Cafeterías", "Cafeterías"),
            ("Retail y tiendas", "Retail y tiendas"),
            ("Barberías", "Barberías"),
            ("Oficinas o comercial", "Oficinas o comercial")
        ]
        for val, text in options:
            opt = soup.new_tag('option', value=val)
            opt.string = text
            form_select.append(opt)

    # JS scripts
    script_tag = soup.find('script')
    if script_tag and script_tag.string:
        js = script_tag.string
        
        # Replace systemsData array
        new_systems_data = """const systemsData = [
                {
                    title: "Audio para <strong>Restaurantes</strong>",
                    desc: "Música ambiental distribuida de forma uniforme para áreas interiores, terrazas y zonas de servicio, cuidando el confort acústico del comensal.",
                    specs: [
                        "Bocinas de plafón o muro premium",
                        "Control multizonas para interior y terraza",
                        "Integración de pantallas para eventos deportivos"
                    ],
                    link: "../applications/restaurantes.html"
                },
                {
                    title: "Sistemas para <strong>Bares y Antros</strong>",
                    desc: "Sonido potente de alto impacto, subwoofers imponentes, consolas de mezcla, iluminación robótica y setups profesionales para DJs.",
                    specs: [
                        "Bocinas PA y subwoofers comerciales",
                        "Consolas de mezcla y monitoreo para DJ",
                        "Iluminación complementaria rítmica"
                    ],
                    link: "../applications/bares-antros.html"
                },
                {
                    title: "Audio para <strong>Gimnasios y Fitness</strong>",
                    desc: "Sonido de alta potencia y definición para clases grupales dirigidas, recepción, áreas de pesas y cardio que motiva a tus clientes.",
                    specs: [
                        "Bocinas comerciales de alta potencia",
                        "Micrófonos inalámbricos de diadema para coach",
                        "Distribución de zonas con volumen independiente"
                    ],
                    link: "../applications/gimnasios.html"
                },
                {
                    title: "Sonido para <strong>Cafeterías</strong>",
                    desc: "Música de fondo cálida y agradable que genera una atmósfera de confort, propicia para trabajar, conversar o relajarse.",
                    specs: [
                        "Bocinas discretas de alta calidad",
                        "Reproductor integrado fácil de operar",
                        "Calibración de volumen bajo y presencia nítida"
                    ],
                    link: "../applications/cafeterias.html"
                },
                {
                    title: "Señalización y Audio para <strong>Retail</strong>",
                    desc: "Branding sonoro comercial, pantallas de gran formato y video walls para comunicar promociones y crear experiencias en tiendas de ropa y retail.",
                    specs: [
                        "Bocinas empotrables de alta fidelidad",
                        "Video walls y señalización digital dinámica",
                        "Sistemas de voceo e intercomunicadores"
                    ],
                    link: "../applications/retail.html"
                },
                {
                    title: "Experiencias en <strong>Barberías</strong>",
                    desc: "Atmósfera acústica cuidada con música moderna y pantallas para entretenimiento de tus clientes mientras esperan o reciben servicio.",
                    specs: [
                        "Bocinas estéticas con gran fidelidad",
                        "Instalación de pantallas HD y conectividad",
                        "Control centralizado e intuitivo desde tablet"
                    ],
                    link: "../applications/barberias.html"
                }
            ];"""
        js = re.sub(r'const systemsData = \[.*?\];', new_systems_data, js, flags=re.DOTALL)

        # Replace blueprintData
        new_bp_data = """const blueprintData = {
                cine: {
                    header: "Audio por Zonas",
                    title: "Distribución <strong>Multizona</strong>",
                    desc: "Planificamos el control de volumen por áreas independientes. Permite tener música ambiental a nivel moderado en el salón comedor, mientras que en la terraza o barra el audio tiene mayor protagonismo.",
                    tech1Title: "Zonas",
                    tech1Desc: "Comedor, terraza, barra, baños",
                    tech2Title: "Operación",
                    tech2Desc: "Control por app móvil centralizado"
                },
                audio: {
                    header: "Música Ambiental",
                    title: "Presencia <strong>Nítida y Agradable</strong>",
                    desc: "Determinamos la cantidad y potencia de bocinas necesarias según la altura y acústica del local para evitar fatiga auditiva o zonas en silencio.",
                    tech1Title: "Bocinas",
                    tech1Desc: "Distribución uniforme de alta gama",
                    tech2Title: "Fidelidad",
                    tech2Desc: "Rango optimizado para voz y música"
                },
                jardin: {
                    header: "Sistemas de Video",
                    title: "Video Walls <strong>y Pantallas</strong>",
                    desc: "Integramos señalización digital comercial y matrices de video para enviar contenidos, partidos deportivos o publicidad a múltiples pantallas.",
                    tech1Title: "Visual",
                    tech1Desc: "Pantallas UHD y videowalls",
                    tech2Title: "Distribución",
                    tech2Desc: "Matrices HDMI sobre cable de red"
                },
                hifi: {
                    header: "Control Comercial",
                    title: "Operación <strong>Simplificada</strong>",
                    desc: "Protegemos tus equipos en un rack climatizado y dejamos un panel simplificado para que tu personal encienda, apague y controle el sistema sin errores técnicos.",
                    tech1Title: "Seguridad",
                    tech1Desc: "Limitadores y racks bajo llave",
                    tech2Title: "Uso",
                    tech2Desc: "Panel táctil o botonera de pared"
                }
            };"""
        js = re.sub(r'const blueprintData = \{.*?\};', new_bp_data, js, flags=re.DOTALL)
        script_tag.string = js

    with open(path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Negocios category page fully customized.")

if __name__ == '__main__':
    fix_eventos()
    fix_negocios()
