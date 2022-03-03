class Playlist:
    __index = 0
    __paths = None
    __size = 0
    end = False

    def __init__(self,dir):
        from allansm.fileHandle import getAllFilesPath as files
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
    from allansm.fileHandle import getLines
    from random import shuffle

    playlists = []

    for line in getLines(file):
        playlists.append(Playlist(line))

    shuffle(playlists)
    
    return playlists

def show(path):
    from allansm.util import toast
    
    print("listening:"+path)
    toast(path,"listening:")

def norepeat(path):
    from allansm.fileHandle import getLines

    flag = True
    for n in getLines(".norepeat"):
        if(n == path):
            flag = False

    return flag

def play(args,next):
    from allansm.ff import playSound as ffplay
    from allansm.fileHandle import writeFile

    flag = True
    if(args.norepeat):
        flag = norepeat(next)
    if(flag):
        show(next)
        ffplay(next)

        if(args.norepeat):
            writeFile(".norepeat",next+"\n")
    else:
        print("skip repeat")

def run():
    from allansm.argsHandle import getArgs
    from os import chdir,getcwd
    from allansm.fileHandle import isdir,getTemp,mkdir

    chdir(getTemp())
    mkdir("player")
    chdir("player")
    
    print(getcwd())

    args = getArgs(["files","?norepeat"])

    if(not isdir(args.files)):
        playlists = Playlists(args.files)

        end = False
        while(not end):
            for playlist in playlists:
                print(playlist.dir)
                next = playlist.next()
                play(args,next)
                '''
                flag = True
                if(args.norepeat):
                    flag = norepeat(next)
                if(flag):
                    show(next)
                    ffplay(next)

                    if(args.norepeat):
                        writeFile(".norepeat",next+"\n")
                else:
                    print("skip repeat")
                '''
                end = playlist.end
    else:
        playlist = Playlist(args.files)

        while(not playlist.end):
            next = playlist.next()
            '''
            flag = True
            if(args.norepeat):
                flag = norepeat(next)
            if(flag):
                show(next)
                ffplay(next)
            '''
            play(args,next)
run()
