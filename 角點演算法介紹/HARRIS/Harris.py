import cv2
import numpy as np
import matplotlib.pyplot as plt

filename = 'road_left.jpg'
filename2 = 'road_right.jpg'
img = cv2.imread(filename)
img2 = cv2.imread(filename2)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
gray2 = np.float32(gray2)
dst = cv2.cornerHarris(gray,4,6,0.04)
dst2 = cv2.cornerHarris(gray2,4,6,0.04)


# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.03*dst.max()]=[255,0,0]
img2[dst2>0.03*dst2.max()]=[0,255,0]

plt.subplot(121)
plt.imshow(dst)
plt.subplot(122)
plt.imshow(dst2)
plt.show()