from ftplib import FTP
from getpass import getpass

ftp = FTP(input("url:"), getpass("user:"), getpass("pass:"))

while(True):
    command = input(ftp.pwd()+" ")
    
    if(command == "exit"):
        break
    
    try:
        if("cd" in command):
            ftp.cwd(command.split(" ")[-1])
        elif(command == "dir" or command == "ls"):
            ftp.retrlines("LIST")
        elif(command == "pwd"):
            print(ftp.pwd())
        else:
            ftp.retrbinary("RETR "+command, lambda x: print(x.decode()))
    except:
        pass

ftp.quit()
