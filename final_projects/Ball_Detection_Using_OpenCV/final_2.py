import cv2
import numpy as np

LOWER_B = np.array([0, 165, 116])
UPPER_B = np.array([6, 255, 255])
MERAH = (0, 0, 255)
KERNEL_BLUR = (9, 9)
CIRCLE_DP = 1.2
CIRCLE_MIN_DIST = 100
CIRCLE_PARAM1 = 50
CIRCLE_PARAM2 = 30
CIRCLE_MIN_RADIUS = 30
CIRCLE_MAX_RADIUS = 200

print("\n\n========== myudakk ==========")

cap = cv2.VideoCapture(int(input("Video Capture (0,1,2,3) > ")))

print(f"LOWER_BOUND = np.array({LOWER_B.tolist()})")
print(f"UPPER_BOUND = np.array({UPPER_B.tolist()})")
print(f"KERNEL BLUR = {KERNEL_BLUR}")
print(f"CIRCLE_DP = {CIRCLE_DP}")
print(f"CIRCLE_MIN_DIST = {CIRCLE_MIN_DIST}")
print(f"CIRCLE_PARAM1 = {CIRCLE_PARAM1}")
print(f"CIRCLE_PARAM2 = {CIRCLE_PARAM2}")
print(f"CIRCLE_MIN_RADIUS = {CIRCLE_MIN_RADIUS}")
print(f"CIRCLE_MAX_RADIUS = {CIRCLE_MAX_RADIUS}")
print("q || CTRL + C to exit")

try:
    while 1:
        ret, frame = cap.read()
        if not ret:
            print("GAK AD VIDEOO")
            break

        hsv = cv2.cvtColor(
            cv2.GaussianBlur(frame, KERNEL_BLUR, 0),
            cv2.COLOR_BGR2HSV,
        )
        mask = cv2.inRange(hsv, LOWER_B, UPPER_B)
        circles = cv2.HoughCircles(
            mask,
            cv2.HOUGH_GRADIENT,
            dp=CIRCLE_DP,
            minDist=CIRCLE_MIN_DIST,
            param1=CIRCLE_PARAM1,
            param2=CIRCLE_PARAM2,
            minRadius=CIRCLE_MIN_RADIUS,
            maxRadius=CIRCLE_MAX_RADIUS,
        )

        if circles is not None:
            circles = np.uint16(np.around(circles))
            for circle in circles[0, :]:
                x, y, radius = circle
                cv2.circle(frame, (x, y), radius, MERAH, 2)
                cv2.circle(frame, (x, y), 3, MERAH, -1)

        cv2.imshow("MASK", mask)
        cv2.imshow("MAIN", frame)

        if cv2.waitKey(1) == ord("q"):
            break

except KeyboardInterrupt:
    pass

print("========== myudakk ==========\n\n")
print("exit...")
cap.release()
