Paket kurulumlarından sonra şöyle bir kod parçasını denedik:
```
import cv2
import numpy as np
from apriltag import apriltag

imagepath = 'test.jpg'
image = cv2.imread(imagepath, cv2.IMREAD_GRAYSCALE)
detector = apriltag("tagStandard41h12")

detections = detector.detect(image)
```

Bu kodu çalıştırırken şöyle bir hata aldık:
``` ImportError: libcblas.so.3: cannot open shared object file: No such file or directory ```

Bu hatayı çözebilmek için opencv'yi pip ile baştan kurduk.
	``` pip3 install open-cv ```

Bu komuttan sonra sırasıyla libcblas-dev, libhdf5 gibi hatalar aldık. Bu hatalar için sırasıyla 
aşağıdaki komutları çalıştırdık:

	* sudo apt-get install libcblas-dev
	* sudo apt-get install libhdf5-dev
	* sudo apt-get install libhdf5-serial-dev
	* sudo apt-get install libatlas-base-dev
	* sudo apt-get install libjasper-dev 
	* sudo apt-get install libqtgui4 
	* sudo apt-get install libqt4-test 

Ardından yukarda yazdığımız kodu "python test.py" komutu ile çalıştırdığımızda hata almadan çalıştırabildik.
