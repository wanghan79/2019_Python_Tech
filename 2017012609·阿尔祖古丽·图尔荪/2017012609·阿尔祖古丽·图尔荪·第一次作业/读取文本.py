import os


def txtreader(file):
    with open(file) as f:
        for line in f:
            print(line)
    f.close()

txtreader("C:\\Users\SD\Desktop\\2017012609·阿尔祖古丽·图尔荪\\2017012609·阿尔祖古丽·图尔荪·第一次作业\\read.txt")