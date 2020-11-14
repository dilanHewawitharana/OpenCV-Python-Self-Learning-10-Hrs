import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Resources/lena.jpg', -1)
cv2.imshow('Image', img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.xticks([])  # remove x axis coordinates
plt.yticks([])  # remove y axis coordinates
plt.show()

title = ['image01', 'image02', 'image03', 'image04', 'image05', 'image06']
images = [img, img, img, img, img, img]

for i in range(len(images)):
    plt.subplot(3, 3, i+1)  # num of row, col
    plt.imshow(images[i], 'gray')
    plt.title(title[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()