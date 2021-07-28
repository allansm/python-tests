import sys
sys.path.append("../functions")

from util import *

def getApi():
    return "https://api.mangadex.org/"

def search(title):
    return getJson(getApi()+"manga?title="+title)

def getFeed(id):
    return getJson(getApi()+"manga/"+id+"/feed")

def getIds(titles):
    ids = []
    for result in titles["results"]: 
        ids.append(result["data"]["id"])

    return ids

titles = search(input("title:"))

#print(getIds(titles))


for result in titles["results"]: 
    print(result["data"]["attributes"]["title"])
