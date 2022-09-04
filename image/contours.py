import cv2, numpy as np

image1 = cv2.imread('shapes.png')
image = cv2.resize(image1, (416,197))
# making a copy of the image
image_contour = image.copy()
image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_blur = cv2.GaussianBlur(image_grayscale, (5,5), 3)
image_canny = cv2.Canny(image_blur,50,50)
image_blank = np.zeros_like(image)

def get_contours(image):
    # findContours(<image>, retrival_method, get_contour_values)
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for c in contours:
        area  = cv2.contourArea(c)
        # drawing contours (_) each time it finds over the image_contour image
        # drawContours(image_to_draw, contour, <contour_index>, (color), thickness)
        if area > 120:
            # only draws contours if the shape has area more than 120 pixels
            cv2.drawContours(image_contour, c, -1, (0,0,255), 2)
            # calculate the curve length
            perimeter = cv2.arcLength(c, True)
            # print(perimeter)
            corner_points = cv2.approxPolyDP(c, 0.02*perimeter, True)
            print('Corner Points:')
            # len(corner_points) gives the total vertices of the shapes
            #  iff the len(corner_points) is high. It denotes a circle
            print(len(corner_points))
            # creating a bounding box around the shapes
            shape_corners = len(corner_points)
            x, y, width, height = cv2.boundingRect(corner_points)

            if shape_corners == 3:shape = 'Triangle'
            elif shape_corners == 4:
                aspect_ratio = width/float(height)
                if aspect_ratio > 0.95 and aspect_ratio < 1.05:
                    shape = 'Square'
                else:
                    shape = 'Rectangle'
            elif shape_corners == 5:shape = 'Pentagon'
            elif shape_corners == 6:shape = 'Hexagon'
            elif shape_corners > 6:shape = 'Circle'
            else:shape = 'None'
            cv2.rectangle(image_contour, (x,y), (x+width, y+height), (0,255,0), 1)
            cv2.putText(image_contour, shape, (int((x+width/2)-20),int((y+height-5))), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255), 1)

# creating and displaying an image stack
image_stack_1 = np.vstack((image_grayscale, image_blur, image_canny))
cv2.imshow('Images', image_stack_1)
# image with contours drawn by the get_contours() function
get_contours(image_canny)
cv2.imshow('Contours', image_contour)

cv2.waitKey(10000)
# cv2.destroyAllWindows()
