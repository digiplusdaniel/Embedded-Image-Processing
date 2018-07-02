# -*- coding: utf8 -*-

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')


import socket
import cv2 
import numpy as np



filename = "original.png"

host = '192.168.8.102'  # 對server端為主機位置
port = 5555
# host = socket.gethostname()
# port = 5000
address = (host, port)

socket01 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET:默認IPv4, SOCK_STREAM:TCP

socket01.bind(address)  # 讓這個socket要綁到位址(ip/port)
socket01.listen(1)  # listen(backlog)
# backlog:操作系統可以掛起的最大連接數量。該值至少為1，大部分應用程序設為5就可以了
print('Socket Startup')

conn, addr = socket01.accept()  # 接受遠程計算機的連接請求，建立起與客戶機之間的通信連接
# 返回（conn,address)
# conn是新的套接字對象，可以用來接收和發送數據。address是連接客戶端的地址
print('Connected by', addr)

##################################################
# 開始接收
print('begin write image file {}'.format(filename))
imgFile = open(filename, 'wb')  # 開始寫入圖片檔
while True:
    imgData = conn.recv(512)  # 接收遠端主機傳來的數據
    if not imgData:
        break  # 讀完檔案結束迴圈
    imgFile.write(imgData)
    
imgFile.close()
print('image save')
##################################################

conn.close()  # 關閉
socket01.close()
print('server close')




img = cv2.imread(filename,0)


h = img.shape[0]
w = img.shape[1]

Mask_x = [[-1,0,1],[-2,0,2],[-1,0,1]]
Mask_y = [[1,2,1],[0,0,0],[-1,-2,-1]]

Sobel_x = np.zeros((h, w, 1),dtype = np.uint8)
Sobel_y = np.zeros((h, w, 1),dtype = np.uint8) 

sum_x = 0
sum_y = 0
print('Deal',filename)
for x in range(1,h-1):
    print('{0:.2f} %'.format(x*100.0/w))
    for y in range(1,w-1):     
        sum_x = 0
        sum_y = 0
        for a in range(3):
            for b in range(3):
                xn = x + a -1
                yn = y + b -1
                # convolution
                sum_x = sum_x + img[xn][yn] * Mask_x[a][b]
                sum_y = sum_y + img[xn][yn] * Mask_y[a][b]
                    
        # /4:正規化  4: 強度 1+2+1
        Sobel_x[x][y] = abs(sum_x/4) 
        Sobel_y[x][y] = abs(sum_y/4) 
Sobel = abs(Sobel_x) + abs(Sobel_y)

print(img.shape)

cv2.imshow("Sobel_x",Sobel_x)
cv2.imshow("Sobel_y",Sobel_y)
cv2.imshow("Sobel",Sobel)
cv2.imshow("Original",img)

cv2.waitKey(0)  
cv2.destroyAllWindows()
