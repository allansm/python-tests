import socket

def getIp():
    return socket.gethostbyname(socket.gethostname())

def server(port,action):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((getIp(),port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            action(conn)

def client(host,port,action):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        action(s)

def http(html):
    header = "HTTP/1.1 200 OK"
    header+="\nContent-Type: text/html;charset=utf-8"
    header+="\n\n"
        
    return header+html
