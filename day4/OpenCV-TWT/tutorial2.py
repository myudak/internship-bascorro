# DOCUMENTATION https://docs.opencv.org/4.10.0/d6/d00/tutorial_py_root.html

import cv2
import random

img = cv2.imread("img/1.jpeg", -1)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
# LOAD AN IMAGE AND TURN IT INTO NUMPY

print(type(img))
print(img.shape)

print(img)

# ACCSESSING PIXEL VALUES
print(img[0][69])

# CHANGING PIXEL COLROS

for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255) for _ in range(3)]

# SLICE IMAGE

tag = img[100:200, 500:600]
img[200:300, 400:500] = tag

# DISPLAYING IMAGE
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
