import sys
from subprocess import call

sys.path.append("F:\\A place for tests\\x")

sys.path.append("F:\\A place for tests\\y")

call("y.bat",shell=True)
