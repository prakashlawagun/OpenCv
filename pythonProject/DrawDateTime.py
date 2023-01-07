import cv2
import numpy as np
import datetime

cap = cv2.VideoCapture('./Data/test2.mp4')
# print("Width==",cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# print("Height==",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print("Width==",cap.get(3))
print("Height==",cap.get(4))

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret:
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        text = 'Height: ' + str(cap.get(4)) + ' Width: ' + str(cap.get(3))
        frame = cv2.putText(frame,text,(10,20),font,1,(0,0,0),1,cv2.LINE_AA)
        date_data = "Date: " + str(datetime.datetime.now())
        frame = cv2.putText(frame, date_data, (10,50), font, 1, (255,255,255),1, cv2.LINE_AA)
        cv2.rectangle(frame,(400,10),(510,128),(50,50,45),8)
        cv2.imshow("Video",frame)
        if cv2.waitKey(30) == ord('e'):
            break
    else:
        break

cap.release()
cv2.destroyAllWIndows()


