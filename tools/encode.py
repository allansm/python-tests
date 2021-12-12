import sys

sys.path.append("../../python-lib")

from argsHandle import *
from base64 import *

args = getArgs(["base","data","--type"])

base = args.base
data = args.data
type = args.type

if(type == None):
    type = "encode"

exec("print(b"+base+type+"(data.encode('utf-8')).decode('utf-8'))")
