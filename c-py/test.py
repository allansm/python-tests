from ctypes import *

def getInt(lib,var):
    return c_int.in_dll(lib,var).value

test = CDLL("./libtest.so")

x = getInt(test,"x")
y = getInt(test,"y")

hello = test.hello

hello()

print(x+y)
