import dependency
import os
from argsHandle import *

args = getArgs(["src","dst"])

os.symlink(args.src,args.dst)
