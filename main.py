from tkinter import *
import os
import time
import threading
from PIL import ImageTk, Image
songs = []
cur = 0
img = Image.open('img.png')
directory = r'songs'
for entry in os.scandir(directory):
    if (entry.path.endswith(".mp3")
            or entry.path.endswith(".mp4")) and entry.is_file():
        songs.append(entry.path)
root = Tk()
root.iconbitmap('icon.ico')
root.title('Python Media Player')
settingsimg = ImageTk.PhotoImage(img.resize((40, 40), Image.ANTIALIAS))

vollable = Label(root, text = "Volume Slider").grid(row = 0, column = 0, padx = 10)
scrublable = Label(root, text = "Scrub Slider").grid(row = 0, column = 1)

def volchng(arg):
    mixer.music.set_volume(vol.get()/100)

vol = Scale(root, from_ = 0, to = 100, command = volchng)
vol.grid(row = 1, column = 0)

from pygame import mixer  # Load the popular external library

poke = IntVar()

def scruba(x):
    mixer.music.set_pos(x)

path = StringVar()
path.set(songs[cur])

mixer.init()

scrub = Scale(root, from_=0, to=mixer.Sound(path.get()).get_length(), orient=HORIZONTAL, variable=poke, command=lambda x: scruba(poke.get()))
scrub.grid(row=1, column=1)

def inta():
    time.sleep(5)
    t.start()
    return

t2 = threading.Thread(target=inta)

def crossfade():
    time.sleep(5)
    while mixer.music.get_busy():
        pass
    path.set(songs[cur])
    play()
    return


t = threading.Thread(target=crossfade)
t.start()
def play():
    global cur
    global scrub
    global path
    cur += 1
    mixer.music.load(path.get())
    mixer.music.play()
    mixer.music.set_volume(0.08)
    vol.set(mixer.music.get_volume()*100)
    scrub.grid_forget()
    scrub = Scale(root, from_=0, to=mixer.Sound(path.get()).get_length(), orient=HORIZONTAL, variable = poke ,command = lambda x: scruba(poke.get()))
    scrub.grid(row=1, column=1)
    scrub.set(mixer.music.get_pos()/100)






drop = OptionMenu(root,path, *songs)
drop.grid(row = 3, column = 0, columnspan = 2)


def settings():
    set = Toplevel()


btn = Button(root,text="Play",command=play)
btn.grid(row = 2, column = 0, columnspan = 2, ipadx = 70, ipady = 40, pady = 10)

settingsbtn = Button(root,height = 10, width = 10, wraplength = 1,image = settingsimg,command = settings)
#settingsbtn.grid(row = 0, column = 5, ipadx = 10, ipady = 10)


root.mainloop()
mixer.music.stop()