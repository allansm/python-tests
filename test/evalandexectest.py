import sys
sys.path.append("../../python-lib")
from fileHandle import *
'''
x = eval("2*5+2")

print(x)

exec("def hello(): print('helloworld')")

hello()

exec("x = eval('2*2')")

print(x+1)

exec("def t():\n\treturn 1\ndef t2():\n\treturn 2")

print(t())

print(t2())
'''
exec(readFile("justtest.py"))

a()
b()
