import sys
sys.path.append("../functions")

from fileHandle import *
from re import search
from os import system

# https://www.youtube.com/watch?v=5abamRO41fE&list=PLS7pGaPiTpwVSx00hLo-3OW9LPrcQjjnf&index=2&ab_channel=Slipknot
# https://www.youtube.com/playlist?list=

remove("persistence.txt")

link = input("playlist link:")
result = search('list=(.*)&', link)
list = result.group(1).split("&")[0]
list = "https://www.youtube.com/playlist?list="+list
print(list)

system("youtube-dl --get-id "+list+" > persistence.txt")

lines = getLines("persistence.txt")
del lines[-1]

remove("persistence.txt")
createFile("persistence.txt")

for line in lines:
    line = "https://www.youtube.com/watch?v="+line+"\n"
    writeFile("persistence.txt",line)

system("youtube-dl -x --audio-format mp3 -a persistence.txt")
remove("persistence.txt")
