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
    return dumpfile

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
