### CSE 8A Project 3
### Author: Dani Nguyen
### Collaborations: None

from PIL import Image
https://pillow.readthedocs.io/en/stable/reference/Image.html

scene = Image.open("scene.jpg")
shaq = Image.open("shaq.jpg")
ball = Image.open("ball.jpg")
out = Image.new("RGB", (scene.width, scene.height))

# flip image
img.putpixel(width() - 1 - x, y, color)

# color filter

# rotate image

# crop image

# edge detection
https://www.geeksforgeeks.org/what-is-edge-detection-in-image-processing/

# overlay images
https://stackoverflow.com/questions/10640114/overlay-two-same-sized-images-in-python


out.Image.show()
out.save("output.jpg")