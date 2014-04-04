import tkinter as tk
from math import sqrt

class Application(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.entryVariable = tk.askfloat()
        self.entry = tk.Entry(self,lwl=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Vessel's Waterline Length")

#    def ths(lwl):
#        print(round(1.34*sqrt(lwl),2))

#    lwl=1

#    while lwl != 0:
#    lwl = float(input("Waterline length of vessel?: "))
#    ths(lwl)

#    print("Goodbye!")

if __name__ == "__main__":
    app = Application(None)
    app.title('Displacement Vessel performance')
    app.mainloop()
