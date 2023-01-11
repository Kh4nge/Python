from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button
import subprocess
import tkinter as tk
from tkinter import *
import os
from datetime import datetime
import wifi_newfile
import wifi_start
import wifi_stop

root = tk.Tk()
root.title("WiFi Page")
root.geometry("480x320")
root.configure(bg="#463E3F")
#root.attributes("-fullscreen", True)

current_time = datetime.now()
time = current_time.strftime("%m%d-%H%M%S")
print (time)

#Functions for button
def b2_command():
    wifi_newfile.newfile_run(t1, time)
def b3_command():
    wifi_newfile.newfile_clear(t1)

# Create output text Campo
t1 = Text(root, bg="black", fg="white")
t1.place(x=120, y=0, width=360, height=320)

b1 = tk.Button(root, text="CLOSE", bg="black", fg="white", command=root.destroy, activeforeground="black", activebackground="red")
b1.place(x=0, y=0, width=120, height=80)
    
b2 = tk.Button(root, text="1. New-File", bg="black", fg="white", command=b2_command, activeforeground="black", activebackground="#00ff5f")
b2.place(x=0, y=80, width=120, height=80)

b3 = tk.Button(root, text="2. Start", bg="black", fg="white", command=b3_command, activeforeground="black", activebackground="#00ff5f")
b3.place(x=0, y=160, width=120, height=80)

b4 = tk.Button(root, text="Stop", bg="black", fg="white", command=root.destroy, activeforeground="black", activebackground="#00ff5f")
b4.place(x=0, y=240, width=120, height=80)

#Loop for not close the window
root.mainloop()