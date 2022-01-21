import sys
sys.path.append("../../python-lib")

from allansm.socketHandle import *
from allansm.fileHandle import remove
from allansm.downloader import *
from allansm.zip import unzip

download("http://127.0.0.1:54321","tmp.zip")

unzip("tmp.zip","tmp")

remove("tmp.zip")

input("")

remove("tmp")
