import socket
s=socket.socket()
host=socket.gethostbyname('www.google.com')
port=80
s.connect((host,port))
s.sendall(b"GET /\r\n")
val = s.recv(10000)

val = val.decode().split('\r\n\r\n',1)[1]
s.close()
print(val)
