#!/usr/bin/env python3
import os
from PIL import Image


def findAllJpgFIles():
    path = os.path.realpath('/Users/Adrian/PycharmProjects/PwJP_laboratorium/JpgIntoPng')
    filesList = []
    for root, d_names, f_names in os.walk(path):
        for i in f_names:
            print(i)
            filesList.append(os.path.realpath(path+'/'+i))
    return filesList


def jpgToPdfConverter(pathToFilesList):
    imList = []
    for i in pathToFilesList:
        imList.append(Image.open(i).convert('RGB'))

    for i in range(len(pathToFilesList)):
        imList[i].save(pathToFilesList[i][:len(pathToFilesList)-3] + "jpg")




if __name__ == '__main__':
    jpgToPdfConverter(findAllJpgFIles())