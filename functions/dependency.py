#put this on main project folder
def include(path):
    import sys
    import os
    from os.path import dirname,realpath
    from glob import glob
    
    tmp = os.getcwd()
    os.chdir(dirname(realpath(__file__)))

    anyFile = glob(path+"/*")[0]
    path = dirname(realpath(anyFile))

    sys.path.append(path)

    os.chdir(tmp)

'''
def include(path,dependency,relocate=None):
    import os
    import sys
    from os.path import dirname,realpath

    tmp = os.getcwd()
    os.chdir(dirname(realpath(__file__)))

    if(relocate != None):
        os.chdir(relocate)

    sys.path.append(path)
    dependency()
    os.chdir(tmp)
'''
