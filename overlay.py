
from PIL import Image, ImageOps, ImageEnhance
import os

img1 = Image.open(r"./assets/cyan_background.png")

img2 = Image.open(r"./assets/magenta_star.png")

img3 = Image.open(r"./assets/1.png")

string = "sudo backgroundremover -i " + "./assets/1.png" + " -m "+ "u2net_human_seg" + " -o ./assets/result.png"

os.system(string)

cropedImage = Image.open("./assets/result.png")

converter = ImageEnhance.Color(cropedImage)
cropedImage = converter.enhance(0)
# Pasting img2 image on top of img1
# starting at coordinates (0, 0)
img1.paste(img2, (0,0), mask = img2)
img1.paste(cropedImage, (0,0), mask = cropedImage)
# Displaying the image

img1 = img1.save("./assets/overlay.png")

