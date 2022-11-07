#!/usr/bin/env python3

import random

def LosujLiczby():
    randomNumbers = [0] * 50
    for i in range(50):
        randomNumbers[i] = random.randint(0,100)
    return randomNumbers

def SortujBabelkowoMalejaco(randomNumbers):
    for i in range(len(randomNumbers) - 1, 0, -1):
        for j in range(0, i):
            if randomNumbers[j + 1] > randomNumbers[j]:
                randomNumbers[j], randomNumbers[j + 1] = randomNumbers[j + 1], randomNumbers[j]
    return randomNumbers

def SprawdzCzyPosortowane(randomNumbers, randomNumbersSorted):
    randomNumbers.sort(reverse = True)
    for i in range(len(randomNumbers)):
        if(randomNumbers[i] != randomNumbersSorted[i]):
            print("Algorytm sortowania nie dziala: ")
            print("Expected Value: ", randomNumbers[i], " but you got: ", randomNumbersSorted[i])
            return False
    print("Wszystko zostalo posortowane poprawnie")
    return True


def WyswietlPosortowaneLiczby(randomNumbers):
    for i in range(len(randomNumbers)):
        print(randomNumbers[i])




if __name__ == '__main__':
    randomNumbers = LosujLiczby()
    randomNumbersSorted = SortujBabelkowoMalejaco(randomNumbers)
    if(SprawdzCzyPosortowane(randomNumbers, randomNumbersSorted)):
        WyswietlPosortowaneLiczby(randomNumbersSorted)