import sys
sys.path.append("../../python-lib")

from imageHandle import *
from fileHandle import *
from elapse import *
from os import chdir,mkdir,getcwd
import socketHandle as sh

def action(s):
    data = sh.receive(s)
    flag = True
    
    while(True):
        html = "<img id='ItemPreview' src=''>"
        
        if(flag):
            html = sh.http(html)
            flag = False
        
        b = bytes(screenshot(),"jpeg",10)
        html += "<script>"
        html += 'document.getElementById("ItemPreview").src = "data:image/jpg;base64,"+"' 
        sh.send(s,html)
        s.sendall(b64(b))
        html = '";</script>'
        
        sh.send(s,html)
        html = ""
        
        from time import sleep
        sleep(0.0165)
        
        sh.send(s,"<script>document.write('');</script>")

sh.server(12345,action)
