import sys
sys.path.append("../../python-lib")

from allansm.socketHandle import *
from allansm.file import *
from allansm.argsHandle import *


fn = getArgs(["fn"]).fn

def run(s):
    data = receive(s)
    tmp = File(fn)
    send(s,http("","*"))
    send(s,tmp.bytes())

while(True):
    server(54321,run)
