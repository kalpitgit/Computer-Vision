import numpy as np
import cv2

#Create a numpy array with First picel as Blue (Only one pixel)

makeMeABlueGreenRedPixel_and_Greypixels_UsingNumPy_2Rows_3Coulmns = np.array(

[
    [
        [255,0,0],
        [0,255,0],
        [0,0,255],

    ],
     [
        [90,90,90],
        [120,120,120],
        [150,150,150],

    ]

]
, np.uint8
)

cv2.imshow("My Image with Two rows and 3 coulmns (blue, green and red) AND Grey Coulmns", makeMeABlueGreenRedPixel_and_Greypixels_UsingNumPy_2Rows_3Coulmns)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("my_2by3_blue_green_red_grey)pixel_using_numPy.png", makeMeABlueGreenRedPixel_and_Greypixels_UsingNumPy_2Rows_3Coulmns)
