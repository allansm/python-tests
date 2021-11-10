import dependency

def rebuild(dn):
    from shutil import rmtree
    from os import mkdir

    try:
        rmtree(dn)
    except:
        dummy = ""

    try:
        mkdir(dn)
    except:
        dummy = ""

def getPaths(args):
    from os import chdir,getcwd
    from fileHandle import getAllFilesPath,getFileName
    
    files = getAllFilesPath(args.dir)
    
    tmp = getcwd()
    
    chdir(args.dir)
    dir = getcwd()
    
    chdir(tmp)

    farr = []
    darr = []

    for f in files:
        fn = getFileName(f)
        
        tmp = "" 
        
        if("/" in dir):
            tok = dir.split("/")[-1]+"/"
            if(tok in f):
                tmp = f.split(tok)[1]
        elif("\\" in dir):
            tok = dir.split("\\")[-1]+"\\"
            if(tok in f):
                tmp = f.split(tok)[1]
        
        fpath = tmp
        dpath = tmp.replace(fn,"")
        
        if(fpath != ""):
            farr.append(fpath)
        if(dpath != ""):
            darr.append(dpath)

    
    arr = []

    arr.append(farr)
    arr.append(darr)
    arr.append(files)

    return arr


def build(paths,isTest=False): 
    from os import chdir
    from os import makedirs as mkdir
    
    if(not isTest):
        rebuild("links")
        chdir("links")
    
    for dir in paths[1]:
        print(dir)
        if(not isTest):
            try:
                mkdir(dir)
            except:
                dummy=""

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
