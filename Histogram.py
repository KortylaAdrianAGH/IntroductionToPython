#!/usr/bin/env python3

import shutil

import random
import os
import time
import multiprocessing

def createDirectory():
    directory = "PlikiDoObrobienia"
    parent_dir = '/Users/Adrian/Desktop/PwJP_laboratorium'

    path = os.path.join(parent_dir, directory)
    shutil.rmtree(path)
    os.mkdir(path)
    return path

def creating_file(number, directoryPath, name):
    path = os.path.join(directoryPath + "/" + name)
    temp_file = open(path, 'w')
    for i in range(number):
        temp_file.write(str(random.randint(1, 5000)) + "\n")
    temp_file.close()
    time.sleep(3)   # previous value 2
    print('Created file {}'.format(path))

def countAverageInFile(path, return_dict):
    tempfile = open(path,'r')
    sum = 0
    elementsCounter = 0
    for i in tempfile:
        sum += int(i)
        elementsCounter += 1
    tempfile.close()
    avg = float(sum) / elementsCounter
    print("Srednia wartosc w pliku: {} to: {}".format(path,avg))
    time.sleep(2)
    return_dict[path] = avg


def pathCreator(directoryPath, name):
    path = os.path.join(directoryPath + "/" + name)
    return path

def countAverageSystem(dict):
    sum = 0
    elementsToCount = 0

    for key, value in dict.items():
        sum += value
        elementsToCount += 1
    avg = float(sum) / elementsToCount
    print("Srednia wartosc wszystkich plikow to: {}".format(avg))


if __name__ == '__main__':
    starttime = time.time()
    processes = []
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    pathToDirectory = createDirectory()
    for i in range(0, 10):
        createFile = multiprocessing.Process(target=creating_file, args=(100,pathToDirectory,"plik" + str(i+1) + ".txt"))
        processes.append(createFile)
        createFile.start()

    for process in processes:
        process.join()

    for i in range(0,10):
        print((pathCreator(pathToDirectory, "plik" + str(i+1) + ".txt")))
        countAverageFile = multiprocessing.Process(target=countAverageInFile, args=(pathCreator(pathToDirectory,"plik" + str(i+1) + ".txt"), return_dict))
        processes.append(countAverageFile)
        countAverageFile.start()

    time.sleep(3)
    print(return_dict)
    countAverageSystem(return_dict)

    print('To zajelo: {} '.format(time.time() - starttime))
