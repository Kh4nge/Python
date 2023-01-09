from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button
import subprocess
import tkinter as tk
from tkterminal import Terminal
import os
from tkinter.messagebox import showwarning

root = tk.Tk()
root.title("WiFi Page")
root.geometry("480x320")
root.configure(bg="#463E3F")
xterm_frame = tk.Frame(root)
xterm_frame.pack(fill=tk.BOTH, expand=True)
frame1 = tk.Frame(root)
frame1.pack()

xterm_frame_id = xterm_frame.winfo_id()

try:
    p = subprocess.Popen(
        ["xterm", "-into", str(xterm_frame_id), "-geometry", "80x20"],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE)
except FileNotFoundError:
    showwarning("Error", "xterm is not installed")
    raise SystemExit

#terminal = Terminal()
#terminal.shell = True
#terminal.pack(expand=True, fill='both')
#terminal.grid(column=1, rowspan=3, sticky="NSEW")

b2 = tk.Button(frame1, text="WiFi-Sniffer", bg="black", fg="white", command=lambda: terminal.run_command('sh ./xterm.sh'))

#Loop for not close the window
root.mainloop()