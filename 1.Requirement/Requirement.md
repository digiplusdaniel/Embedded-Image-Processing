Function: Panorama Stitching

Inner Interface
  MCU send the images to cloud by TCP/IP, and compute on cloud. After that, send the result to UI
  1. MQTT mode:TCP/IP
  2. Socket mode:TCP/IP
  3. Monitor UI
	
External Interface 
  MCU get the images from camera by USB, and display on the monitor
  1. web camera * 3
  2. Raspberry Pi * 4
  3. VGA display
                                  
Effiency¡BLimit
  1. 5 sec/page
  2. image angle < 140° 

Verification
  UI can read stitched panorama
  1. Driver  : Can watch 3 directions of images by screen, and upload to Cloud
  2. Cloud   : Receive 3 images and stitching, allocating the resource properly
  3. Manager : Display panorama on UI

![Usage diagram](https://github.com/digiplusdaniel/embedded/blob/master/1.Requirement/Requirement.png)
