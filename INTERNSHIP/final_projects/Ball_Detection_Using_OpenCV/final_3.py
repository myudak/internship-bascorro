import cv2
import numpy as np

LOWER_B = np.array([0, 165, 116])
UPPER_B = np.array([6, 255, 255])
MERAH = (0, 0, 255)
KERNEL_BLUR = (9, 9)

print("\n\n========== myudakk ==========")

cap = cv2.VideoCapture(int(input("Video Capture (0,1,2,3) > ")))

print(f"LOWER BOUND = np.array({LOWER_B.tolist()})")
print(f"UPPER BOUND = np.array({UPPER_B.tolist()})")
print(f"KERNEL BLUR = {KERNEL_BLUR}")
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

        cnts, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE,
        )

        if cnts:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (
                (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                if M["m00"] > 0
                else None
            )

            if radius > 10:
                cv2.circle(frame, (int(x), int(y)), int(radius), MERAH, 2)
                if center:
                    cv2.circle(frame, center, 5, MERAH, -1)

        cv2.imshow("MASK", mask)
        cv2.imshow("MAIN", frame)

        if cv2.waitKey(1) == ord("q"):
            break

except KeyboardInterrupt:
    pass

print("========== myudakk ==========\n\n")
print("exit...")
cap.release()
