import sys
sys.path.append("../../python-lib")

from imageHandle import *
from fileHandle import *
from elapse import *
from os import chdir,mkdir,getcwd
import socketHandle as sh
from time import sleep

def action(s):
    data = sh.receive(s)
    flag = True
    
    e = Elapse()
    i = 0

    while(True):
        html = "<img id='ItemPreview' src='' style='width:640px;height:480px'>"
        
        if(flag):
            html = sh.http(html)
            flag = False
        
        b = bytes(screenshot(),"jpeg",33)
        html += "<script>"
        html += 'document.getElementById("ItemPreview").src = "data:image/jpg;base64,"+"' 
        sh.send(s,html)
        s.sendall(b64(b))
        html = '";</script>'
        
        sh.send(s,html)
        html = ""
         
        sleep(0.0165)
        
        sh.send(s,"<script>document.write('');</script>")
          
        if(e.elapsed() > 1000):
            print("fps:"+str(i))
            e = Elapse()
            i=0
        else:
            i+=1

sh.server(12345,action)#,"127.0.0.1")
