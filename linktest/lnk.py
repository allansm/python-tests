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

def getPaths(p):
    from os import chdir,getcwd
    from fileHandle import getAllFilesPath,getFileName,dirname
    
    files = getAllFilesPath(p)
    
    tmp = getcwd()
    
    chdir(p)
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
            darr.append(dirname(dpath))

    
    arr = []

    arr.append(farr)
    arr.append(darr)
    arr.append(files)

    return arr


def build(paths,isTest=False,remake=True): 
    from os import chdir
    from os import makedirs as mkdir
    
    if(not isTest):
        if(remake):
            rebuild("links")

        chdir("links")
    
    for dir in paths[1]:
        print(dir)
        if(not isTest):
            try:
                mkdir(dir)
            except:
                dummy=""


