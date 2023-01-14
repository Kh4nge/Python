from tkinter import Tk, mainloop, TOP
from tkinter import *
from tkinter.ttk import Button
import subprocess as sub
import tkinter as tk
from subprocess import Popen
import os
from PIL import Image, ImageTk

#----------------------------------
# Configuration Windows and Image
#----------------------------------

root = tk.Tk()
root.title("Main Page")
root.geometry("480x320")
root.configure(bg="#463E3F")
root.attributes("-fullscreen", True)

image = Image.open("desk1.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo)
label.configure(background='black')
label.place(x=0, y=0, width=480, height=320)

#----------------------------------
# Configuration buttons and objects
#----------------------------------

b1 = tk.Button(root, text="CLOSE", bg="black", fg="white", command=root.destroy, activeforeground="black", activebackground="red")
b1.config(font=("Encode Sans SemiExpanded", 18))
b1.configure(highlightthickness=0)
b1.place(x=4, y=4, width=114, height=74)

b2 = tk.Button(root, text="WiFi-Sniffer", bg="black", fg="white", command=lambda: os.system('python3 menu-sniffer.py'), activeforeground="black", activebackground="#00ff5f")
b2.config(font=("Encode Sans SemiExpanded", 20))
b2.configure(highlightthickness=0)
b2.place(x=4, y=82, width=234, height=116)

b3 = tk.Button(root, text="RasAP", bg="black", fg="white", activeforeground="black", activebackground="#00ff5f")
b3.config(font=("Encode Sans SemiExpanded", 25))
b3.configure(highlightthickness=0)
b3.place(x=242, y=82, width=234, height=116)

b4 = tk.Button(root, text="OpenVAS", bg="black", fg="white", activeforeground="black", activebackground="#00ff5f")
b4.config(font=("Encode Sans SemiExpanded", 25))
b4.configure(highlightthickness=0)
b4.place(x=4, y=202, width=234, height=114)

b5 = tk.Button(root, text="Kismet", bg="black", fg="white", activeforeground="black", activebackground="#00ff5f")
b5.config(font=("Encode Sans SemiExpanded", 25))
b5.configure(highlightthickness=0)
b5.place(x=242, y=202, width=234, height=114)

#Loop for not close the window
root.mainloop()