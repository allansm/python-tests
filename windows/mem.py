from proc import *
from allansm.argsHandle import *

args = getArgs(["--exe"])

out = getOutput()
proc = getProcess(out)
mem = getMemory(out)

rr = lambda array: list(dict.fromkeys(array))

program = {}

for n in range(0,len(proc)):
    try:
        if(program[proc[n]] == None):
            program[proc[n]] = 0
    except:
        program[proc[n]] = 0

    program[proc[n]]+= float(mem[n])

print("------------------------------------")
print("process                       mb")
print("------------------------------------")

h = {}
h["mem"] = 0
for n in rr(proc):
    if(program[n] > h["mem"]):
        h["name"] = n
        h["mem"] = program[n]

order = []
order.append(h["name"])

while(len(order) < len(rr(proc))):
    tmp = {}
    tmp["name"] = None
    tmp["mem"] = 0

    for n in rr(proc):
        if(program[n] < h["mem"] and program[n] > tmp["mem"]):
           tmp["name"] = n
           tmp["mem"] = program[n]
    
    order.append(tmp["name"])
    
    h = tmp

for n in order:
    try:
        if(args.exe != None):
            size = len(n)
            space = ""
            if(size < 30):
                for x in range(1,30-size):
                    space+=" "

            if(args.exe+".exe" == n.strip()):
                print(n+space+" "+str(round(program[n]/1024)))
        else:
            size = len(n)
            space = ""
            if(size < 30):
                for x in range(1,30-size):
                    space+=" "

            print(n+space+" "+str(round(program[n]/1024)))
    except:
        dummy=0

print("------------------------------------")
