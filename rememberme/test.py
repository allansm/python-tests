import fileHandle
import datetime
import datetime

now = datetime.datetime.now()
now = str(now)
date = now.split(" ")[0]
time = now.split(" ")[1].split(".")[0]
print(date)
print(time)
print("thing to register:")
register = input()

#fileHandle.createFile(date)
fileHandle.writeFile(date,time+":"+register)

