#Drawing function in opencv

import numpy as np
import cv2

# img = cv2.imread("./Data/avengers.jpg")
# img = cv2.resize(img,(700,600))
img = np.zeros([512,512,3],np.uint8)*255
# img = np.ones([512,512,3],np.uint8)*255
# Here line accept 5 parameter(img,starting,ending,color,thickness
img = cv2.line(img,(0,0),(200,200),(254,7,31),5)

# Here  arrowed line accept 5 parameter(img,starting,ending,color,thickness
img = cv2.arrowedLine(img,(0,125),(255,255),(255,0,125),10)

# Here retangle accept 5 parameter(img,starting,ending,color,thickness
img = cv2.rectangle(img,(384,10),(510,128),(128,0,255),5)

# Here retangle accept 5 parameter(img,starting,radius,color,thickness
img = cv2.circle(img,(447,125),63,(128,0,255),-5)

# Here retangle accept 5 parameter(img,text,starting,font,fontsize,color,thickness,line type
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img,'THOR',(20,500),font,4,(0,125,255),10,cv2.LINE_AA)

# Here retangle accept 5 parameter(img,starting,(length,height),color,thickness
img = cv2.ellipse(img,(400,500),(100,50),0,0,180,155,5)

cv2.imshow("Res",img)
cv2.waitKey(0)
cv2.destroyAllWindow()