from tkinter import *
from tkinter import StringVar
import pygame
import os


root = Tk()
root.geometry("600x420")
root.resizable(0,0)
root.title("Music Player")



status = StringVar()



pygame.init()
pygame.mixer.init()

def playsong():
    songtrack.config(state=NORMAL)
    songtrack.delete('1.0',END)
    songtrack.insert('1.0',playlist.get(ACTIVE))
    songtrack.config(state=DISABLED)

    status.set("-Playing")

    pygame.mixer.music.load(playlist.get(ACTIVE))
    pygame.mixer.music.play()

def stopsong():
    songtrack.config(state=NORMAL)
    songtrack.delete('1.0',END)
    songtrack.config(state=DISABLED)

    status.set("-Stopped")

    pygame.mixer.music.stop()


def pausesong():
    status.set("-Paused")
    pygame.mixer.music.pause()

def unpausesong():
    status.set("-Playing")
    pygame.mixer.music.unpause()

trackframe = LabelFrame(root, text='Song Track', font=("Arial", 15, "bold"),
 bg='#a887e0', fg='white',bd=5, relief=GROOVE)
trackframe.place(x=0, y=200, width=600, height=120 )

songtrack = Text(trackframe, width=40, height=2, font=("Arial", 15),
bg='#8a1553', fg='white', state=DISABLED)

songtrack.grid(row=0, column=0, padx=10, pady=5)

trackstatus = Label(trackframe, textvariable= status,font=("Sans-serif", 12),
bg='#8a1553', fg='white')
trackstatus.grid(row=0, column=1, padx=10, pady=5)

buttonframe = LabelFrame(root, text='Control Panel', font=('Arial',15,'bold'), 
bg='#a887e0', fg='white', bd=5 , relief=GROOVE, pady=10)
buttonframe.place(x=0,y=320, width=600, height=100)

playbtn = Button(buttonframe, text='Play', width=6, height=1, font=('Arial', 16), 
fg='white', bg='#8a1553', command=playsong)
playbtn.grid(row=0, column=0, padx=10, pady=5)

pasuebtn = Button(buttonframe, text='Pause', width=6, height=1, font=('Arial', 16), 
fg='white', bg='#8a1553', command=pausesong)
pasuebtn.grid(row=0, column=1, padx=10, pady=5)

unpasuebtn = Button(buttonframe, text='Unpause', width=10, height=1, font=('Arial', 16), 
fg='white', bg='#8a1553', command=unpausesong)
unpasuebtn.grid(row=0, column=2, padx=10, pady=5)

stopbtn = Button(buttonframe, text='Stop', width=6, height=1, font=('Arial', 16), 
fg='white', bg='#8a1553', command=stopsong)
stopbtn.grid(row=0, column=3, padx=10, pady=5)


songsframe = LabelFrame(root, text='Songs Playlist', font=('Arial', 15, 'bold'),
bg='grey', fg='white', bd=5, relief=GROOVE)
songsframe.place(x=0,y=0,width=600, height=200)

scroll_y = Scrollbar(songsframe, orient=VERTICAL)
playlist = Listbox(songsframe, selectbackground="gold", selectmode=SINGLE,
font=('Arial', 12), bg='silver', fg='navyblue', bd=5, relief=GROOVE, yscrollcommand=scroll_y.set)
scroll_y.config(command=playlist.yview)
scroll_y.pack(side=RIGHT, fill=Y)
playlist.pack(fill=BOTH)

os.chdir(r"C:\Users\Mahdi\Music")
songtracks = os.listdir()
for track in songtracks:
    if ".mp3" in track:
        playlist.insert(END,track )
    else:
        pass

root.mainloop()

#! Made Bye Seyed Mahdi Olamaei ~ EXxZAM
#! Tutorial on how to make a music player on https://aparat.com/iranfun2000
#! 2021

