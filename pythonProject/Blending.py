# import cv2
# import numpy as np
#
# img1 = cv2 .imread('./Data/thor.jpg')
# img1 = cv2.resize(img1,(500,700))
# img2= cv2 .imread('./Data/bro_thor.jpg')
# img2 = cv2.resize(img2,(500,700))
#
# cv2.imshow("S1",img1)
# cv2.imshow("S2",img2)
# # result = img1+img2
# # result = cv2.add(img1,img2)
# result = cv2.addWeighted(img1,0.7,img2,0.3,0)
# cv2.imshow("S3",result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np

img1 = cv2.imread('./Data/roi_opr.jpg')
img1 = cv2.resize(img1, (500, 700))
img2 = cv2.imread('./Data/bro_thor.jpg')
img2 = cv2.resize(img2, (500, 700))


def blend(x):
    pass


img = np.zeros((400, 400, 3), np.uint8)
cv2.namedWindow('win')
cv2.createTrackbar('alpha', 'win', 1, 100, blend)
switch = '0:OFF\n1:ON'
cv2.createTrackbar(switch, 'win', 0, 1, blend)

while True:
    s = cv2.getTrackbarPos(switch,'win')
    a = cv2.getTrackbarPos('alpha','win')
    n = float(a/100)
    print(n)

    if s == 0:
        dst = img[:]
    else:
        dst = cv2.addWeighted(img2,1-n,img1,n,0)
        cv2.putText(dst,str(a),(20,50),cv2.FONT_ITALIC,2,(0,125,255),2)

    cv2.imshow('dst',dst)
    if cv2.waitKey(1) == ord('e'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
