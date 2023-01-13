#Background Subtraction is a way to access the foreground objects.
#Technically, you need to extract the moving
#foreground from static background.
#There are multiple approach for backgroud subtract
import cv2
import numpy as np

cap = cv2.VideoCapture('./Data/test2.mp4')

algo1= cv2.createBackgroundSubtractorMOG2(detectShadows= True)
algo2= cv2.createBackgroundSubtractorKNN(detectShadows= True)

while True:
    _,frame = cap.read()
    frame = cv2.resize(frame,(600,400))
    res1 = algo1.apply(frame)
    res2 = algo2.apply(frame)
    cv2.imshow("Original",frame)
    cv2.imshow("Result 1", res1)
    cv2.imshow("Result 2", res2)

    if cv2.waitKey(25) == ord('e'):
        break
cv2.destroyAllWindows()