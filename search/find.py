import sys
sys.path.append("../functions")
import os
from argsHandle import *

args = getArgs(["path","text","ext"],"")

path = args.path
text = args.text
ext = args.ext

fold = os.walk(path)
for root, dirs, files in fold:
    for name in files:
        tmp = os.path.realpath(os.path.join(root, name))
        if(text.lower() in tmp.lower()):
            if(ext != None):
                if(ext.lower() in tmp.lower()):
                    print(tmp)

            else:
                print(tmp)


