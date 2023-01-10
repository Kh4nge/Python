from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button
import subprocess
import tkinter as tk
import os

root = tk.Tk()
root.title("WiFi Page")
root.geometry("480x320")
root.configure(bg="#463E3F")
root.attributes("-fullscreen", True)

xterm_frame = tk.Frame(root, bg="black")
xterm_frame.pack(fill=tk.BOTH, expand=True)
frame1 = tk.Frame(root)
frame1.pack()

xterm_frame_id = xterm_frame.winfo_id()
xterm_frame.place(x=120, y=0, width=360, height=320)

def ls():
    xterm_frame.bind('<B1-Motion>', motion)

b1 = tk.Button(root, text="CLOSE", bg="black", fg="white", command=root.destroy, activeforeground="black", activebackground="red")
b1.place(x=0, y=0, width=120, height=80)

b2 = tk.Button(root, text="1. New-File", bg="black", fg="white", activeforeground="black", activebackground="red")
b2.place(x=0, y=80, width=120, height=80)
#command=subprocess.Popen(["xterm", "-into", str(xterm_frame_id), "-e", "ls"]

b3 = tk.Button(root, text="2. Start", bg="black", fg="white", command=root.destroy, activeforeground="black", activebackground="red")
b3.place(x=0, y=160, width=120, height=80)

b4 = tk.Button(root, text="Stop", bg="black", fg="white", command=root.destroy, activeforeground="black", activebackground="red")
b4.place(x=0, y=240, width=120, height=80)

try:
    p = subprocess.Popen(
        ["xterm", "-into", str(xterm_frame_id), "-geometry", "360x320"],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE)
except FileNotFoundError:
    showwarning("Error", "xterm is not installed")
    raise SystemExit

#Loop for not close the window
root.mainloop()