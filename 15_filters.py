import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Resources/SOS/1.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32)/25
filter2D = cv2.filter2D(img, -1, kernel=kernel)
blur = cv2.blur(img, (5, 5))
GaussianBlur = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 5)
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['image', '2D Convolution', 'blur', 'Gaussian Blur', 'median', 'bilateralFilter']
images = [img, filter2D, blur, GaussianBlur, median, bilateralFilter]

for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
