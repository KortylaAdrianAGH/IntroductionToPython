#!/usr/bin/env python3

import math

def CalculateDelta(a,b,c):
    return b*b-4*a*c

def RozwiazRownanieKwadratowe():
    a = float(input("Wprowadz wspolczynnik a rownania kwadratowego: "))
    b = float(input("Wprowadz wspolczynnik b rownania kwadratowego: "))
    c = float(input("Wprowadz wspolczynnik c rownania kwadratowego: "))
    delta = CalculateDelta(a,b,c)
    if(delta < 0):
        print("Brak rozwiazan rownania")
    elif (delta == 0):
        print("Istnieje jedno rozwiazanie: ", -b/2*a)
    else:
        print("Istnieja dwa rozwiazania x1: ", (-b-math.sqrt(delta))/2*a, " oraz x2: ", (-b+math.sqrt(delta))/2*a)

if __name__ == '__main__':
    RozwiazRownanieKwadratowe()