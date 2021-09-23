import dependency

from fileHandle import *

folders = getAllPaths(input("path:"))
bin = input("binary folder name:")

res = ""

for f in folders:
    if(bin == f.split("\\")[-1]):
        print(f)
        res+=f+";"

print()
print(res)
