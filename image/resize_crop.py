import cv2

image = cv2.imread('bosco.jpg')
print(image.shape)
# (height, width, color_channels)
# we use the resize(<image>,(width, height)) function to resize a image
image_resized = cv2.resize(image, (225,300))

# Image cropping: image[start:finish<width>, start:finish<height>]
image_cropped = image[0:300,0:225]

cv2.imshow('Image:Resized',image_resized)
cv2.imshow('Image:Cropped', image_cropped)
cv2.waitKey(10000)
