from PIL import ImageGrab

def capture(fn):
    ext = fn.split(".")[-1]
    screenshot = ImageGrab.grab()
    screenshot.save(fn, ext)

def screenshot(bbox = None):
    return ImageGrab.grab(bbox)
