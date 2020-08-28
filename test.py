import cv2
import numpy as np

cap = cv2.VideoCapture(1)
cv2.namedWindow("frame")

while True:
    ret, frame = cap.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    blur = cv2.GaussianBlur(hsv, (5,5), 0)
    lower_skin = np.array([0, 48, 80])
    upper_skin = np.array([20, 255, 255])
    mask = cv2.inRange(blur, lower_skin, upper_skin)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    
cap.release()
cv2.destroyAllWindows()