from subprocess import check_output

def getCpu():
    command = "ps -e -o %c, -o %cpu"

    out = check_output(command, shell=True).decode()
    cpus = check_output("lscpu | egrep 'CPU\(s\)'", shell=True).decode().split("\n")[0].split(" ")[-1]
    cpus = int(cpus)

    data = []

    for n in out.split("\n"):
        tmp = n.split(",")
        if(len(tmp) > 1):
            program = tmp[0].strip()
            cpu = tmp[1].strip()
            if(program != "COMMAND"):
                data.append({"program":program, "cpu":cpu})

    cpu = {}

    cpu["total in use"] = 0.0

    for n in data:
        cpu[n["program"]] = 0.0

    for n in data:
        try:
            cpu[n["program"]]+=float(n["cpu"])/cpus
            cpu["total in use"]+=float(n["cpu"])/cpus
        except Exception as e:
            pass
    
    if(cpu["total in use"] >= 100):
        cpu["total in use"] = 99.9
  
    return cpu

def getRam():
    command = "ps -e -o %c, -o %mem"

    out = check_output(command, shell=True).decode()

    data = []

    for n in out.split("\n"):
        tmp = n.split(",")
        if(len(tmp) > 1):
            program = tmp[0].strip()
            ram = tmp[1].strip()
            if(program != "COMMAND"):
                data.append({"program":program, "ram":ram})

    ram = {}

    ram["total in use"] = 0.0

    for n in data:
        ram[n["program"]] = 0.0
    
    for n in data:
        try:
            ram[n["program"]]+=(float(n["ram"]))
            ram["total in use"]+=(float(n["ram"]))
        except Exception as e:
            pass
    
    magic = check_output("free | grep Mem | awk '{print $3/$2 * 100.0}'", shell=True).decode()
    magic = float(magic.replace("\n", "").replace(",", "."))
    
    magic = (1/magic)*ram["total in use"]
    for n in ram:
        #if(n != "total in use"):
        ram[n] = ram[n]/magic
    
    if(ram["total in use"] >= 100):
        ram["total in use"] = 99.9

    return ram
