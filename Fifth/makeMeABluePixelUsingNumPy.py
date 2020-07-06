import numpy as np
import cv2

#Create a numpy array with First picel as Blue (Only one pixel)

myBluePixelInNumPy = np.array(

[
    [
        [255,0,0]
    ]

]
, np.uint8
)

cv2.imshow("My Image with only one blue pixel", myBluePixelInNumPy)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("my_1by1_blue_pixel_using_numPy.png", myBluePixelInNumPy)
