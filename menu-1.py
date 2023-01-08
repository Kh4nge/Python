from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button
import subprocess as subprocess

screen = Tk()
#screen.title("Main Page")

screen.geometry("400x350")
screen.configure(bg="#463E3F")

b1 = Button(screen, text="REBOOT", command=lambda: sub.call('./reboot.sh'))
b1.pack()

screen.wm_attributes("-fullscreen", "True")
screen.mainloop()