import cv2, numpy as np

# importing the cascade file provided by opencv for frontal face detection
cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

image1 = cv2.imread('people.jpg')
image = cv2.resize(image1, (464,348))
image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# finding the faces in the image using the cascade file.
# cascade.detectMultiScale(image, scale_factor,  minimum_neighbours)
faces = cascade.detectMultiScale(image_grayscale, 1.1, 4)

for (x,y,width,height) in faces:
    cv2.rectangle(image, (x,y), (x+width, y+height), (0,255,0), 1)
    cv2.putText(image, 'face', (x,int((y+height+12))), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,255,0), 1)

cv2.imshow('Image', image)
if cv2.waitKey(0) & 0xFF == ord('q'):cv2.destroyAllWindows()
