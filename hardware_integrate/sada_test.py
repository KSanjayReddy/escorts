import cv2
import numpy as np
import time

import serial

ser = serial.Serial('/dev/ttyACM1', 2000000, timeout=0.1)
flap = serial.Serial('/dev/ttyACM0', 9600, timeout=0.1)
cap = cv2.VideoCapture(0)

def nothing(x):
    pass
flag=0

cv2.namedWindow('bar frame')
cv2.createTrackbar('H_Upper', 'bar frame', 90, 100, nothing)
cv2.createTrackbar('S_Upper', 'bar frame', 76, 255, nothing)
cv2.createTrackbar('V_Upper', 'bar frame', 190, 255, nothing)
cv2.createTrackbar('H_Lower', 'bar frame', 39, 100, nothing)
cv2.createTrackbar('S_Lower', 'bar frame', 18, 255, nothing)
cv2.createTrackbar('V_Lower', 'bar frame', 79, 255, nothing)




#lower_green = np.array([40, 100, 50])
#upper_green = np.array([80, 255, 255])

cabbage_crossed = False
cabbage_present = False
prev_data = 0
khulja = []
khulja_pos = 0
bandhoja = []
bandhoja_pos = 0
error_a = 0
error_b = 0
while(1):
#    var = 'a'
#    ser.write(bytes(var.encode('ascii')))
    data = ser.readline()[:-2] 
    if data:
        print(data)
    else:
        print("Data not found")	
    _, frame = cap.read()
 
    frame=cv2.flip(frame,3)
    rows,cols,channels = frame.shape
#rotates the frame by 90degrees    
#    M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
#    frame = cv2.warpAffine(frame,M,(cols,rows))


#Crops out some rows from top and below
    frame = frame[50:430,0:640]
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hu = cv2.getTrackbarPos('H_Upper', 'bar frame')
    su = cv2.getTrackbarPos('S_Upper', 'bar frame')
    vu = cv2.getTrackbarPos('V_Upper', 'bar frame')
    hl = cv2.getTrackbarPos('H_Lower', 'bar frame')
    sl = cv2.getTrackbarPos('S_Lower', 'bar frame')
    vl = cv2.getTrackbarPos('V_Lower', 'bar frame')
    lower_green = np.array([hl, sl, vl])
    upper_green = np.array([hu, su, vu])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    cnts = cv2.findContours(mask.copy(),        cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    res = cv2.bitwise_not(frame.copy(),frame.copy(), mask= mask)
    center = None

    cv2.line(frame,(0,250),(640,250),(255,0,0),2)
    cv2.line(frame,(0,170),(640,170),(255,0,0),2)
    cv2.line(frame,(320,0),(320,480),(255,0,0),2)
    cv2.imshow("original frame", frame)
    cv2.imshow("tracking",mask)
#    cv2.imshow("bar frame",frame)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
