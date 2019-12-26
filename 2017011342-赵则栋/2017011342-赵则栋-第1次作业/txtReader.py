import os

def txtReader(file):     #定义文本读取函数
    with open(file) as f:   #打开txt
        for line in f:      #遍历txt文件
            print(line)     #打印输出
    f.close()               #关闭文件
txtReader("a.txt")          #运行函数
