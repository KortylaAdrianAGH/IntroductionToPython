#!/usr/bin/env python3
import math

class LiczbaZespolona:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def WyswietlLiczbaZespolona(self):
        if(self.imag >= 0):
            return f"{self.real}+{self.imag}j"
        else:
            return f"{self.real}{self.imag}j"

    def getReal(self):
        return self.real

    def getImag(self):
        return self.imag

    def __add__(self, liczbaZespolona2):
        real = self.real + liczbaZespolona2.getReal()
        imag = self.imag + liczbaZespolona2.getImag()
        return LiczbaZespolona(real, imag)

    def __sub__(self, liczbaZespolona2):
        real = self.real - liczbaZespolona2.getReal()
        imag = self.imag - liczbaZespolona2.getImag()
        return LiczbaZespolona(real, imag)

    def __mul__(self, liczbaZespolona2):
        real = self.real * liczbaZespolona2.getReal() - self.imag * liczbaZespolona2.getImag()
        imag = self.real * liczbaZespolona2.getImag() + self.imag * liczbaZespolona2.getReal()
        return LiczbaZespolona(real, imag)

    def __truediv__(self, liczbaZespolona2) :
        real = (self.real * liczbaZespolona2.getReal() + self.imag * liczbaZespolona2.getImag()) / (math.pow(liczbaZespolona2.getReal(), 2) + math.pow(liczbaZespolona2.getImag(), 2))
        imag = (self.imag * liczbaZespolona2.getReal() - self.real * liczbaZespolona2.getImag()) / (math.pow(liczbaZespolona2.getReal(), 2) + math.pow(liczbaZespolona2.getImag(), 2))
        return LiczbaZespolona(real, imag)

def SprawdzPoprawnoscDzialan(liczba1, liczba2):
    liczba1Complex = complex(liczba1.getReal(), liczba1.getImag())
    liczba2Complex = complex(liczba2.getReal(), liczba2.getImag())
    print("Sprawdzam poprawnosc dodawania")
    print("Wbudowana funkcja: ", liczba1Complex + liczba2Complex)
    wynik = liczba1 + liczba2
    print("Moj algorytm: ", wynik.WyswietlLiczbaZespolona())

    print("Sprawdzam poprawnosc odejmowania")
    print("Wbudowana funkcja: ", liczba1Complex - liczba2Complex)
    wynik = liczba1 - liczba2
    print("Moj algorytm: ", wynik.WyswietlLiczbaZespolona())

    print("Sprawdzam poprawnosc mnozenia")
    print("Wbudowana funkcja: ", liczba1Complex * liczba2Complex)
    wynik = liczba1 * liczba2
    print("Moj algorytm: ", wynik.WyswietlLiczbaZespolona())

    print("Sprawdzam poprawnosc dzielenia")
    print("Wbudowana funkcja: ", liczba1Complex / liczba2Complex)
    wynik = liczba1 / liczba2
    print("Moj algorytm: ", wynik.WyswietlLiczbaZespolona())

if __name__ == '__main__':
    liczba1 = LiczbaZespolona(1,2)
    liczba2 = LiczbaZespolona(1,-2)
    liczba1.WyswietlLiczbaZespolona()
    liczba2.WyswietlLiczbaZespolona()

    SprawdzPoprawnoscDzialan(liczba1,liczba2)
