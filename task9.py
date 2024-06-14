import cv2
import multiprocessing as mp

def display(vid_path):
    cap = cv2.VideoCapture(vid_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow(vid_path, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()

if __name__ == '__main__':
    vid_path1 = 'Resources/darj.mp4'
    vid_path2 = 'Resources/mkmkc.mp4'

    p1 = mp.Process(target=display, args=(vid_path1,))
    p2 = mp.Process(target=display, args=(vid_path2,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

print("Done Executing")
