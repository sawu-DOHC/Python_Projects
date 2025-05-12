import os
from PIL import Image

assets_folder = r"C:\Users\Sam\OneDrive\Desktop Cloud"
highres_folder = os.path.join(assets_folder, "new pics")
thumbnails_folder = os.path.join(assets_folder, "new thumb")
log_file_path = os.path.join(assets_folder, "thumb_log.txt")

def create_thumbnail(image_path, output_path, size=(700, 800)):
    with Image.open(image_path) as img:
        img.thumbnail(size)
        img.save(output_path)
        print(f"Created: {os.path.basename(image_path)} -> {os.path.basename(output_path)}")
        return os.path.basename(image_path), os.path.basename(output_path)

if not os.path.exists(thumbnails_folder):
    os.makedirs(thumbnails_folder)

created_pairs = []

if os.path.exists(highres_folder):
    for filename in os.listdir(highres_folder):
        if filename.lower().endswith(".jpg"):
            img_path = os.path.join(highres_folder, filename)
            thumb_name = f"{os.path.splitext(filename)[0]}_thumb.jpg"
            thumbnail_path = os.path.join(thumbnails_folder, thumb_name)

            pair = create_thumbnail(img_path, thumbnail_path)
            created_pairs.append(pair)
else:
    print(f"Folder not found: {highres_folder}")

# Write pairs to log
with open(log_file_path, "w") as f:
    for original, thumb in created_pairs:
        f.write(f"{original} -> {thumb}\n")

print(f"\nLog saved to: {log_file_path}")
