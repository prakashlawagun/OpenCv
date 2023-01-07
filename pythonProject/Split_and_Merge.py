#Image operation with pixel and coordinates
import cv2
import numpy as np

#Read an Image
img = cv2 .imread('./Data/pikachu.jpg')
print("shape==",img.shape)
print("no. of pixels==",img.size)
print("data types",img.dtype)
print("Image type==",type(img))

#Now try to split an image
b,g,r = cv2.split(img)
# cv2.imshow("Blue",b)
# cv2.imshow("Green",g)
# cv2.imshow("Red",r)

#Now mixed the channel use merge
m1 = cv2.merge((r,g,b))
cv2.imshow("rgb",m1)
px = img[420,480]
print("The pixel of that coordinate=",px)
cv2.imshow("res",img)
cv2.waitKey(0)
cv2.destroyAllWindows()