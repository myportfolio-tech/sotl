import os
import cv2

os.chdir('D:/sotl/images')
img1 = cv2.imread('headphones.jpg')

scale_percent = 0.08
width = int(img1.shape[1]* scale_percent)
height = int(img1.shape[0]* scale_percent)

dimension = (width, height)

resize = cv2.resize(img1, dimension, interpolation=cv2.INTER_AREA)

cv2.imshow('Test', resize)
cv2.imwrite('headphones-smallest.jpg', resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
