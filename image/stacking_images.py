import cv2, numpy as np

image = cv2.imread('bosco.jpg')

image_horizontal = np.hstack((image, image, image))
image_vertical = np.vstack((image, image, image))

cv2.imshow('Image Horizontal Stack', image_horizontal)
cv2.imshow('Image Vertical Stack', image_vertical)

cv2.waitKey(0)
