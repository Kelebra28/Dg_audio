import os
import shutil

src_dir = "example/WEB DG Audiosound/02 assets/Imagenes"
dst_dir = "assets/Imagenes"

def sync():
    if not os.path.exists(src_dir):
        print("Source directory does not exist.")
        return
        
    copied_count = 0
    for root, dirs, files in os.walk(src_dir):
        relative_path = os.path.relpath(root, src_dir)
        target_dir = os.path.join(dst_dir, relative_path)
        
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
            
        for file in files:
            # Skip hidden files
            if file.startswith('.'):
                continue
            src_file = os.path.join(root, file)
            dst_file = os.path.join(target_dir, file)
            if not os.path.exists(dst_file) or os.path.getmtime(src_file) > os.path.getmtime(dst_file):
                shutil.copy2(src_file, dst_file)
                print(f"Copied: {src_file} -> {dst_file}")
                copied_count += 1
                
    print(f"Sync complete. Copied {copied_count} files.")

if __name__ == '__main__':
    sync()
