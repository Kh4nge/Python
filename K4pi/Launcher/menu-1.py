from tkinter import Tk, mainloop, TOP
from tkinter import *
from tkinter.ttk import Button
import subprocess as sub
import tkinter as tk
from subprocess import Popen
import os

#Configuration Windows
root = tk.Tk()
root.title("Main Page")
root.geometry("480x320")
root.configure(bg="#463E3F")
root.attributes("-fullscreen", True)

#Configuration buttons and objects
b1 = tk.Button(root, text="CLOSE", bg="black", fg="white", command=root.destroy, activeforeground="black", activebackground="red")
b1.place(x=0, y=0, width=120, height=80)

l1 = tk.Label(root, text="GB - Launcher for Rapsberry", bg="black", fg="white")
l1.place(x=120, y=0, width=360, height=80)

b2 = tk.Button(root, text="WiFi-Sniffer", bg="black", fg="white", command=lambda: os.system('python3 menu-sniffer.py'), activeforeground="black", activebackground="#00ff5f")
b2.place(x=0, y=80, width=240, height=160)

b3 = tk.Button(root, text="Altro", bg="black", fg="white", activeforeground="black", activebackground="#00ff5f")
b3.place(x=240, y=80, width=240, height=160)

b4 = tk.Button(root, text="Altro", bg="black", fg="white", activeforeground="black", activebackground="#00ff5f")
b4.place(x=0, y=200, width=240, height=150)

b5 = tk.Button(root, text="Altro", bg="black", fg="white", activeforeground="black", activebackground="#00ff5f")
b5.place(x=240, y=200, width=240, height=150)

#Loop for not close the window
root.mainloop()