import cv2
import numpy as np

img = cv2.imread('./Data/thor.jpg')

img = cv2.resize(img,(1000,600))

#creating border  -10,10 = top,bottom and 15,15 = right,left
border = cv2.copyMakeBorder(img,10,10,15,15,cv2.BORDER_CONSTANT,value=[255,0,125])
cv2.imshow("screen",border)
cv2.waitKey(0)
cv2.destroyAllWindows()