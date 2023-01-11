from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button
import subprocess
import tkinter as tk
from tkinter import *
import os

root = tk.Tk()
root.title("WiFi Page")
root.geometry("480x320")
root.configure(bg="#463E3F")
#root.attributes("-fullscreen", True)

def run_command(cmd):
    # Esegui il comando in una shell Linux
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Legge l'output del comando
    output, error = process.communicate()
    
    # Stampa l'output del comando
    output_field.config(state=NORMAL)
    output_field.delete("1.0", END)
    output_field.insert("1.0", output.decode())
    output_field.config(state=DISABLED)

# Create output text Campo
output_field = Text(root)
output_field.place(x=120, y=0, width=360, height=320)

b1 = tk.Button(root, text="CLOSE", bg="black", fg="white", command=root.destroy, activeforeground="black", activebackground="red")
b1.place(x=0, y=0, width=120, height=80)

b2 = tk.Button(root, text="1. New-File", bg="black", fg="white", command=lambda: run_command("sudo apt-get update"), activeforeground="black", activebackground="#00ff5f")
b2.place(x=0, y=80, width=120, height=80)

b3 = tk.Button(root, text="2. Start", bg="black", fg="white", command=root.destroy, activeforeground="black", activebackground="#00ff5f")
b3.place(x=0, y=160, width=120, height=80)

b4 = tk.Button(root, text="Stop", bg="black", fg="white", command=root.destroy, activeforeground="black", activebackground="#00ff5f")
b4.place(x=0, y=240, width=120, height=80)

#Loop for not close the window
root.mainloop()