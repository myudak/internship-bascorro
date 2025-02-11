# Drawing (Lines, Images, Circles & Text)
# Cameras and VideoCapture

import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while 1:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0, 0), (width, height), (0, 0, 255), 2)
    img = cv2.line(img, (0, 0), (width, 90), (200, 80, 255), 2)
    img = cv2.rectangle(img, (100, 100), (200, 200), (0, 0, 255), 2)
    img = cv2.circle(img, (200, 200), 100, (0, 0, 255), 5)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, "Hello cok", (200, 200), font, 2, (0, 0, 255), 2)

    cv2.imshow("frame", img)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
