# -*- coding: cp950 -*-
import socket

# host = socket.gethostname()
# port = 5000
host = '192.168.8.100'  # ��server�ݬ��D����m
port = 5555
address = (host, port)

socket02 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET:�q�{IPv4, SOCK_STREAM:TCP

socket02.connect(address)  # �ΨӽШD�s�����{�A�Ⱦ�

##################################
# �}�l�ǿ�
print('start send image')
imgFile = open("file.png", "rb")
while True:
    imgData = imgFile.readline(512)
    if not imgData:
        break  # Ū���ɮ׵����j��
    socket02.send(imgData)
imgFile.close()
print('transmit end')
##################################

socket02.close()  # ����
print('client close')
