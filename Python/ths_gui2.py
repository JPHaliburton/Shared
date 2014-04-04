# Displacement Vessel Performance Numbers
# written by J. Peter Haliburton
# Started: 2013-12-19
# Latest Update: 2013-12-22
# ----------------------------------------
# Import Window builder and math operators
from tkinter import *
from math import sqrt
# Define app's working name
dvpnapp = Tk()
# Define variables
getlwl=StringVar()
ths=StringVar()
# Formula for calculating hull speed
def calcths(lwl):
#    lwlout = boatlwl.get()
#    lwl = float(getlwl.get())
    lwllabel_1 = Label(lwl).grid(row=5, column=0, columnspan=4)
    ths = (round(1.34*sqrt(lwl),2))
# Draw the app window
dvpnapp.geometry('600x180+150+80')
dvpnapp.title("Displacement Vessel Performance Numbers")
# Place app titles
authorlabel_1 = Label(text="Displacement Vessel Performance Numbers v0.1b",
                     fg="navy", bg="yellow", font="Times 14 bold").grid(row=0, column=0, columnspan=4,ipadx=100)
authorlabel_2 = Label(text="by J. Peter Haliburton 2013",
                     fg="navy", font="Times 10 italic").grid(row=1, column=0, columnspan=4)
authorlabel_3 = Label(text="").grid(row=2, column=0, columnspan=4)
spacerlabel_1 = Label(text="").grid(row=3, column=0, columnspan=4)
# App input and output
lwllabel = Label(text="Waterline length of vessel in feet?: ").grid(row=4, column=0)
lwlentry = Entry(dvpnapp, textvariable=getlwl,width=8).grid(row=4, column=1, sticky=W)
lwl = getlwl.get()
thslabel = Label(text="Maximum calculated speed in knots is:").grid(row=4, column=2)
thsoutput = Label(text=ths).grid(row=4, column=3)
# Position the button
spacerlabel_2 = Label(text="").grid(row=5, column=0, columnspan=4)
calcbutton = Button(dvpnapp, text="Calculate", command=calcths).grid(row=6, column=0, columnspan=4)

# Formula for calculating hull speed
def calcths(lwl):
#    lwlout = boatlwl.get()
#    lwl = float(getlwl.get())
    lwllabel_1 = Label(lwl).grid(row=5, column=0, columnspan=4)
    ths = (round(1.34*sqrt(lwl),2))

# loop the app
dvpnapp.mainloop()
# The End!
