# Step 2 - AprilTag Usage with Raspberry Pi Zero W
* First of all, we need to install the operating system in the raspberry pi zero. We used the Raspberry Pi Imager program for this. After installing the Raspberry Pi Imager program, we selected Raspberry Pi Full OS and installed the operating system on our SD card.
* We ran the Raspberry Pi by making the necessary connections, then activated the camera, SSH and VNC.
* For an easier use, we connected to Raspberry Pi from our computer with VNC Viewer and made the necessary installations.
1. We are installing a full version of Raspbian OS system with Raspberry Pi Imager to our RaspberryPi Zero.
Matplotlib, Numpy, SciPy, OpenCV libraries are installed with pip. Some of them will come installed because we have installed the full OS.
	* For OpenCV installation:
		- ``` sudo apt update ```
		- ``` sudo apt install python3-opencv ```
	* To verify installation:
		- ``` python3 -c 'import cv2; print(cv2.__version__)' ```
		- After running this command, cv2 version should be written on the screen.
2. We download the repository at https://github.com/AprilRobotics/apriltag and run it with the ``` cmake ``` command.
Then we complete the installation with the ``` sudo make install ``` command.
3. We now have AprilTag on our Raspberry Pi.
