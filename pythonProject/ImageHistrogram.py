#Imgage Histogram - Find, Plot and Analyze
#It which gives you an overall idea about the intensity distribution of an image.
#It distribute data along x and y axis.
# x - axis contain range of color vlaues.
# y - axis contain numbers of pixels in an image.
#With histogram to extrct information about contast, brigthness and intensity etc.

#plot histomgram using matplotlib
import cv2
import numpy as np
import matplotlib.pyplot as plt
'''
#ploting with calcHist
img = np.zeros((200,200),np.uint8)
cv2.rectangle(img,(0,100),(200,200),(255),-1)
cv2.rectangle(img,(0,50),(40,100),(127),-1)
#It accept parameters like ([img],[channel],mask,[histsize],range[0-255]).
hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)
plt.show()
cv2.imshow("Res",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

#histogram for color image
img = cv2.imread('./Data/thor.jpg')
img = cv2.resize(img,(500,650))
'''
b,g,r = cv2.split(img)
cv2.imshow("Img",img)
cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.title("Color Image Intensity")
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindow()
'''
#GrayScale
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
"""
hist = cv2.calcHist([img_gray],[0],None,[256],[0,256])
plt.plot(hist)
plt.title("Gray Scale Intensity")
plt.show()
"""
'''
#Histogram equalization is good when  of the image is confined to a particular region.
#It accept gray scale image
equ = cv2.equalizeHist(img_gray)
res = np.hstack([img_gray,equ])
cv2.imshow('equ',res)
hist1 = cv2.calcHist([equ],[0],None,[256],[0,256])
plt.plot(hist1)
plt.title("Equalization")
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

#CLAHE (Contrast Limited Adaptive Histogram Equalization)
# create a CLAHE object (Arguments are optional).
#It is used to enchance image and also handle noise froom image region
#gray scale imge is required

clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
c1 = clahe.apply(img_gray)
cv2.imshow("C1",c1)
hist = cv2.calcHist([c1],[0],None,[256],[0,256])
plt.plot(hist)
plt.title("CLAHE")
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()