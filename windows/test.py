from subprocess import check_output

output = check_output("tasklist",shell=True)

list = str(output).split("\\r\\n")

for item in list:
    if(item != "" and " K" in item):
        array = item.split(" ")

        array = [i for i in array if i]
        
        exe = array[0]
        pid = array[1]
        memory = array[4].replace(".","")

        print(exe+ " "+memory)
