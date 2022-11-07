#!/usr/bin/env python3
import os

def filesTreeOutput():
    path = os.path.expanduser("/Users/Adrian/PycharmProjects/PwJP_laboratorium/A")
    for root, d_names, f_names in os.walk(path):
        print(root, d_names, f_names)

if __name__ == '__main__':
    filesTreeOutput()