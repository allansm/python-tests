from allansm.socketHandle import *

def totext(text):
    from base64 import b16decode

    hex = []
    
    i = 0
    for n in text:
        if(n == "%"):
            hex.append(text[i+1]+text[i+2])
        i+=1
    
    for n in hex:
        text = text.replace("%"+n,b16decode(n).decode())

    return text

def action(s):
    from time import sleep

    global users
    global messages
    
    sleep(1)

    ip = s.getpeername()[0]
    
    users[ip] = "nameless"
    message = ""
    
    recv = receive(s)
    
    try:
        url = recv.split(" ")[1]
    except:
        url = ""
    
    if("message=" in url):
        users[ip] = url.split("user=")[1].split("&")[0]
        message = url.split("message=")[1]

    message = message.replace("\n","").replace("\r","")
    
    try:
        users[ip] = totext(users[ip]).replace("+"," ")
        message = users[ip]+": "+totext(message)
    except:
        error=0
    
    if(len(messages) > 0):
        if(message != messages[-1]):
            msg = message
            if("<img" in msg):
                u = msg.split(":")[0]
                msg = u+":"+msg.split("src='")[1].split("'")[0]
            elif("<a" in msg):
                u = msg.split(":")[0]
                msg = u+":"+msg.split("href='")[1].split("'")[0]
            
            print(msg)
            
            messages.append(message)
    else:
        msg = message
        if("<img" in msg):
            u = msg.split(":")[0]
            msg = u+":"+msg.split("src='")[1].split("'")[0]
        elif("<a" in msg):
                u = msg.split(":")[0]
                msg = u+":"+msg.split("href='")[1].split("'")[0]
        
        print(msg)
            
        messages.append(message)

    html = http()
    
    html+="<style>"
    html+="*{padding:0px;margin:0px;color:#0f0}"
    html+="input{padding:10px;background:#111;color:#0f0;border:none}"
    html+="input:focus{border:none;outline:none}"
    html+="body{background:#000}"
    html+="</style>"
    
    html+="<script>"
    html+="function image(){message = document.getElementById('message').value;document.getElementById('message').value = \"<a href='\"+message+\"'><img src='\"+message+\"' width='100%' height='300'></a>\";document.getElementById('send').click();}"
    html+="function link(){message = document.getElementById('message').value;document.getElementById('message').value = \"<a href='\"+message+\"'>\"+message+\"</a>\";document.getElementById('send').click();}"
    html+="</script>"
    
    html+="<div style='margin:1%;padding:1%;width:96%;height:80%;overflow:auto'>"
    for n in messages:
        n = n.replace("+"," ")
        html+="<div display='block'>"+n+"</div>"
    html+="</div>"
    
    html+="<div style='margin:1%;pading:1%;width:96%;height:11%'>"
    html+="<form method='GET' action='./'><input placeholder='username' style='width:75px' type='text' name='user' value='"+users[ip]+"'>&nbsp;&nbsp;<input placeholder='message' type='text' style='width:50%' id='message' name='message' autofocus>&nbsp;&nbsp;<input id='send' type='submit' value='send'>&nbsp;&nbsp;<input type='button' onclick='image()' value='image'>&nbsp;&nbsp;<input type='button' onclick='link()' value='link'></form>"
    html+="</div>"

    send(s,html)

users = {}
messages = []
while(True):
    server(54321, action)

