from os import system, chdir, getcwd
from allansm.argsHandle import *
from allansm.fileHandle import *
from allansm.util import *
from getpass import getpass

args = getArgs(["path"])

if(isdir(args.path)):
    pw = getpass("password:")
    if(pw == getpass("confirm password:")):
        dname = realpath(args.path)
        fname = "../"+dname.replace("\\","/").split("/")[-1].split("7z")[0]+".7z"
        chdir(dname)
        exec("7z a "+fname+" . -p"+pw)
        chdir("..")
        remove(dname)
    else:
        print("incorrect password try again.")
else:
    fname = realpath(args.path)
    dname = fname.replace("\\","/").split("/")[-1].split("7z")[0]
   
    remove(dname)
    mkdir(dname)
    chdir(dname)
    
    print("password:", end="\r")
    exec("7z x "+fname)
    remove(fname)
