
from PIL import Image, ImageEnhance
import os
from random import randrange
import secrets
import glob

def do_the_trick(path):
	img = Image.open(path)

	rand = secrets.token_hex(16)
	basewidth = 500
	wpercent = (basewidth/float(img.size[0]))
	hsize = int((float(img.size[1])*float(wpercent)))
	img = img.resize((basewidth,hsize), Image.ANTIALIAS)
	img.save("./images/"+rand+"_up.png")
	string = "backgroundremover -i " + "./images/"+rand+"_up.png" + " -m "+ "u2net_human_seg" + " -o " + "./images/"+rand+"_res.png"
	os.system(string)
	cropedImage = Image.open("./images/"+rand+"_res.png")
	converter = ImageEnhance.Color(cropedImage)
	cropedImage = converter.enhance(0)
	cropedImage.save("./images/"+rand+".png")
	files = glob.glob('./images/*_up.png') + glob.glob('./images/*_res.png')
	for file in files:
		os.remove(file)
	return rand
