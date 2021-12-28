import sys

i=1
for n in sys.stdin:
    print(str(i)+" : "+n.replace("\n",""))
    i+=1
