
from PIL import Image, ImageEnhance
import os
from random import randrange

def do_the_trick(path):
	img = Image.open(path)

	rand = str(randrange(10000000000))
	basewidth = 500
	wpercent = (basewidth/float(img.size[0]))
	hsize = int((float(img.size[1])*float(wpercent)))
	img = img.resize((basewidth,hsize), Image.ANTIALIAS)
	img.save("./assets/"+rand+"_up.png")
	string = "backgroundremover -i " + "./assets/"+rand+"_up.png" + " -m "+ "u2net_human_seg" + " -o " + "./assets/"+rand+"_res.png"
	os.system(string)
	cropedImage = Image.open("./assets/"+rand+"_res.png")
	converter = ImageEnhance.Color(cropedImage)
	cropedImage = converter.enhance(0)
	cropedImage.save("./assets/"+rand+".png")
	return rand
