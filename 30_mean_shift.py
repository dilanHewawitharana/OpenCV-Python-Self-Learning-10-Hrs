import numpy as np
import cv2

cap = cv2.VideoCapture("Resources/eagle2.avi")
ret, frame = cap.read()
cv2.imwrite('Output/frame.png', frame)

x, y, width, height = 543, 423, 180, 120
track_window = (x, y, width, height)

roi = frame[y:y+height, x:x+width]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 30., 80.)), np.array((60., 255., 255.)))
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

# cv2.imshow("ROI", roi)

while True:
    ret, frame = cap.read()
    if frame is None:
        break
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

        ret, track_window = cv2.meanShift(dst, track_window, term_crit)
        x, y, w, h = track_window
        final_image = cv2.rectangle(frame, (x, y), (x+w, y+h), 255, 3)
        # cv2.imshow("DST", dst)
        cv2.imshow("final_image", final_image)

    cv2.waitKey(50)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('Output/frame.png', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()