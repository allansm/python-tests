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
            print(message)
            messages.append(message)
    else:
        print(message)
        messages.append(message)

    html = http()
    
    html+="<style>"
    html+="*{padding:0px;margin:0px;}"
    html+="</style>"
    
    html+="<div style='margin:1%;padding:1%;width:96%;height:80%;border:1px dashed black;overflow:auto'>"
    for n in messages:
        n = n.replace("+"," ")
        html+="<div display='block'>"+n+"</div>"
    html+="</div>"
    
    html+="<div style='margin:1%;pading:1%;width:96%;height:11%'>"
    html+= "<form method='GET' action='./'><input style='width:75px' type='text' name='user' value='"+users[ip]+"'>&nbsp;&nbsp;<input type='text' name='message'>&nbsp;&nbsp;<input type='submit' value='send'></form>"
    html+="</div>"

    send(s,html)

users = {}
messages = []
while(True):
    server(54321, action)

