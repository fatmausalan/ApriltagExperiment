import RPi.GPIO as GPIO
#car connections
in1 = 23
in2 = 24
en = 25
in3= 17

in4=27
en2=22

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

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