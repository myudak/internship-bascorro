# here is the edges and mask, tuned the parameters so it fits only one circle on this image

# Load the uploaded image to analyze it and check for potential adjustments to the circle detection.
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Path to the uploaded image
image_path = "/mnt/data/image.png"

# Load the image
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# Convert to grayscale for edge detection (HoughCircles works on grayscale)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (9, 9), 2)

# Use Canny edge detection to enhance edges
edges = cv2.Canny(blurred, 50, 150)

# Show the grayscale, blurred, and edges for verification
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
ax[0].imshow(gray, cmap="gray")
ax[0].set_title("Grayscale Image")
ax[1].imshow(blurred, cmap="gray")
ax[1].set_title("Blurred Image")
ax[2].imshow(edges, cmap="gray")
ax[2].set_title("Edges Detected")
plt.tight_layout()
plt.show()

# Apply Hough Circle Transform to detect circles
circles = cv2.HoughCircles(
    blurred,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=100,  # Minimum distance between the centers of detected circles
    param1=50,  # Canny high threshold
    param2=30,  # Accumulator threshold for circle detection
    minRadius=30,  # Minimum radius of the circle
    maxRadius=200,  # Maximum radius of the circle
)

# Make a copy of the original image to draw circles
output = image.copy()

# If some circles are detected, draw them
if circles is not None:
    circles = np.uint16(np.around(circles))
    for circle in circles[0, :]:
        # Draw the circle
        cv2.circle(output, (circle[0], circle[1]), circle[2], (0, 255, 0), 2)
        # Draw the center of the circle
        cv2.circle(output, (circle[0], circle[1]), 3, (0, 0, 255), 3)

# Display the result
plt.figure(figsize=(10, 10))
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.title("Detected Circles")
plt.axis("off")
plt.show()
