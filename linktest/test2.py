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
        elif("\\" in args.dir):
            tok = args.dir.split("\\")[-1]+"\\"
            if(tok in f):
                tmp = f.split(tok)[1]
        else:
            if("/" in f):
                tmp = f.split(args.dir+"/")[1]
            elif("\\" in f):
                tmp = f.split(args.dir+"\\")[1]
            
            if(tmp == "/"):
                tmp.replace("/","")
            elif(tmp == "\\"):
                tmp.replace("\\","")

        fpath = tmp
        dpath = tmp.replace(fn,"")
        
        if(fpath != ""):
            farr.append(fpath)
        if(dpath != ""):
            darr.append(dpath)

    #arr = {'files':farr,'folders':darr,'original':files};
    arr = []

    arr.append(farr)
    arr.append(darr)
    arr.append(files)

    return arr

def run():
    from os import mkdir,chdir,symlink,getcwd
    
    from argsHandle import getArgs

    args = getArgs(["dir","--out","?test"])
    
    paths = getPaths(args)
    
    build("links")
    chdir("links")

    for dir in paths[1]:
        print(dir)
        if(not args.test):
            mkdir(dir)

    i=0
    for file in paths[0]:
        print(file+" "+paths[2][i])
        if(not args.test):
            symlink(paths[2][i],file)
        i = i+1;

run()
