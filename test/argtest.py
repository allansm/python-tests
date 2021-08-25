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

def test(): 
    parser = argparse.ArgumentParser()

    parser.add_argument("--flag",action="store_true",dest="flag")
    #parser.set_defaults(flag=False)

    args = parser.parse_args()

    print(args.flag)

args = getArgs(["?flag","required","--name","??negative"])

if(args.flag):
    print(args.name)
else:
    print(args.required)

print(args.negative)
