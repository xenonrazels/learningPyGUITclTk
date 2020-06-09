from tkinter import *
from tkinter import ttk
class hello_app:
    def __init__(self,master):
        self.label=ttk.Label(master,text="hello gui")
        self.label.grid(row=0, column=0, columnspan = 2)
        ttk.Button(master, text="texas", command=self.taxes_hello).grid(row=1, column=0)
        ttk.Button(master, text='finnish', command=self.finish_hello).grid(row=1, column=1)
    def taxes_hello(self):
        self.label.config(text="hola in texas").grid(row=0,column=0,columnspan=2)
    def finish_hello(self):
        self.label.config(text="suhollaa in finish") 



def main():
    root = Tk()
    app = hello_app(root)
    root.mainloop()

if __name__ =="__main__":
    main()
