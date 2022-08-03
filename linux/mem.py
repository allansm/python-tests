from subprocess import check_output

command = "ps -e -o %c, -o %p, -o %C, -o %mem"

out = check_output(command, shell=True).decode()

data = []

for n in out.split("\n"):
    tmp = n.split(",")
    if(len(tmp) > 1):
        program = tmp[0].strip()
        pid = tmp[1].strip()
        cpu = tmp[2].strip()
        ram = tmp[3].strip()
        command = ""
        try:
            command = tmp[4].strip()
        except:
            pass
        data.append({"program":program, "pid":pid, "cpu":cpu, "ram":ram, "command":command})

ram = {}

ram["total in use"] = 0.0

for n in data:
    ram[n["program"]] = 0.0

for n in data:
    try:
        ram[n["program"]]+=float(n["ram"])
        ram["total in use"]+=float(n["ram"])
    except Exception as e:
        pass

for n in ram:
    percent = ram[n]
    if(percent > 0):
        print(n, end=" ")
        print(" "*(20-len(n)), end="")
        current = 0
        x = 0
        while(current < percent):
            if(x == 5):
                print("█", end='')
                x=0

            current+=1
            x+=1
        
        x = 0
        while(current <= 100):
            if(x == 5):
                print("░", end='')
                x=0

            current+=1
            x+=1
         
        print(" "+("{:.3}".format(ram[n]))+"%\n")
        
