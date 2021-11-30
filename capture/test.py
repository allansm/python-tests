import sys
sys.path.append("../../python-lib")

from imageHandle import *
from fileHandle import *
from elapse import *
from os import chdir,mkdir,getcwd
import socketHandle as sh

#chdir(getTemp())

#remove("capturetest")
#mkdir("capturetest")
#chdir("capturetest")

print(getcwd())

def action(s):
    import base64
    data = sh.receive(s)
    b = bytes(screenshot(),"png")
    html = "<img id='ItemPreview' src=''>"
    html += "<script>"
    html += 'document.getElementById("ItemPreview").src = "data:image/png;base64,"+"'
    html = sh.http(html)
    sh.send(s,html)
    s.sendall(base64.b64encode(b))
    html = '";</script>'
    sh.send(s,html)

sh.server(12345,action)

'''
i=0
count = 0
e = Elapse()
while(True):
    if(e.elapsed() > 60000):
        print(count/60)
        count = 0
        e = Elapse()

    fn = str(i)#'{:0>3}'.format(i)
    ss = screenshot()
    ss.save(fn+".jpg",quality=33)
    i+=1
    count+=1
'''
