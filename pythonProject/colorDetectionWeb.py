import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def nothing(x):
    pass

cv2.namedWindow("Color Adjustment")

cv2.createTrackbar("Lower_H","Color Adjustment",0,255,nothing)
cv2.createTrackbar("Lower_S","Color Adjustment",0,255,nothing)
cv2.createTrackbar("Lower_V","Color Adjustment",0,255,nothing)

cv2.createTrackbar("Upper_H","Color Adjustment",255,255,nothing)
cv2.createTrackbar("Upper_S","Color Adjustment",255,255,nothing)
cv2.createTrackbar("Upper_V","Color Adjustment",255,255,nothing)

while True:
    _,frame = cap.read()
    frame = cv2.resize(frame,(400,400))

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("Lower_H", "Color Adjustment")
    l_s = cv2.getTrackbarPos("Lower_S", "Color Adjustment")
    l_v = cv2.getTrackbarPos("Lower_V", "Color Adjustment")

    u_h = cv2.getTrackbarPos("Upper_H", "Color Adjustment")
    u_s = cv2.getTrackbarPos("Upper_S", "Color Adjustment")
    u_v = cv2.getTrackbarPos("Upper_V", "Color Adjustment")

    lower_bound = np.array([l_h,l_s,l_v])
    upper_bound = np.array([u_h,u_s,u_v])

    mask = cv2.inRange(hsv,lower_bound,upper_bound)

    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("original frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    k = cv2.waitKey(25)
    if k == ord('e'):
        break

cap.release()
cv2.destroyAllWindows()