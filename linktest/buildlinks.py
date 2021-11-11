from lnk import *

def test(p,isTest=False):
    from os import symlink,getcwd,chdir,remove
    from os.path import exists

    paths = getPaths(p)
    if(not exists("links")):
        print("create first u.u")
        exit()
    else:
        
        build(paths,isTest,False)
    
    i=0
    for file in paths[0]:
        print(file+" "+paths[2][i])
        if(not isTest):
            try:
                if(exists(file)):
                    remove(file)
                symlink(paths[2][i],file)
            except:
                print("error on file:"+file)
        i = i+1;

def run():
    from argsHandle import getArgs
    from fileHandle import getLines
    from os import getcwd,chdir
    args = getArgs(["list","--out","?test"])
    
    start = getcwd()
    
    rebuild("links")

    print("---------------------------------------")
    for line in getLines(args.list):
        print(line+":")
        print("---------------------------------------")
        test(line,args.test)
        print("---------------------------------------")

        chdir(start)
run()
