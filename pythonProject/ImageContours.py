#Contours -
#Contours can be explained simply as a curve joining all the continuous points
#(along the boundary), having same color or intensity.

#The contours are a useful tool for shape analysis and object detection and recognition

#For better accuracy, use binary images and also apply edge detection before
#finding countours.

#findCountour function manipulate original imge so copy it before proceeding.
#findContour is like finding white object from black background.
#so you must turn image in white and background is black.

#We have to find and draw contours as per the requirement.

import cv2
import numpy as np

img = cv2.imread("./Data/logo.jpg")
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(img1,20,255,0)

cnts,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print(cnts,len(cnts))

img = cv2.drawContours(img,cnts,-1,(176,10,15),4)

cv2.imshow("Original==",img)
cv2.imshow("Gray==",img1)
cv2.imshow("Thresh==",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
