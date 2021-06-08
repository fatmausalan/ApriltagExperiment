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

* After the setup process was complete, we ran our first test for AprilTag.
After the package installations, we tried a code snippet like this:
```
import cv2
import numpy as np
from apriltag import apriltag

imagepath = 'test.jpg'
image = cv2.imread(imagepath, cv2.IMREAD_GRAYSCALE)
detector = apriltag("tagStandard41h12")

detections = detector.detect(image)
```

While running this code, we got an error like this:
``` ImportError: libcblas.so.3: cannot open shared object file: No such file or directory ```

We have installed opencv from scratch with pip to solve this error:
	``` pip3 install open-cv ```

After this command, we got errors such as libcblas-dev, libhdf5 respectively. 
For these errors, we ran the following commands in order:

	- sudo apt-get install libcblas-dev
	- sudo apt-get install libhdf5-dev
	- sudo apt-get install libhdf5-serial-dev
	- sudo apt-get install libatlas-base-dev
	- sudo apt-get install libjasper-dev 
	- sudo apt-get install libqtgui4 
	- sudo apt-get install libqt4-test 


Then, when we ran the code we wrote above with the command "python test.py", we were able to run it without any error.
