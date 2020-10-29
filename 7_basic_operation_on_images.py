import cv2

img1 = cv2.imread('Resources/messi5.jpg')
img2 = cv2.imread('Resources/star.jpg')

print(img1.shape)
print(img1.size)
print(img1.dtype)
b_channel, g_channel, r_channel = cv2.split(img1)
img_recreate = cv2.merge((b_channel, g_channel, r_channel))

ball = img1[280:340, 330: 390]
img_recreate[273:333, 100:160] = ball

img_recreate = cv2.resize(img_recreate, (400, 400))
img2 = cv2.resize(img2, (400, 400))

added_img = cv2.add(img_recreate, img2)
added_w_img = cv2.addWeighted(img_recreate, 0.8, img2, 0.6, 0)

cv2.imshow('Original Image', img1)
cv2.imshow('Recreated Original Image', img_recreate)
cv2.imshow('Added Image', added_img)
cv2.imshow('Added Weighted Image', added_w_img)


cv2.waitKey(0)
cv2.destroyAllWindows()

