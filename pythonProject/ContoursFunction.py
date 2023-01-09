#Contours and its function
#Moment
#Approximation
#ConvexHull
"""
import cv2
import numpy as np

img = cv2.imread('./Data/shapes.png')
img = cv2.resize(img,(600,700))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(img_gray,200,255,cv2.THRESH_BINARY_INV)

cnts,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print("Contour=",cnts,len(cnts))
print("Hier==",hier)

# img = cv2.drawContours(img,cnts,-1,(10,20,100),4)
for c in cnts:
    M = cv2.moments(c)
    print(M)
    cX = int(M['m10']/M['m00'])
    cY = int(M['m01']/M['m00'])
    img = cv2.drawContours(img,[c],-1,(0,255,0),4)
    cv2.circle(img,(cX,cY),7,(255,255,255),-1)
    cv2.putText(img,"center",(cX-20,cY-20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)

cv2.imshow("Original",img)
cv2.imshow("Gray",img_gray)
cv2.imshow("Thresh",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

import cv2
import numpy as np

img = cv2.imread('./Data/shapes.png')
img = cv2.resize(img,(600,700))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(img_gray,200,255,cv2.THRESH_BINARY_INV)

cnts,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print("Contour=",cnts,len(cnts))
print("Hier==",hier)

area1 = []
# img = cv2.drawContours(img,cnts,-1,(10,20,100),4)
for c in cnts:
    M = cv2.moments(c)
    print(M)
    cX = int(M['m10']/M['m00'])
    cY = int(M['m01']/M['m00'])

    area = cv2.contourArea(c)
    area1.append(area)

    if area <10000:
        #contour approx
        epsilon = 0.01*cv2.arcLength(c,True)

        data = cv2.approxPolyDP(c,epsilon,True)

        #cnvex hull

        hull = cv2.convexHull(data)

        x,y,w,h = cv2.boundingRect(hull)
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(125,10,20),5)




        img = cv2.drawContours(img,[c],-1,(0,255,0),4)
        cv2.circle(img,(cX,cY),7,(255,255,255),-1)
        cv2.putText(img,"center",(cX-20,cY-20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)

cv2.imshow("Original",img)
cv2.imshow("Gray",img_gray)
cv2.imshow("Thresh",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()