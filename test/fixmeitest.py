import sys
sys.path.append("../functions")

from fileHandle import selfFileLocation
import os

#os.chdir(fileHandle.getTemp())
tmp = selfFileLocation

print(tmp(__file__))

