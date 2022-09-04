import cv2, numpy as np

image = cv2.imread('wrap.jpg')
# np.float32([],[],[],[])
width = 300
height = 150
# work out the corners
frame_1 = np.float32([[227,114],[192,42],[374,516],[493,209]])
frame_2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# using getPerspectiveTransform() to get the tranformation matrix
matrix = cv2.getPerspectiveTransform(frame_1,frame_2)
# getting the outut image using the transformation matrix on the source image
warpped_image = cv2.warpPerspective(image,matrix,(width,height))

cv2.imshow('Original Image', warpped_image)
cv2.waitKey(0)
