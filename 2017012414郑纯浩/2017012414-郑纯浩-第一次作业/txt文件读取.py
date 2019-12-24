import os                       #头文件

def txtreader(file):            #定义txt文件读取函数
    with open(file) as f:       #打开txt文件
        for line in f:          #遍历txt文件
            print(line)         #输出
    f.close                     #关闭txt文件

txtreader('a_night.txt')        #使用txt文件读取函数