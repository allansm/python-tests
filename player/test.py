from dependency import *

include("../../python-lib")

class Playlist:
    __index = 0
    __paths = None
    __size = 0
    end = False

    def __init__(self,dir):
        from fileHandle import getAllFilesPath as files
        from random import shuffle
        
        self.dir = dir
        self.__paths = files(dir)
        shuffle(self.__paths)
        self.__size = len(self.__paths)
    
    def next(self):
        i = self.__index
        
        if(i < self.__size-1):
            self.__index+=1
        else:
            self.end = True

        return self.__paths[i]

def Playlists(file):
    from fileHandle import getLines
    from random import shuffle

    playlists = []

    for line in getLines(file):
        playlists.append(Playlist(line))

    shuffle(playlists)
    
    return playlists

def run():
    from ff import playSound as ffplay
    from fileHandle import isdir
    from argsHandle import getArgs

    from util import toast

    args = getArgs(["files"])

    if(not isdir(args.files)):
        playlists = Playlists(args.files)

        end = False
        while(not end):
            for playlist in playlists:
                print(playlist.dir)
                ffplay(playlist.next())
                
                end = playlist.end
    else:
        playlist = Playlist(args.files)

        while(not playlist.end):
            ffplay(playlist.next())

run()
