#!/usr/bin/env python3

from threading import Semaphore, Thread
import time


semA = Semaphore(1)
semB = Semaphore(0)
semC = Semaphore(0)

def ProblemFilozofow(liczbaFilozofow = 5):
    filozofowie = []
    liczbaWidelcow = []
    for i in range(liczbaFilozofow):
        liczbaWidelcow.append(False)
        filozofowie.append(0)

def printA():
    while True:
        semA.acquire()
        print('A ', end="")
        time.sleep(1)
        semB.release()

def printB():
    while True:
        semB.acquire()
        print('B ', end="")
        time.sleep(1)
        semC.release()

def printC():
    while True:
        semC.acquire()
        print('C ', end="")
        time.sleep(1)
        semA.release()


if __name__ == '__main__':
    print("Zaczynam")
    threads = []  # deklarujemy tablic¦
    threads.append(Thread(target=printA))  # dodajemy do niej procesy jako w¡tki
    threads.append(Thread(target=printB))
    threads.append(Thread(target=printC))
    for thread in threads:
        thread.start()  # uruchamiamy wątki