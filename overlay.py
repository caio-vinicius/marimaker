
from PIL import Image, ImageEnhance
import os

def do_the_trick(path):
	img = Image.open(path)

	basewidth = 500
	wpercent = (basewidth/float(img.size[0]))
	hsize = int((float(img.size[1])*float(wpercent)))
	img3 = img.resize((basewidth,hsize), Image.ANTIALIAS)
	img.save("./assets/upload.png")
	string = "sudo backgroundremover -i " + "./assets/upload.png" + " -m "+ "u2net_human_seg" + " -o ./assets/result.png"
	os.system(string)
	cropedImage = Image.open("./assets/result.png")
	converter = ImageEnhance.Color(cropedImage)
	cropedImage = converter.enhance(0)
	cropedImage.save("./assets/overlay.png")
