from tkinter import *
from tkinter import filedialog
from tinytag import TinyTag
from threading import Thread
import pygame.mixer as mixer        # pip install pygame
import os
import time


songs = []
keep_time = True

def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    song_name.set(songs_list.get(ACTIVE))
    mixer.music.unload()
    mixer.music.load(songs_list.get(ACTIVE))
    mixer.music.play()
    status.set("playing")
    upcomming_song.set(next_song(song_name))

def stop_song(status: StringVar):
    mixer.music.stop()
    status.set("stop")

def next_song(current_song: StringVar):
    next_song_index = int(songs.index(current_song.get())) + 1
    next_song_name = str(songs[int(next_song_index)])
    return next_song_index, next_song_name

def skip(current_song: StringVar, songs_list: Listbox, status: StringVar):
    index, name = (next_song(current_song))
    mixer.music.stop()
    mixer.music.unload()
    del_from_list(current_song.get(), songs_list)
    mixer.music.load(name)
    mixer.music.play()
    status.set("playing")
    current_song.set(name)
    upcomming_song.set(next_song(current_song))  

def del_from_list(current_song ,songs_list: Listbox):
    idx = songs_list.get(0, "end").index(current_song)
    songs_list.delete(idx)
    songs.remove(songs[idx])

def ban_song(current_song ,songs_list: Listbox):
    del_from_list(current_song, songs_list)

def load(listbox):
    os.chdir(filedialog.askdirectory(title='Open a songs directory'))
    tracks = os.listdir()
    for track in tracks:
        listbox.insert(END, track)
        songs.append(track)

def pause_resume(status: StringVar):
    if status.get() == "playing":
        mixer.music.pause()
        status.set("paused")
    #if paused play
    elif status.get() == "paused":
        mixer.music.unpause()
        status.set("playing")

def rewind():
    mixer.music.rewind()

def adjust_volume(event):
    mixer.music.set_volume(volume.get()/100)

def calculate_play_time(status: StringVar):
    while keep_time:
        if status.get() == "playing":
            #Length
            tag = TinyTag.get(current_song.get())
            total_length = int(tag.duration)
            played_length = int(mixer.music.get_pos() / 1000)
            delta_time = total_length - played_length
            current_song_time.set(f"{delta_time}s")
            time.sleep(0.75)

def kill_threads():
    global keep_time
    keep_time = False
    root.destroy()
    exit

mixer.init()

root = Tk()
root.geometry('720x260')
root.title('PythonGeeks Music Player')
root.resizable(0, 0)

song_frame = LabelFrame(root, text='Current Song', bg='LightGrey', width=420, height=110)
song_frame.place(x=0, y=0)

button_frame = LabelFrame(root, text='Control Buttons', bg='Grey', width=420, height=130)
button_frame.place(y=110)

listbox_frame = LabelFrame(root, text='Playlist', bg='slategray')
listbox_frame.place(x=420, y=0, height=250, width=300)

# All Tkitner variables
current_song = StringVar(root, value='Not Selected')
upcomming_song = StringVar(root, value='Not Avaiable')
song_status = StringVar(root, value='Not Available')
current_song_time = IntVar(root,value=0)
volume = IntVar(root,value=50)

# Playlist ListBox
playlist = Listbox(listbox_frame, font=('Helvetica', 11), selectbackground='LightBlue', selectforeground='Black')

scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=BOTH)

playlist.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=playlist.yview)
playlist.pack(fill=BOTH, padx=5, pady=5)

# SongFrame Labels
Label(song_frame, text='CURRENTLY PLAYING:', bg='LightGrey', font=('Calibri', 10, "bold")).place(x=5, y=3)
song_lbl = Label(song_frame, textvariable=current_song, bg='White', font=("Arial", 10), width=31)
song_lbl.place(x=130, y=2)

Label(song_frame, text='NEXT SONG:', bg='LightGrey', font=('Calibri', 10, 'bold')).place(x=5, y=31)
next_lbl = Label(song_frame, textvariable=upcomming_song, bg='White', font=("Arial", 10), width=31)
next_lbl.place(x=130, y=30)

Label(song_frame, text='TIME TO NEXT SONG:', bg='LightGrey', font=('Calibri', 10, "bold")).place(x=5, y=59)
time_lbl = Label(song_frame, textvariable=current_song_time, bg='White', font=("Arial", 10), width=31)
time_lbl.place(x=130, y=58)

# Buttons in the main screen
pause_btn = Button(button_frame, text='Pause', bg='Aqua', font=("Georgia", 13), width=5,
                    command=lambda: pause_resume(song_status))
pause_btn.place(x=10, y=10)

stop_btn = Button(button_frame, text='Stop', bg='Aqua', font=("Georgia", 13), width=5,
                  command=lambda: stop_song(song_status))
stop_btn.place(x=75, y=10)

play_btn = Button(button_frame, text='Play', bg='Aqua', font=("Georgia", 13), width=5,
                  command=lambda: play_song(current_song, playlist, song_status))
play_btn.place(x=140, y=10)

skip_btn = Button(button_frame, text='Skip', bg='Aqua', font=("Georgia", 13), width=5,
                    command=lambda: skip(current_song, playlist, song_status))
skip_btn.place(x=205, y=10)

rewind_btn = Button(button_frame, text='Rewind', bg='Aqua', font=("Georgia", 13), width=5,
                    command=lambda: rewind())
rewind_btn.place(x=270, y=10)

delete_btn = Button(listbox_frame, text='Delete', bg='Aqua', font=("Georgia", 10), width=5,
                    command=lambda: del_from_list(playlist.get(ACTIVE), playlist))
delete_btn.place(x=10, y=192)

ban_btn = Button(listbox_frame, text='Ban', bg='Aqua', font=("Georgia", 10), width=5,
                    command=lambda: ban_song(playlist.get(ACTIVE), playlist))
ban_btn.place(x=75, y=192)

slider = Scale(
    button_frame, from_=100, to=0, orient='vertical', variable=volume, command=adjust_volume, width=10, sliderlength=20, label="Volume")
slider.place(x = 380, y=0)

load_btn = Button(button_frame, text='Load Directory', bg='Aqua', font=("Georgia", 13), width=35, command=load(playlist))
load_btn.place(x=10, y=55)

# Finalizing the GUI
Thread(target=calculate_play_time, args=[song_status]).start()
# Label at the bottom that displays the state of the music
Label(root, textvariable=song_status, bg='SteelBlue', font=('Times', 9), justify=LEFT).pack(side=BOTTOM, fill=X)
root.update()
root.protocol("WM_DELETE_WINDOW", kill_threads)
root.mainloop()