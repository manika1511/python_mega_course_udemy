import cv2

#read the image in grayscale.. 0 shows grayscale; 1 shows rbg scale
img=cv2.imread("galaxy.jpg", 0)

#shape of image: 1485X990
print (img.shape)
#no. of dimensions
print (img.ndim)
