from asciimage import *
from PIL import Image

image = Image.open(input("image:")).convert("L").quantize(colors=int(input("colors number:")), method=2)
image = toAscii(image, 167, 48,["0","1"])

i=0
ii=0
name = "ALLANSM "
newimage = ""
for n in image:
    if(n == "1"):
        newimage += name[i]
        i+=1
        if(i == len(name)):
            i=0
    elif(n == "\n"):
        newimage+="\n"
    else:
        newimage+=" "
    ii+=1

print(newimage)
