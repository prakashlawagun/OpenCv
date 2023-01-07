# #Extracting object from the image and place an another image
# #Random figure ROI or Background
#
# import cv2
# import numpy as np
# img1 = cv2.imread('./Data/hero1.jpg')
# img2 = cv2.imread('./Data/strom_breaker.JPG')
#
# img1 = cv2.resize(img1,(1024,650))
# img2 = cv2.resize(img2,(600,650))
#
# # Fixed Image 2 data into Imgage 1
# r,c,ch = img2.shape
# print("Row,Column,channel == ",r,c,ch)
#
# # create ROI
# roi = img1[0:r,0:c]
#
# #Now creating mask for img2
# img_gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
#
# #create  mask using threshold
# _,mask = cv2.threshold(img_gray ,50,255,cv2.THRESH_BINARY)
#
# #remove background
# mask_inv= cv2.bitwise_not(mask)
#
# #put mask into roi
# img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
#
#
# # Take only region of figure from original image.
# img2_fg = cv2.bitwise_and(img2,img2 ,mask=mask)
#
# res = cv2.add(img1_bg,img2_fg)
#
# # cv2.imshow("Img1",img1)
# # cv2.imshow("Img2",img2)
# # cv2.imshow("ROI ",roi)
# # cv2.imshow("Step -1 gray== ",img_gray)
# cv2.imshow("Step - 2 Mask ",mask)
# cv2.imshow("Step - 3 Mask ",mask_inv)
# cv2.imshow("Step - 4 Mask ",img1_bg)
# cv2.imshow("Step - 5 Mask",img2_fg)
# cv2.imshow("Result",res)
#
# final_img = img1
#
# final_img[0:r,0:c] = res
# cv2.imshow("Final ",final_img)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np
img1 = cv2.imread('./Data/hero1.jpg')
img2 = cv2.imread('./Data/hero2.jpg')


img1 = cv2.resize(img1,(1024,650))
img2 = cv2.resize(img2,(600,650))

r,c,ch = img2.shape

roi = img1[:r,:c]

img_gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

_,mask = cv2.threshold(img_gray,50,255,cv2.THRESH_BINARY)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)


img2_fg = cv2.bitwise_and(img2,img2,mask=mask)
res = cv2.add(img1_bg,img2_fg)

# cv2.imshow("Img1",img1)
# cv2.imshow("Img2",img2)
# cv2.imshow("ROI ",roi)
cv2.imshow("Step -1 gray== ",img_gray)
cv2.imshow("Step - 2 Mask ",mask)
cv2.imshow("Step - 3 Mask ",mask_inv)
cv2.imshow("Step - 4 Mask ",img1_bg)
cv2.imshow("Step - 5 Mask",img2_fg)
cv2.imshow("Result",res)

final = img1

img1[:r,:c]=res

cv2.imshow("Final",final)



# cv2.imshow("IMG1 ",img1)
# cv2.imshow("IMG2 ",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()