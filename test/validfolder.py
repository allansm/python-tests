import re
from os import mkdir

removeSimbol = lambda txt : re.sub(r'[^\w]', '', txt)

fold = "!@#%&(()_+f$o¨l*d(e)r?$¨7*(!@#!@!#$!¨&()_+_"

fold = removeSimbol(fold)

mkdir(fold)
print("all ok")
