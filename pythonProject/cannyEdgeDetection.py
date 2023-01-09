#Canny Edge Detection using OpenCV
#Canny Edge Detection is a popular edge detection approach.
#It is use  multi-stage algorithm to detect a edges.
#It was developed by John F. Canny in 1986.
#This approach combine with 5 steps.
# 1) -  NOise reduction(gauss)), 2) -Gradient calculation( ,
# 3) - Non-maximum suppresson, 4) - Double Threshold,
# 5) - Edge Tracking by Hysteresis

import cv2
import numpy as np
#load image into gray scale
#
# img = cv2.imread("./Data/building.jpg",0)
#
# #canny(img,thresh1,thresh2) thresh1 and thresh2 at different lvl
# canny = cv2.Canny(img,50,150)
# cv2.imshow("Img",img)
# cv2.imshow("Canny",canny)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


img = cv2.imread("./Data/Stone.jpg",0)
img = cv2.resize(img,(400,400))

def nothing(x):
    pass

cv2.namedWindow("Canny")
cv2.createTrackbar("Threshold","Canny",0,255,nothing)

while True:
    a = cv2.getTrackbarPos("Threshold","Canny")
    print(a)
    res = cv2.Canny(img,a,255)
    cv2.imshow("Canny", res)
    k=cv2.waitKey(1)
    if k == ord('e'):
        break
cv2.destroyAllWindows()