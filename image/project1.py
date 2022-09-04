# importing the openCV package
import cv2

print('openCV is working on this project')

# using the imread() function to read a image file
image = cv2.imread("bosco.jpg")

# using the imshow() function to show the image
# we use two arguements. Name of the window and the input image file
cv2.imshow('output',image)
# we add a delay for the window to close. It is in milliseconds. '0' is infinite delay.
cv2.waitKey(10000)
