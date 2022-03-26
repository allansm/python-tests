from allansm.fileHandle import ls, getAllFiles, mkdir, move, remove, rename, realpath, getFileName, isdir
from allansm.argsHandle import getArgs
from shutil import copytree as copy
from os import chdir, getcwd
import py_compile

def compile(f, output):
    try:
        if(not ".pyc" in f and not isdir(f) and ".py" in f):
            py_compile.compile(f)
            f = getFileName(f)
            print(output+"/"+f+"c")
            rename(getAllFiles("__pycache__")[0], output+"/"+f+"c")

            return True
    except:
        print("erro on :"+f)
        error=0

    return False

def compiledir(removeFiles=False, keepName=False):
    for n in ls():
        if(not isdir(n)):
            candelete = compile(n, ".")
            if(removeFiles and candelete):
                print("removing :"+n)
                remove(n)
                if(keepName):
                    rename(n+"c",n)
        else:
            back = getcwd()
            chdir(n)
            compiledir(removeFiles,keepName)
            chdir(back)

    remove("__pycache__")

args = getArgs(["path","?samename"])

remove("output")
copy(args.path, "output")
chdir("output")
compiledir(True,args.samename)
