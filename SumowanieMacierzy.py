#!/usr/bin/env python3
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

#funkcja losujaca macierz 128 x 128
def LosujMacierz():
    macierz = TworzMacierz(128)
    for i in range(128):
        for j in range(128):
            macierz[i][j] = random.randint(0,100)
    return macierz

def SumowanieMacierzy(macierzA, macierzB):
    wynik = TworzMacierz(128)
    for i in range(128):
        for j in range(128):
            wynik[i][j] = macierzA[i][j] + macierzB[i][j]
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

    numArraySum = numArrayA + numArrayB

    for i in range(len(macierzA)):
        for j in range(len(macierzA)):
            if(wynik[i][j] !=  numArraySum[i][j]):
                print("Wartosci nie sa rowne na pozycji i: ", i, " j: ", j)
                return
    print("Sumowanie jest dobre")

if __name__ == '__main__':
    macierzA = LosujMacierz()
    macierzB = LosujMacierz()

    wynik = SumowanieMacierzy(macierzA, macierzB)
    SprawdzCzyDobreWyniki(macierzA,macierzB,wynik)
