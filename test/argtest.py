import sys

sys.path.append("../functions")

from argsHandle import *

args = getArgs(["name","--lastname","--age"])

name = args.name
lastname = args.lastname
age = args.age

if(lastname == None):
    lastname = ""

if(age == None):
    age = ""


print("name:"+name+"\nlastname:"+lastname+"\nage:"+age)
