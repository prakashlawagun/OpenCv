import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def nothing(x):
    pass

#window name
cv2.namedWindow("Color Adjustment",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Color Adjustment",(300,300))
cv2.createTrackbar("Thresh","Color Adjustment",0,255,nothing)

#Coloe Detection Track
cv2.createTrackbar("Lower_H","Color Adjustment",0,255,nothing)
cv2.createTrackbar("Lower_S","Color Adjustment",0,255,nothing)
cv2.createTrackbar("Lower_V","Color Adjustment",0,255,nothing)
cv2.createTrackbar("Upper_H","Color Adjustment",255,255,nothing)
cv2.createTrackbar("Upper_S","Color Adjustment",255,255,nothing)
cv2.createTrackbar("Upper_V","Color Adjustment",255,255,nothing)

while True:
    _,frame = cap.read()
    frame = cv2.resize(frame,(400,400))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("Lower_H","Color Adjustment")
    l_s = cv2.getTrackbarPos("Lower_S","Color Adjustment")
    l_v = cv2.getTrackbarPos("Lower_V","Color Adjustment")
    u_h = cv2.getTrackbarPos("Upper_H","Color Adjustment")
    u_s = cv2.getTrackbarPos("Upper_S","Color Adjustment")
    u_v = cv2.getTrackbarPos("Upper_V","Color Adjustment")

    lower_bound = np.array([l_h,l_s,l_v])
    upper_bound = np.array([u_h,u_s,u_v])


    mask = cv2.inRange(hsv,lower_bound,upper_bound)

    filter = cv2.bitwise_and(frame,frame,mask=mask)

    mask1 = cv2.bitwise_not(mask)
    m_g = cv2.getTrackbarPos("Thresh","Color Adjustment")
    ret,thresh = cv2.threshold(mask1,m_g,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh,(1,1),iterations=6)


    cnts,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    # frame = cv2.drawContours(frame,cnts,-1,(176,10,15),4)

    for c in cnts:
        elipson = 0.001*cv2.arcLength(c,True)
        data = cv2.approxPolyDP(c,elipson,True)

        hull = cv2.convexHull(data)
        cv2.drawContours(frame,[c],-1,(50,50,150),2)
        cv2.drawContours(frame,[hull],-1,(0,0,255),2)

        hull1 = cv2.convexHull(data,returnPoints=False)
        defect = cv2.convexityDefects(data[0],hull)
        print("Defects==",defect)




    cv2.imshow("Thresh",thresh)
    cv2.imshow("Mask",mask)
    cv2.imshow("Filter",filter)
    cv2.imshow("Result",frame)
    if cv2.waitKey(25) == ord("e"):
        break
cv2.destroyAllWindows()
