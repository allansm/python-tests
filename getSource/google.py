from allansm.downloader import getSource
from allansm.argsHandle import *

code = getSource("https://www.google.com/search?q="+getArgs(["q"]).q)
code = code.replace("\n","")

arr = []

for n in code.split("<a "):
    if("href" in n and "/url?" in n):
        for x in n.split("<div "):
            x = x.replace("\"","\n")
            x = x.replace("'","\n")
            x = x.replace("<","\n")
            x = x.replace(">","\n")
            
            islink = False
            isText = False
            
            data = x.split("\n")

            if(data[0] == "href="):
                islink = True
            if(islink):
                arr.append(data[1])
            else:
                for y in x.split("\n"):
                    if("/h3" in y):
                        isText = True
                if(isText):
                    arr.append(data[3])

data = {"title":"","links":[]}
full = []

for n in arr:
    if(not "wiki" in n.lower()):
        if(not "url?" in n):
            data["title"] = n
            full.append(data)
            data = {"title":"","links":[]}
        else:
            data["links"].append(n.replace("/url?q=",""))

for n in full:
    if(len(n["links"]) > 0):
        print(n["title"])
        for x in n["links"]:
            print(x)
        print("")

