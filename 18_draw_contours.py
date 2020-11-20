import cv2
import  numpy as np

img = cv2.imread('Resources/opencv-logo.png', cv2.IMREAD_UNCHANGED)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 100, 255, 0)
_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print('Number of contours = ' + str(len(contours)))

for index in range(len(contours)):
    color1 = (list(np.random.choice(range(256), size=3)))
    color = [int(color1[0]), int(color1[1]), int(color1[2])]
    cv2.drawContours(img, contours, index, color, 8)

# cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

cv2.imshow('Image', img)
cv2.imshow('Gray', img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()