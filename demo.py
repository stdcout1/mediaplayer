from tkinter import *
import os
songs = []
cur = 0
directory = r'songs'
for entry in os.scandir(directory):
    if (entry.path.endswith(".mp3")
            or entry.path.endswith(".mp4")) and entry.is_file():
        songs.append(entry.path)
root = Tk()
root.title('Python Media Player')

vollable = Label(root, text = "Volume Slider").grid(row = 0, column = 0, padx = 10)
scrublable = Label(root, text = "Scrub Slider").grid(row = 0, column = 1)

def volchng(arg):
    pass

vol = Scale(root, from_ = 0, to = 100, command = volchng)
vol.grid(row = 1, column = 0)

poke = IntVar()

def scruba(x):
    pass

path = StringVar()
path.set(songs[cur])

scrub = Scale(root, from_=0, to = 200, orient=HORIZONTAL, variable=poke, command=lambda x: scruba(poke.get()))
scrub.grid(row=1, column=1)

def play():
    pass

drop = OptionMenu(root,path, *songs)
drop.grid(row = 3, column = 0, columnspan = 2)

btn = Button(root,text="Play",command=play)
btn.grid(row = 2, column = 0, columnspan = 2, ipadx = 70, ipady = 40, pady = 10)

root.mainloop()