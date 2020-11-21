import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Resources/SOS/58.jpg')


plt.hist(img.ravel(), 256, [0, 256])

# hist = cv2.calcHist([img], [0], None, [256], [0, 256])
# plt.plot(hist)

cv2.imshow('Image', img)
plt.show()
cv2.waitKey(0)

cv2.destroyAllWindows()
