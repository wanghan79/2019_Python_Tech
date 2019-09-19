import os


def reader(file):
    with open(file) as f:
        for line in f:
            print(line)
        f.close()
reader("D:\\zhangwl\\Rtxt.txt")