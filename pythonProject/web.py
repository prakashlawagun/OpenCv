import cv2

cap = cv2.VideoCapture(0)
print("cap:", cap)

# DIVX, XVID,MJPG,X264,WMV1,WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# It contain 4 parameter,name,codec,fps,resolution
output = cv2.VideoWriter("./output.avi", fourcc, 20.0, (640, 480),0)
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", frame)
        cv2.imshow("gray", gray)
        output.write(gray)
        k = cv2.waitKey(25)
        if k == ord('e'):
            break
cap.release()
output.release()
cv2.destroyAllWindows()
