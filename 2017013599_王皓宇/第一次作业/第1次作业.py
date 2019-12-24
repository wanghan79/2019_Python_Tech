import os


def txtReader(file):        #定义一个函数
    with open(file) as f:   #打开文档
        for line in f:           #遍历文档
            print(line)          #输出文档
    f.close()                     #关闭文档
 
txtReader("D:\\wanghaoyu\\text.txt")

