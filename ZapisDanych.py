#!/usr/bin/env python3

def pinUserInput():
    pin = input("Podaj 4 cyfrowy szyfr: ")
    return pin


def ifUserInputIsValid():
    while(1):
        pin = pinUserInput()
        if len(pin) != 4:
            print("Wprowadzono szyfr w niepoprawnej postaci\nWprowadz go jeszcze raz")
        else:
            break;
    return pin


def checkIfPinMatches(originalPin):
    pin = ifUserInputIsValid()
    if pin == originalPin:
        print("Oba piny się zgadzają")
    else:
        print("Wprowadzone piny różnia się")



if __name__ == '__main__':
    originalPin = ifUserInputIsValid()
    checkIfPinMatches(originalPin)
