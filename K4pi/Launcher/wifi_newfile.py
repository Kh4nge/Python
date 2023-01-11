from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button
import subprocess
import tkinter as tk
from tkinter import *
import os
import getpass

def process(x, cmd, text):
    command = str(cmd)
    text_print = str(text)
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    x.config(state=NORMAL)
    x.delete("1.0", END)
    x.insert("1.0", text_print)
    x.insert("1.0", output.decode())
    x.config(state=DISABLED)
    
def newfile_run(y, time):
    #Create a Folder
    user = getpass.getuser()
    folder_path = ("/home/" + user + "/dumpfile")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        subprocess.call(['mkdir', "-p", folder_path])
        subprocess.call(['chmod', '777', folder_path])
        print(f"K4pi >>> The folder {folder_path} has been created.")
        text = "K4pi >>> The folder " + folder_path + " has been created."
        process(y, "2>/dev/null", text)
        #Create a File
        text = "K4pi >>> File " + time + ".txt has been created"
        dumpfile = time + ".pcapng"
        process(y, "touch /home/" + user + "/dumpfile/" + dumpfile, text)
        text = "---------------------------------"
        process(y, "2>/dev/null", text)
    else:
        print(f"K4pi >>> The folder {folder_path} already exists")
        text = "K4pi >>> The folder " + folder_path + " already exists"
        process(y, "2>/dev/null", text)   

def newfile_clear(y):
    process(y, "cat wifi_start.py")