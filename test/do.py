from os import getcwd
from os import chdir
from os import system

def do(that,inside):
    tmp = getcwd()

    chdir(inside)
    that()
    chdir(tmp)

that = lambda : system("dir")

do(that,"c:/")

