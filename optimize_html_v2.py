import os
from bs4 import BeautifulSoup

def process_file(file_path):
    print(f"Applying accessibility and SEO optimizations to {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    soup = BeautifulSoup(content, 'html.parser')
    modified = False
    
    # 1. Decompose unused google-analytics preconnect
    for link in soup.find_all('link', rel='preconnect'):
        href = link.get('href', '')
        if 'google-analytics.com' in href:
            link.decompose()
            modified = True
            
    # 2. Add aria-label to social links
    social_links = soup.find_all('div', class_='social-links')
    for wrapper in social_links:
        for a in wrapper.find_all('a'):
            href = a.get('href', '')
            if 'facebook.com' in href and not a.get('aria-label'):
                a['aria-label'] = "Facebook"
                modified = True
            elif 'instagram.com' in href and not a.get('aria-label'):
                a['aria-label'] = "Instagram"
                modified = True

    # 3. Add aria-label to whatsapp-float
    for a in soup.find_all('a', class_='whatsapp-float'):
        if not a.get('aria-label'):
            a['aria-label'] = "Contacto por WhatsApp"
            modified = True
            
    # 4. Add aria-hidden to decorative process numbers
    for span in soup.find_all('span', class_='process-number'):
        if not span.get('aria-hidden'):
            span['aria-hidden'] = "true"
            modified = True
            
    # 5. Change h4 in trust bar to div.trust-title
    for trust_text in soup.find_all('div', class_='trust-text'):
        for h4 in trust_text.find_all('h4'):
            h4.name = 'div'
            h4['class'] = h4.get('class', []) + ['trust-title']
            modified = True

    # 6. Check if style.css is still used instead of style.min.css (just in case)
    for link in soup.find_all('link', rel='stylesheet'):
        href = link.get('href', '')
        if 'style.css' in href and 'style.min.css' not in href:
            link['href'] = href.replace('style.css', 'style.min.css')
            modified = True

    # 7. Add srcset to dg_logo.webp to support Retina screens and pass PageSpeed
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if 'dg_logo.webp' in src:
            base = src.replace('dg_logo.webp', '')
            new_srcset = f"{src} 1x, {base}dg_logo@2x.webp 2x"
            if img.get('srcset') != new_srcset:
                img['srcset'] = new_srcset
                modified = True

    # 8. Use local FontAwesome CSS with font-display: swap to solve FCP/LCP warning
    base_dir = "/Users/kelebra/Documents/Rpm_Code/Dg_audio"
    rel_depth = os.path.relpath(base_dir, os.path.dirname(file_path))
    if rel_depth == '.':
        fa_path = 'assets/font-awesome.min.css'
    else:
        fa_path = os.path.join(rel_depth, 'assets/font-awesome.min.css').replace('\\', '/')

    for link in soup.find_all('link'):
        href = link.get('href', '')
        if 'cdnjs.cloudflare.com' in href and 'font-awesome' in href and 'all.min.css' in href:
            link['href'] = fa_path
            modified = True

    # 9. Add defer to script.js to remove it from the critical path
    for script in soup.find_all('script'):
        src = script.get('src', '')
        if 'script.js' in src:
            if not script.has_attr('defer') and not script.has_attr('async'):
                script['defer'] = ''
                modified = True

    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
            
def main():
    base_dir = "/Users/kelebra/Documents/Rpm_Code/Dg_audio"
    
    dirs_to_process = [
        base_dir,
        os.path.join(base_dir, "subpage"),
        os.path.join(base_dir, "subpage/soluciones"),
        os.path.join(base_dir, "subpage/applications"),
        os.path.join(base_dir, "subpage/blog")
    ]
    
    for directory in dirs_to_process:
        if not os.path.exists(directory):
            continue
        for file in os.listdir(directory):
            if file.endswith(".html"):
                file_path = os.path.join(directory, file)
                # Skip stubs in root
                if file == 'cine_en_casa.html' and directory == base_dir:
                    continue
                process_file(file_path)

if __name__ == "__main__":
    main()
