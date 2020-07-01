# Open Yellow image
# Read Yellow Image

import numpy as np
import cv2

myYellowImage = cv2.imread("yellow.png")
#print (myYellowImage)
print(myYellowImage)

print(myYellowImage.shape)

print("my height is:", myYellowImage.shape[0])

print("my width is:", myYellowImage.shape[1])

