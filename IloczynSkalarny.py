#!/usr/bin/env python3

import numpy as np
def PoliczIloczynSkalarny():
    a = [1, 2, 12, 4]
    b = [2, 4, 2, 8]
    wynikIloczynu = 0
    for i in range(len(a)):
        wynikIloczynu += a[i] * b[i]
    return a, b, wynikIloczynu


def SprawdzCzyDobreWyniki(macierzA, macierzB, wynik):
    numArrayA = np.zeros(len(macierzA))
    numArrayB = np.zeros(len(macierzB))
    for i in range(len(macierzA)):
        numArrayA[i]= macierzA[i]
        numArrayB[i] = macierzB[i]

    numArrayFinal = np.dot(macierzA,macierzB)

    for j in range(len(macierzA)):
            if(wynik !=  numArrayFinal):
                print("Wartosci nie sa rowne:")
                print("Numpy: ", numArrayFinal)
                print("Moj algorytm: ", wynik)
                return
    print("Iloczyn wektorowy jest dobre")

if __name__ == '__main__':
    macierzA, macierzB, wynikAlgorytmu = PoliczIloczynSkalarny()
    SprawdzCzyDobreWyniki(macierzA,macierzB,wynikAlgorytmu)