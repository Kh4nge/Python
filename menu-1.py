from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button
import subprocess as sub
import tkinter as tk

#Configurazione finestra
root = tk.Tk()
root.title("Main Page")
root.geometry("400x350")
root.configure(bg="#463E3F")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.rowconfigure(1, weight=1)

#Creazione pulsanti
b1 = tk.Button(root, text="CLOSE", bg="black", fg="white", command=root.destroy)
b1.grid(column=0, row=0, columnspan=2, ipadx=20, ipady=20, sticky="NSEW")
b2 = tk.Button(root, text="WiFi-Sniffer", bg="black", fg="white", command=lambda: sub.call('./xterm.sh'))
b2.grid(column=0, row=1, ipadx=20, ipady=10, sticky="NSEW")
b3 = tk.Button(root, text="Reboot OS", bg="black", fg="white", command=lambda: sub.call('./reboot.sh'))
b3.grid(column=1, row=1, ipadx=10, ipady=10, sticky="NSEW")

#Loop per non chiudere la finestra
root.mainloop()