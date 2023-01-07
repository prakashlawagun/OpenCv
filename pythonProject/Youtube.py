import cv2
import pafy

url = 'https://youtu.be/xVz2YVda6p0'
data = pafy.new(url)
data = data.getbest(preftype="mp4")
cap = cv2.VideoCapture(0)
cap.open(data.url)

print("check== ",cap.isOpened())

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter('./hero.mp4',fourcc,20.0,(640,480))

while (cap.isOpened()):
    ret,frame = cap.read()
    if ret:
        frame = cv2.resize(frame,(700,700))
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray",gray)
        cv2.imshow("Colorframe",frame)
        if cv2.waitKey(1) == ord('e'):
            break

cap.release()
cv2.destroyAllWindows()

