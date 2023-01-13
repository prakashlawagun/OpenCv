import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
img = cv2.imread('./Data/avengers.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img = cv2.resize(img,(700,600))

m,n = img.shape

mask = np.ones([3,3],np.uint8)
mask = mask/9

filtered_img = np.zeros([m,n])

for i in range(1,m-1):
    for j in  range(1,n-1):
        temp = img[i-1,j-1]*mask[0,0]+img[i-1,j]*mask[0,1]+img[i,j-1]*mask[1,0]+img[i+1,j+1]*mask[1,1]

print("Original Shape==",img.shape)
cv2.imshow('Original',img)
cv2.imshow('Gray',gray)

cv2.waitKey(0)
cv2.destroyAllWindows()