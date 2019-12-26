import os

def TXTreader(file):       #定义函数 用以读取文件
    with open(file) as f:  #打开测设文件
        for line in f:     #逐行读取文件数据
            print(line)
    f.close()

TXTreader('test1.txt')     #调用函数，读取测试文件
