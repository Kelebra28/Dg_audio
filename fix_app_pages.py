import os
import re
import urllib.parse
from bs4 import BeautifulSoup

# Mapping from application file to image subfolder in assets/Imagenes/aplicaciones/
folder_mapping = {
    "restaurantes.html": "restaurantes",
    "bares-antros.html": "bares y antros",
    "gimnasios.html": "gimnasios",
    "cafeterias.html": "Cafeteria",
    "retail.html": "retail",
    "barberias.html": "barberia",
    "podcast.html": "podcast",
    "streamers.html": "streamers",
    "sonidos-dj.html": "sonidos-y-dj",
    "centros-de-culto.html": "Centros de culto",
    "cine-independiente.html": "cine-independiente",
    "musicos-vocalistas.html": "musicos-y-vocalistas"
}

# Image translation mapping for Centros de Culto (since files on disk have auditorio/corporativo names)
culto_translation = {
    "audio-video-centros-culto-hero.webp": "audio-video-auditorios-corporativos-hero-dg-audiosound.webp",
    "audio-video-centros-culto-sistema.webp": "auditorio-institucional-dg-audiosound.webp",
    "audio-video-centros-culto-microfonia.webp": "microfonia-auditorio-corporativo-dg-audiosound.webp",
    "audio-video-centros-culto-sistemas-pa.webp": "refuerzo-sonoro-auditorio-corporativo-dg-audiosound.webp",
    "audio-video-centros-culto-consolas.webp": "mezcla-control-auditorio-corporativo-dg-audiosound.webp",
    "audio-video-centros-culto-monitoreo.webp": "centro-capacitacion-corporativo-dg-audiosound.webp",
    "audio-video-centros-culto-streaming.webp": "modernizacion-auditorio-corporativo-dg-audiosound.webp",
    "audio-video-centros-culto-pantallas-proyectores.webp": "proyeccion-video-auditorio-corporativo-dg-audiosound.webp",
    "audio-video-centros-culto-pequeno.webp": "espacio-multiproposito-corporativo-dg-audiosound.webp",
    "audio-video-centros-culto-mediano.webp": "salon-conferencias-corporativo-dg-audiosound.webp",
    "audio-video-centros-culto-auditorio.webp": "auditorio-empresarial-dg-audiosound.webp",
    "audio-video-centros-culto-solucion-integral.webp": "instalacion-auditorio-corporativo-dg-audiosound.webp"
}

# Specific image fallbacks for missing assets on disk
specific_fallbacks = {
    "gimnasios.html": {
        "recepcion-gimnasio-audio-video.webp": "ambiente-gimnasio-audio-video-profesional.webp",
        "audio-para-clases-grupales-gimnasio.webp": "gimnasio-clases-eventos-audio-video.webp"
    }
}

# Personalized WhatsApp prefilled message mapping
whatsapp_messages = {
    "restaurantes.html": "Hola%20DG%20Audiosound%2C%20me%20interesa%20cotizar%20una%20soluci%C3%B3n%20de%20audio%20y%20video%20para%20mi%20restaurante.",
    "bares-antros.html": "Hola%20DG%20Audiosound%2C%20me%20interesa%20cotizar%20una%20soluci%C3%B3n%20de%20audio%2C%20video%20e%20iluminaci%C3%B3n%20para%20mi%20bar%20o%20antro.",
    "gimnasios.html": "Hola%20DG%20Audiosound%2C%20me%20interesa%20cotizar%20una%20soluci%C3%B3n%20de%20audio%20y%20video%20para%20mi%20gimnasio.",
    "cafeterias.html": "Hola%20DG%20Audiosound%2C%20me%20interesa%20cotizar%20una%20soluci%C3%B3n%20de%20audio%20y%20video%20para%20mi%20cafeter%C3%ADa.",
    "retail.html": "Hola%20DG%20Audiosound%2C%20me%20interesa%20cotizar%20una%20soluci%C3%B3n%20de%20audio%20y%20pantallas%20para%20mi%20tienda%20retail.",
    "barberias.html": "Hola%20DG%20Audiosound%2C%20me%20interesa%20cotizar%20una%20soluci%C3%B3n%20de%20audio%20y%20video%20para%20mi%20barber%C3%ADa.",
    "podcast.html": "Hola%20DG%20Audiosound%2C%20me%20interesa%20cotizar%20una%20soluci%C3%B3n%20de%20audio%20y%20video%20para%20mi%20estudio%20de%20podcast.",
    "streamers.html": "Hola%20DG%20Audiosound%2C%20me%20interesa%20cotizar%20una%20soluci%C3%B3n%20de%20audio%2C%20video%20e%20iluminaci%C3%B3n%20para%20streaming.",
    "sonidos-dj.html": "Hola%20DG%20Audiosound%2C%20me%20interesa%20cotizar%20un%20sistema%20de%20sonido%20e%20iluminaci%C3%B3n%20para%20DJ%20o%20evento.",
    "centros-de-culto.html": "Hola%20DG%20Audiosound%2C%20me%20interesa%20cotizar%20una%20soluci%C3%B3n%20de%20audio%20y%20video%20para%20mi%20centro%20de%20culto.",
    "cine-independiente.html": "Hola%20DG%20Audiosound%2C%20me%20interesa%20cotizar%20una%20soluci%C3%B3n%20de%20proyecci%C3%B3n%20y%20sonido%20para%20cine%20independiente.",
    "musicos-vocalistas.html": "Hola%20DG%20Audiosound%2C%20me%20interesa%20cotizar%20una%20soluci%C3%B3n%20de%20audio%20y%20monitoreo%20para%20m%C3%BAsicos%20o%20vocalistas."
}

