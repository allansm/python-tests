from lnk import *

def run():
    from os import symlink,getcwd 
    from argsHandle import getArgs

    args = getArgs(["dir","--out","?test"])
    
    paths = getPaths(args)
    build(paths,args.test)
    
    i=0
    for file in paths[0]:
        print(file+" "+paths[2][i])
        if(not args.test):
            try:
                symlink(paths[2][i],file)
            except:
                print("error on file:"+file)
        i = i+1;

run()
