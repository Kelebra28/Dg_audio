import os
from datetime import datetime

def get_html_files(base_dir):
    html_files = []
    
    # 1. Add homepage (root index.html)
    # We will represent this as just "https://dgaudiosound.com/"
    html_files.append({
        'url': 'https://dgaudiosound.com/',
        'priority': '1.0',
        'changefreq': 'weekly'
    })
    
    # Helper to check if a file should be ignored
    def should_ignore(file_path):
        filename = os.path.basename(file_path)
        # Ignore redirects, stubs, example pages, templates
        if filename == 'index.html' and os.path.dirname(file_path) == base_dir:
            return True # Already added as '/'
        if filename == 'cine_en_casa.html' and os.path.dirname(file_path) == base_dir:
            return True # Root cine_en_casa.html is a stub redirect
        if 'example' in file_path.lower():
            return True
        if '.git' in file_path or '.vscode' in file_path:
            return True
        return False

    # 2. Walk directories to find public html files
    for root, dirs, files in os.walk(base_dir):
        if 'example' in root.lower() or '.git' in root or '.vscode' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                full_path = os.path.join(root, file)
                if should_ignore(full_path):
                    continue
                
                # Get relative path from base_dir
                rel_path = os.path.relpath(full_path, base_dir)
                url = f"https://dgaudiosound.com/{rel_path}"
                
                # Determine priority and changefreq based on path structure
                priority = '0.7'
                changefreq = 'monthly'
                
                if 'soluciones.html' in rel_path or 'soluciones/' in rel_path:
                    priority = '0.8'
                elif 'aplicaciones.html' in rel_path:
                    priority = '0.8'
                elif 'cine_en_casa.html' in rel_path:
                    priority = '0.8'
                elif 'bares_y_cafeterias.html' in rel_path:
                    priority = '0.8'
                elif 'blog.html' in rel_path:
                    priority = '0.7'
                    changefreq = 'weekly'
                elif 'blog/' in rel_path:
                    priority = '0.6'
                
                html_files.append({
                    'url': url,
                    'priority': priority,
                    'changefreq': changefreq
                })
                
    return html_files

def main():
    base_dir = "/Users/kelebra/Documents/Rpm_Code/Dg_audio"
    sitemap_path = os.path.join(base_dir, "sitemap.xml")
    
    html_files = get_html_files(base_dir)
    
    # Sort files to make the sitemap clean and ordered
    html_files.sort(key=lambda x: (x['url'] != 'https://dgaudiosound.com/', x['priority'], x['url']), reverse=True)
    # Actually sort by priority descending first, then url ascending
    html_files.sort(key=lambda x: (-float(x['priority']), x['url']))
    
    today = datetime.today().strftime('%Y-%m-%d')
    
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    
    for file in html_files:
        xml_lines.append('   <url>')
        xml_lines.append(f'      <loc>{file["url"]}</loc>')
        xml_lines.append(f'      <lastmod>{today}</lastmod>')
        # optional: include changefreq
        if file['url'] == 'https://dgaudiosound.com/' or file['changefreq'] == 'weekly':
            xml_lines.append(f'      <changefreq>{file["changefreq"]}</changefreq>')
        xml_lines.append(f'      <priority>{file["priority"]}</priority>')
        xml_lines.append('   </url>')
        
    xml_lines.append('</urlset>')
    
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(xml_lines) + '\n')
        
    print(f"Generated sitemap with {len(html_files)} URLs at {sitemap_path}")

if __name__ == "__main__":
    main()
