import cv2
import numpy as np
"""
img = cv2.imread('./Data/col_balls.jpg')

img2 = img.copy()
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray,5)
#parameters---(img,circle_method,dp,mindist,parm1,parm2[p1>p2],)
circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)

data = np.uint16(np.around(circles))

for (x,y,r) in data[0, :]:
    cv2.circle(img2,(x,y),r,(50, 10, 50),3)
    cv2.circle(img2,(x,y),2,(0, 255, 100),-1)

cv2.imshow("Original",img2)
cv2.imshow("Gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    frame2 = frame.copy()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray,5)
    circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,50,param1=50,param2=30,minRadius=0,maxRadius=0)
    if circles is not None:
        data = np.uint16(np.around(circles))
        for (x,y,r) in data[0, :]:
           cv2.circle(frame2,(x,y),r,(50,10,50),3)
    cv2.circle(frame2, (x, y), 2, (0, 255, 100), -1)
    cv2.imshow("Result",frame2)
    k= cv2.waitKey(25)
    if k == ord("e"):
        break

cap.release()
cv2.destroyAllWindows()