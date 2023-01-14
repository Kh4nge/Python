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
    #x.delete("1.0", END)
    x.insert("1.0", text_print)
    x.insert("1.0", output.decode())
    x.config(state=DISABLED)
    
def newfile_run(y, time):
    global dumpfile
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
        process(y, "touch /home/" + user + "/dumpfile/" + dumpfile, text2)
        text3 = "                                            "
        process(y, "2>/dev/null", text3)
    else:
        print(f"K4pi >>> The folder {folder_path} already exists")
        text1 = "K4pi >>> The folder already exists          "
        process(y, "2>/dev/null", text1)
        #Create a File
        #K4pi >>> File " + time + ".txt create!       "
        #--------------------------------------------- row K4pi >>> for terminal
        #
        text2 = "K4pi >>> File " + time + ".txt create!       "
        dumpfile = time + ".pcapng"
        process(y, "touch /home/" + user + "/dumpfile/" + dumpfile, text2)
        text3 = "                                            "
        process(y, "2>/dev/null", text3)
    return dumpfile