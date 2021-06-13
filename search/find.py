import sys
sys.path.append("../functions")
import os
from argsHandle import *

args = getArgs(["path","text"],"")

path = args.path
text = args.text

fold = os.walk(path)
for root, dirs, files in fold:
    for name in files:
        tmp = os.path.realpath(os.path.join(root, name))
        if(text in tmp):
            print(tmp)


