import logging
import threading
import time
import os

def thread_function(name):
    os.system("notepad")
    
x = threading.Thread(target=thread_function, args=(1,))
x.start()