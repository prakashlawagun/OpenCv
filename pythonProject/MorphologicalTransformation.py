#-------------Morphological Transformations-----------------------

#Morphological transformations are some simple operations based on the image shape.
#It is normally performed on binary images.
# It needs two inputs, 1)- original image, 2)- structuring element(kernel).
#Two more basic Morphological Transformations are
#1) - Opening and 2) - Closing
import  cv2
import numpy as np

#Opening --
#Opening is just another name of erosion followed by dilation.
# #means first erosion take place then dilation
# img = cv2.imread("./Data/col_balls.jpg",0)
# _,mask  = cv2.threshold(img,230,255,cv2.THRESH_BINARY_INV)
# kernel = np.ones((4,4),np.uint8)#5*5 kernel with full of ones.
# o = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)#optional parameter iterations =2
# c = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)#optional parameter iterations =2
# cv2.imshow("Img",img)
# cv2.imshow("Ker",kernel)
# cv2.imshow("Mask",mask)
# cv2.imshow("Closing",c)
# cv2.imshow("Opening",o)
#
# x1= cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel)#diff bwetn mask and opening
# x2= cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel)#diff bwetn dilation and erosion
# x3= cv2.morphologyEx(mask,cv2.MORPH_BLACKHAT,kernel) # diff closing and input image
# cv2.imshow("x1",x1)
# cv2.imshow("x2",x2)
# cv2.imshow("x3",x3)

img = cv2.imread("./Data/girl.jpg",0)
_,mask  = cv2.threshold(img,230,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((4,4),np.uint8)#5*5 kernel with full of ones.
e = cv2.erode(mask,kernel)
d = cv2.dilate(mask,kernel)
o = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)#optional parameter iterations =2
c = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)#optional parameter iterations =2

x1= cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel)#diff bwetn mask and opening
x2= cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel)#diff bwetn dilation and erosion
x3= cv2.morphologyEx(mask,cv2.MORPH_BLACKHAT,kernel) # diff closing and input image

cv2.imshow("Img",img)
cv2.imshow("Ker",kernel)
cv2.imshow("Mask",mask)
cv2.imshow("Closing",c)
cv2.imshow("Opening",o)
cv2.imshow("x1",x1)
cv2.imshow("x2",x2)
cv2.imshow("x3",x3)



titles = ['image','mask','erosion','dilation','opening','closing','x1','x2','x3']
image = [img,mask,e,d,o,c,x1,x2,x3]
import matplotlib.pyplot as plt
for i in range(9):
    plt.subplot(3,3,i+1)
    plt.imshow(image[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

