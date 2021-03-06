import cv2
import numpy as np
from apriltag import apriltag

imagepath = '../Images/test.jpg'
image = cv2.imread(imagepath, cv2.IMREAD_GRAYSCALE)
detector = apriltag("tag36h11")

detections = detector.detect(image)

print(detections)