from PIL import Image
import os

# Windows-style path (make sure to use raw string r"..." to handle backslashes)
input_folder = r'C:\Users\Sam\OneDrive\Desktop Cloud\HTML_Projects\expservicecenter.com\Assets'
output_folder = r'C:\Users\Sam\OneDrive\Desktop Cloud\HTML_Projects\expservicecenter.com\Assets\compressed'

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through images img1.jpg to img20.jpg
for i in range(1, 21):
    img_path = os.path.join(input_folder, f'img{i}.jpg')
    output_path = os.path.join(output_folder, f'img{i}.jpg')

    # Open and process
    img = Image.open(img_path)

    # (Optional) Resize if you want
    # img = img.resize((img.width // 2, img.height // 2))

    # Save with reduced quality
    img.save(output_path, 'JPEG', quality=30, optimize=True)

print("All images compressed successfully!")
