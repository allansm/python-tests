def indent():
    return "    "

def getter(line):
    tmp = line.split()
    tmp[2] = tmp[2].replace(";","")

    generated = indent()+"public "+tmp[1]+" get"+tmp[2].capitalize()+"(){\n"+indent()+indent()+"return this."+tmp[2]+";\n"+indent()+"}"
    return generated

def setter(line):
    tmp = line.split()
    tmp[2] = tmp[2].replace(";","")
    generated = indent()+"public void set"+tmp[2].capitalize()+"("+tmp[1]+" "+tmp[2]+"){\n"+indent()+indent()+"this."+tmp[2]+" = "+tmp[2]+";\n"+indent()+"}"
    return generated

print(getter("public String name;"))
print(setter("public String name;"))

