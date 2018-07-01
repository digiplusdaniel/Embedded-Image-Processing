Environment :

Raspbian  -- Stretch

Python    -- 2.7

Numpy     -- 1.12.1

OpenCV    -- 3.3.0

Paho-mqtt -- 1.3.1

Installation Manual : 
Raspbian Python Numpy OpenCV :

https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/

Paho-mqtt :
$ sudo pip install paho-mqtt

https://pypi.org/project/paho-mqtt/

step0. Erect the webcam(EZCam PCM-512) on MCU by USB hub

step1. Enter CloudMQTT and register github account (website:https://customer.cloudmqtt.com/login)

step2. Create a free broker and you can get the MQTT infomation 
![MQTT](https://github.com/digiplusdaniel/embedded/blob/master/4.Quick%20Start/4.PNG)

step3. Connect to MQTT monitor->websocket UI(P.S. if you want to see the dataflow)

step4. Download embedded/6.Source Code/MCU_TCPSend.py、Rasp1_MQTTPUB_ImageArray_TCPRecive.py、Rasp2_MQTTSCB_Panorama_TCPSend.py

step5. Open Raspberry's terminal and cd to the your file location 

step6. Execute the program
![RSP1](https://github.com/digiplusdaniel/embedded/blob/master/4.Quick%20Start/1.PNG)
![MCU](https://github.com/digiplusdaniel/embedded/blob/master/4.Quick%20Start/3.PNG)
![RSP2](https://github.com/digiplusdaniel/embedded/blob/master/4.Quick%20Start/2.PNG)

step6. Open UI.exe and the panorama will show on UI
![UI](https://github.com/digiplusdaniel/embedded/blob/master/4.Quick%20Start/UI.PNG)


