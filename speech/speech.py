from allansm.file import *

from gtts import gTTS
from playsound import playsound
import os

out = gTTS(text=File("speech.py").read(), lang="en", slow=False)

out.save(".mp3")

playsound(".mp3")

os.remove(".mp3")
