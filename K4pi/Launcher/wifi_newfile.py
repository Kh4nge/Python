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
    
"""
def process_sudo(x, cmd):
    password = "Toldo93xd2"
    cmd2 = str(cmd)
    command = "sudo" + cmd2
    process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate(input=password.encode() + b"\n")
    x.config(state=NORMAL)
    x.delete("1.0", END)
    x.insert("1.0", output.decode())
    x.insert("1.0", result.stdout.decode())
    x.insert("1.0", result.stderr.decode())
    x.config(state=DISABLED)
"""

def newfile_run(y, time):
    user = getpass.getuser()
    folder_path = ("/home/" + user + "/dumpfile")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        subprocess.call(['mkdir', "-p", folder_path])
        subprocess.call(['chmod', '777', folder_path])
        print(f"K4pi >>> The folder {folder_path} has been created.")
        text = "K4pi >>> The folder " + folder_path + " has been created."
        process(y, "2>/dev/null", text)


        text = "K4pi >>> File " + time + ".txt has been created"
        process(y, "touch /home/" + user + "/dumpfile/" + time + ".txt", text)

        text = "---------------------------------"
        process(y, "2>/dev/null", text)

        #subprocess.call(['echo', 'Toldo93xd2', '|', 'sudo', 'touch', folder_path])
        #subprocess.call(['echo', 'Toldo93xd2', '|', 'sudo', 'chmod', '777', folder_path])
        #print(f"K4pi >>> The file dump.txt has been created.")
    else:
        print(f"K4pi >>> The folder {folder_path} already exists")
        text = "K4pi >>> The folder " + folder_path + " already exists"
        process(y, "2>/dev/null", text)
    
    
    
    #print (folder_path)
    #path2 = "touch " + folder_path + "/dump.txt"
    #p#rint (path2)
    #test = process(y, "/usr/bin/touch" + folder_path + "/dump.txt", "Creazione file touch")
    #process(y, "chmod " + " 777 " + folder_path + "/dump.txt")
    #process(y, folder_path + "ls")
    

def newfile_clear(y):
    process(y, "cat wifi_start.py")