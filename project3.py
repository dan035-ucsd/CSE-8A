### CSE 8A Project 3
### Author: Dani Nguyen
### Collaborations: None

from PIL import Image
# https://pillow.readthedocs.io/en/stable/reference/Image.html

scene = Image.open("scene.jpg")
shaq = Image.open("shaq.jpg")
ball = Image.open("ball.jpg")

scene = scene.resize((1600, 1200))

def flipHoriz(inp):     # flip image horizontally
    out = Image.new("RGB", (inp.width, inp.height))
    for x in range(inp.width):
        for y in range(inp.height):
            out.putpixel((inp.width - 1 - x, y), inp.getpixel((x, y)))
    return out

def flipVert(inp):      # flip image vertically
    out = Image.new("RGB", (inp.width, inp.height))
    for x in range(inp.width):
        for y in range(inp.height):
            out.putpixel((x, inp.height - 1 - y), inp.getpixel((x, y)))
    return out

def overlay(inp, overlay, xloc, yloc):         # overlay an image
    out = Image.new("RGB", (inp.width, inp.height))
    for x in range(xloc, xloc + overlay.width):
        for y in range(yloc, yloc + overlay.height):
            for i in range(overlay.width):
                for j in range(overlay.height):
                    inp.putpixel((x, y), overlay.getpixel((x - xloc, y - yloc)))
    


# color filter

# edge detection
# https://www.geeksforgeeks.org/what-is-edge-detection-in-image-processing/

# overlay images
# https://stackoverflow.com/questions/10640114/overlay-two-same-sized-images-in-python

# out.save("output.jpg")