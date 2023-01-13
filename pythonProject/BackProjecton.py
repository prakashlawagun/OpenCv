#BackProjection using histogram technique
import cv2
import numpy as np

original_img = cv2.imread('./Data/green.jpg')
original_img = cv2.resize(original_img,(600,650))
hsv_original = cv2.cvtColor(original_img,cv2.COLOR_BGR2HSV)

roi = cv2.imread('./Data/g.jpg')
hsv_roi = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

#Histrogram ROI
roi_hist = cv2.calcHist([hsv_roi],[0,1],None,[180,256],[0,180,0,256])
mask = cv2.calcBackProject([hsv_original],[0,1],roi_hist,[0,180,0,256],1)

#filtering remove noise

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
mask = cv2.filter2D(mask,200,255,cv2.THRESH_BINARY)
_,mask = cv2.threshold(mask,200,255,cv2.THRESH_BINARY)

mask = cv2.merge((mask,mask,mask))
result = cv2.bitwise_or(original_img,mask)

cv2.imshow("Original image",original_img)
cv2.imshow("Result",result)
cv2.waitKey(0)
cv2.destroyAllWindows()