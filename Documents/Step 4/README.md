# Step 4 - Giving Basic Command to Car with AprilTag
At this stage, we combined our code that recognizes AprilTags with our code that guides our tool. We wrote 5 functions to give direction to the vehicle. These are stop(), backward(), forward(), turnLeft() and turnRight() functions. We can consider the forward function from these functions.
```
def forward():
    p.ChangeDutyCycle(80)
    p1.ChangeDutyCycle(80)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
```
The PWM signal we defined using the enable pins is as follows.
```
p = GPIO.PWM(en,1000)
p1=GPIO.PWM(en2,1000)
p.start(80)
p1.start(80)
```
In this way, we can control the speed of the motors. By sending HIGH to IN2 and IN4 pins at the same time, we ensure that the vehicle moves straight. The turnLeft() function we directed is as follows.
```
def turnLeft():
    p.ChangeDutyCycle(80)
    p1.ChangeDutyCycle(80)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
```
We chose the Tag36h11 from the AprilTag family to steer the vehicle. We used tags with IDs of 2, 7, 12, 17 and 22.* 2 --> stop
* 7 --> backward
* 12 --> turnLeft
* 17 --> forward
* 22 --> turnRight
We have added the vehicle control codes on [test2.py](https://github.com/fux00/ApriltagExperiment/blob/main/Code/test2.py) we wrote before.
You can find the complete code in the [car2.py](https://github.com/fux00/ApriltagExperiment/blob/main/Code/car2.py) file under the Code folder.

We used VNC Viewer to complete our connections and run the code. We ran the code we installed by connecting to our Raspberry Pi tool with VNC viewer. As a result, we can give commands to our vehicle by showing the tags. However, it is of course not suitable for active use. Tags are recognized within 2-3 seconds. This means that it is very slow for a system that needs to work in real time. In this direction, our next step will focus on the recognition of tags and their use in robotic systems. In addition, efforts will be made to speed up the system.

------
# Adım 3 - AprilTag ile Araca Basit Komutlar Verme
Bu aşamada AprilTag'leri tanıma işlemi yapan kodumuz ile aracımıza yön veren kodumuzu birleştirdik. Araca yön verebilmek için 5 fonksiyon yazdık. Bunlar stop(), backward(), forward(), turnLeft() and turnRight() fonksiyonlarıdır. Bu fonksiyonlardan forward fonksiyonunu ele alabiliriz.
```
def forward():
    p.ChangeDutyCycle(80)
    p1.ChangeDutyCycle(80)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
```
Enable pinlerini kullanarak tanımladığımız PWM sinyali aşağıdaki gibiidr.
```
p = GPIO.PWM(en,1000)
p1=GPIO.PWM(en2,1000)
p.start(80)
p1.start(80)
```
Bu sayede motorların hızlarını kontrol edebilmekteyiz. IN2 ve IN4 pinlerine aynı anda HIGH göndererek aracın düz bir şekilde ilerlemesini sağlıyoruz. Yön verdiğimiz turnLeft() foksiyonu da aşağıdaki gibidir.
```
def turnLeft():
    p.ChangeDutyCycle(80)
    p1.ChangeDutyCycle(80)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
```
Araca yön vermek için AprilTag ailesinden Tag36h11'i seçtik. Bunlardan da 2, 7, 12, 17 ve 22 ID'lerine sahip olan tagleri kullandık.
* 2 --> stop
* 7 --> backward
* 12 --> turnLeft
* 17 --> forward
* 22 --> turnRight
Daha önce yazmış olduğumuz [test2.py](https://github.com/fux00/ApriltagExperiment/blob/main/Code/test2.py) üzerine araç kontrol kodlarını eklemiş olduk.
Kodun tamamına Code klasörü altındaki [car2.py](https://github.com/fux00/ApriltagExperiment/blob/main/Code/car2.py) dosyasından ulaşabilirsiniz. 

Bağlantılarımızı tamamlayıp kodu çalıştırmak için VNC Viewer kullandık. VNC viewer ile Raspberry Pi aracımıza bağlanarak yüklediğimiz kodu çalıştırdık. Sonuç olarak aracımıza tagleri göstererek komut verebiliyoruz. Ancak aktif bir şekilde kullanıma tabii ki uygun değil. Tag'lerin tanınması 2-3 saniye içerisinde gerçekleşiyor. Bu da real time çalışması gereken bir sistem için çok yavaş olduğu anlamına gelmektedir. Bu doğrultuda sonraki adımımızda taglerin tanınması robotik sistemlerde kullanımı üzerinde durulacaktır. Ayrıca sistemin hızlandırılmasına çalışılacaktır. 
