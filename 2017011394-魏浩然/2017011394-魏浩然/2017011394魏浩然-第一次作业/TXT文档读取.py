import os

'''定义TXTreader函数'''
def TXTreader(file):
    with open(file) as f:
        for abcd in f:
            print(abcd)
    f.close()

TXTreader('TXT1.txt')

