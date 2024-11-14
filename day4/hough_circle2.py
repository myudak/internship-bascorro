import cv2
import numpy as np

video = cv2.VideoCapture(0)
prevCirc = 0
dist = lambda x1, y1, x2, y2: (x1 - y1) ** 2 + (x2 - y2) ** 2

while 1:
    ret, frame = video.read()
    if not ret or frame is None:
        break

    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurFrame = cv2.GaussianBlur(grayFrame, (17, 17), 0)

    circles = cv2.HoughCircles(
        blurFrame,
        cv2.HOUGH_GRADIENT,
        1.2,
        100,
        param1=100,
        param2=30,
        minRadius=75,
        maxRadius=400,
    )

    if circles is not None:
        circles = np.uint16(np.around(circles))
        chosen = None
        for i in circles[0, :]:
            if chosen is None:
                chosen = i
            if prevCirc is not None:
                if dist(i[0], i[1], prevCirc[0], prevCirc[1]) < dist(
                    chosen[0], chosen[1], prevCirc[0], prevCirc[1]
                ):
                    chosen = i
            prevCirc = i
        cv2.circle(frame, (chosen[0], chosen[1]), chosen[2], (0, 0, 255), 4)
        cv2.putText(
            frame,
            "Circle",
            (chosen[0], chosen[1]),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2,
        )

    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

video.release()
