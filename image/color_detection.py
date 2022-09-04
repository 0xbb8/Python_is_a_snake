import cv2, numpy as np

def empty(x):
    pass

image_large = cv2.imread('/home/bosco/ctf/btlo/squid_gme/Dalgona.png')
image = cv2.resize(image_large, (464,348))
# changing the image color space into HSV (Hue, Saturation, Value)
image_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars',640,240)
cv2.createTrackbar('Hue Min','Trackbars',0,179,empty)
cv2.createTrackbar('Hue Max','Trackbars',115,179,empty)
cv2.createTrackbar('Saturation Min','Trackbars',0,255,empty)
cv2.createTrackbar('Saturation Max','Trackbars',150,255,empty)
cv2.createTrackbar('Brightness Min','Trackbars',0,255,empty)
cv2.createTrackbar('Brightness Max','Trackbars',100,255,empty)

while True:
    hue_minimum = cv2.getTrackbarPos('Hue Min', 'Trackbars')
    hue_maximum = cv2.getTrackbarPos('Hue Max', 'Trackbars')
    saturation_minimum = cv2.getTrackbarPos('Saturation Min', 'Trackbars')
    saturation_maximum = cv2.getTrackbarPos('Saturation Max', 'Trackbars')
    brightness_minimum = cv2.getTrackbarPos('Brightness Min', 'Trackbars')
    brightness_maximum = cv2.getTrackbarPos('Brightness Max', 'Trackbars')

    lower_limit = np.array([hue_minimum, saturation_minimum, brightness_minimum])
    upper_limit = np.array([hue_maximum, saturation_maximum, brightness_maximum])
    #  gives the filtered image using the given values
    mask = cv2.inRange(image_HSV, lower_limit, upper_limit)
    # cv2.bitwise_and(original_image, new_image_reerence, mask=<mask_applied>)
    image_result = cv2.bitwise_and(image,image_HSV, mask=mask)

    print('Hue:' + str(hue_minimum) + ' :: ' + str(hue_maximum))
    print('Brightness:' + str(saturation_minimum) + ' :: ' + str(saturation_maximum))
    print('Brightness:' + str(brightness_minimum) + ' :: ' + str(brightness_maximum))

    stack_image = np.hstack((image, image_HSV))
    cv2.imshow('Original and HSV images', stack_image)
    cv2.imshow('Masked Image', mask)
    cv2.imshow('New Image', image_result)
    cv2.waitKey(1)

cv2.destroyAllWindows()
