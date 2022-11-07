#!/usr/bin/env python3
import os

def fileCounterInGivenDirectory(directoryPath = r'/Users/Adrian/Desktop/PwJP_laboratorium/A'):
    fileCounter = 0
    for path in os.listdir(directoryPath):
        if os.path.isfile(os.path.join(directoryPath, path)):
            fileCounter += 1
    print("Liczba plikow w folderze " + directoryPath + " to: ", fileCounter)

# all files in directory and su
def fileCounterInAllSubDirectories(directoryPath = r'/Users/Adrian/Desktop/PwJP_laboratorium/A'):
    fileCounter = 0
    for root_dir, cur_dir, files in os.walk(directoryPath):
        fileCounter += len(files)
    print("Liczba plikow w folderze " + directoryPath + " to: ", fileCounter)


if __name__ == '__main__':
    fileCounterInGivenDirectory()
    fileCounterInAllSubDirectories(r'/Users/Adrian/Desktop/PwJP_laboratorium/A')