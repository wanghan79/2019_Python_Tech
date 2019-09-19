import os


def txt(file):
    with open(file) as f:
        for line in f:
            print(line)
    f.close()



txt("D:\\baimayangjin\\jin.html")


