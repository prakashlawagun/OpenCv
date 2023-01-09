import cv2
import numpy as np

img = cv2.imread('./Data/hand2.jpg')
img = cv2.resize(img, (600, 700))
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(img1, 9)
_, thresh = cv2.threshold(blur, 240, 255, cv2.THRESH_BINARY_INV)

# findCounter
cnts, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("Number of contour is ", cnts, "Total contou= ", len(cnts))
print("Hierarchy==", hier)

for c in cnts:
    elipson = 0.0001 * cv2.arcLength(c, True)
    data = cv2.approxPolyDP(c, elipson, True)

    hull = cv2.convexHull(data)

    cv2.drawContours(img, [c], -1, (540, 50, 150), 2)
    cv2.drawContours(img, [hull], -1, (0, 255, 0), 2)

# find convexity defect
hull2 = cv2.convexHull(cnts[0], returnPoints=False)
# defect  return an array  which contains value [start_point,end_point,farthest_point,approximation point].
defect = cv2.convexityDefects(cnts[0], hull2)

for i in range(defect.shape[0]):
    s,e,f,d = defect[i,0]
    print(s,e,f,d)
    start = tuple(c[s][0])
    end = tuple(c[e][0])
    far = tuple(c[f][0])
    cv2.circle(img,far,5,[0,0,255],-1)

#Extreme Points---
# It means topmost ,bottommost,rightmost,leftmost point of the objects.
c_max = max(cnts,key=cv2.contourArea)

#determine the most extreme points  along the contour
extLeft = tuple(c_max[c_max[:,:,0].argmin()][0])
extRight = tuple(c_max[c_max[:,:,0].argmax()][0])
extTop = tuple(c_max[c_max[:,:,1].argmin()][0])
extBottom = tuple(c_max[c_max[:,:,1].argmax()][0])

cv2.circle(img,extLeft,8,(255,0,255),-1)
cv2.circle(img,extRight,8,(0,125,255),-1)
cv2.circle(img,extTop,8,(255,10,0),-1)
cv2.circle(img,extBottom,8,(19,152,152),-1)




cv2.imshow("Original", img)
cv2.imshow("Gray", img1)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
