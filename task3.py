import cv2

def Capture_Event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"({x},{y})")

if __name__ == "__main__":
    img = cv2.imread('Resources/leana.png')
    cv2.imshow("Image",img)
    cv2.setMouseCallback('Image',Capture_Event)
    cv2.waitKey(0)
