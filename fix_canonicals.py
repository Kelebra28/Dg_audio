import os
from bs4 import BeautifulSoup

def fix_canonical_in_file(file_path, base_dir):
    filename = os.path.basename(file_path)
    # Ignore stubs/redirects in root
    if filename == 'cine_en_casa.html' and os.path.dirname(file_path) == base_dir:
        return
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    soup = BeautifulSoup(content, 'html.parser')
    
    # Calculate correct canonical URL
    if filename == 'index.html' and os.path.dirname(file_path) == base_dir:
        correct_url = "https://dgaudiosound.com/"
    else:
        rel_path = os.path.relpath(file_path, base_dir)
        correct_url = f"https://dgaudiosound.com/{rel_path}"
        
    # Find existing canonical tag
    canonical = soup.find('link', rel='canonical')
    
    if canonical:
        current_href = canonical.get('href', '')
        if current_href != correct_url:
            print(f"Updating canonical in {os.path.relpath(file_path, base_dir)}: {current_href} -> {correct_url}")
            canonical['href'] = correct_url
            # Write back
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
    else:
        print(f"Inserting missing canonical in {os.path.relpath(file_path, base_dir)}: {correct_url}")
        new_canonical = soup.new_tag('link', rel='canonical', href=correct_url)
        # Insert inside head
        if soup.head:
            # Let's insert it after charset/viewport/title
            # We can just append it or insert it as the first element
            soup.head.insert(0, new_canonical)
            # Write back
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
        else:
            print(f"Warning: No <head> tag found in {file_path}")

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
                fix_canonical_in_file(file_path, base_dir)

if __name__ == "__main__":
    main()
