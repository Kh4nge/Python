from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button
import subprocess as sub

screen = Tk()
#screen.title("Main Page")

screen.geometry("400x350")
screen.configure(bg="#463E3F")

b1 = Button(screen, text="WiFi-Sniffer", command=lambda: sub.call('./wifi_sniffer.sh'))
b1.pack()

b2 = Button(screen, text="Reboot OS", command=lambda: sub.call('./reboot.sh'))
b2.pack()

screen.mainloop()