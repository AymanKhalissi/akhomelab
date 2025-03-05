from PIL import Image

# Open the image
img = Image.open("icon.png")  # Replace with your image path

# Convert to .ico
img.save("icon.ico", format="ICO", sizes=[(256, 256)])  # 256x256 recommended
