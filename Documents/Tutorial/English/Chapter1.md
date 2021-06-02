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

	* sudo apt-get install libcblas-dev
	* sudo apt-get install libhdf5-dev
	* sudo apt-get install libhdf5-serial-dev
	* sudo apt-get install libatlas-base-dev
	* sudo apt-get install libjasper-dev 
	* sudo apt-get install libqtgui4 
	* sudo apt-get install libqt4-test 


Then, when we ran the code we wrote above with the command "python test.py", we were able to run it without any error.