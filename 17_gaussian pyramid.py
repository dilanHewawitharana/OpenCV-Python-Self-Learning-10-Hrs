import cv2
from matplotlib import pyplot as plt

img = cv2.imread("Resources/SOS/3.jpg")
layer = img.copy()
gp = []

gp.append(layer)
for i in range(5):
    layer = cv2.pyrDown(layer)
    gp.append(layer)

layer = img.copy()
gp.append(layer)
for i in range(5):
    layer = cv2.pyrUp(layer)
    gp.append(layer)


title = [
        'Image', 'gpl1', 'gpl2', 'gpl3', 'gpl4', 'gpl5',
        'Image', 'gpu1', 'gpu2', 'gpu3', 'gpu4', 'gpu5',
        ]

for i in range(len(gp)):
    plt.subplot(2, 6, i+1)
    plt.imshow(gp[i])
    plt.title(title[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
