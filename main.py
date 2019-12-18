import random
import sys
from PIL import Image

assert len(sys.argv) == 3, "Please specify an input path and output path"

input_path = sys.argv[1]
output_path = sys.argv[2]

img = Image.open(input_path)
width, height = img.size

# Create a new, all-white image that's the same size as the original
new_img = Image.new("RGB", (width * 2 - 3, height * 2 - 4), "white")

members = [0] * 9
for i in range(1, width - 1):
    for j in range(1, height - 1):
        r, g, b = img.getpixel((i, j))
        members[0] = img.getpixel((i - 1, j - 1))
        members[1] = img.getpixel((i - 1, j))
        members[2] = img.getpixel((i - 1, j + 1))
        members[3] = img.getpixel((i, j - 1))
        members[4] = img.getpixel((i, j))
        members[5] = img.getpixel((i, j + 1))
        members[6] = img.getpixel((i + 1, j - 1))
        members[7] = img.getpixel((i + 1, j))
        members[8] = img.getpixel((i + 1, j + 1))
        r, g, b = (random.choice(members))
        new_img.putpixel((i - 1, j - 1), (255 - r, 255 - g, 255 - b))
        new_img.putpixel((i + width - 3, j - 1), (r, 0, b))
        new_img.putpixel((i - 1, j + height - 3), (r, g, 0))
        new_img.putpixel((i + width - 3, j + height - 3), (0, g, b))

new_img.save(output_path)
