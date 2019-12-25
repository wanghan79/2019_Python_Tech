import os
import shutil

def reader(file):
    with open(file) as f:
        for line in f:
            print(line)
        f.close()

reader("E:\\Pycharm_zhangwl\\2019_Python_Tech\\2017010186_张雯丽\\2017010186-张雯丽-第一次作业\\txt.txt")