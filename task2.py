import cv2
import numpy as np

img = cv2.imread('Resources/leana.png')
print(img.shape)
imgResized = cv2.resize(img,(150,180))
imgCropped = imgResized[50:70,50:70]
imgRotated = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

cv2.imshow('Image',img)
cv2.imshow('Resized',imgResized)
cv2.imshow('Cropped',imgCropped)
cv2.imshow('Rotated',imgRotated)
cv2.waitKey(0)