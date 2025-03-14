### CSE 8A Project 3
### Author: Dani Nguyen
### Collaborations: None

from PIL import Image
# https://pillow.readthedocs.io/en/stable/reference/Image.html

scene = Image.open("scene.jpg")
shaq = Image.open("shaq.jpg")
ball = Image.open("ball.jpg")
pile = Image.open("pile.jpg")

scene = scene.resize((1600, 1200))
shaq = shaq.resize((1028, 786))
ball = ball.resize((152, 149))
pile = pile.resize((200, 200))


def flipHori(inp):     # flip image horizontally
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

def overlay(inp, overlay, xloc, yloc, rthresh, gthresh, bthresh, lessthan):     
    """ Over lays an image on top of another image while keying out certain
    RGB values of the overlay image"""   
    for x in range(xloc, xloc + overlay.width):
        for y in range(yloc, yloc + overlay.height):
            if lessthan == 1:
                if overlay.getpixel((x - xloc, y - yloc)) <= (rthresh, gthresh, bthresh):
                    inp.putpixel((x, y), overlay.getpixel((x - xloc, y - yloc)))
            elif lessthan == 0:
                if overlay.getpixel((x - xloc, y - yloc)) >= (rthresh, gthresh, bthresh):
                    inp.putpixel((x, y), overlay.getpixel((x - xloc, y - yloc)))
            else:
                print("Invalid parameter")
                quit()
    return inp

step1 = overlay(scene, shaq, 600, 414, 235,235,235, 1)
step2 = overlay(step1, ball, 1250, 573, 20,20,20, 0)
step3 = overlay(step2, flipHori(ball.resize((114,111))), 1000, 500, 20,20,20, 0)
step4 = overlay(step3, flipVert(ball.resize((84,81))), 800, 560, 20,20,20, 0)
step5 = overlay(step4, ball.resize((54,51)).rotate(40), 650, 690, 20,20,20, 0)
step6 = overlay(step5, ball.resize((30,27)), 530, 900, 20,20,20, 0)
step7 = overlay(step6, pile, 410, 1000, 20,20,20, 0)

step7.show()
