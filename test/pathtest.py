import sys

sys.path.append("../functions")

from fileHandle import *

paths = getAllPaths(input("path:"))

for path in paths:
    print(path)
