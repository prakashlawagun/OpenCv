import cv2

path = input("Enter photo path:")
img1 = cv2.imread(path,0)
img1 = cv2.flip(img1,-1)
img1 = cv2.resize(img1,(1280,700))
print(img1)
cv2.imshow("Gray scale",img1)

k=cv2.waitKey(0)
if k==ord("s"):
    cv2.imwrite("./output.png",img1)
else:
    cv2.destroyAllWindows()
