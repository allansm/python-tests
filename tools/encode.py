import sys

sys.path.append("../../python-lib")

from argsHandle import *
from base64 import *

def b(base,type,data):
    exec("global x;x = b"+base+type+"(data.encode('utf-8')).decode('utf-8')")
    
    global x
    tmp = x
    
    x = None
    del x

    return tmp

args = getArgs(["--base","data","?decode"])

base = args.base

if(base == None):
    base = "64"

data = args.data
type = args.decode

if(not type):
    type = "encode"
else:
    type = "decode"

print(b(base,type,data))
