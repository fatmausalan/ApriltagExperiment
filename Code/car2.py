from apriltag import apriltag
import cv2
import numpy as np
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

def backward():
    p.ChangeDutyCycle(80)
    p1.ChangeDutyCycle(80)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
def forward():
    p.ChangeDutyCycle(80)
    p1.ChangeDutyCycle(80)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
def turnLeft():
    p.ChangeDutyCycle(80)
    p1.ChangeDutyCycle(80)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
def turnRight():
    p.ChangeDutyCycle(80)
    p1.ChangeDutyCycle(80)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    
    
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, image = cap.read()
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,640)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detector = apriltag('tag36h11')
    detections = detector.detect(image)
    #print(detections)
    for r in detections:
        print(r["id"])
        if (int)(r["id"]) == 12:
            turnLeft()
        elif (int)(r["id"]) == 22:
            turnRight()
        elif (int)(r["id"]) == 17:
            forward()
            #print("he")
        elif (int)(r["id"]) == 7:
            backward()
    # Display the resulting frame
    #cv2.imshow('frame',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
