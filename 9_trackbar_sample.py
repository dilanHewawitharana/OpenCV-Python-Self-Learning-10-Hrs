import numpy as np
import cv2

img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('Window')


def pos_change(pos):
    print(pos)


cv2.createTrackbar('B', 'Window', 0, 255, pos_change)
cv2.createTrackbar('G', 'Window', 0, 255, pos_change)
cv2.createTrackbar('R', 'Window', 0, 255, pos_change)

while True:
    cv2.imshow('Window', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    b = cv2.getTrackbarPos('B', 'Window')
    g = cv2.getTrackbarPos('G', 'Window')
    r = cv2.getTrackbarPos('R', 'Window')

    img[:] = [b, g, r]

cv2.destroyAllWindows()