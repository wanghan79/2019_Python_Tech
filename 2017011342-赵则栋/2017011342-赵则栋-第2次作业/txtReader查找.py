import os

def txtReader(file):            #定义txt函数
    with open(file) as f:       #打开文件
        row = 0
        container = []          #设置container放置元组
        for line in f:          #遍历文件
            str = line.split(" ")      #用空格将字符串切片
            for col, item in enumerate(str):   #遍历这个可迭代对象
                element = (row, col, item)     #将行列信息赋值给元组
                container.append(element)      #将元组添加到container中
            row += 1
        for element in container:
            if element[2] == "Jiang":
                print(element)                 #打印输出"Jiang"的位置元组信息
txtReader('a.txt')                   #运行函数

