# imorting openCV package for image stuff and numpy for math stuff
import cv2, numpy as np
# readinf image file
image = cv2.imread("bosco.jpg")
# np.<all_values_are_one>((<size_of_the_matrix>),type_of_object:unsigned_integer_of_8_bits)
kernel = np.ones((5,5), np.uint8)

# Converting the image to grayscale using cvtColot() function.
# Using two arguements: image and colorspace. (channel order is BGR in OpenCV)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Using blur function: GaussianBlur(src, ksize(x,y), sigmaX, dst=None, sigmaY=None,borderType=None)
# ksize must be in odd numbers
image_blur = cv2.GaussianBlur(image, (3,3), 10)
# Edge deteciting using Canny(src,threshold1,threshold2) function.
image_canny = cv2.Canny(image, 100, 100)
# Image dilation (increasing thickness of our lines) using dilate(canny_image, kernel, how-much-do-we-want-the-kernel-to-move)
image_dilation = cv2.dilate(image_canny, kernel, iterations = 1)
# opposite of dilation.
image_eroded = cv2.erode(image_dilation, kernel, iterations = 1)

cv2.imshow("Blur Image", image_blur)
cv2.imshow("Grayscale Image", image_gray)
cv2.imshow("Canny Image", image_canny)
cv2.imshow("Dilated Image", image_dilation)
cv2.imshow("Eroded Image", image_eroded)
cv2.waitKey(10000)
