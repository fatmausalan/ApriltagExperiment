# Step 4 - Giving Basic Command to Car with AprilTag
<img src="https://github.com/fux00/ApriltagExperiment/blob/main/Images/Img/11.jpeg" width="400"  height = "300" /><img src="https://github.com/fux00/ApriltagExperiment/blob/main/Images/Img/22.jpeg" width="400" height = "300"  />

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
# Ad??m 3 - AprilTag ile Araca Basit Komutlar Verme
<img src="https://github.com/fux00/ApriltagExperiment/blob/main/Images/Img/11.jpeg" width="400" height = "300" /><img src="https://github.com/fux00/ApriltagExperiment/blob/main/Images/Img/22.jpeg" width="400" height = "300"  />

Bu a??amada AprilTag'leri tan??ma i??lemi yapan kodumuz ile arac??m??za y??n veren kodumuzu birle??tirdik. Araca y??n verebilmek i??in 5 fonksiyon yazd??k. Bunlar stop(), backward(), forward(), turnLeft() and turnRight() fonksiyonlar??d??r. Bu fonksiyonlardan forward fonksiyonunu ele alabiliriz.
```
def forward():
    p.ChangeDutyCycle(80)
    p1.ChangeDutyCycle(80)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
```
Enable pinlerini kullanarak tan??mlad??????m??z PWM sinyali a??a????daki gibiidr.
```
p = GPIO.PWM(en,1000)
p1=GPIO.PWM(en2,1000)
p.start(80)
p1.start(80)
```
Bu sayede motorlar??n h??zlar??n?? kontrol edebilmekteyiz. IN2 ve IN4 pinlerine ayn?? anda HIGH g??ndererek arac??n d??z bir ??ekilde ilerlemesini sa??l??yoruz. Y??n verdi??imiz turnLeft() foksiyonu da a??a????daki gibidir.
```
def turnLeft():
    p.ChangeDutyCycle(80)
    p1.ChangeDutyCycle(80)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
```
Araca y??n vermek i??in AprilTag ailesinden Tag36h11'i se??tik. Bunlardan da 2, 7, 12, 17 ve 22 ID'lerine sahip olan tagleri kulland??k.
* 2 --> stop
* 7 --> backward
* 12 --> turnLeft
* 17 --> forward
* 22 --> turnRight
Daha ??nce yazm???? oldu??umuz [test2.py](https://github.com/fux00/ApriltagExperiment/blob/main/Code/test2.py) ??zerine ara?? kontrol kodlar??n?? eklemi?? olduk.
Kodun tamam??na Code klas??r?? alt??ndaki [car2.py](https://github.com/fux00/ApriltagExperiment/blob/main/Code/car2.py) dosyas??ndan ula??abilirsiniz. 

Ba??lant??lar??m??z?? tamamlay??p kodu ??al????t??rmak i??in VNC Viewer kulland??k. VNC viewer ile Raspberry Pi arac??m??za ba??lanarak y??kledi??imiz kodu ??al????t??rd??k. Sonu?? olarak arac??m??za tagleri g??stererek komut verebiliyoruz. Ancak aktif bir ??ekilde kullan??ma tabii ki uygun de??il. Tag'lerin tan??nmas?? 2-3 saniye i??erisinde ger??ekle??iyor. Bu da real time ??al????mas?? gereken bir sistem i??in ??ok yava?? oldu??u anlam??na gelmektedir. Bu do??rultuda sonraki ad??m??m??zda taglerin tan??nmas?? robotik sistemlerde kullan??m?? ??zerinde durulacakt??r. Ayr??ca sistemin h??zland??r??lmas??na ??al??????lacakt??r. 
