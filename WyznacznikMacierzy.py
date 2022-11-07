#!/usr/bin/env python3
import numpy
import random

import numpy as np


def TworzMacierz(rozmiar):
    macierz = []
    for i in range(rozmiar):
        temp = []
        for j in range(rozmiar):
            temp.append(0)
        macierz.append(temp)
    return macierz

def LosujMacierz():
    macierz = TworzMacierz(4)
    for i in range(len(macierz)):
        for j in range(len(macierz)):
            macierz[i][j] = random.randint(-5,5)
    return macierz

def WyznaczWyznacznikMacierzy(macierzA):
    wynik = 0
    indices = list(range(len(macierzA)))
    if len(macierzA) == 2 and len(macierzA[0]) == 2:
        wyznacznikKoncowej = macierzA[0][0] * macierzA[1][1] - macierzA[1][0] * macierzA[0][1]
        return wyznacznikKoncowej

    for i in indices:
        # macierz B -> macierz utworzona z macierzy A pomnniejszona o kolumne i wiersz (zgodnie z rozwinieciem laplace'a)
        macierzB = macierzA.copy()
        macierzB = macierzB[1:]
        wysokosc = len(macierzB)

        for j in range(wysokosc):
            macierzB[j] = macierzB[j][0:i] + macierzB[j][i + 1:]

        sign = (-1) ** (i % 2)  # F)
        sub_det = WyznaczWyznacznikMacierzy(macierzB)
        wynik += sign * macierzA[0][i] * sub_det

    return wynik

def SprawdzCzyDobreWyniki(wynik,macierzA):
    numArray = np.zeros([len(macierzA),len(macierzA)])
    for i in range(len(macierzA)):
        for j in range(len(macierzA)):
            numArray[i][j] = macierzA[i][j]

    if(wynik == round(np.linalg.det(numArray))):
        print("Wyniki sie zgadzaja")
        print("Numpy: ", round(np.linalg.det(numArray)))
        print("Moja funkcja: ", wynik)
    else:
        print("Wyniki sie nie zgadzaja")
        print("Numpy: ", np.linalg.det(numArray))
        print("Moja funkcja: ", wynik)

if __name__ == '__main__':
    macierzA = LosujMacierz()
    wynikObliczen = WyznaczWyznacznikMacierzy(macierzA)
    SprawdzCzyDobreWyniki(wynikObliczen, macierzA)