import os
import re
from bs4 import BeautifulSoup

def optimize_html_file(file_path):
    print(f"Optimizing {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # BeautifulSoup parse
    soup = BeautifulSoup(content, 'html.parser')
    
    # 1. Update style.css to style.min.css
    for link in soup.find_all('link', rel='stylesheet'):
        href = link.get('href', '')
        if 'style.css' in href:
            link['href'] = href.replace('style.css', 'style.min.css')
            
    # 2. Defer Google Fonts
    for link in soup.find_all('link', rel='stylesheet'):
        href = link.get('href', '')
        if 'fonts.googleapis.com/css2' in href:
            orig_href = href
            link['rel'] = ['preload']
            link['as'] = 'style'
            link['onload'] = "this.onload=null;this.rel='stylesheet'"
            
            # Check if noscript already exists to avoid double wrapping
            sibling = link.next_sibling
            while sibling and sibling.name != 'noscript' and sibling.name != 'link':
                sibling = sibling.next_sibling
            
            if not sibling or sibling.name != 'noscript':
                noscript = soup.new_tag('noscript')
                fallback_link = soup.new_tag('link', rel='stylesheet', href=orig_href)
                noscript.append(fallback_link)
                link.insert_after(noscript)
            
    # 3. Defer FontAwesome
    for link in soup.find_all('link', rel='stylesheet'):
        href = link.get('href', '')
        if 'font-awesome' in href or 'cdnjs.cloudflare.com/ajax/libs/font-awesome' in href:
            orig_href = href
            link['rel'] = ['preload']
            link['as'] = 'style'
            link['onload'] = "this.onload=null;this.rel='stylesheet'"
            
            sibling = link.next_sibling
            while sibling and sibling.name != 'noscript' and sibling.name != 'link':
                sibling = sibling.next_sibling
                
            if not sibling or sibling.name != 'noscript':
                noscript = soup.new_tag('noscript')
                fallback_link = soup.new_tag('link', rel='stylesheet', href=orig_href)
                noscript.append(fallback_link)
                link.insert_after(noscript)
            
    # 4. Remove Facebook preconnect
    for link in soup.find_all('link', rel='preconnect'):
        href = link.get('href', '')
        if 'connect.facebook.net' in href:
            link.decompose()
            
    # 5. Add dimensions to dg_logo.webp
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if 'dg_logo.webp' in src:
            if not img.get('width') or not img.get('height'):
                img['width'] = "105"
                img['height'] = "105"
                
    # 6. Add dimensions to DG.png
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if 'DG.png' in src:
            if not img.get('width') or not img.get('height'):
                img['width'] = "112"
                img['height'] = "60"
                
    # 7. Add dimensions to cards
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if 'home-card-dg-audiosound' in src:
            if not img.get('width') or not img.get('height'):
                img['width'] = "634"
                img['height'] = "422"

    html = str(soup)
    
    # 8. Deferred GTM load (only on index.html)
    if os.path.basename(file_path) == "index.html":
        gtm_loader_regex = r'\s*// GTM loader\s*\(function\(w,d,s,l,i\)\{.*?\}\)\(window,document,\'script\',\'dataLayer\',window\.DG_TRACKING_CONFIG\.googleTagManagerId\);'
        
        deferred_gtm = """
      // Deferred GTM loader (PageSpeed Optimization)
      function loadGTM() {
        if (window.gtmLoaded) return;
        window.gtmLoaded = true;
        
        // Remove event listeners
        events.forEach(function(e) { window.removeEventListener(e, loadGTM); });
        
        (function(w,d,s,l,i){
          w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});
          var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';
          var jScript=d.createElement(s);jScript.async=true;jScript.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;
          f.parentNode.insertBefore(jScript,f);
        })(window,document,'script','dataLayer',window.DG_TRACKING_CONFIG.googleTagManagerId);
      }
      
      var events = ['scroll', 'click', 'mousemove', 'touchstart', 'keydown'];
      events.forEach(function(e) { window.addEventListener(e, loadGTM, { passive: true }); });
      setTimeout(loadGTM, 3500);"""
        
        html = re.sub(gtm_loader_regex, deferred_gtm, html, flags=re.DOTALL)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)

def main():
    base_dir = "/Users/kelebra/Documents/Rpm_Code/Dg_audio"
    
    # List of directories to search
    dirs_to_process = [
        base_dir,
        os.path.join(base_dir, "subpage"),
        os.path.join(base_dir, "subpage/soluciones"),
        os.path.join(base_dir, "subpage/applications")
    ]
    
    count = 0
    for directory in dirs_to_process:
        if not os.path.exists(directory):
            continue
        for file in os.listdir(directory):
            if file.endswith(".html"):
                file_path = os.path.join(directory, file)
                optimize_html_file(file_path)
                count += 1
                
    print(f"Finished. Optimized {count} HTML files.")

if __name__ == "__main__":
    main()
