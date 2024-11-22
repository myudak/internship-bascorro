"""
COBA
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(3)

lower_b = np.array([0, 165, 116])
upper_b = np.array([6, 255, 255])
# lower_b = np.array([0, 0, 147])
# upper_b = np.array([179, 255, 255])


while 1:
    ret, frame = cap.read()
    if not ret:
        print("gk kedetek")
        break

    hsv = cv2.cvtColor(
        cv2.GaussianBlur(frame, (11, 11), 0),
        cv2.COLOR_BGR2HSV,
    )
    mask = cv2.inRange(hsv, lower_b, upper_b)

    circles = cv2.HoughCircles(
        mask,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=100,
        param1=80,
        param2=30,
        minRadius=75,
        maxRadius=900,
    )

    if circles is not None:
        circles = np.uint16(np.around(circles))

        print(circles)
        for i in circles[0, :]:
            # Tengah
            cv2.circle(frame, (i[0], i[1]), 1, (69, 69, 69), 3)
            # Circle
            cv2.circle(frame, (i[0], i[1]), i[2], (255, 255, 255), 3)

    cv2.imshow("Mask", mask)
    cv2.imshow("Bola Oren", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
