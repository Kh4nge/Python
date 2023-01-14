from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button
import subprocess
import tkinter as tk
from tkinter import *
import os
import wifi_newfile

"""
Comandi:
sudo systemctl start NetworkManager.service
sudo systemctl start wpa_supplicant.service
"""

def stop_run(y):
    text1 = "                                            "
    wifi_newfile.process(y, "2>/dev/null", text1)
    text3 = "K4pi >>> STOP SCANNER.                      "
    wifi_newfile.process(y, "sudo systemctl stop NetworkManager.service", text)