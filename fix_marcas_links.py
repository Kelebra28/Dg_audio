import os
import re

root_dir = "/Users/kelebra/Documents/Rpm_Code/Dg_audio"
example_dir = os.path.join(root_dir, "example")

def get_rel_path_to(current_file_dir, target_rel_path):
    target_abs_path = os.path.join(root_dir, target_rel_path)
    rel = os.path.relpath(target_abs_path, current_file_dir)
    return rel

for dirpath, _, filenames in os.walk(root_dir):
    if example_dir in dirpath:
        continue
    for filename in filenames:
        if filename.endswith(".html"):
            filepath = os.path.join(dirpath, filename)
            # Skip root index.html and root cine_en_casa.html
            if filepath in [os.path.join(root_dir, "index.html"), os.path.join(root_dir, "cine_en_casa.html")]:
                continue
                
            current_file_dir = os.path.dirname(filepath)
            rel_index = get_rel_path_to(current_file_dir, "index.html")
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Check if this subpage has the Marcas heading
            has_marcas_heading = "Marcas profesionales para soluciones de" in content
            
            if has_marcas_heading:
                # Add id="marcas" to the container div if it doesn't have it
                # Target: <div class="container" style="text-align: center; max-width: 800px; margin-top: 5rem; margin-bottom: 2rem;">
                # followed by class="eyebrow" containing "Marcas y tecnología"
                div_pattern = r'(<div class="container" style="text-align: center; max-width: 800px; margin-top: 5rem; margin-bottom: 2rem;">)(\s*<span class="eyebrow[^>]*>\s*Marcas y tecnología)'
                if re.search(div_pattern, content):
                    content = re.sub(div_pattern, r'<div id="marcas" class="container" style="text-align: center; max-width: 800px; margin-top: 5rem; margin-bottom: 2rem;">\g<2>', content)
                    print(f"Added id='marcas' to div in {filename}")
                
                # Update navbar link to scroll locally
                content = re.sub(r'(<a[^>]*class="nav-link[^"]*"[^>]*href=")[^"]*("[^>]*>\s*Marcas\s*</a>)', r'\g<1>#marcas\2', content)
                # Update footer link to scroll locally
                content = re.sub(r'(<li>\s*<a[^>]*href=")[^"]*("[^>]*>\s*Nuestras Marcas\s*</a>\s*</li>)', r'\g<1>#marcas\2', content)
                print(f"Set local #marcas link in {filename}")
            else:
                # Update navbar link to go to index.html#marcas
                content = re.sub(r'(<a[^>]*class="nav-link[^"]*"[^>]*href=")[^"]*("[^>]*>\s*Marcas\s*</a>)', r'\g<1>' + rel_index + r'#marcas\2', content)
                # Update footer link to go to index.html#marcas
                content = re.sub(r'(<li>\s*<a[^>]*href=")[^"]*("[^>]*>\s*Nuestras Marcas\s*</a>\s*</li>)', r'\g<1>' + rel_index + r'#marcas\2', content)
                
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
                
print("Done fixing Marcas links.")
