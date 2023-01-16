from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button
import subprocess
import tkinter as tk
from tkinter import *
import os
import wifi_newfile
import wifi_start

stop_process = wifi_start.start_run_process()
stop_process.terminate()

def stop_run(y, dump):
    text1 = "                                            "
    wifi_newfile.process(y, "2>/dev/null", text1)
    text2 = "K4pi >>> STOP SCANNER.                      "
    wifi_newfile.process(y, "2>/dev/null", text2)
    text3 = "K4pi >>> Start NetworkManager.service       "
    wifi_newfile.process(y, "sudo systemctl start NetworkManager.service", text3)
    text4 = "K4pi >>> Start wpa_supplicant.service       "
    wifi_newfile.process(y, "sudo systemctl start wpa_supplicant.service", text4)