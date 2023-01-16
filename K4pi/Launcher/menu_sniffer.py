from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button
import subprocess
from subprocess import Popen
import tkinter as tk
from tkinter import *
import os
from datetime import datetime
from PIL import Image, ImageTk
import getpass
import psutil
from common import process, newfile_run, start_run, stop_run, b2_command
#import wifi_newfile
#import wifi_start
#import wifi_stop

dumpfile = 0

#-----------------------------------------------------------------------#
#                Configuration Windows, Image, Time                     #
#-----------------------------------------------------------------------#

root = tk.Tk()
root.title("WiFi Page")
root.geometry("480x320")
root.configure(bg="#463E3F")
root.attributes("-fullscreen", True)
image = Image.open("desk2.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo)
label.configure(background='black')
label.place(x=0, y=0, width=480, height=320)

current_time = datetime.now()
time = current_time.strftime("%m%d%H%M%S")

#-----------------------------------------------------------------------#
#                Configuration buttons and Text label                   #
#-----------------------------------------------------------------------#

t1 = Text(root, bg="black", fg="white")
t1.place(x=122, y=4, width=354, height=312)

b1 = tk.Button(root, text="CLOSE", bg="black", fg="white", command=root.destroy, activeforeground="black", activebackground="red")
b1.config(font=("Encode Sans SemiExpanded", 18))
b1.configure(highlightthickness=0)
b1.place(x=4, y=4, width=114, height=74)
    
b2 = tk.Button(root, text="New-File", bg="black", fg="white", command=lambda: (dumpfile = newfile_run(t1, time)), activeforeground="black", activebackground="#00ff5f")
b2.config(font=("Encode Sans SemiExpanded", 15))
b2.configure(highlightthickness=0)
b2.place(x=4, y=82, width=114, height=76)

b3 = tk.Button(root, text="Start", bg="black", fg="white", command=lambda: start_run(t1, dumpfile), activeforeground="black", activebackground="#00ff5f")
b3.config(font=("Encode Sans SemiExpanded", 20))
b3.configure(highlightthickness=0)
b3.place(x=4, y=162, width=114, height=76)

b4 = tk.Button(root, text="Stop", bg="black", fg="white", command=lambda: stop_run(t1, dumpfile), activeforeground="black", activebackground="#00ff5f")
b4.config(font=("Encode Sans SemiExpanded", 20))
b4.configure(highlightthickness=0)
b4.place(x=4, y=242, width=114, height=74)

text1 = "K4pi >>> Please create a new file.           "
process(t1, "2>/dev/null", text1)
text2 = "                                            "
process(t1, "2>/dev/null", text2) 

root.mainloop()