import sys
sys.path.append("../../python-lib")

from fileHandle import *
import zlib
from base64 import *

raw_image = "89 50 4E 47 0D 0A 1A 0A"
raw_image+= "00 00 00 0D 49 48 44 52"
raw_image+= "00 00 00 03 00 00 00 03"
raw_image+= "08 02 00 00 00 02 50 58"
raw_image+= "EA 00 00 00 12 49 44 41"
raw_image+= "54"

idat = (
            b"\x00"
            b"\xff\x00\x00"
            b"\x00\xff\x00"
            b"\x00\x00\xff"
            
            b"\x00"
            b"\xff\x00\x00"
            b"\x00\xff\x00"
            b"\x00\x00\xff"

            b"\x02"
            b"\0\0\0"
            b"\0\0\0"
            b"\0\0\0"
       )

raw_image+= b16encode(zlib.compress(idat)).decode()

raw_image+= "65 62 10 33 00 00 00 00"
raw_image+= "49 45 4E 44 AE 42 60 82"

image = raw_image.replace(" ","")
image = b16decode(image)
writeBytes("image.png",image)
