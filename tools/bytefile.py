import sys
sys.path.append("../../python-lib")

from fileHandle import readBytes
from argsHandle import *

print(readBytes(getArgs(["file"]).file))
