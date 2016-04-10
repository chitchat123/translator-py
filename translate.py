import sys
import time
import os
import subprocess
from textblob import TextBlob
from PyQt4.QtCore import *
from PyQt4.QtGui import *
app = QApplication(sys.argv) 
myClipBoard = QApplication.clipboard()
myClipBoard.clear()
clip = myClipBoard.text()
unfmessage = ''
message = ''
lang = 'ru'
while 1:
    clip = myClipBoard.text()
    if clip != unfmessage:
        print(clip)
        blob = TextBlob(clip)
        try:
            translated = str(blob.translate(to=lang))
        except BaseException:
            translated = "oops"
        unfmessage = clip
        if message.startswith(" "):
            message = unfmessage[1:]
        subprocess.call(['notify-send', 'Translator', translated])  
