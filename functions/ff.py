#all here require ffplay

from subprocess import call

def playSound(link):
    call("ffplay -nodisp -autoexit -loglevel 0 \""+link+"\"",shell=True)


def playVideo(x,y,top,left,op,link):
     call("ffplay "+op+" -x "+x+" -y "+y+" -top "+top+" -left "+left+" -noborder -framedrop -autoexit -loglevel 0 \""+link+"\"",shell=True)

def playMiniature():
    needcodehere = ""

