from allansm.fileHandle import *
from allansm.argsHandle import *
from os import chdir

remove(".apps")
mkdir(".apps")

files = getAllFiles(getArgs(["path"]).path)

for n in files:
    if(realpath(n) != realpath(__file__) and ".pyc" in n):
        file = realpath(n)
        chdir(".apps")
        fn = file.split("/")[-1].replace(".pyc","")
        writeFile(fn, "#!/bin/bash\npython3 "+file+" $@")
        chdir("..")
