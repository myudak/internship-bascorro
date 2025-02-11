import cv2
import torch
import numpy as np

# Load the YOLOv5 model from a local file
model_path = """file\content\yolov5\\runs\\train\exp\\best.pt"""  # Replace with the path to the .pt file you downloaded
model = torch.load(model_path, map_location=torch.device("cpu"))[
    "model"
].float()  # or use 'cuda' for GPU

# Set the model to evaluation mode
model.eval()


# Function to perform inference
def run_inference(image):
    # Convert the image to a format YOLOv5 expects
    img = [image]  # YOLOv5 expects a list of images
    img = (
        torch.from_numpy(img).permute(0, 3, 1, 2).float()
    )  # Convert to tensor and change dimension order
    img /= 255.0  # Normalize image to [0, 1]

    # Perform inference
    with torch.no_grad():
        results = model(img)

    return results


# Function to render the results on the image
def render_results(results, img):
    # Get the results (bounding boxes, class labels, and confidence)
    pred = results.pred[0]
    labels = pred[:, -1].cpu().numpy()  # Class labels
    boxes = pred[:, :-1].cpu().numpy()  # Bounding boxes
    confidences = pred[:, -2].cpu().numpy()  # Confidence scores

    # Iterate through predictions and draw bounding boxes on the image
    for box, label, confidence in zip(boxes, labels, confidences):
        x1, y1, x2, y2 = box
        cv2.rectangle(
            img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2
        )  # Draw rectangle
        cv2.putText(
            img,
            f"{int(label)} {confidence:.2f}",
            (int(x1), int(y1) - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2,
        )  # Label and confidence

    return img


# # Load an image using OpenCV (replace with your image path)
# img_path = "your_image.jpg"  # Replace with the path to your image
# img = cv2.imread(img_path)

# # Run inference on the image
# results = run_inference(img)

# # Render results on the image
# output_img = render_results(results, img)

# # Display the result
# cv2.imshow("YOLOv5 Detection", output_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# --- Video Stream (Webcam) Example ---

# Open a video capture (0 for webcam or replace with video file path)
cap = cv2.VideoCapture(1)  # Replace 0 with video file path for pre-recorded video

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run inference on the frame
    results = run_inference(frame)

    # Render the results (bounding boxes and labels)
    output_frame = render_results(results, frame)

    # Display the frame
    cv2.imshow("YOLOv5 Detection (Webcam)", output_frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
