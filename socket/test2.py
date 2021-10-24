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

#while True:
#    server('127.0.0.1',65432,action1)

while True:
    server('127.0.0.1',8080,action2)
