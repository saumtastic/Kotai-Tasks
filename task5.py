import cv2
import numpy as np

def draw_polygon(event, x, y, flags, param):
    global clickX, clickY, image, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        clickX.append(x)
        clickY.append(y)
        drawing = True

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        cv2.imshow('Polygon Drawing', image.copy())
        cv2.polylines(image_copy, [np.array([clickX, clickY]).T], False, (0, 255, 0), 2)

    elif event == cv2.EVENT_LBUTTONUP and drawing:
        cv2.polylines(image, [np.array([clickX, clickY]).T], False, (0, 255, 0), 2)
        drawing = False

image = cv2.imread('Resources/leana.png')
image_copy = image.copy()

clickX, clickY = [], []
drawing = False

cv2.namedWindow('Polygon Drawing')
cv2.setMouseCallback('Polygon Drawing', draw_polygon)

while True:
    cv2.imshow('Polygon Drawing', image_copy)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


