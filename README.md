# Parking-Spot-Detector_Embedded-Systems

## How to set up the embedded system
1.  Install the raspberry pi image from: [https://github.com/Qengineering/RPi-image](https://github.com/Qengineering/RPi-image). This contains all the necessary dependencies pre installed.
	- Use the rapberry-pi imager to burn the image into the sd card
	- The deafult username is **pi** and password is **3.14**
	- The raspberry pi used for this purpose is is rapberry pi 4 connected to a raspberry pi camera.
2.  Clone the repository by typing the following in the terminal:
	- `git clone https://github.com/Capstone-Projects-2022-Fall/Parking-Spot-Detector_Embedded-Systems`
3.  Change directory to the cloned repository by typing the following in the terminal:
	-  `cd Parking-Spot-Detector_Embedded-Systems`
4.  Activate the virtual environment named camera-unit by typing:
	- `source camera-unit/bin/activate` 
5.  Configure the **config.yml** file according to your configuration
	- Important information such as which mask file to use, the confidence score threshold for car detection, the camera id and the server address can be changed here
6.  Activate the program by typing the following line:
	- `python3 start.py` 
