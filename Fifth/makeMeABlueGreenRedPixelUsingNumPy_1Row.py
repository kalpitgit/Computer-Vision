import numpy as np
import cv2

#Create a numpy array with First picel as Blue (Only one pixel)

myBlueGreenRedPixelInNumPy = np.array(

[
    [
        [255,0,0],
        [0,255,0],
        [0,0,255],

    ]

]
, np.uint8
)

cv2.imshow("My Image with one row and 3 coulmns (blue, green and red)", myBlueGreenRedPixelInNumPy)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("my_1by3_blue_green_red_pixel_using_numPy.png", myBlueGreenRedPixelInNumPy)
