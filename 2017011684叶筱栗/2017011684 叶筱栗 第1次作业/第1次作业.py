import os

'''第一次作业：打开txt文档
写一个函数，按行打开，调用函数打开D盘名为text.txt的文档'''
def txtReader(file):
    with open(file) as f:
        for line in f:
            print(line)
    f.close()

txtReader("D:\\yexiaoli\\text.txt")

