from os import chdir
from os import system

import sys

sys.path.append("modules/pillow-8.2.0/src/pil")
sys.path.append("modules/pillow-8.2.0/src")

from PIL import ImageGrab

chdir("modules/pillow-8.2.0/src/pil")

filepath = 'my_image.png'

screenshot = ImageGrab.grab()
screenshot.save(filepath, 'PNG')  

