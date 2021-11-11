from lnk import *

def run():
    from os import symlink,getcwd,chdir,remove
    from argsHandle import getArgs
    from os.path import exists
    args = getArgs(["dir","--out","?test"])
    
    paths = getPaths(args)
    if(not exists("links")):
        print("create first u.u")
        exit()
    else:
        
        build(paths,args.test,False)
    
    i=0
    for file in paths[0]:
        print(file+" "+paths[2][i])
        if(not args.test):
            try:
                if(exists(file)):
                    remove(file)
                symlink(paths[2][i],file)
            except:
                print("error on file:"+file)
        i = i+1;

run()
