import cv2
import numpy as np


image_path = "bola1.png"
image = cv2.imread(image_path)

print(f"\n\n========== CARI BOUND {image_path} ==========\n\n")

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_initial_guess = np.array([0, 50, 50])
upper_initial_guess = np.array([10, 255, 255])

mask = cv2.inRange(hsv_image, lower_initial_guess, upper_initial_guess)
result = cv2.bitwise_and(image, image, mask=mask)

masked_hsv = hsv_image[mask > 0]
mean_hsv = masked_hsv.mean(axis=0)
std_hsv = masked_hsv.std(axis=0)

refined_lower_bound = np.maximum(mean_hsv - 2 * std_hsv, [0, 0, 0]).astype(int)
refined_upper_bound = np.minimum(mean_hsv + 2 * std_hsv, [179, 255, 255]).astype(int)

print(
    f"""
lower_b = np.array({refined_lower_bound.tolist()})
upper_b = np.array({refined_upper_bound.tolist()})
"""
)
