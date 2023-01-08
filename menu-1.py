from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button
import subprocess as subprocess

screen = TK()
screen.title("Main Page")
screen.geometry("200x170")
screen.configure("#463E3F")

b1 = Button(screen, text="REBOOT", command=lambda: sub.call('./command.sh'))
b1.pack(side=TOP, pady=5)

screen.mainloop()