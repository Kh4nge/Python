from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button
import subprocess
from subprocess import Popen
import tkinter as tk
from tkinter import *
import os
from datetime import datetime
from PIL import Image, ImageTk
import wifi_newfile
import wifi_start
import wifi_stop
import wifi_newfile

#------------------------------------
# Configuration Windows, Image, Time
#------------------------------------

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

#--------------------------------------
# Button Function's
#--------------------------------------

def b2_command():
    wifi_newfile.newfile_run(t1, time)
    print (b2_command)
def b3_command():
    wifi_start.start_run(t1)

#--------------------------------------
# Configuration buttons and Text label
#--------------------------------------

t1 = Text(root, bg="black", fg="white")
t1.place(x=122, y=4, width=354, height=312)

b1 = tk.Button(root, text="CLOSE", bg="black", fg="white", command=root.destroy, activeforeground="black", activebackground="red")
b1.config(font=("Encode Sans SemiExpanded", 18))
b1.configure(highlightthickness=0)
b1.place(x=4, y=4, width=114, height=74)
    
b2 = tk.Button(root, text="New-File", bg="black", fg="white", command=b2_command, activeforeground="black", activebackground="#00ff5f")
b2.config(font=("Encode Sans SemiExpanded", 15))
b2.configure(highlightthickness=0)
b2.place(x=4, y=82, width=114, height=76)

b3 = tk.Button(root, text="Start", bg="black", fg="white", command=b3_command, activeforeground="black", activebackground="#00ff5f")
b3.config(font=("Encode Sans SemiExpanded", 20))
b3.configure(highlightthickness=0)
b3.place(x=4, y=162, width=114, height=76)

b4 = tk.Button(root, text="Stop", bg="black", fg="white", command=root.destroy, activeforeground="black", activebackground="#00ff5f")
b4.config(font=("Encode Sans SemiExpanded", 20))
b4.configure(highlightthickness=0)
b4.place(x=4, y=242, width=114, height=74)

#        --------------------------------------------- row K4pi >>> for terminal
text1 = "K4pi >>> Please create a new file.           "
wifi_newfile.process(t1, "2>/dev/null", text1)
text2 = "                                            "
wifi_newfile.process(t1, "2>/dev/null", text2) 

#Loop for not close the window
root.mainloop()