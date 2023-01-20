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
from common import process, newfile_run, start_run, stop_run
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

#-----------------------------------------------------------------------#
#                Configuration functions                                #
#-----------------------------------------------------------------------#

def start(current_time):
    folder_name = "/home/Kh4nge/dumpfile/"
    text1 = "K4pi >>> The folder has been created.           "
    process(y, "2>/dev/null", text1)
    os.makedirs(folder_name, 0o777, exist_ok=True)
    file_name = current_time + ".pcapng"
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, "w") as f:
        pass
    os.chmod(file_path, 0o777)
    text2 = "K4pi >>> File " + file_name + ".pcapng create!    "
    process(y, "2>/dev/null", text2)
    os.system("sudo systemctl stop NetworkManager.service")
    os.system("sudo systemctl stop wpa_supplicant.service")
    text3 = "K4pi >>> Stop Network Service!                    "
    process(y, "2>/dev/null", text3)
    cmd = "sudo gnome-terminal -- bash -c 'ls -la; bash'"
    #cmd = "sudo gnome-terminal --geometry 354x312+122+4 --hide-menubar -- bash -c 'sudo /home/Kh4nge/Script/GBLauncher/Python/K4pi/hcxdumptool/hcxdumptool -i wlan1 -o " + file_path + " --active_beacon --enable_status=15'"
    os.system(cmd)
    text4 = "K4pi >>> START SCANNER.                     "
    process(y, "2>/dev/null", text4)

def stop():
    os.system("pkill -f gnome-terminal")
    text = "K4pi >>> STOP SCANNER. View last file create!"
    process(y, "2>/dev/null", text)

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

def button_press():
    current_time = time.strftime("%m%d%H%M%S")
    if button_var.get() == "Start":
        start(current_time)
    elif button_var.get() == "Stop":
        stop()

#-----------------------------------------------------------------------#
#                Configuration buttons and Text label                   #
#-----------------------------------------------------------------------#

button_var = StringVar()

t1 = Text(root, bg="black", fg="white")
t1.place(x=122, y=4, width=354, height=312)

b1 = tk.Button(root, text="CLOSE", bg="black", fg="white", command=root.destroy, activeforeground="black", activebackground="red")
b1.config(font=("Encode Sans SemiExpanded", 18))
b1.configure(highlightthickness=0)
b1.place(x=4, y=4, width=114, height=74)
    
b2 = tk.Button(root, text="Start", bg="black", fg="white", variable=button_var, value="Start", command=button_press, activeforeground="black", activebackground="#00ff5f")
b2.config(font=("Encode Sans SemiExpanded", 15))
b2.configure(highlightthickness=0)
b2.place(x=4, y=82, width=114, height=76)

b3 = tk.Button(root, text="Stop", bg="black", fg="white", variable=button_var, value="Stop", command=button_press, activeforeground="black", activebackground="#00ff5f")
b3.config(font=("Encode Sans SemiExpanded", 20))
b3.configure(highlightthickness=0)
b3.place(x=4, y=162, width=114, height=76)

b4 = tk.Button(root, text="", bg="black")
b4.config(font=("Encode Sans SemiExpanded", 20))
b4.configure(highlightthickness=0)
b4.place(x=4, y=242, width=114, height=74)

root.mainloop()