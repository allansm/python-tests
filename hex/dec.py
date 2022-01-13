from dependency import include
from base64 import *

include("../../python-lib")

from allansm.argsHandle import *
from allansm.fileHandle import *

args = getArgs(["fn","--x","--out"])

fn = args.fn
x = args.x
out = args.out

if(out == None):
    out="out"

if(x != None):
    x = int(x)

if(exists(fn)):
    data = readFile(fn)
    data = data.replace("\n","").replace(" ","")
    writeBytes(out,b16decode(data))
