
from PIL import Image, ImageOps, ImageEnhance
import os

def do_the_trick(path):
	img1 = Image.open(r"./assets/cyan_background.png")

	img2 = Image.open(r"./assets/magenta_star.png")

	img3 = Image.open(path)

	basewidth = 500
	wpercent = (basewidth/float(img3.size[0]))
	hsize = int((float(img3.size[1])*float(wpercent)))
	img3 = img3.resize((basewidth,hsize), Image.ANTIALIAS)

	img3.save("./assets/2.png")

	string = "sudo backgroundremover -i " + "./assets/2.png" + " -m "+ "u2net_human_seg" + " -o ./assets/result.png"

	os.system(string)

	cropedImage = Image.open("./assets/result.png")

	converter = ImageEnhance.Color(cropedImage)
	cropedImage = converter.enhance(0)

	img1.paste(img2, (0,0), mask = img2)
	img1.paste(cropedImage, (40,130), mask = cropedImage)

	img1 = img1.save("./assets/overlay.png")
