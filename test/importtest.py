import sys

def test(path):
    sys.path.append(path)


test("../functions")

from util import *

if(isWindows()):
    print("works")
