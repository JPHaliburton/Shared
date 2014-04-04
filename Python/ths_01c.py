# Displacement Vessel Performance Numbers
# written by J. Peter Haliburton
# Initially Started: 2013-12-19
# Restarted On: 2013-12-27
# Latest Update: 2013-12-27
# Version #0.1c
# ----------------------------------------

## Load the Tk interface window builder and math operators
import tkinter as tk
from math import sqrt

## Draw the window
appwin = tk.Tk()
appwin.title("Displacement Vessel Performance Numbers")
appwin.geometry("600x180+150+80")
#appwin.wm_iconbitmap("sailboaticon.ico")

## Application Title Information
authorlabel_1 = tk.Label(text="Displacement Vessel Performance Numbers v0.1c",
                     fg="navy", bg="yellow", font="Times 14 bold").grid(row=0, column=0, columnspan=4,ipadx=100)
authorlabel_2 = tk.Label(text="by J. Peter Haliburton 2013",
                     fg="navy", font="Times 10 italic").grid(row=1, column=0, columnspan=4)

## Collect and process the data


## Formula for calculating hull speed
#def calcths(lwl):
#    ths = (round(1.34*sqrt(lwl),2))

## loop the app
#dvpnapp.mainloop()
## The End!
