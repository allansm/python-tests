from ftplib import FTP
from getpass import getpass
from os import system

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
        elif(">" in command):
            tmp = command.split(">")
            f = open(tmp[0].strip(), "rb")
            ftp.storbinary("STOR "+(tmp[1].strip()), f)
            f.close()
        elif("<" in command):
            tmp = command.split("<")
            f = open(tmp[0].strip(), "wb")
            ftp.retrbinary("RETR "+(tmp[1].strip()), f.write)
            f.close()
        elif("mkdir" in command):
            ftp.mkd(command.replace("mkdir ", ""))
        elif("delete" in command):
            ftp.delete(command.replace("delete ", ""))
        elif("rmdir" in command):
            ftp.rmd(command.replace("rmdir ", ""))
        elif("system" in command):
            system(command.replace("system ", ""))
        else:
            ftp.retrbinary("RETR "+command, lambda x: print(x.decode()))
    except:
        pass

ftp.quit()
