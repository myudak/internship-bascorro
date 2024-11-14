import cv2

"""
LINKS https://github.com/techwithtim/OpenCV-Tutorials

COVERED IN
THIS VIDEO

Installation & Setup 01:46
Loading an Image 05:45
Displaying an Image 7:56
Resizing an Image 10:35
Rotating an Image 12:45
"""

# install opencv
# pip install opencv-python

img = cv2.imread("img/1.jpeg", 0)
# RESIZE
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
# ROTATE
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# SAVE IMAGE
cv2.imwrite("img/out.jpeg", img)

"""
0 : grayscale
1 : color
2 : any color
3 : load as is
"""

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
