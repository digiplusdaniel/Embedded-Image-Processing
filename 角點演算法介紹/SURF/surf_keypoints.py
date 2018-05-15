import sys
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('road_left.jpg')
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)

surf = cv.xfeatures2d.SURF_create()
kp = surf.detect(gray,None)

img=cv.drawKeypoints(gray,kp,img)

plt.imshow(img),plt.show()


