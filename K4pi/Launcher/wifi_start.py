from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button
import subprocess
import tkinter as tk
from tkinter import *
import os
import wifi_newfile
#import common
import psutil

def start_run_process(dump):
        command = "sudo terminator --borderless --geometry 354x312+122+4 -e 'sudo /home/Kh4nge/Script/GBLauncher/Python/K4pi/hcxdumptool/hcxdumptool -i wlan1 -o "+ dump +" --active_beacon --enable_status=15'"
        return subprocess.run(command, shell=True)

def start_run(y, dump):
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
    
    command = "sudo /home/Kh4nge/Script/GBLauncher/Python/K4pi/hcxdumptool/hcxdumptool -i wlan1 -o test1.pcapng --active_beacon --enable_status=15"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, bufsize=1)
    terminal = Tk()
    text = Text(terminal)
    text.pack()
    for line in iter(process.stdout.readline, b''):
        text.insert(INSERT, line)
        text.see(END)
        terminal.update()
    process.communicate()
    text.insert(INSERT, "Process completed!")
    terminal.mainloop()
    """
    text3 = "K4pi >>> START SCANNER.                     "
    wifi_newfile.process(y, "2>/dev/null", text3)
    start_run_process(dump)
    


