from proc import *

out = getOutput()
proc = getProcess(out)
mem = getMemory(out)

rr = lambda array: list(dict.fromkeys(array))

test = {}

for n in range(0,len(proc)):
    try:
        if(test[proc[n]] == None):
            test[proc[n]] = 0
    except:
        test[proc[n]] = 0

    test[proc[n]]+= float(mem[n])

print("------------------------------------")
print("process                       mb")
print("------------------------------------")

for n in rr(proc):
    size = len(n)
    space = ""
    if(size < 30):
        for x in range(1,30-size):
            space+=" "

    print(n+space+" "+str(round(test[n]/1024)))

print("------------------------------------")
