import sys
from allansm.argsHandle import *

args = getArgs(["text","--delimiter"])

text = ""
for n in sys.stdin:
    text+=n

delimiter = args.delimiter
if(args.delimiter == None):
    delimiter = "\n"

for n in text.split(delimiter):
    if(args.text in n):
        print(n)
