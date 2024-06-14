import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
img = cv2.imread("Resources/leana.png")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img,(5,5),0)
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("Image", img)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("RGB Image", imgRGB)
cv2.imshow("HSV Image", imgHSV)

cv2.waitKey(0)