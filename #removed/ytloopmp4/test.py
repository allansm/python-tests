import sys

sys.path.append("../functions")

from yt import *
from fileHandle import *
from subprocess import call
from os import chdir
from os import mkdir


link = input("link:")

chdir(getTemp())
try:
    mkdir("ytloopmp4")
    
except:
    print("folder exists.")

chdir("ytloopmp4")

while(True):
    call("youtube-dl --get-url "+link+" > url",shell="true")

    url = getLines("url")[0]

    call("ffplay -an -x 300 -y 170 -noborder -alwaysontop -top 28 -left 1000 -loglevel 0 "+url,shell=True)
