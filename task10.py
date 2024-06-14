import cv2
Cam = cv2.VideoCapture(0)

if(Cam.isOpened()):
    print("The Camera is successfully opened")
else:
    print("Couldn't open the camera")

frameWidth = int(Cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(Cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
frameRate = int(Cam.get(cv2.CAP_PROP_FPS))

fourccCode = cv2.VideoWriter_fourcc(*'DIVX')
VideoFileName = 'Resources/RecordedVid.avi'
VideoDimension = (frameWidth,frameHeight)

RecordedVideo = cv2.VideoWriter(VideoFileName,fourccCode,frameRate,VideoDimension)

while True:
    success,frame = Cam.read()
    if not success:
        print("Not able to read the frame. End")
        break
    cv2.imshow('Camera Video',frame)
    RecordedVideo.write(frame)

    if cv2.waitKey(1) == ord('q'):
        break
RecordedVideo.release()
Cam.release()