# Solution select dropdown options
negocios_options = [
    ("Restaurantes", "Restaurantes"),
    ("Bares y antros", "Bares y antros"),
    ("Gimnasios o fitness", "Gimnasios o fitness"),
    ("Cafeterías", "Cafeterías"),
    ("Retail y tiendas", "Retail y tiendas"),
    ("Barberías", "Barberías"),
    ("Oficinas o comercial", "Oficinas o comercial")
]

eventos_options = [
    ("Podcast o grabación", "Podcast o grabación"),
    ("Streaming o creación de contenido", "Streaming o creación de contenido"),
    ("Sonidos y DJ", "Sonidos y DJ"),
    ("Centro de culto", "Centro de culto"),
    ("Cine independiente", "Cine independiente"),
    ("Músicos o vocalistas", "Músicos o vocalistas"),
    ("Otro proyecto de producción", "Otro proyecto de producción")
]

negocios_files = {"restaurantes.html", "bares-antros.html", "gimnasios.html", "cafeterias.html", "retail.html", "barberias.html"}
eventos_files = {"podcast.html", "streamers.html", "sonidos-dj.html", "centros-de-culto.html", "cine-independiente.html", "musicos-vocalistas.html"}

transparent_gif = "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"

def resolve_src(src, app_filename):
    if not src:
        return src
    if src.startswith('data:') or src.startswith('http') or src.startswith('//'):
        return src
    
    # If the original path already exists on disk, keep it as-is!
    unescaped_src = urllib.parse.unquote(src)
    normalized_path = unescaped_src.replace('../../', '')
    if os.path.exists(normalized_path) and os.path.isfile(normalized_path):
        return src
    
    # Basename of the file
    basename = os.path.basename(src)
    
    # Check for specific translations or fallbacks
    if app_filename in specific_fallbacks and basename in specific_fallbacks[app_filename]:
        basename = specific_fallbacks[app_filename][basename]
        
    # Check for global assets that should remain under ../../assets/
    if basename in ['dg_logo.webp', 'DG.png', 'Marcas.png', 'dg-audiosound-og.jpg', 'dg-audiosound-logo.png']:
        return f"../../assets/{basename}"
        
    solucion_folder_mapping = {
        "restaurantes.html": "Negocios y experiencias comerciales/aplicacion-restaurantes-audio-video-dg-audiosound.webp",
        "bares-antros.html": "Negocios y experiencias comerciales/aplicacion-bares-y-antros-audio-video-dg-audiosound.webp",
        "gimnasios.html": "Negocios y experiencias comerciales/aplicacion-gimnasios-audio-video-dg-audiosound.webp",
        "cafeterias.html": "Negocios y experiencias comerciales/aplicacion-cafeterias-audio-video-dg-audiosound.webp",
        "retail.html": "Negocios y experiencias comerciales/aplicacion-retail-tiendas-audio-video-dg-audiosound.webp",
        "barberias.html": "Negocios y experiencias comerciales/aplicacion-barberia-audio-video-dg-audiosounddiosound.webp",
        "podcast.html": "Eventos creadores y produccion/eventos-creadores-produccion-podcast.webp",
        "streamers.html": "Eventos creadores y produccion/eventos-creadores-produccion-streaming.webp",
        "sonidos-dj.html": "Eventos creadores y produccion/eventos-creadores-produccion-sonidos-dj.webp",
        "centros-de-culto.html": "Eventos creadores y produccion/eventos-creadores-produccion-centros-culto.webp",
        "cine-independiente.html": "Eventos creadores y produccion/eventos-creadores-produccion-cine-independiente.webp",
        "musicos-vocalistas.html": "Eventos creadores y produccion/eventos-creadores-produccion-musicos-vocalistas.webp"
    }

    # Check for solutions category images if it is a hero/og
    if basename.endswith("-hero.webp") or "hero" in basename.lower() or "og" in basename.lower():
        sol_rel = solucion_folder_mapping.get(app_filename)
        if sol_rel:
            local_sol_path = f"assets/Imagenes/soluciones/{sol_rel}"
            if os.path.exists(local_sol_path):
                escaped_sol_rel = urllib.parse.quote(sol_rel)
                return f"../../assets/Imagenes/soluciones/{escaped_sol_rel}"

    folder = folder_mapping.get(app_filename)
    if not folder:
        return src

    # Cafeterías & Cine independiente empty/transparent fallbacks for non-hero images
    if folder in ["Cafeteria", "cine-independiente"]:
        return transparent_gif

    # Centros de culto translation
    if app_filename == "centros-de-culto.html":
        if basename in culto_translation:
            basename = culto_translation[basename]

    # Check if the file physically exists on disk in the application subfolder
    local_path = f"assets/Imagenes/aplicaciones/{folder}/{basename}"
    if os.path.exists(local_path):
        escaped_folder = urllib.parse.quote(folder)
        escaped_basename = urllib.parse.quote(basename)
        return f"../../assets/Imagenes/aplicaciones/{escaped_folder}/{escaped_basename}"

    # Default fallback to transparent spacer to prevent broken image icons on page
    print(f"  [Warning] Asset not found: {basename} in folder '{folder}'. Using transparent spacer.")
    return transparent_gif

