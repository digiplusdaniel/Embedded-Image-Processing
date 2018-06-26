MCU
input  : three images
output : image array
1. Input three images by Web Camera
2. Save three images into one array
3. Send the array to Raspberry Pi 1 by TCP/IP

Raspberry Pi 1
input  : image array
output : image array
1. Recieve the array from MCU
2. Use MQTT to dispatch the array to Raspberry Pi 2 & 3

Raspberry Pi 2
input  : image array
output : Stitched image
1. Recieve the array from Raspberry Pi 1
2. Cut the array into three images
3. Panorama stitching

Raspberry Pi 3
input  : image array
output : Stitched image
1. Recieve the array from Raspberry Pi 1
2. Cut the array into three images
3. Panorama stitching

UI
input  : Stitched image
output : VGA 
1. Recieve the Panorama stitching image from Raspberry Pi 2 & 3
2. Display on the Monitor

![Arch](https://github.com/digiplusdaniel/embedded/blob/master/3.Design/Architecture%20diagram.png)
