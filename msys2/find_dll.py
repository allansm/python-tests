from subprocess import check_output
from shutil import copy
from os.path import realpath
from os import getenv, environ
from os import system

environ["path"] = ""

exec = lambda x: check_output(x,shell=True).decode('utf-8').split("\\r\\n")[0]

msys2 = getenv("msys2")

if(msys2 == "" or msys2 == None):
    raise Exception("please add msys2 environment variable")

msys2 = realpath(msys2)

flag = True
while(flag):
    try:
        while(flag):
            flag = False
            for n in exec(msys2+"\\usr\\bin\\ldd.exe *.exe").split("\n"):
                if("not found" in n.lower()):
                    flag = True
                    
                    dll_name = (n.split(" ")[0].strip())
                    dll = msys2+"\\mingw64\\bin\\"+dll_name
                    
                    print(dll_name+" >> "+dll)
                    
                    copy(dll, dll_name)

            for n in exec(msys2+"\\usr\\bin\\ldd.exe *.dll").split("\n"):
                if("not found" in n.lower()):
                    flag = True
                    
                    dll_name = (n.split(" ")[0].strip())
                    dll = msys2+"\\mingw64\\bin\\"+dll_name
                    
                    print(dll_name+" >> "+dll)
                    
                    copy(dll, dll_name)
    except:
        flag = True

