from allansm.fileHandle import *
from allansm.argsHandle import *
from allansm.file import *
from os import chdir

config = File(".config")
remove("alias")

for n in config.lines():
    tmp = n.split(";")
    if(len(tmp) > 1):
        action = tmp[0]
        ext = tmp[1]
        print(action)
        print(ext)

        dirs = ls(getArgs(["path"]).path)
        for d in dirs:
            files = ls(d)
            for n in files:
                if(realpath(n) != realpath(__file__) and ext in n):
                    file = realpath(n)
                    
                    fn = file.split("/")[-1].replace(ext,"")
                    
                    add("alias","alias "+fn+"=\""+action+" "+file+" $@\"\n")
