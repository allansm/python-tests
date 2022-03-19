from allansm.progressbar import *
from allansm.util import clear
from urllib import request

def test(n, size ,total):
    clear()
    print(ProgressBar(total).progress(n*size))

request.urlretrieve("http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4","dummy",test)
