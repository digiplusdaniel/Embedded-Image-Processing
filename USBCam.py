# -*- coding: utf-8 -*-

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import numpy as np
import cv2
import threading

class myThread (threading.Thread):
    def __init__(self, threadID, name, DrivesID):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.DrivesID = DrivesID
    def run(self):
        print "Starting " + self.name
        cap1 = cv2.VideoCapture(self.DrivesID)
        s, img1 = cap1.read()
        # Save
        cv2.imwrite(seld.DrivesID +'.jpg',img1)
        # When everything done, release the capture
        cap1.release()
        print "Done.." + self.name


# 创建新线程
thread1 = myThread(1, "Thread-1", 0)
thread2 = myThread(2, "Thread-2", 1)
thread3 = myThread(3, "Thread-3", 2)
 
# 开启线程
thread1.start()
thread2.start()
thread3.start()
print "All Done.."


##cv2.imshow('R',img1)
##cv2.imshow('M',img2)
##cv2.imshow('L',img3)
##cv2.waitKey(0)
##cv2.destroyAllWindows()













