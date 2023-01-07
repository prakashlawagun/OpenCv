#Image Gradient--
#It is a directional change in the color or intensity in an image.
#It is most important part to find information from image
#Like finding edges within the images.
#There are various methods to find image gradient.
#These are - Laplacian Derivatives,SobelX and SobelY.
#All these functions have diff. mathematical approach to get result.
#All load image in the gray scale

import cv2
import numpy as np

#load image into gray scale
img = cv2.imread("./Data/building.jpg")
img = cv2.resize(img,(300,400))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Laplacian Derivative---It calculate laplace derivate
#parameter(img,data_type for -ve val,ksize)
#kernal size must be odd

lap = cv2.Laplacian(img_gray,cv2.CV_64F,ksize=3)
lap=np.uint8(np.absolute(lap))

#Sobel operation -
# is a joint Gausssian smoothing plus differentiation operation,
#so it is more  resistant to noise
#This is use for x and y bth
#parameter (img,type for -ve val,x = 1,y = 0,ksize)
#Sobel X focus on vertical lines
#Sobel y focus on horizontal lines
sobelX = cv2.Sobel(img_gray,cv2.CV_64F,1,0,ksize=3)
sobelY = cv2.Sobel(img_gray,cv2.CV_64F,0,1,ksize=3)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

#finally combine sobel X and sobel Y
sobelcombine = cv2.bitwise_or(sobelX,sobelY)


cv2.imshow('Original',img)
cv2.imshow('Gray',img_gray)
cv2.imshow('Lap',lap)
cv2.imshow('Sobel X',sobelX)
cv2.imshow('Sobel Y',sobelY)
cv2.imshow('Sobel Comine',sobelcombine)

import matplotlib.pyplot as plt

titles = ['Original','Laplacian','SobelX','SobelY','Sobel Combine']
images = [img,lap,sobelX,sobelY,sobelcombine]

for i in range(5):
    plt.subplot(3,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
