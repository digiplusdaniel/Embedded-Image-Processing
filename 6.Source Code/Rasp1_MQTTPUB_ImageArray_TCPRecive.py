import cv2
import time
import paho.mqtt.client as mqtt
import socket
import numpy as np

filename = "receive.jpg"
Con_Flag=0
host = '192.168.1.111'  
port = 5555
#host = socket.gethostname()
# port = 5000
address = (host, port)


####################
def on_connect(client, userdata, flags, rc):
    print("Connected with code :"+ str(rc))
    client.subscribe("test/#")

def on_message(client, userdata, msg):
    print (str(msg.payload))
    
    
####################
#initial
#tcp
socket01 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket01.bind(address)  
socket01.listen(1)  
print('Socket Startup')
#mqtt
broker="m12.cloudmqtt.com"
MQTTport =14699
client = mqtt.Client()
print("Connecting to broker",broker)
client.username_pw_set("hsfirkgo", "s209oFyCMG-9")
client.connect(broker,MQTTport,60)
client.loop_start()


#main
while(True):
    print('waiting...')
    conn, addr = socket01.accept()  
    print('Connected by', addr)

    ##################################################
    print('begin write image file {}'.format(filename))
    imgFile = open(filename, 'wb') 
    while True:
        imgData = conn.recv(512)  
        if not imgData:
            break  
        imgFile.write(imgData)
        
    imgFile.close()
    print('image save')
    ##################################################

    Time = time.strftime('%Y/%m:/%d: ==> %H:%M:%S',time.localtime(time.time()))
    image = open(filename,"rb")
    fileContent = image.read()
    byteArr = bytearray(fileContent)
    if (Con_Flag % 2 == 0): 
        client.publish("Time_RSP1",Time,0)
        client.publish("Image_RSP1",byteArr,0)
    if (Con_Flag % 2 == 1):
        client.publish("Time_RSP2",Time,0)
        client.publish("Image_RSP2",byteArr,0)
    Con_Flag += 1 
    time.sleep(10)
    
conn.close()  
socket01.close()
client.loop_stop()
client.disconnect()
cv2.destroyAllWindow()

