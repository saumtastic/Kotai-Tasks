import cv2
import numpy as np

img = cv2.imread('Resources/leana.png')

new_img = cv2.polylines(img = img, pts = [np.array([[105,34],[54,132],[50,214],[176,214],[177,130]])] , isClosed = True ,color = (111,255,234),thickness = 4,lineType=16 )

cv2.imshow("Poly Image",new_img)
cv2.waitKey(0)