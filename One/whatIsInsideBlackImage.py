# Open Black image
# Read Black Image

import numpy as np
import cv2

myBlackImage = cv2.imread("FullBlack.png")
#print (myBlackImage)

print(myBlackImage.shape)

print("my height is:", myBlackImage.shape[0])

print("my width is:", myBlackImage.shape[1])

