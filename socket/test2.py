import socket

def server(host,port,action):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host,port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            action(conn)

def action1(conn):
    from os import system

    data = conn.recv(1024).decode('utf-8')
    system(data)

def action2(conn): 
    data = conn.recv(1024).decode('utf-8')
    
    if(not data or data == ""):
        dummy = ""
    else:
        header = "HTTP/1.1 200 OK"
        header+="\nContent-Type: text/html;charset=utf-8"
        header+="\n\n"
        
        print(data)

        html = "" 
        
        if("/ " in data):
            html = "o.O"
        elif("/hello" in data):
            html = "helloworld"

        response = header+html

        conn.sendall(response.encode('utf-8'))
        print("send")

def action3(sock):
    from subprocess import check_output as check
    data = sock.recv(1024).decode('utf-8')

    if(not data or data == ""):
        dummy = ""
    else:
        header = "HTTP/1.1 200 OK"
        header+="\nContent-Type: text/html;charset=utf-8"
        header+="\n\n"
        
        print(data)

        html = "u.u"

        if("?test=" in data):
            html = check("dir",shell=True).decode("utf-8").replace("\r\n","<br>")

        response = header+html
        
        sock.sendall(response.encode("utf-8"))

#while True:
#    server('127.0.0.1',65432,action1)

#while True:
#    server('127.0.0.1',8080,action2)

while True:
    server('127.0.0.1',9191,action3)
