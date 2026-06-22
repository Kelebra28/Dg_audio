import re
import os

def minify_css(css_content):
    # Remove comments
    css = re.sub(r'/\*.*?\*/', '', css_content, flags=re.DOTALL)
    # Remove whitespace around punctuation
    css = re.sub(r'\s*([\{\}:;,])\s*', r'\1', css)
    # Replace multiple spaces with a single space
    css = re.sub(r'\s+', ' ', css)
    # Strip leading and trailing whitespace
    return css.strip()

def main():
    base_dir = "/Users/kelebra/Documents/Rpm_Code/Dg_audio"
    src_path = os.path.join(base_dir, "style.css")
    dest_path = os.path.join(base_dir, "style.min.css")
    
    if not os.path.exists(src_path):
        print(f"Error: {src_path} does not exist.")
        return

    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()

    minified = minify_css(content)
    
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(minified)

    original_size = os.path.getsize(src_path) / 1024
    minified_size = os.path.getsize(dest_path) / 1024
    print(f"Minified CSS: {original_size:.2f} KiB -> {minified_size:.2f} KiB")

if __name__ == "__main__":
    main()
