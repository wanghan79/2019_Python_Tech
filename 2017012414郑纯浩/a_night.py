import os


def txtreader(file):
    with open(file) as f:
        for line in f:
            print(line)
    f.close()
txtreader("D:\\a_night\\蒟蒻.txt")
txtreader("D:\\a_night\\蒟蒻.xml")