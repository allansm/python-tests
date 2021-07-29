import sys
sys.path.append("../functions")

from util import *

def getApi():
    return "https://api.mangadex.org/"

def search(title):
    return getJson(getApi()+"manga?title="+title)

def getFeed(id):
    return getJson(getApi()+"manga/"+id+"/feed")

def getIds(mangas):
    ids = []
    for result in mangas["results"]: 
        ids.append(result["data"]["id"])

    return ids

def getTitles(mangas):
    titles = []
    for result in mangas["results"]:
        title = result["data"]["attributes"]["title"]
        titles.append(title["en"])

    return titles


mangas = search(input("title:"))
titles = getTitles(mangas)
ids = getIds(mangas)

#print(getTitles(mangas))

