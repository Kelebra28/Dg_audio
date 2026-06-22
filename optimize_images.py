import os
from PIL import Image

def optimize_image(src_path, dest_path, size=None, quality=80):
    if not os.path.exists(src_path):
        print(f"Error: {src_path} does not exist.")
        return False
    try:
        img = Image.open(src_path)
        
        # Convert RGBA to RGB if saving to webp or jpeg without alpha channel
        # webp supports alpha, but if we don't need it, we can keep it
        if img.mode in ('RGBA', 'LA') and src_path.endswith('.png'):
            # keep alpha for png/webp
            pass

        if size:
            print(f"Resizing {src_path} from {img.size} to {size}...")
            img = img.resize(size, Image.Resampling.LANCZOS)
        
        img.save(dest_path, "WEBP", quality=quality, optimize=True)
        old_size_kb = os.path.getsize(src_path) / 1024
        new_size_kb = os.path.getsize(dest_path) / 1024
        print(f"Saved {dest_path}: {old_size_kb:.2f} KiB -> {new_size_kb:.2f} KiB")
        return True
    except Exception as e:
        print(f"Failed to optimize {src_path}: {e}")
        return False

def main():
    base_dir = "/Users/kelebra/Documents/Rpm_Code/Dg_audio"
    
    # 1. Optimize logo (210x210 for retina display fallback of 105x105)
    logo_path = os.path.join(base_dir, "assets/dg_logo.webp")
    optimize_image(logo_path, logo_path, size=(210, 210), quality=85)
    
    # 2. Optimize Home solutions cards to 634x422 (displayed size in CSS)
    home_dir = os.path.join(base_dir, "assets/Home")
    cards = [
        "home-card-dg-audiosound-residencial-premium.webp",
        "home-card-dg-audiosound-negocios-experiencias-comerciales.webp",
        "home-card-dg-audiosound-corporativo-institucional.webp",
        "home-card-dg-audiosound-eventos-creadores-produccion.webp"
    ]
    
    for card in cards:
        card_path = os.path.join(home_dir, card)
        optimize_image(card_path, card_path, size=(634, 422), quality=80)

if __name__ == "__main__":
    main()
