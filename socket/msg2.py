from allansm.socketHandle import *

def action(s):
    global messages
    
    message = ""
    recv = receive(s)
    url = recv.split(" ")[1]
    
    if("?message=" in url):
        message = url.split("?message=")[1]

    message = message.replace("\n","").replace("\r","")
    
    if(len(messages) > 0):
        if(message != messages[-1]):
            print(message)
            messages.append(message)
    else:
        print(message)
        messages.append(message)

    html = http()
    html+= "<form method='GET' action='./'><input type='text' name='message'><input type='submit' value='send'></form>"
    html+= "<br/>"
    
    for n in messages:
        n = n.replace("+"," ")
        html+=n+"<br/>"

    send(s,html)

messages = []
while(True):
    server(54321, action)

