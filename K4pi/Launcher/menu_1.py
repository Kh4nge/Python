from tkinter import Tk, mainloop, TOP
from tkinter import *
from tkinter.ttk import Button
import subprocess as sub
import tkinter as tk
from subprocess import Popen
import os
from PIL import Image, ImageTk
from datetime import datetime

#----------------------------------
# Configuration Windows and Image
#----------------------------------

root = tk.Tk()
root.title("Main Page")
root.geometry("480x320")
root.configure(bg="#463E3F")
root.attributes("-fullscreen", True)

image = Image.open("desk1.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo)
label.configure(background='black')
label.place(x=0, y=0, width=480, height=320)

def start():
    timeset = datetime.now()
    current_time = timeset.strftime("%m%d%H%M%S")
    folder_name = "/home/kali/dumpfile/"
    os.makedirs(folder_name, 0o777, exist_ok=True)
    file_name = current_time + ".pcapng"
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, "w") as f:
        pass
    os.chmod(file_path, 0o777)
    os.system("sudo systemctl stop NetworkManager.service")
    os.system("sudo systemctl stop wpa_supplicant.service")
    #output = os.popen("sudo hcxdumptool -i wlan1 -o "+ file_path +" --active_beacon --enable_status=15;bash").read()
    #cmd = "sudo xterm -hold -e 'sudo hcxdumptool -i wlan1 -o " + file_path + " --active_beacon --enable_status=15;bash'"
    #cmd = "sudo hcxdumptool -i wlan0 -o "+ file_path +" --active_beacon --enable_status=15;bash"
    cmd = "sudo terminator -e 'sudo hcxdumptool -i wlan1 -o "+ file_path +" --active_beacon --enable_status=15;bash'"
    os.system(cmd)

#----------------------------------
# Configuration buttons and objects
#----------------------------------

b1 = tk.Button(root, text="CLOSE", bg="black", fg="white", command=root.destroy, activeforeground="black", activebackground="red")
b1.config(font=("Encode Sans SemiExpanded", 18))
b1.configure(highlightthickness=0)
b1.place(x=4, y=4, width=114, height=74)

b2 = tk.Button(root, text="WiFi-Sniffer", bg="black", fg="white", command=lambda: start(), activeforeground="black", activebackground="#00ff5f")
b2.config(font=("Encode Sans SemiExpanded", 20))
b2.configure(highlightthickness=0)
b2.place(x=4, y=82, width=234, height=116)

b3 = tk.Button(root, text="RasAP", bg="black", fg="white", activeforeground="black", activebackground="#00ff5f")
b3.config(font=("Encode Sans SemiExpanded", 25))
b3.configure(highlightthickness=0)
b3.place(x=242, y=82, width=234, height=116)

b4 = tk.Button(root, text="OpenVAS", bg="black", fg="white", activeforeground="black", activebackground="#00ff5f")
b4.config(font=("Encode Sans SemiExpanded", 25))
b4.configure(highlightthickness=0)
b4.place(x=4, y=202, width=234, height=114)

b5 = tk.Button(root, text="Kismet", bg="black", fg="white", activeforeground="black", activebackground="#00ff5f")
b5.config(font=("Encode Sans SemiExpanded", 25))
b5.configure(highlightthickness=0)
b5.place(x=242, y=202, width=234, height=114)

#Loop for not close the window
root.mainloop()
