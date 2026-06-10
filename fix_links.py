import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Restaurantes
content = re.sub(r'href="[^"]*"\s*class="sub-item"([^>]*>\s*<i class="fa-solid fa-utensils"></i>\s*<h4>Restaurantes)', r'href="subpage/applications/restaurantes.html" class="sub-item"\1', content)

# Replace Bares y Antros
content = re.sub(r'href="[^"]*"\s*class="sub-item"([^>]*>\s*<i class="fa-solid fa-glass-cheers"></i>\s*<h4>Bares y Antros)', r'href="subpage/applications/bares-antros.html" class="sub-item"\1', content)

# Replace Gimnasios
content = re.sub(r'href="[^"]*"\s*class="sub-item"([^>]*>\s*<i class="fa-solid fa-dumbbell"></i>\s*<h4>Gimnasios)', r'href="subpage/applications/gimnasios.html" class="sub-item"\1', content)

# Replace Cafeterias
content = re.sub(r'href="[^"]*"\s*class="sub-item"([^>]*>\s*<i class="fa-solid fa-coffee"></i>\s*<h4>Cafeterías)', r'href="subpage/applications/cafeterias.html" class="sub-item"\1', content)

# Replace Retail (it might not be in index, but if it is)
content = re.sub(r'href="[^"]*"\s*class="sub-item"([^>]*>\s*<i class="[^"]*"></i>\s*<h4>Retail)', r'href="subpage/applications/retail.html" class="sub-item"\1', content)

# Replace Barberias (might not be there)
content = re.sub(r'href="[^"]*"\s*class="sub-item"([^>]*>\s*<i class="[^"]*"></i>\s*<h4>Barberías)', r'href="subpage/applications/barberias.html" class="sub-item"\1', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Links fixed in index.html")
