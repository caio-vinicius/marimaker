
from PIL import Image, ImageOps, ImageEnhance
import cv2
import matplotlib.pyplot as plt
import os

def contour():
	image = cv2.imread("./assets/cropResult.png")
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
	_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV)
	contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	image = cv2.drawContours(image, contours, -1, (255, 255, 0), 5)
	plt.imshow(image)
	plt.savefig("./assets/countornedResult.png", bbox_inches='tight', pad_inches=0)

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
