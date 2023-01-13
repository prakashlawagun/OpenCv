"""
#Template Matching --
It is a method for searching and finding the location of a template image
in a larger image.OpenCV comes with a function cv2.matchTemplate() for this
purpose. It simply slides the template image over the input image
(as in 2D convolution) and compares the template and patch of input image
under the template image.
"""

import cv2
import numpy as np
'''
img = cv2.imread('./Data/avengers.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

template = cv2.imread("./Data/temp.jpg",0)

w,h = template.shape[::-1]

#this function accept parameter (img,template,method)
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCORR_NORMED)
print("res",res)

threshold = 0.999
loc = np.where(res>=threshold) #finding the bright points

print("Bright pixels==",loc)

count = 0
for i in zip(*loc[::-1]):
    print("i== ",i)
    cv2.rectangle(img,i,(i[0]+w,i[1]+h),(0,0,255),2)
    count += 1
print("Number of iterations==",count)
img = cv2.resize(img,(800,600))
res = cv2.resize(res,(800,600))
cv2.imshow("img",img)
cv2.imshow("match temp==",res)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#check All the method
img = cv2.imread('./Data/avengers.jpg',0)
img2 =img.copy()

template = cv2.imread("./Data/temp.jpg",0)

w,h = template.shape[::-1]
#all the 6 methods for comparison in a list
methods =['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF',
            'cv2.TM_SQDIFF_NORMED']
for i in methods:
    print("I==",i)
    img = img2.copy()
    method = eval(i)

    res = cv2.matchTemplate(img,template,method)
    threshold = cv2.minMaxLoc(res) #minMax Loc return 4 values
    #getting coordinates from threshold
    x1 = threshold[3]
    cv2.rectangle(img,x1,(x1[0]+w,x1[1]+h),(255,0,255),2)

    #result display

    img = cv2.resize(img,(400,600))
    cv2.imshow(i+"+img",img)
    res = cv2.resize(res,(400,600))
    cv2.imshow(i+ "+res",res)

cv2.waitKey(0)
cv2.destroyAllWindows()