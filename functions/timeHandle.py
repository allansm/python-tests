import datetime

def getDate():
    now = datetime.datetime.now()
    now = str(now)
    date = now.split(" ")[0]
    
    return date

def getTime():
    now = datetime.datetime.now()
    now = str(now)
    time = now.split(" ")[1].split(".")[0]
    
    return time

