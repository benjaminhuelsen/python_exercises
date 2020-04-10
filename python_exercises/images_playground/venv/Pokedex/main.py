import sys
import os
from PIL import Image

img = Image.open("./pikatchu.jpg")
filtered_img = img.convert("L")
filtered_img.save("grey.png", "png")
filtered_img.show()