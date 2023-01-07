#Screen Recorder ---

import pyautogui as pg
import cv2
import numpy as np

rs = pg.size()

fn = input("Enter file name and path")
fps = 60.0

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter(fn,fourcc,fps,rs)

cv2.namedWindow("Live_Recording",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live_Recording",(600,400))

while True:
    img = pg.screenshot()
    f=np.array(img)
    f=cv2.cvtColor(f,cv2.COLOR_BGR2RGB)
    output.write(f)
    cv2.imshow("Live_Recording",f)
    if cv2.waitKey(1)== ord('e'):
        break

output.release()
cv2.destroyAllWindows()



#Capture Multiple Images and Store in a folder

# import cv2
#
# vidcap = cv2.VideoCapture(0)
# ret,image = vidcap.read()#READ THE VIDEO
#
#
#
# count = 0
#
# while True:
#   if ret == True:
#       cv2.imwrite("frames\\imgN%d.jpg" % count, image)     # save frame as JPEG file
#       vidcap.set(cv2.CAP_PROP_POS_MSEC,(count**100)) #used to hold speed of frane generation
#       ret,image = vidcap.read()
#       cv2.imshow("res",image)
#       print ('Read a new frame:',count ,ret)
#       count += 1
#       if cv2.waitKey(1) & 0xFF == ord("q"):
#           break
#           cv2.destroyAllWindows()
#   else:
#       break
#
# vidcap.release()
# cv2.destroyAllWindows()
#
#
#
#
#e
#
#
#
#
