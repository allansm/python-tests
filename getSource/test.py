import sys
sys.path.append("../../python-lib")

from downloader import getSource
from argsHandle import *

txt = getSource(getArgs(["page"]).page)

txt.replace("'","\"")

arr = []
for n in txt.split("\""):
    #if(not "{" in n and not ";" in n and not "(" in n and not "<" in n):
    print(n+"\n")
