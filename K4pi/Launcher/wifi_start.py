from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button
import subprocess
import tkinter as tk
from tkinter import *
import os
import wifi_newfile
import common
import psutil

"""
Comandi:
sudo systemctl stop NetworkManager.service
sudo systemctl stop wpa_supplicant.service
iwconfig
sudo hcxdumptool -i wlan1 -o dumpfile.pcapng --active_beacon --enable_status=15 
"""

def start_run(y):
    text = "K4pi >>> Stop NetworkManager.service        "
    wifi_newfile.process(y, "sudo systemctl stop NetworkManager.service", text)
    text1 = "K4pi >>> Stop wpa_supplicant.service        "
    wifi_newfile.process(y, "sudo systemctl stop wpa_supplicant.service", text1)
    text2 = "                                            "
    wifi_newfile.process(y, "2>/dev/null", text2)
    """
    text3 = "K4pi >>> START SCANNER. Press Stop in 5 min."
    wifi_newfile.process(y, "/home/Kh4nge/Script/GBLauncher/Python/K4pi/hcxdumptool/hcxdumptool -i wlan1 -o " + common.menu_start + " --active_beacon --enable_status=15", text3)
    #find ID hcxdumptool process
    for process in psutil.process_iter():
        if process.name() == "hcxdumptool":
            pid = process.pid
            break
    print("PID of hcxdumptool:", pid)
    """
    command = "ls -l"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    output, error = process.communicate()
    terminal = Tk()
    xterm = Xterm(terminal)
    xterm.feed(output)
    terminal.mainloop()