def process_file(filename):
    filepath = f"subpage/applications/{filename}"
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return
        
    print(f"Processing: {filename}")
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Fix SEO metadata / OG tags using page content
    title_text = soup.title.string if soup.title else ""
    desc_tag = soup.find('meta', {'name': 'description'})
    desc_text = desc_tag['content'] if desc_tag else ""
    
    # OG Title
    og_title = soup.find('meta', {'property': 'og:title'})
    if og_title and title_text:
        og_title['content'] = title_text
        
    # OG Description
    og_description = soup.find('meta', {'property': 'og:description'})
    if og_description and desc_text:
        og_description['content'] = desc_text
        
    # Clean keywords (remove Altavoces residenciales, Sonido multiroom for commercial applications)
    keywords_tag = soup.find('meta', {'name': 'keywords'})
    if keywords_tag and keywords_tag.get('content'):
        k_content = keywords_tag['content']
        k_content = k_content.replace('altavoces residenciales, ', '')
        k_content = k_content.replace('sonido multiroom, ', '')
        # Add commercial terms
        if filename in negocios_files and 'comercial' not in k_content:
            k_content = "sonorización comercial, audio para negocios, " + k_content
        elif filename in eventos_files and 'profesional' not in k_content:
            k_content = "audio profesional, producción de audio, " + k_content
        keywords_tag['content'] = k_content
        
    # Fix og:image
    og_image = soup.find('meta', {'property': 'og:image'})
    if og_image:
        # Resolve OG image path
        original_img = og_image['content']
        resolved_img = resolve_src(original_img, filename)
        # If it resolves to relative path, keep it as absolute url if needed or correct it
        if resolved_img.startswith('../../'):
            # Convert to absolute canonical url style if specified
            basename = os.path.basename(resolved_img)
            og_image['content'] = f"https://dgaudiosound.com/assets/Imagenes/dg-audiosound-og.jpg"

    # 2. Fix images in <img> tags
    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            resolved = resolve_src(src, filename)
            img['src'] = resolved

    # 3. Fix background-image inline styles
    for el in soup.find_all(style=True):
        style = el['style']
        match = re.search(r'background-image:\s*url\([\'"]?([^\'"\)]+)[\'"]?\)', style)
        if match:
            bg_url = match.group(1)
            resolved = resolve_src(bg_url, filename)
            new_style = re.sub(r'background-image:\s*url\([\'"]?([^\'"\)]+)[\'"]?\)', f"background-image: url('{resolved}')", style)
            el['style'] = new_style

    # 4. Personalize WhatsApp link CTAs
    wa_msg = whatsapp_messages.get(filename)
    if wa_msg:
        for a in soup.find_all('a', href=True):
            href = a['href']
            if 'wa.me' in href or 'api.whatsapp.com' in href:
                # Replace query string text parameter
                new_href = f"https://wa.me/525537270177?text={wa_msg}"
                a['href'] = new_href

    # 5. Fix Form selector option list to match commercial category options
    select_tag = soup.find('select', id='cb-project')
    if select_tag:
        select_tag.clear()
        target_options = negocios_options if filename in negocios_files else eventos_options
        for val, text in target_options:
            opt_tag = soup.new_tag('option', value=val)
            opt_tag.string = text
            select_tag.append(opt_tag)

    # 6. Clean residential residues in text paragraphs
    for el in soup.find_all(['p', 'span', 'li', 'h2', 'h3', 'h4', 'div']):
        # If the element has children nodes, process only direct string nodes to avoid corrupting tags
        if el.string:
            text = el.string
            # Replace home/residential references when they appear in general descriptions
            if filename in negocios_files:
                text = text.replace(' en tu hogar', ' en tu negocio')
                text = text.replace(' en el hogar', ' en tu negocio')
                text = text.replace(' tu hogar', ' tu negocio')
                text = text.replace(' el hogar', ' tu negocio')
                text = text.replace('residencial', 'comercial')
            elif filename in eventos_files:
                text = text.replace(' en tu hogar', ' en tu proyecto')
                text = text.replace(' en el hogar', ' en tu proyecto')
                text = text.replace(' tu hogar', ' tu proyecto')
                text = text.replace(' el hogar', ' tu proyecto')
                text = text.replace('residencial', 'profesional')
            el.string = text

    # 7. Fix footer links
    footer_tag = soup.find('footer', class_='footer')
    if footer_tag:
        for col in footer_tag.find_all('div', class_='footer-col'):
            title_el = col.find('h4', class_='footer-title')
            if title_el:
                title_text = title_el.get_text().strip()
                if title_text == "Navegación":
                    ul = col.find('ul')
                    if ul:
                        ul.clear()
                        nav_links = [
                            ("../../index.html#inicio", "Inicio"),
                            ("../soluciones.html", "Soluciones"),
                            ("../../index.html#marcas", "Nuestras Marcas"),
                            ("../tienda.html", "Tienda"),
                            ("../blog.html", "Blog DG")
                        ]
                        for href, text in nav_links:
                            li = soup.new_tag('li')
                            a = soup.new_tag('a', href=href)
                            a.string = text
                            li.append(a)
                            ul.append(li)
                elif title_text == "Soluciones":
                    ul = col.find('ul')
                    if ul:
                        ul.clear()
                        sol_links = [
                            ("../soluciones/residencial-premium.html", "Audio Residencial"),
                            ("../soluciones/negocios-y-experiencias.html", "Audio para Negocios"),
                            ("../soluciones/corporativo-e-institucional.html", "Salas Corporativas"),
                            ("../soluciones/eventos-y-produccion.html", "Estudios y Creadores"),
                            ("../soluciones/negocios-y-experiencias.html", "Instalación Comercial")
                        ]
                        for href, text in sol_links:
                            li = soup.new_tag('li')
                            a = soup.new_tag('a', href=href)
                            a.string = text
                            li.append(a)
                            ul.append(li)

    # Write back fixed HTML
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Finished: {filename}\n")

if __name__ == '__main__':
    all_files = list(folder_mapping.keys())
    for f in all_files:
        process_file(f)
    print("All application files processed successfully!")
