from dependency import include
from base64 import *

include("../../python-lib")

from argsHandle import *
from fileHandle import *

args = getArgs(["fn","--x","--out"])

fn = args.fn
x = args.x
out = args.out

if(x != None):
    x = int(x)

data=""

if(exists(fn)):
    data = readBytes(fn)
else:
    data = fn.encode()

data = b16encode(data).decode()

i = 0
c = 0
arr = [""," "]
res = ""
for n in data:
    res+=n+arr[i]
    i+=1
    
    if(i > 1):
        i=0
        c+=1
    
    if(c == x):
        res+="\n"
        c=0

if(out == None):
    print(res)
else:
    writeFile(out,res)
