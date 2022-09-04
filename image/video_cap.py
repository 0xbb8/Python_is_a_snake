import cv2

capture = cv2.VideoCapture("sample_video.mp4")

while True:
    success, image = capture.read()
    cv2.imshow("Video Capture", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
