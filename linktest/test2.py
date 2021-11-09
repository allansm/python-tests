import dependency

def build(dn):
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
    from fileHandle import getAllFilesPath,getFileName
    
    files = getAllFilesPath(args.dir)
    
    farr = []
    darr = []

    for f in files:
        fn = getFileName(f)
        
        tmp = "" 
        
        if("/" in args.dir):
            tok = args.dir.split("/")[-1]+"/"
            if(tok in f):
                tmp = f.split(tok)[1]
        if("\\" in args.dir):
            tok = args.dir.split("\\")[-1]+"\\"
            if(tok in f):
                tmp = f.split(tok)[1]

        fpath = tmp
        dpath = tmp.replace(fn,"")
        
        if(fpath != ""):
            farr.append(fpath)
        if(dpath != ""):
            darr.append(dpath)

    arr = {'files':farr,'folders':darr,'original':files};

    return arr

def run():
    from os import mkdir,chdir,symlink,getcwd
    
    from argsHandle import getArgs

    args = getArgs(["dir","--out"])
    
    paths = getPaths(args)
    
    build("links")
    chdir("links")

    for dir in paths["folders"]:
        mkdir(dir)

    #for file in paths["files"]:
    #    symlink(file)

run()
