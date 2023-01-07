import cv2
import numpy as np

#read img
img = cv2.imread('./Data/roi_opr.jpg')
img2 = cv2.imread('./Data/ironman.jpg')
img2 = cv2.resize(img2,(900,600))
img = cv2.resize(img,(800,800))

#[(y1,y2),(x1,x2)]
roi = img[50:205,320:440]

#now passing data into img
img[50:205,431:551] = roi
img[50:205,552:672] = roi
img[50:205,200:320] = roi
img[50:205,80:200] = roi

img2[1:156,560:680]=roi
cv2.imshow("ROI",img2)


#ROI
cv2.waitKey(0)
cv2.destroyAllWindows()