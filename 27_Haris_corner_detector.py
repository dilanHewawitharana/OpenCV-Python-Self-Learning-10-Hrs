import numpy as np
import cv2

img = cv2.imread("Resources/chessboard.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

dst = cv2.dilate(dst, None)
img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv2.imshow("Dst", img)

cv2.waitKey(0)
cv2.destroyAllWindows()