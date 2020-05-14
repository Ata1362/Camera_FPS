import cv2 as cv
import time


cam = cv.VideoCapture(0)

cam.set(3, 640)
cam.set(4, 480)

cnt = 0
t1 = time.time()
while True:
    ret, frame = cam.read()
    cnt += 1
    cv. imshow("live", frame)
    if cv.waitKey(10) & 0xff == ord("q"):
        t2 = time.time()
        break
    if cnt == 30:
        t2 = time.time()
        t = (t2-t1)
        print("FPS = ", cnt / t)
        cnt = 0
        t1 = time.time()



cam.release()
cv.destroyAllWindows()