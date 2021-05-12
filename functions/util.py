from random import shuffle
import platform

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

def fakeshuffle(arr):
    h1,h2 = split_list(arr)

    a,b = split_list(h1)
    c,d = split_list(h2)

    shuffle(a)
    shuffle(a)
    shuffle(a)
    shuffle(a)

    shuffle(b)
    shuffle(b)
    shuffle(b)

    shuffle(c)
    shuffle(c)
    shuffle(c)

    shuffle(d)
    shuffle(d)
    shuffle(d)
    shuffle(d)

    arr = a+b+c+d

    return arr

def isWindows():
    if(platform.system() == "Windows"):
        return True
    
    return false
