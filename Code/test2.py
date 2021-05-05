#Bu kod kameraya gösterilen AprilTag'i detect edip çerçeve içine alıyor.
import cv2
from apriltag import apriltag
import numpy as np


cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,640);  
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,640); 
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detector = apriltag('tag36h11')
    results = detector.detect(frame)
    print(results)
    
    for r in results:
	# extract the bounding box (x, y)-coordinates for the AprilTag
	# and convert each of the (x, y)-coordinate pairs to integers
        (ptA, ptB, ptC, ptD) = r["lb-rb-rt-lt"]
        ptB = (int(ptB[0]), int(ptB[1]))
        ptC = (int(ptC[0]), int(ptC[1]))
        ptD = (int(ptD[0]), int(ptD[1]))
        ptA = (int(ptA[0]), int(ptA[1]))
	# draw the bounding box of the AprilTag detection
        cv2.line(frame, ptA, ptB, (0, 255, 0), 2)
        cv2.line(frame, ptB, ptC, (0, 255, 0), 2)
        cv2.line(frame, ptC, ptD, (0, 255, 0), 2)
        cv2.line(frame, ptD, ptA, (0, 255, 0), 2)
	# draw the center (x, y)-coordinates of the AprilTag
        (cX, cY) = (int(r["center"][0]), int(r["center"][1]))
        cv2.circle(frame, (cX, cY), 5, (255, 255, 0), -1)
	# draw the tag family on the image
        
    

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
