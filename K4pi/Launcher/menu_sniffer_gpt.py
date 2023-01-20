"""
import os
import subprocess
from tkinter import *
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

current_time = datetime.now()
time = current_time.strftime("%m%d%H%M%S")

def newfile():
    folder_path = ("/home/giulio/dumpfile")
    os.makedirs(folder_path, exist_ok=True)
    open(folder_path + "/" + time + ".pcapng", "w").close()
    output_label.config(text="File dumpfile.pcapng creato in /home/utente/dumpfile")

def start():
    subprocess.call(["systemctl", "stop", "NetworkManager.service"])
    subprocess.call(["systemctl", "stop", "wpa_supplicant.service"])
    process = subprocess.Popen(["sudo", "terminator", "--borderless", "--geometry", "354x312+122+4", "-e", "sudo /home/Kh4nge/Script/GBLauncher/Python/K4pi/hcxdumptool/hcxdumptool -i wlan1 -o dumpfile.pcapng --active_beacon --enable_status=15"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stdout,stderr = process.communicate()
    output_label.config(text=stdout.decode())

def close():
    subprocess.call(["pkill", "terminator"])
    output_label.config(text="Terminator chiuso")



root = Tk()
root.title("WiFi Page")
root.geometry("480x320")
root.configure(bg="#463E3F")
root.attributes("-fullscreen", True)
image = Image.open("desk2.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo)
label.configure(background='black')
label.place(x=0, y=0, width=480, height=320)

t1 = Text(root, bg="black", fg="white")
t1.place(x=122, y=4, width=354, height=312)

b1 = tk.Button(root, text="CLOSE", bg="black", fg="white", command=root.destroy, activeforeground="black", activebackground="red")
b1.config(font=("Encode Sans SemiExpanded", 18))
b1.configure(highlightthickness=0)
b1.place(x=4, y=4, width=114, height=74)
    
b2 = tk.Button(root, text="New-File", bg="black", fg="white", command=lambda: newfile, activeforeground="black", activebackground="#00ff5f")
b2.config(font=("Encode Sans SemiExpanded", 15))
b2.configure(highlightthickness=0)
b2.place(x=4, y=82, width=114, height=76)

b3 = tk.Button(root, text="Start", bg="black", fg="white", command=lambda: start, activeforeground="black", activebackground="#00ff5f")
b3.config(font=("Encode Sans SemiExpanded", 20))
b3.configure(highlightthickness=0)
b3.place(x=4, y=162, width=114, height=76)

b4 = tk.Button(root, text="Stop", bg="black", fg="white", command=lambda: close, activeforeground="black", activebackground="#00ff5f")
b4.config(font=("Encode Sans SemiExpanded", 20))
b4.configure(highlightthickness=0)
b4.place(x=4, y=242, width=114, height=74)

root.mainloop()
"""

import os
from tkinter import *
import time

def start(current_time):
    folder_name = "/home/kali/dumpfile/"
    os.makedirs(folder_name, 0o777, exist_ok=True)
    file_name = current_time + ".pcapng"
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, "w") as f:
        pass
    os.chmod(file_path, 0o777)
    cmd = "sudo gnome-terminal -- bash -c 'ls -la; bash'"
    #cmd = "sudo terminator --borderless --geometry 354x312+122+4 -e 'sudo /home/Kh4nge/Script/GBLauncher/Python/K4pi/hcxdumptool/hcxdumptool -i wlan1 -o " + file_path + " --active_beacon --enable_status=15'"
    os.system(cmd)

def stop():
    os.system("pkill -f terminator")

def button_press():
    current_time = time.strftime("%m%d%H%M%S")
    if button_var.get() == "Start":
        start(current_time)
    elif button_var.get() == "Stop":
        stop()

root = Tk()
root.title("Programma")

button_var = StringVar()

start_button = Radiobutton(root, text="Start", variable=button_var, value="Start", command=button_press)
start_button.pack()

stop_button = Radiobutton(root, text="Stop", variable=button_var, value="Stop", command=button_press)
stop_button.pack()

root.mainloop()

