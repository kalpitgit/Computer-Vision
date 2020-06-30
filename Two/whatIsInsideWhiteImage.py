# Open Black image
# Read Black Image

import numpy as np
import cv2

myWhiteImage = cv2.imread("myWhiteImage.png")
#print (myWhiteImage)
print(myWhiteImage)

print(myWhiteImage.shape)

print("my height is:", myWhiteImage.shape[0])

print("my width is:", myWhiteImage.shape[1])

