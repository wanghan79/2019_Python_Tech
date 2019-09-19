import os

def txtReader(file):
    with open(file) as f:
        for line in f:
            print(line)
    f.close()
txtReader("D:\\arzu\\MW")

