import os


def txtreader(file):
    with open(file) as f:
        for line in f:
            print(line)
    f.close()

txtreader("D:\\wanghan\\RXml.xml")