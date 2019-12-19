import os


def txtreader(file):
    with open(file) as f:
        for line in f:
            print(line)
    f.close()

txtreader("C:\\Users\SD\Documents\GitHub\\2019_Python_Tech\\2017010053-韩进辉\\2017010053-韩进辉\\2017010053-韩进辉-第一次作业\\文本.txt")