import sys
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('road.jpg')
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)

sift = cv.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)

img=cv.drawKeypoints(gray,kp,img)

cv.imwrite('sift_keypoints1.jpg',img)

img=cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv.imwrite('sift_keypoints2.jpg',img)

#plt.imshow(img),plt.show()
cv.imshow('sift key points', img)
cv.waitKey()
