import sys
sys.path.append("../../python-lib")

from base64 import *
import zlib
from fileHandle import *
from argsHandle import *

args = getArgs(["file"])

b = readBytes(args.file)

hex = b16encode(b).decode()

test = hex.split("49444154")[1]

test = test.split("CD")[0]+"CD"

test = b16decode(test)

i = 0
i2 = 0
for n in b16encode(zlib.decompress(test)).decode():
    print(n,end="")
    if(i == 1):
        i=0
        print(" ",end="")
    else:
        i+=1

    if(i2 == 13):
        i2=0
        print("")
    else:
        i2+=1
