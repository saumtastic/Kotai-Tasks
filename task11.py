import cv2
import multiprocessing as mp

def display(vid_path,queue):
    cap = cv2.VideoCapture(vid_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow(vid_path, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    queue.put(True)

if __name__ == '__main__':
    vid_path1 = 'Resources/darj.mp4'
    vid_path2 = 'Resources/mkmkc.mp4'

    queue = mp.Queue()

    p1 = mp.Process(target=display, args=(vid_path1,queue))
    p2 = mp.Process(target=display, args=(vid_path2,queue))

    p1.start()

    queue.get()
    display(vid_path2,queue)
    p2.start()
    p2.join()

print("Done Executing")
