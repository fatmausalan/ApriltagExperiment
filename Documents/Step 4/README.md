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
You can find the complete code in the [car2.py](https://github.com/fux00/ApriltagExperiment/blob/main/Code/car2.py) file under the Code folder.
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
Kodun tamamına Code klasörü altındaki [car2.py](https://github.com/fux00/ApriltagExperiment/blob/main/Code/car2.py) dosyasından ulaşabilirsiniz. 
