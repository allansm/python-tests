from allansm.socketHandle import *
from allansm.file import *
from allansm.argsHandle import *

def run(s):
    data = receive(s)
    tmp = File(fn)
    send(s,http("","*"))
    send(s,tmp.bytes())

args = getArgs(["fn", "--port"])

fn = args.fn
port = args.port

if(port == None):
    port=54321
else:
    port=int(port)

while(True):
    server(port,run)
