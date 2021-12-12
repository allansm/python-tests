import sys

sys.path.append("../../python-lib")

from argsHandle import *
from base64 import *

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

exec("print(b"+base+type+"(data.encode('utf-8')).decode('utf-8'))")
