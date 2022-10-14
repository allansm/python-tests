import socket
    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("127.0.0.1",80))
    
    s.listen(1)
    conn, addr = s.accept()
    
    with conn:
        recv = conn.recv(1024)
        
        conn.sendall(b"HTTP/1.1 301 Moved Permanently\nLocation: https://www.google.com\r\n")
