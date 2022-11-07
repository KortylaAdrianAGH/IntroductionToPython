#!/usr/bin/env python3
import numpy as np
import random

def TworzMacierz(rozmiar):
    macierz = []
    for i in range(rozmiar):
        temp = []
        for j in range(rozmiar):
            temp.append(0)
        macierz.append(temp)
    return macierz

def LosujMacierz(rozmiar):
    macierz = TworzMacierz(rozmiar)
    for i in range(len(macierz)):
        for j in range(len(macierz)):
            macierz[i][j] = random.randint(-5,5)
    return macierz

def MnozenieMacierz(macierzA, macierzB):
    wynik = TworzMacierz(len(macierzA))
    suma = 0
    for i in range(len(macierzA)):
        for j in range(len(macierzA)):
            for k in range(len(macierzA)):
                suma += macierzA[i][k] * macierzB[k][j]
            wynik[i][j] = suma
            suma = 0
    return wynik

def WyswietlMacierz(macierz):
    print(macierz)

def SprawdzCzyDobreWyniki(macierzA, macierzB, wynik):
    numArrayA = np.zeros([len(macierzA),len(macierzA)])
    numArrayB = np.zeros([len(macierzB),len(macierzB)])
    for i in range(len(macierzA)):
        for j in range(len(macierzA)):
            numArrayA[i][j] = macierzA[i][j]
            numArrayB[i][j] = macierzB[i][j]

    numArrayFinal = np.dot(macierzA,macierzB)

    for i in range(len(macierzA)):
        for j in range(len(macierzA)):
            if(wynik[i][j] !=  numArrayFinal[i][j]):
                print("Wartosci nie sa rowne na pozycji i: ", i, " j: ", j)
                print("Numpy: ", numArrayFinal[i][j])
                print("Moj algorytm: ", wynik[i][j])
                return
    print("Mnozenie macierz jest dobre")


if __name__ == '__main__':
    macierzA = LosujMacierz(4)
    macierzB = LosujMacierz(4)

    wynik = MnozenieMacierz(macierzA,macierzB)

    SprawdzCzyDobreWyniki(macierzA,macierzB,wynik)
