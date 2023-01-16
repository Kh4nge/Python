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
#import wifi_newfile
#import wifi_start
#import wifi_stop

dumpfile_text = 0

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
#                          Process Functions                            #
#-----------------------------------------------------------------------#

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

#---------------------------------------------------------------------#
#                            wifi_newfile                             #
#---------------------------------------------------------------------#
    
def newfile_run(y, time):
    #Create a Folder
    user = getpass.getuser()
    folder_path = ("/home/" + user + "/dumpfile")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        subprocess.call(['mkdir', "-p", folder_path])
        subprocess.call(['chmod', '777', folder_path])
        print(f"K4pi >>> The folder {folder_path} has been created.")
        text1 = "K4pi >>> The folder has been created.       "
        process(y, "2>/dev/null", text1)
        #Create a File
        text2 = "K4pi >>> File " + time + ".pcapng create!       "
        dumpfile = time + ".pcapng"
        dumpfile_text = str(dumpfile)
        process(y, "touch /home/" + user + "/dumpfile/" + dumpfile, text2)
        text3 = "                                            "
        process(y, "2>/dev/null", text3)
    else:
        print(f"K4pi >>> The folder {folder_path} already exists")
        text1 = "K4pi >>> The folder already exists          "
        process(y, "2>/dev/null", text1)
        #Create a File
        text2 = "K4pi >>> File " + time + ".txt create!       "
        dumpfile = time + ".pcapng"
        process(y, "touch /home/" + user + "/dumpfile/" + dumpfile, text2)
        text3 = "                                            "
        process(y, "2>/dev/null", text3)
    return dumpfile_text

#---------------------------------------------------------------------#
#                            wifi_start                               #
#---------------------------------------------------------------------#

def start_run_process(dump):
        command = "sudo terminator --borderless --geometry 354x312+122+4 -e 'sudo /home/Kh4nge/Script/GBLauncher/Python/K4pi/hcxdumptool/hcxdumptool -i wlan1 -o "+ dump +" --active_beacon --enable_status=15'"
        return subprocess.run(command, shell=True)

def start_run(y, dump):
    text = "K4pi >>> Stop NetworkManager.service        "
    process(y, "sudo systemctl stop NetworkManager.service", text)
    text1 = "K4pi >>> Stop wpa_supplicant.service        "
    process(y, "sudo systemctl stop wpa_supplicant.service", text1)
    text2 = "                                            "
    process(y, "2>/dev/null", text2)
    text3 = "K4pi >>> START SCANNER.                     "
    process(y, "2>/dev/null", text3)
    start_run_process(dump)

#---------------------------------------------------------------------#
#                            wifi_stop                                #
#---------------------------------------------------------------------#

def stop_run(y, dump):
    stop_process = start_run_process(dump)
    stop_process.terminate()
    text1 = "                                            "
    process(y, "2>/dev/null", text1)
    text2 = "K4pi >>> STOP SCANNER.                      "
    process(y, "2>/dev/null", text2)
    text3 = "K4pi >>> Start NetworkManager.service       "
    process(y, "sudo systemctl start NetworkManager.service", text3)
    text4 = "K4pi >>> Start wpa_supplicant.service       "
    process(y, "sudo systemctl start wpa_supplicant.service", text4)

#-----------------------------------------------------------------------#
#                          Button Function's                            #
#-----------------------------------------------------------------------#

def b2_command():
    dumpfile = newfile_run(t1, time)
    print (dumpfile)
def b3_command():
    dumpfile = newfile_run(t1, time)
    start_run(t1, dumpfile)
def b4_command():
    dumpfile = newfile_run(t1, time)
    stop_run(t1, dumpfile)

#-----------------------------------------------------------------------#
#                Configuration buttons and Text label                   #
#-----------------------------------------------------------------------#

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

b4 = tk.Button(root, text="Stop", bg="black", fg="white", command=b4_command, activeforeground="black", activebackground="#00ff5f")
b4.config(font=("Encode Sans SemiExpanded", 20))
b4.configure(highlightthickness=0)
b4.place(x=4, y=242, width=114, height=74)

text1 = "K4pi >>> Please create a new file.           "
process(t1, "2>/dev/null", text1)
text2 = "                                            "
process(t1, "2>/dev/null", text2) 

root.mainloop()