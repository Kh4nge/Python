from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button
import subprocess
import tkinter as tk
from tkinter import *
import os
import wifi_newfile

"""
Comandi:
sudo systemctl stop NetworkManager.service
sudo systemctl stop wpa_supplicant.service
iwconfig
sudo hcxdumptool -i wlan1 -o dumpfile.pcapng --active_beacon --enable_status=15
sudo systemctl start NetworkManager.service
sudo systemctl start wpa_supplicant.service 
"""

def start_run(y):
    text = "K4pi >>> Stop NetworkManager.service"
    wifi_newfile.process(y, "sudo systemctl stop NetworkManager.service", text)
    text = "K4pi >>> Stop wpa_supplicant.service"
    wifi_newfile.process(y, "sudo systemctl stop wpa_supplicant.service", text)
    text = "                                            "
    wifi_newfile.process(y, "2>/dev/null", text)
    text = "K4pi >>> START SCANNER"
    wifi_newfile.process(y, "/home/Kh4nge/Script/GBLauncher/Python/K4pi/hcxdumptool/hcxdumptool -i wlan1 -o " + wifi_newfile.dumpfile + " --active_beacon --enable_status=15", text)
