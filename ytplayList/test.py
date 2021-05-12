from os import system
from subprocess import call
import sys
sys.path.append("../functions")
from os import chdir

from fileHandle import *
from util import *

notifu = selfLocation(__file__)+"\\bin\\notifu"

print(notifu)

chdir(getTemp())

if(isWindows()):
    call("start \"\" \""+notifu+"\" /m \"test\" /p \"test\"",shell=True)
