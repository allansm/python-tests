def getAllFilesIgnoring(path,ignore=""):
    from glob import glob as ls
    from os.path import isdir

    def filter(path,ignore):
        if(";" in ignore):
            arr = ignore.split(";")
            
            for n in arr:
                if(n in path.lower()):
                    return True
        else:
            if(ignore in path.lower()):
                return True

        return False

    def fun(path,ignore=""):
        root = ls(path+"/*")
        files = []
        dirs = []
        flag = False
        for f in root:
            f = f.replace("\\","/")
            if(isdir(f)):
                if(not filter(f,ignore) or ignore == ""):
                    dirs.append(f)
                    #print(f)
                    flag = True
            else:
                 if(not filter(f,ignore) or ignore == ""):
                    files.append(f)
        
        hidden = ls(path+"/.*")
        for f in hidden:
            f = f.replace("\\","/")
            if(isdir(f)):
                 if(not filter(f,ignore) or ignore == ""):
                    dirs.append(f)
                    #print(f)
                    flag = True
            else:
                 if(not filter(f,ignore) or ignore == ""):
                    files.append(f)
        return [files,dirs,flag]


    def fun2(res,ignore=""):
        files = res[0]
        if(res[2]):
            #print("run")
            for d in res[1]:
                res2 = fun(d,ignore)

                files = files+fun2(res2,ignore)
            
            return files
        else:
            return files


    res = fun(path,ignore)
    files = fun2(res,ignore)

    return files

files = getAllFilesIgnoring("../../",".git;unity;eclipse;__pycache")

for f in files:
    if("." in f):
        if("py" in f.split(".")[-1]):
            print(f)
