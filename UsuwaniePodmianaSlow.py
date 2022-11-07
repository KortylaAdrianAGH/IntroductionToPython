#!/usr/bin/env python3
import os

def eraseGivenWordsFromStringInput():
    with open(os.path.abspath('/Users/Adrian/PycharmProjects/PwJP_laboratorium/Tekstowego/input1.txt'), 'r') as file:
        for line in file:
            print("Original Line:\n" + line)
            print(eraseGivenWords(line))
        file.close()

def eraseGivenWords(line):
    word = ['się', 'oraz', 'nigdy', 'dlaczego', ' i ']
    for w in word:
        line = line.replace(w, '')
    return ("Replaced Line:\n" + line)


def replaceGivenWordsFromStringInput():
    with open(os.path.abspath('/Users/Adrian/PycharmProjects/PwJP_laboratorium/Tekstowego/input1.txt'), 'r') as file:
        for line in file:
            print("Original Line:\n" + line)
            print(replaceWords(line))
        file.close()


def replaceWords(line):
    wordToBeReplaced = [' i ', 'oraz', 'nigdy', 'dlaczego', ]
    wordReplacement = [' Oraz ', 'i', 'prawie nigdy', 'czemu']
    for i in range(len(wordToBeReplaced)):
        line = line.replace(wordToBeReplaced[i], wordReplacement[i])
    return line


if __name__ == '__main__':
    eraseGivenWordsFromStringInput()
    print("\n\n")
    replaceGivenWordsFromStringInput()