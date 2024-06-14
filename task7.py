import cv2
cap = cv2.VideoCapture('Resources/mkmkc.mp4')
while True:
    success, img = cap.read()
    cv2.imshow('Video', img)
    if cv2.waitKey(1) == 27:
        break