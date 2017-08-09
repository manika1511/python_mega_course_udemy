import numpy
import cv2

img_gray = cv2.imread("smallgray.png", 0) #0 for gray scale
img_brg = cv2.imread("smallgray.png", 1) #1 for bgr scale

new_img = cv2.imwrite("new.png", img_brg) #creating an image with given pixel values

