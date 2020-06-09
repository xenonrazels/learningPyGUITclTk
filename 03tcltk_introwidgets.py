from tkinter import *
from tkinter import ttk
root = Tk()
logo=PhotoImage(file="kct-logo.png")

btn = ttk.Button(root, text="Proceed")
btn.pack()
def proceed():
    print("clicked!")
btn.config(command=proceed)
label=ttk.Label(root,text="Welcome!!")
label.pack()
btn.config(image=logo,compound=LEFT)
small_logo=logo.subsample(5,5)
btn.config(image=small_logo)


