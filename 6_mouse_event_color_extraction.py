import cv2
import numpy as np


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        extracted_color_img = np.zeros((100, 100, 3), np.uint8)
        extracted_color_img[:] = [blue, green, red]
        cv2.imshow('Extracted Color', extracted_color_img)


# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('Resources/color_grid.jpg')
cv2.imshow('Image', img)
points = []
cv2.setMouseCallback('Image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
