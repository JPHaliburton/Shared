from math import sqrt

def ths(lwl):
    print(round(1.34*sqrt(lwl),2))

lwl = float(input("Waterline length of vessel?: "))

ths(lwl)
