from subprocess import check_output

out = check_output("df -h | awk '{print $1\" \"$5}'", shell=True).decode()
lines = out.split("\n")

del lines[0]

for n in lines:
    try:
        data = n.split(" ")
        path = data[0]
        if(path != "tmpfs"):
            percent = float(data[1].replace("%", ""))
            diff = 15 - len(path)

            print(path, end=" "*diff)
            print("█"*round(percent/5), end="")
            print("░"*round((100-percent)/5),end="")
            print(" "+str(percent)+"%\n")
    except:
        pass
