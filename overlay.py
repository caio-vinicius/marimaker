
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
	img1 = Image.open(r"./assets/cyan_background.png")

	img2 = Image.open(r"./assets/magenta_star.png")

	img3 = Image.open(path)

	basewidth = 400
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
	img1.paste(cropedImage, (90,170), mask = cropedImage)

	img1 = img1.save("./assets/overlay.png")
