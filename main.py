"""
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
"""
from pynput.keyboard import Key, Listener
from pygame import mixer
import random
import os

def on_press(key):
    if str(key) == '\x03':
        exit()
    else:
        try:
            mixer.music.load(random.choice(sample_list))
            mixer.music.play()
        except:
            print("error opening audio : {}".format(random_sample))


mixer.init()

#mixer.music.load('sound/key01.mp3')
sample_list = []
for item in range(5):
    sample_list.append('./sound/key0{}.mp3'.format(str(item + 1)))
print(sample_list)

with Listener(on_press=on_press) as listener :
    listener.join()

"""
app = QApplication([])
app.setQuitOnLastWindowClosed(False)

icon = QIcon('./icons/keyboard.ico')
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)


menu = QMenu()
quit = QAction("Close")
quit.triggered.connect(os.kill)
menu.addAction(quit)

tray.setContextMenu(menu)
app.show()
"""