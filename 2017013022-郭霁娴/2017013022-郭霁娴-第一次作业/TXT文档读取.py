import os

'''定义TXTreader函数'''
def TXTreader(file):
    with open(file) as f:#打开文件读取数据
        for line in f:#循环输出每行内容
            print(line)
    f.close()

TXTreader('txtreader.txt')

