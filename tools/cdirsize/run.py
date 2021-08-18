import os
from os.path import dirname

tmp = os.getcwd()

os.chdir(dirname(__file__))
os.chdir("..")

from cdirSize import getSize

os.chdir(tmp)

getSize()
