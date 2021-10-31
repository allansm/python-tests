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

def isFree(ip,port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((ip, port))
            return True
        except socket.error as e:
            return False

i=0
while(isFree("127.0.0.1",i)):
    print(i)
    i = i+ 1

print("o.O")
