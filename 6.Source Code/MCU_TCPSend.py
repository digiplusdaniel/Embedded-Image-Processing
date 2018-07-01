# -*- coding: utf-8 -*-

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import cv2
import socket
import thread
import numpy as np
import time
import socket

import multiprocessing as mp

L_Camera_DrivesID = 0
M_Camera_DrivesID = 1
R_Camera_DrivesID = 2

#TCP
host = '192.168.1.111'   # sever's IP
port = 5555 #sever's port
address = (host, port)

Send_Image_X = 240
Send_Image_Y = 320

def funtion1():
        
    #initialize
    cap_L = cv2.VideoCapture(L_Camera_DrivesID)
    print(type(cap_L))
    
    print("open  L_Camera")
    cap_M = cv2.VideoCapture(M_Camera_DrivesID)
   
    print("open  M_Camera")
    cap_R = cv2.VideoCapture(R_Camera_DrivesID)
  
    print("open  R_Camera")
    flag_error = False

    while(True):
        print("Start")
        print(time.time())

        #Read_Camera_L_Image
        while(True):
            if not cap_L.grab():
                flag_error = True
                print("error L_Camera")
                break
            ret_L, image_L = cap_L.read()
            #print(image.shape)
            if not ret_L:
                continue
                #    Save        
            cv2.imwrite(str("L_Camera") + '.jpg',image_L)
            print("Done  L_Camera")
            break

        #Read_Camera_M_Image
        if (flag_error == False) :
            while(True):
                if not cap_M.grab():
                    flag_error = True
                    print("error M_Camera")
                    break
                ret_M, image_M = cap_M.read()
                #print(image.shape)
                if not ret_M:
                    continue
                    #    Save        
                cv2.imwrite(str("M_Camera") + '.jpg',image_M)
                print("Done  M_Camera")
                break

        #Read_Camera_R_Image
        if (flag_error == False) :
            while(True):
                if not cap_R.grab():
                    flag_error = True
                    print("error R_Camera")
                    break
                ret_R, image_R = cap_R.read()
                #print(image.shape)
                if not ret_R:
                    continue
                    #    Save        
                cv2.imwrite(str("R_Camera") + '.jpg',image_R)
                print("Done  R_Camera")
		break

           
    
        #Delay
        print(".\n.\n.\n")
        

         #Combine_Image
        if (flag_error == False) :
            L_Photo = cv2.imread('L_Camera.jpg')
            L_Photo = cv2.resize(L_Photo,(Send_Image_Y,Send_Image_X))    
            #print L_Photo.shape        
            M_Photo = cv2.imread('M_Camera.jpg')
            M_Photo = cv2.resize(M_Photo,(Send_Image_Y,Send_Image_X))
            R_Photo = cv2.imread('R_Camera.jpg')
            R_Photo = cv2.resize(R_Photo,(Send_Image_Y,Send_Image_X))
                    #imgFile1 = cv2.resize(imgFile1, (640, 480))
                    #imgFile2 = cv2.resize(imgFile2, (640, 480))
                    #imgFile3 = cv2.resize(imgFile3, (640, 480))
            imgArray = np.zeros([Send_Image_X,Send_Image_Y*3,3]).astype('uint8')
            imgArray[0:Send_Image_X, 0:Send_Image_Y] = np.copy(L_Photo)
            imgArray[0:Send_Image_X, Send_Image_Y:Send_Image_Y*2] = np.copy(M_Photo)
            imgArray[0:Send_Image_X, Send_Image_Y*2:Send_Image_Y*3] = np.copy(R_Photo)    
            cv2.imwrite("L_M_R_Photo.jpg",imgArray)
            print("Combie Done..")
        if cv2.waitKey(1) &0xFF ==ord('q'):  #按q键退出
            break

	flag_error == False

        #tcp
        socket02 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket02.connect(address)
        ##################################
        print('start send image')
        imgFile = open("L_M_R_Photo.jpg", "rb")
        while True:
            imgData = imgFile.readline(1024)
            if not imgData:
                break  
            socket02.send(imgData)
        imgFile.close()
        print('transmit end')
        ##################################
        socket02.close()  #
        print('client close')
        
        time.sleep(5)


if __name__ == "__main__":
    #thread
    m1 = mp.Process(target=funtion1,args=())
    m1.start()
    m1.join()
    


