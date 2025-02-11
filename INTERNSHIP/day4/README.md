# DAY 4 RANGKUMAN STUDY NOTES BASCORRO INTERNSHIP

11 November 2024

https://trello.com/invite/b/672e1fee0d9a11c6015fb019/ATTI11c8be3f6be9d2939ca00bd244967d1c71F1849C/ews-bascorro-internship

https://trello.com/b/tDnxwbmm/ews-bascorro-internship

## OpenCV Course

This meeting discusses the OpenCV library and its application to two methods, namely HSV and Hough Transform (Hough Circle).

Reference

https://www.youtube.com/watch?v=qCR2Weh64h4&list=PLzMcBGfZo4-lUA8uGjeXhBUUzPYc6vZRn

https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python

https://github.com/Prometheussx/Hough-Circle

https://github.com/sanjeewa999/HSV-Color-Detector-On-Images

### ELI5

Imagine you want to make a program that can spot a ball in a video or a live camera feed. To do this, we can use a tool called **OpenCV**. Think of OpenCV as a powerful set of "eyes" that helps the computer recognize objects in images and videos.

In this discussion, we’re looking at **two different ways** to find a ball in an image or video: **HSV color filtering** and the **Hough Circle Transform**.

### Method 1: HSV (Color Filtering)

HSV stands for **Hue, Saturation, and Value**, which are just fancy words to describe color in a way that makes it easier for the computer to spot specific colors. Here’s a simple breakdown:

- **Hue** is the actual color (like red, blue, or orange).
- **Saturation** is how pure or intense the color is.
- **Value** is how bright or dark the color is.

Let’s say we have an orange ball. We tell the computer, “Look for anything that’s orange in color.” The computer then:

1. Converts the camera image from its normal colors to HSV colors.
2. Uses the "hue" part to find everything that matches orange.
3. Creates a black-and-white image where only the orange areas (the ball) are white, while everything else is black.

Now we have an outline of the ball! The computer can find this outline and mark it as the ball.

### Method 2: Hough Circle Transform

The **Hough Circle Transform** method is another trick in OpenCV's toolkit, but this one doesn’t care about color; it looks specifically for **round shapes** in the image. Here’s how it works:

1. OpenCV searches the image to find anything shaped like a circle.
2. When it spots a circle, it marks it for us.

This is helpful if the ball might be in a color that’s hard to filter with HSV, but it still keeps its round shape.

### Why Use Both?

- **HSV** is great when the ball has a bright, unique color (like bright orange or green) that stands out from everything else.
- **Hough Circle Transform** is useful when the ball is easy to spot by its round shape, even if the color is similar to the background.

By combining both methods, you get a program that’s really good at spotting the ball, even if it’s moving around or there’s a lot happening in the background!
