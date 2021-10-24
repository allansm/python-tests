import socket
from os import system

HOST = '127.0.0.1'
PORT = 9999

while(True):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            #while True:
            data = conn.recv(1024)
            #if not data:
             #   break
            
            recv = data.decode('utf-8')

            #system(command)
            print(recv)

            head = "HTTP/1.1 200 OK"
            head+="\nContent-Type: text/html;charset=utf-8"
            #head+="\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0"
            #head+="\nContent-Length: "
            if(not "/" in recv):
                html = "\n\n<!DOCTYPE html><html><head><meta http-equiv='content-type' content='text/html; charset=utf-8' /></head>helloworld<br/><div style='width:50px;height:50px;background:#000'></div></html>"
            elif("/doThat" in recv):
                html = "\n\nworks :D"
            elif("/hello" in recv):
                html = "\n\n>> helloworld <<"
            #head+= str(len(html))
            html = head+html
            
            conn.sendall(html.encode("utf-8"))
