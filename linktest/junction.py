#only windows
from os import system

import dependency
from argsHandle import *

args = getArgs(["src","dst"])

system("mklink /J "+args.dst+" "+args.src)
