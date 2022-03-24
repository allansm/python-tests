from allansm.downloader import *
from allansm.argsHandle import *

def _not(arr, text):
	for n in arr:
		if(n in text):
			return False
	return True

def _has(arr, text):
	return not _not(arr, text)

src = getSource(getArgs(["url"]).url)
src = src.replace("'","\"")

for n in src.split("\""):
	if(_not(["(", "[", "<", ";", ","], n)):
		if(_has(["http", "/"], n)):
			print(n)
