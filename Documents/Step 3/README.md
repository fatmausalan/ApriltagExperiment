# Step 3 - Basic Car with Raspberry Pi Zero
In this step, motor driver and motor connections were made with Raspberry Pi. We made our power supply with LiPo. We connected the positive and negative terminals we received from the LiPo to the 12V input of the motor driver and the GND input. In order to power the Raspberry, we cut the micro usb cable and separated the red and black wires. We connected the black one to GND and the red one to the 5V output of the motor driver. In this way, we have made the power supply of the motors and Raspberry.
The connections with the motor driver and Raspberry Pi are as follows.
* IN1 --> GPIO 23
* IN2 --> GPIO 24
* ENA --> GPIO 25
* IN3 --> GPIO 17
* IN4 --> GPIO 27
* ENB --> GPIO 22
After making the connections correctly, we tested whether the motors work correctly. For this, we imported the RPi.GPIO library.
```
import RPİ.GPIO as GPIO
```
We created our variables for the motor connections.
```
in1 = 23
in2 = 24
en = 25
in3= 17
in4=27
en2=22
```
We did the setup with GPIO.
```
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
```
Son olarak motorları çalıştırdık. 
```
p = GPIO.PWM(en,1000)
p1=GPIO.PWM(en2,1000)
p.start(80)
p1.start(80)
while(true):
    p.ChangeDutyCycle(80)
    p1.ChangeDutyCycle(80)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)    
```
One of the points we should pay attention to for connections was the GND connection. In order for the motors to be operated with the motor driver, a common GND connection must be made from the motor driver for Raspberry and LiPo.
------------------------------------------------------------------------------------------------------------------------------------------
# Adım 3 - Raspberry Pi Zero ile Basit Araba
Bu adımda Raspberry Pi ile motor sürücü ve motorların bağlantıları yapıldı. Güç beslememizi LiPo ile yaptık. LiPo üzerinden aldığımız pozitif ve negatif uçları motor sürücünün 12V girişi ile GND girişine bağladık. Raspberry'e güç beslemesi yapabilmek için micro usb kablosunu keserek kırmızı ve siyah kabloyu ayırdık. Bu kablolardan siyahı GND'ye kırmızı olanı motor sürücünün 5V çıkışına bağladık. Bu şekilde motorların ve Raspberry'nin güç beslemesini yapmış olduk.
Motor sürücü ve Raspberry Pi ile olan bağlantılar da aşağıdaki gibidir.
* IN1 --> GPIO 23
* IN2 --> GPIO 24
* ENA --> GPIO 25
* IN3 --> GPIO 17
* IN4 --> GPIO 27
* ENB --> GPIO 22
Bağlantıları doğru şekilde yaptıktan sonra motorların doğru çalışıp çalışmadığını test ettik. Bunun için RPi.GPIO kütüphanesini import ettik. 
```
import RPİ.GPIO as GPIO
```
Motor bağlantıları için değişkenlerimizi oluşturduk.
```
in1 = 23
in2 = 24
en = 25
in3= 17
in4=27
en2=22
```
GPIO ile setup işlemlerini yaptık.
```
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
```
Son olarak motorları çalıştırdık. 
```
p = GPIO.PWM(en,1000)
p1=GPIO.PWM(en2,1000)
p.start(80)
p1.start(80)
while(true):
    p.ChangeDutyCycle(80)
    p1.ChangeDutyCycle(80)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)    
```
Bağlantılar için dikkat etmmemiz gereken noktalardan biri GND bağlantısı oldu. Motorların motor sürücü ile çalıştırılabilmesi için motor sürücüden Raspberry ve LiPo için ortak GND bağlantısı yapılması gerekiyor. 
