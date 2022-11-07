#!/usr/bin/env python3
import math

# import
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


#TODO parsing input problem :d
class Kalkulator:
    def __init__(self):
        while(True):
            num1 = complex(input("Enter first number: "))
            num2 = complex(input("Enter second number: "))

            # try except expression

            num1 = LiczbaZespolona(num1.real, num1.imag)
            num2 = LiczbaZespolona(num2.real, num2.imag)

            operation = input("Enter valid operator: ")

            if operation == '+':
                wynik = num1 + num2

            elif operation == '-':
                wynik = num1 - num2

            elif operation == '*':
                wynik = num1 * num2

            elif operation == '/':
                wynik = num1 / num2

            elif operation == 'end':
                print("You close calculator properly")
                break

            else:
                print("You entered wrong operator!")

            print(wynik.WyswietlLiczbaZespolona())


if __name__ == '__main__':
    k = Kalkulator()