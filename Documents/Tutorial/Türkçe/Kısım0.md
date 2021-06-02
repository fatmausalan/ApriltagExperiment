# Kısım 0

Bu partta gerekli olan kurulumları yapacağız.
1. RaspberryPi Zeromuza Raspberry Pi Imager ile Raspbian OS sisteminin full versiyonunu yüklüyoruz.
Matplotlib, Numpy, SciPy, OpenCV kütüphaneleri pip ile kurulur. Bazıları full OS yüklediğimiz için yüklü gelecektir.
	* OpenCV kurulumu yapmak için:
		- ``` sudo apt update ```
		- ``` sudo apt install python3-opencv ``` 
	* Kurulumun yapıldığını doğrulmak için:
		- ``` python3 -c 'import cv2; print(cv2.__version__)' ```
		- Bu komutu çalıştırdıktan sonra ekranda cv2 versiyonu yazmalıdır.
2. https://github.com/AprilRobotics/apriltag adresindeki repository'yi indirip cmake komutu ile çalıştırırız.
Ardından sudo make install komutu ile kurulumu tamamlarız.
3. Artık Raspberrymizde AprilTag'e sahibiz.
