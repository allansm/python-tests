import sys

sys.path.append("../../python-lib")

from argsHandle import *
from base64 import *
from util import clear

def b(base,type,data):
    exec("global x;x = b"+base+type+"(data.encode('utf-8')).decode('utf-8')")
    
    global x
    tmp = x
    
    x = None
    del x

    return tmp

def run(args):
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

def loop(args):
    
    data = args.data
    
    while(True):
        base = input("base:")
        type = input("type:")
        
        clear()
        data = b(base,type,data)
        print(data)
        
args = getArgs(["--base","data","?decode","?loop"])

if(not args.loop):
    run(args)
else:
    loop(args)

