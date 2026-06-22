import os
from bs4 import BeautifulSoup

def verify_file(file_path):
    errors = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # 1. Check if style.min.css is loaded instead of style.css
        style_links = soup.find_all('link', rel='stylesheet')
        for link in style_links:
            href = link.get('href', '')
            if 'style.css' in href and 'style.min.css' not in href:
                errors.append(f"Loads unminified stylesheet: {href}")
        
        # 2. Check for preload/noscript duplication or malformation
        preloads = soup.find_all('link', rel='preload')
        for p in preloads:
            # Check for double rel list or attributes
            rel = p.get('rel')
            if isinstance(rel, list) and len(rel) > 1:
                errors.append(f"Multiple rels in preload link: {rel}")
        
        # 3. Check for image width/height attributes
        imgs = soup.find_all('img')
        for img in imgs:
            src = img.get('src', '')
            if 'dg_logo.webp' in src:
                if not img.get('width') or not img.get('height'):
                    errors.append(f"Logo img missing width or height: {src}")
            elif 'DG.png' in src:
                if not img.get('width') or not img.get('height'):
                    errors.append(f"Footer logo img missing width or height: {src}")
            elif 'home-card-dg-audiosound' in src:
                if not img.get('width') or not img.get('height'):
                    errors.append(f"Solution card img missing width or height: {src}")
        
        # 4. Check for preconnect count
        preconnects = soup.find_all('link', rel='preconnect')
        if len(preconnects) > 4:
            errors.append(f"Too many preconnect links ({len(preconnects)})")
        for pc in preconnects:
            if 'facebook.net' in pc.get('href', ''):
                errors.append("Unused facebook.net preconnect still present")
                
        # 5. Check if GTM loader exists and is deferred on index.html
        if os.path.basename(file_path) == "index.html":
            scripts = soup.find_all('script')
            gtm_found = False
            gtm_deferred = False
            for s in scripts:
                text = s.string or ''
                if 'gtm.js' in text:
                    gtm_found = True
                    if 'loadGTM' in text and 'addEventListener' in text:
                        gtm_deferred = True
            if gtm_found and not gtm_deferred:
                errors.append("GTM loader found but is NOT deferred")
                
    except Exception as e:
        errors.append(f"Error parsing file: {e}")
        
    return errors

def main():
    base_dir = "/Users/kelebra/Documents/Rpm_Code/Dg_audio"
    files_to_check = [
        os.path.join(base_dir, "index.html"),
        os.path.join(base_dir, "subpage/cine_en_casa.html"),
        os.path.join(base_dir, "subpage/soluciones/negocios-y-experiencias.html"),
        os.path.join(base_dir, "subpage/applications/cafeterias.html")
    ]
    
    total_errors = 0
    for file_path in files_to_check:
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue
        errors = verify_file(file_path)
        if errors:
            print(f"❌ Verification failed for {os.path.relpath(file_path, base_dir)}:")
            for err in errors:
                print(f"  - {err}")
                total_errors += 1
        else:
            print(f"✅ Verification passed for {os.path.relpath(file_path, base_dir)}")
            
    if total_errors == 0:
        print("\n🎉 ALL CHECKS PASSED SUCCESSFULLY!")
    else:
        print(f"\nFound {total_errors} errors total.")

if __name__ == "__main__":
    main()
