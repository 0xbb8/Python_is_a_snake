import cv2
# Using the VideoCapture() function to get the webcam feed. We use 0 for the
# built-in webcam and increment it if we have more webcams.
capture = cv2.VideoCapture(0)
# ID for the height and width settings are 3 and 4 resp.
capture.set(3, 720)
capture.set(4, 480)
# ID for the brightness setting is 10
capture.set(10, 20)

while True:
    # success is a boolean and the image variable storea our image
    success, image = capture.read()
    # Showin image in a window
    cv2.imshow("Web Cam", image)
    # Adding delay of 1 millisecond and exits program if pressed 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
