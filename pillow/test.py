from PIL import Image, ImageDraw
from os import remove

img = Image.new("RGB", (100,100), "#FFFFFF")
draw = ImageDraw.Draw(img)

draw.pieslice((0, 0, 100, 100), start=0, end=90, fill="#0000FF")

for y in range(50):
    for x in range(50):
        if(y % 2 == 0):
            draw.point((x, y, 1, 1), fill="#FF0000")

for y in range(50):
    for x in range(50):
        if(x % 2 == 0):
            draw.point((x, y, 1, 1), fill="#FF0000")

img.save("test.png")
img.show()
remove("test.png")
