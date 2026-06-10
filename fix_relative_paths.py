import os
import re

apps_dir = 'subpage/applications/'
files = [f for f in os.listdir(apps_dir) if f.endswith('.html') and f != 'audio-distribuido.html']

for filename in files:
    path = os.path.join(apps_dir, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements to make them two levels deep (../../)
    content = content.replace('href="../style.css"', 'href="../../style.css"')
    content = content.replace('src="../assets/', 'src="../../assets/')
    content = content.replace('href="../index.html', 'href="../../index.html')
    content = content.replace("url('../assets/", "url('../../assets/")
    content = content.replace('url("../assets/', 'url("../../assets/')
    content = content.replace('src="../script.js"', 'src="../../script.js"')

    # Also replace logo images and header icons if they are pointing to single level up
    content = content.replace('src="../assets/dg_logo.webp"', 'src="../../assets/dg_logo.webp"')
    content = content.replace('src="../assets/DG.png"', 'src="../../assets/DG.png"')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Fixed paths in: {filename}")

print("All relative paths fixed successfully.")
