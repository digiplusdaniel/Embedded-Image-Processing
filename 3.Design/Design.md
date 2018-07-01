MCU
input  : three images
output : image array
1. Input three images by Web Camera
2. Save three images into one array
3. Send the array to Raspberry Pi 1 by TCP/IP

![MCU](https://github.com/digiplusdaniel/embedded/blob/master/3.Design/MCU_block.png)
[MCU_Code](https://github.com/digiplusdaniel/embedded/blob/master/6.Source%20Code/MCU_TCPSend.py)

Raspberry Pi 1
input  : image array
output : image array
1. Recieve the array from MCU
2. Use MQTT to dispatch the array to Raspberry Pi 2 & 3

![RSP1](https://github.com/digiplusdaniel/embedded/blob/master/3.Design/RSP1_block.png)
[RSP1_Code](https://github.com/digiplusdaniel/embedded/blob/master/6.Source%20Code/Rasp1_MQTTPUB_ImageArray_TCPRecive.py)

Raspberry Pi 2
input  : image array
output : Stitched image
1. Recieve the array from Raspberry Pi 1
2. Cut the array into three images
3. Panorama stitching

![RSP2](https://github.com/digiplusdaniel/embedded/blob/master/3.Design/RSP2_block.png)
[RSP2_Code](https://github.com/digiplusdaniel/embedded/blob/master/6.Source%20Code/Rasp2_MQTTSCB_Panorama_TCPSend.py)

Raspberry Pi 3
input  : image array
output : Stitched image
1. Recieve the array from Raspberry Pi 1
2. Cut the array into three images
3. Panorama stitching

![RSP3](https://github.com/digiplusdaniel/embedded/blob/master/3.Design/RSP3_block.png)
[RSP3_Code](https://github.com/digiplusdaniel/embedded/blob/master/6.Source%20Code/Rasp2_MQTTSCB_Panorama_TCPSend.py)

UI
input  : Stitched image
output : VGA 
1. Recieve the Panorama stitching image from Raspberry Pi 2 & 3
2. Display on the Monitor

![UI](https://github.com/digiplusdaniel/embedded/blob/master/3.Design/UI_block.png)
[UI_Code](https://github.com/digiplusdaniel/embedded/blob/master/6.Source%20Code/UI/UI/Form1.cs)

![Arch](https://github.com/digiplusdaniel/embedded/blob/master/3.Design/Architecture%20diagram.png)
