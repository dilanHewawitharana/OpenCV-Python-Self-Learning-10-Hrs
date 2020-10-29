import cv2

img_color = cv2.imread('Resources/lena.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.imread('Resources/lena.jpg', cv2.IMREAD_GRAYSCALE)
img_ori = cv2.imread('Resources/lena.jpg', cv2.IMREAD_UNCHANGED)  # Read image with alpha channel

cv2.imshow('Color Image', img_color)
cv2.imshow('Gray Image', img_gray)
cv2.imshow('Original Image', img_ori)

k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('Output/lena_copy.png', img_ori)
    cv2.destroyAllWindows()
