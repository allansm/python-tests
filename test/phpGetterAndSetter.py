def indent():
    return "    "

def getter(line):
    tmp = line.split()
    tmp[1] = tmp[1].replace(";","")

    generated = indent()+"public function get"+tmp[1].replace("$","").capitalize()+"(){\n"+indent()+indent()+"return $this->"+tmp[1].replace("$","")+";\n"+indent()+"}"
    
    return generated

def setter(line):
    tmp = line.split()
    tmp[1] = tmp[1].replace(";","")

    generated = indent()+"public function set"+tmp[1].replace("$","").capitalize()+"("+tmp[1]+"){\n"+indent()+indent()+"$this->"+tmp[1].replace("$","")+" = "+tmp[1]+";\n"+indent()+"}"
    
    return generated

print(getter("public $name;"))
print(setter("public $name;"))
