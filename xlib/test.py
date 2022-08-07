from Xlib import display, X
from PIL import Image

display = display.Display()
root = display.screen().root

capture = root.get_image(0, 0, 800, 600, X.ZPixmap, 0xffffffff)

image = Image.frombytes("RGB", (800, 600), capture.data, "raw", "BGRX")
image.show()

display.close()
