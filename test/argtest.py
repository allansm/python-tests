import sys

sys.path.append("../functions")

from argsHandle import *

def oldTest():
    args = getArgs(["name","--lastname","--age"])

    name = args.name
    lastname = args.lastname
    age = args.age

    if(lastname == None):
        lastname = ""

    if(age == None):
        age = ""


    print("name:"+name+"\nlastname:"+lastname+"\nage:"+age)

# :(
def imposssible():
    args = getArgs(["required"])

    required = args.required


    args = getArgs(["--test","--test2"])

    test = args.test

    test2 = args.test2
