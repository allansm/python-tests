#import sys

#sys.path.append("../functions")

#from argsHandle import *

import json
from urllib.request import urlopen

def getJson(url):
    response = urlopen(url)
    data = json.loads(response.read().decode())

    return data

url = input("url:") #getArgs(["url"]).url
data = getJson(url)

print(data)
print()    
