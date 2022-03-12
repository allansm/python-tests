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
    global users
    global messages
    
    ip = s.getpeername()[0]
    
    try:
        if(users[ip] == None):
            users[ip] = ""
    except:
        users[ip] = ""
    
    message = ""
    
    recv = receive(s)
    
    page = recv.split(" ")[1]
    
    if(page != "/messages"):
        flag = False
        try:
            url = recv.split(" ")[1]
        except:
            url = ""
        
        if("message=" in url):
            flag = True
            users[ip] = url.split("user=")[1].split("&")[0]
            message = url.split("message=")[1]

        message = message.replace("\n","").replace("\r","")
        output = totext(message)

        if(message != ""):
            try:
                users[ip] = totext(users[ip]).replace("+"," ")
                message = "<div style='float:left'>"+users[ip]+":</div> "+"<div>"+totext(message)+"</div>"
            except:
                error=0
            
            if(len(messages) > 0):
                if(message != messages[-1]):
                    print(users[ip]+":"+output)
                    
                    messages.append(message)
            else:
                print(users[ip]+":"+output)
                    
                messages.append(message)

        html = http()
        
        html+="<style>"
        html+="*{padding:0px;margin:0px;color:#0f0}"
        html+="input{padding:10px;background:#000;color:#0f0;border:1px solid #111}"
        html+="input:focus{border:none;outline:none}"
        html+="body{background:#000}"
        html+="</style>"
        
        html+="<div id='messages' style='margin:1%;padding:1%;width:96%;height:79%;overflow:auto;background:#000;border:1px solid #111'>"
        for n in messages:
            n = n.replace("+"," ")
            html+="<div display='block'>"+n+"</div><br/>"
        html+="</div>"
        
        html+="<div style='margin:1%;pading:1%;width:96%;height:11%'>"
        html+="<form method='GET' action='./'><input required placeholder='username' style='width:75px' type='text' name='user' value='"+users[ip]+"'>&nbsp;&nbsp;<input required placeholder='message' type='text' style='width:30%' id='message' name='message' autofocus>&nbsp;&nbsp;<input style='visibility:hidden' id='send' type='submit' value='send'>&nbsp;&nbsp;<input type='button' onclick='image()' value='image'>&nbsp;&nbsp;<input type='button' onclick='link()' value='link'>&nbsp;&nbsp;<input type='button' onclick='video()' value='mp4'>&nbsp;&nbsp;<input type='button' onclick='yt()' value='youtube'>&nbsp;&nbsp;<input type='button' onclick='update()' value='refresh'></form>"
        html+="</div>"
        
        html+="<script>"
        html+="var last='';"
        html+="function image(){message = document.getElementById('message').value;document.getElementById('message').value = \"<br/><a href='\"+message+\"'><img style='max-width:100%' src='\"+message+\"'></a>\";document.getElementById('send').click();}"
        html+="function link(){message = document.getElementById('message').value;document.getElementById('message').value = \"<a href='\"+message+\"'>\"+message+\"</a>\";document.getElementById('send').click();}"
        html+="function video(){message = document.getElementById('message').value;document.getElementById('message').value = \"<br/><video controls style='max-width:100%'><source src='\"+message+\"' type='video/mp4'></video>\";document.getElementById('send').click();}"
        html+="function yt(){message = document.getElementById('message').value;message = message.split('v=')[1];if(message.includes('&')){message = message.split('&')[0];}message = 'https://www.youtube.com/embed/'+message;document.getElementById('message').value = \"<br/><iframe width='560' height='315' src='\"+message+\"' title='YouTube video player' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>\";document.getElementById('send').click();}"
        html+="function ajax(method,url,run){var xhttp = new XMLHttpRequest();xhttp.onreadystatechange = function(){run(this.responseText);};xhttp.open(method, url, true);xhttp.send();}"
        html+="function refresh(response){if(response != last && response != ''){document.getElementById('messages').innerHTML = response;last=response;}console.log(response);}"
        html+="function update(){ajax('GET', '/messages', refresh);}"
        html+="setInterval(function(){ajax('GET', '/messages', refresh);}, 3000);"
        if(flag):
            html+="window.location.replace('/');"
        html+="</script>"
    
    else:
        html = http()

        for n in messages:
            n = n.replace("+"," ")
            html+="<div display='block'>"+n+"</div><br/>"
    
    send(s,html)

users = {}
messages = []
while(True):
    server(54321, action, 10)

