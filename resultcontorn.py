from cgitb import grey
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("result.png", cv2.IMREAD_UNCHANGED)

*_, alpha = cv2.split(image)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(image, contours, -1, (255, 255, 0), 5)

cv2.imwrite("./write_countour.png", image)
plt.axis('off')
plt.imshow(image)
plt.savefig("result_out.png", bbox_inches='tight', pad_inches=0)

# show it
