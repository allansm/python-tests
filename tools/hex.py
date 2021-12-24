from dependency import include
from base64 import *

include("../../python-lib")

from argsHandle import *
from fileHandle import *

args = getArgs(["fn","--x"])

fn = args.fn
x = args.x

if(x != None):
    x = int(x)

data = readBytes(fn)
data = b16encode(data).decode()

i = 0
c = 0
arr = [""," "]
for n in data:
    print(n,end=arr[i])
    
    i+=1
    
    if(i > 1):
        i=0
        c+=1
    
    if(c == x):
        print("")
        c=0

