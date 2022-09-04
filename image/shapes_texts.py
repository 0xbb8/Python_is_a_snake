import cv2, numpy as np

## image created with matrix filled with zeros(black pixels)
## the (height,width,color_channels), np.unint8: 8 bit color values
image = np.zeros((300,300,3),np.uint8)
## image[:] : define the limits for width and height of the image (limits are matrix co-ordinates)
# image [125:175, 50:250] = 2,15,188
# image [50:250, 125:175] = 188,15,2
# image [0:50, 0:50] = 0,255,0
# image [250:300, 250:300] = 0,255,0
# image [0:50, 250:300] = 0,255,0
# image [250:300, 0:50] = 0,255,0

## Creating a line uning the line(image, (start co-ordinate), (end co-ordinate), (color channel values), thickness) function in the cv2 package
# cv2.line(image, (0,100), (100,225), (0,0,255), 5)

# using image.shape tuple values as inputs for endpoint co-ordinates (width, height)
cv2.line(image, (0,100), (image.shape[1],image.shape[0]-100), (0,0,255), 5)
# drawing a circle using circle(image, (center co-ordinates), radius, (color channel values), thickness)
cv2.circle(image, (150,150), 125, (0,255,0), 2)
# drawing a rectangle using rectangle(image, (start co-ordinates), (end co-ordinates), (color channel values), thickness <cv2.FILLED is used to fill the shape>)
cv2.rectangle(image, (125,125), (image.shape[1]-125, image.shape[0]-125), (255,0,0), cv2.FILLED)
# puttng text on an image using putText(image, <text>, (start co-ordinate), <font>, scale, color, thickness)
cv2.putText(image, 'OpenCV', (75,275), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,150), 1)

print(image.shape)
print(image)

cv2.imshow('Around the blocks', image)
cv2.waitKey(10000)
