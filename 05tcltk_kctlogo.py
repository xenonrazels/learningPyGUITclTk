from tkinter import *
from tkinter import ttk
root = Tk()
label = ttk.Label(root, text="HELLO TO SAMAJIK")
label.pack()
label.config(text="WElCOME!!! to KCT desktop applications.Now explore the kct learning desktop app")
label.config(wraplength=400)
logo=PhotoImage(file="kct-logo.png")
label.img = logo
label.config(justify='center')
label.config(foreground='white', background='orange')
label.config(font=('sans-serif', 20, 'bold'))
label.config(compound='left')
label.config(image=label.img)

