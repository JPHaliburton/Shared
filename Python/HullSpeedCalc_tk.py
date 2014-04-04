from tkinter import *
from math import sqrt

class App(object):
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("Hull Speed Calc")
        self.label = Label (self.root, text= "Enter your boat's waterline length.")
        self.label.pack()

        self.entrytext = StringVar()
        Entry(self.root, textvariable=self.entrytext).pack()

        self.buttontext = StringVar()
        self.buttontext.set("Calculate")
        Button(self.root, textvariable=self.buttontext, command=self.clicked1).pack()

        self.label = Label (self.root, text="")
        self.label.pack()

        self.root.mainloop()

    def clicked1(self):
        input = self.entrytext.get()
        result = round(1.34*sqrt(float(input)),2)
        self.label.configure(text=result)

    def button_click(self, e):
        pass

App()
