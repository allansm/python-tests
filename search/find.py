import sys
sys.path.append("../functions")
import os
from argsHandle import *
from fileHandle import *
from os import chdir

args = getArgs(["path","text","ext"],"")

path = args.path
text = args.text
ext = args.ext

chdir(getTemp())
chdir("search")
found = getLines(".found")

fold = os.walk(path)
for root, dirs, files in fold:
    for name in files:
        tmp = os.path.realpath(os.path.join(root, name))
        
        exist = False

        chdir(getTemp())
        chdir("search")

        for fo in found:
            if(fo == tmp):
                exist = True
                break

        if(not exist):          
            writeFile(".found",tmp+"\n")

        if(text.lower() in tmp.lower()):
            if(ext != None):
                if(ext.lower() in tmp.lower()):
                    print(tmp)

            else:
                print(tmp)


