# Overview
This simple script performs an operation known as chroma keying on two input images: a foreground and a background image, to achieve a 'Green Screen Effect'. By defining a green color range. For every pixel in the image, if the pixel's color is within the green range, it replaces the corresponding pixel in the new image with the color of the pixel from the background image at the same position. Otherwise, the new image's pixel at that position is replaced by the corresponding foreground's pixel.

> [!NOTE]  
> This is a simple script with limited functionality. You might encounter unexpected issues or limitations. Your feedback is appreciated and encouraged.

# Usage
This program leverages John Zelle's `graphics.py` library. Make sure to supply two images with **matching dimensions**, where the foreground has a valid **green range**. When completed, give the output image a name. 
