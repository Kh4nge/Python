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
image = Image.open("Kalilogo.jpg")
photo2 = ImageTk.PhotoImage(image)
label2 = Label(root, image=photo2)
label2.configure(background='black')
label2.place(x=4, y=242, width=114, height=74)

#-----------------------------------------------------------------------#
#                Configuration functions                                #
#-----------------------------------------------------------------------#

def start():
    timeset = datetime.now()
    current_time = timeset.strftime("%m%d%H%M%S")
    folder_name = "/home/Kh4nge/dumpfile/"
    text1 = "K4pi >>> Folder create or already exists.  "
    process(t1, "2>/dev/null", text1)
    os.makedirs(folder_name, 0o777, exist_ok=True)
    file_name = current_time + ".pcapng"
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, "w") as f:
        pass
    os.chmod(file_path, 0o777)
    text2 = "K4pi >>> File " + file_name + " create.    "
    process(t1, "2>/dev/null", text2)
    os.system("sudo systemctl stop NetworkManager.service")
    os.system("sudo systemctl stop wpa_supplicant.service")
    text3 = "K4pi >>> Stop Network Service!             "
    process(t1, "2>/dev/null", text3)
    cmd = "sudo terminator --borderless --geometry 354x312+122+4 -e 'sudo /home/Kh4nge/Script/GBLauncher/Python/K4pi/hcxdumptool/hcxdumptool -i wlan1 -o "+ file_path +" --active_beacon --enable_status=15"'"
    #cmd = "sudo gnome-terminal --geometry 354x312+122+4 --hide-menubar -- bash -c 'ls -la; bash'"
    #cmd = "sudo gnome-terminal --geometry 354x312+122+4 --hide-menubar -- bash -c 'sudo /home/Kh4nge/Script/GBLauncher/Python/K4pi/hcxdumptool/hcxdumptool -i wlan1 -o " + file_path + " --active_beacon --enable_status=15; bash'"
    os.system(cmd)
    text4 = "K4pi >>> START SCANNER.                    "
    process(t1, "2>/dev/null", text4)

def stop():
    os.system("pkill -f gnome-terminal")
    text = "K4pi >>> STOP SCANNER. Download File       "
    process(t1, "2>/dev/null", text)
    text2 = "                                           "
    process(t1, "2>/dev/null", text2)

def process(x, cmd, text):
    command = str(cmd)
    text_print = str(text)
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    x.config(state=NORMAL)
    #x.delete("1.0", END)
    x.insert("1.0", text_print)
    x.insert("1.0", output.decode())
    x.config(state=DISABLED)

#-----------------------------------------------------------------------#
#                Configuration buttons and Text label                   #
#-----------------------------------------------------------------------#

t1 = Text(root, bg="black", fg="white")
t1.place(x=122, y=4, width=354, height=312)

b1 = tk.Button(root, text="CLOSE", bg="black", fg="white", command=root.destroy, activeforeground="black", activebackground="red")
b1.config(font=("Encode Sans SemiExpanded", 18))
b1.configure(highlightthickness=0)
b1.place(x=4, y=4, width=114, height=74)
    
b2 = tk.Button(root, text="Start", bg="black", fg="white", command=lambda: start(), activeforeground="black", activebackground="#00ff5f")
b2.config(font=("Encode Sans SemiExpanded", 20))
b2.configure(highlightthickness=0)
b2.place(x=4, y=82, width=114, height=76)

b3 = tk.Button(root, text="Stop", bg="black", fg="white", command=lambda: stop(), activeforeground="black", activebackground="#00ff5f")
b3.config(font=("Encode Sans SemiExpanded", 20))
b3.configure(highlightthickness=0)
b3.place(x=4, y=162, width=114, height=76)

root.mainloop()