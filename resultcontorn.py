from cgitb import grey
import cv2
import matplotlib.pyplot as plt
import numpy as np

# *_, alpha = cv2.split(image)
image = cv2.imread("result.png", cv2.IMREAD_UNCHANGED)

gray = cv2.cvtColor(image, cv2.COLOR_RGBA2GRAY)
cv2.imwrite("AGORA.png", gray)
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(image, contours, -1, (255, 255, 0, 255), 5)
img_gray = image[:, :, 3]
plt.axis('off')
plt.imshow(img_gray, cmap='gray', vmin=0, vmax=255)
plt.savefig("ztoma.png", bbox_inches='tight', pad_inches=0)
plt.imshow(image)
plt.savefig("result_out.png", bbox_inches='tight', pad_inches=0)


# dst = cv2.merge((gray, gray, gray, alpha))
# cv2.imwrite("zz.png", dst)

plt.axis('off')
plt.imshow(image)
plt.savefig("result_out.png", bbox_inches='tight', pad_inches=0)
