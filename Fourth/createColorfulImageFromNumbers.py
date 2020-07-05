from PIL import Image
myColorfulImage = Image.new('RGB', (1, 3))
myColorfulImage.putdata([(255,0,0), (0, 255,0), (0,0,255)])
myColorfulImage.save("RGB_1_Coulmn_3_Rows_RGB.png")

import cv2
myColorfulImage = cv2.imread("RGB_1_Coulmn_3_Rows_RGB.png")
print(myColorfulImage)
myColorfulImage = cv2.imshow("My Image Window",myColorfulImage )
cv2.waitKey(0)
cv2.destroyAllWindows()
