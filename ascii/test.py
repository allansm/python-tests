from PIL import Image
from random import shuffle

img = Image.open(input("image:")).convert("L")

def test(img,w,h,arr):
    image = ""

    img = img.resize((w,h))

    for y in range(0,h):
        for x in range(0,w):
            px = img.getpixel((x,y))
            image+=arr[px%len(arr)]
        
        image+="\n"
    
    return image

image = test(img,150,75,[" ","|","'","!",".","-"])

print(image)
