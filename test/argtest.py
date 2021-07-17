'''
import argparse

parser = argparse.ArgumentParser()
   
parser.add_argument('name')

parser.add_argument('--lastname', required=False)

parser.add_argument('age')

args = parser.parse_args()
'''

import sys

sys.path.append("../functions")

from argsHandle import *

args = getArgsTest(["name","--lastname","--age"])

name = args.name
lastname = args.lastname
age = args.age

if(lastname == None):
    lastname = ""

if(age == None):
    age = ""


print("name:"+name+"\nlastname:"+lastname+"\nage:"+age)
