
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import numpy as np
import cv2

def Main:
	print("Start..")
	# Capture frame-by-frame
	cap1 = cv2.VideoCapture(0)
	s, img1 = cap1.read()
	# Save
	cv2.imwrite('1.jpg',img1)
	# When everything done, release the capture
	cap1.release()

	cap2 = cv2.VideoCapture(1)
	s, img2 = cap2.read()
	cv2.imwrite('2.jpg',img2)
	cap2.release()

	cap3 = cv2.VideoCapture(2)
	s, img3 = cap3.read()
	cv2.imwrite('3.jpg',img3)
	cap3.release()

	print("Done...")


	cv2.imshow('R',img1)
	cv2.imshow('M',img2)
	cv2.imshow('L',img3)
	cv2.waitKey(0)
	cv2.destroyAllWindows()













