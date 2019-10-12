import os

def TXTreader(file):
    with open(file) as f:
        for line in f:
            print(line)
    f.close()
TXTreader("E:\\文档\\GitHub\\lxc-2017012702\\reader-test\\TXTreader.html")