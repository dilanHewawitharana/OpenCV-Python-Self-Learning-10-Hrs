import numpy as np
import cv2

cap = cv2.VideoCapture("Resources/vtest.avi")
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
fgbg02 = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if frame is None:
        break

    fgmask = fgbg.apply(frame)
    fgmask02 = fgbg.apply(frame)

    cv2.imshow("Frame", frame)
    cv2.imshow("FGBG", fgmask)
    cv2.imshow("FGBG02", fgmask02)

    keyboard = cv2.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break

cap.release()
cv2.destroyAllWindows()