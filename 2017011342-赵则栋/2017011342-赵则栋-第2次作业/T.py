from typing import List,Tuple

class txtReader:                 #创建txtReader类
    def parser(self,file):       #定义parser函数
        with open(file) as f:    #打开文件
            row = 0
            container = []       #创建一个container放列表
            for line in f:       #遍历文件
                words = line.split(" ")   #用空格切片
                container.append(words)   #将切片列表放入container
        f.close()                         #关闭文件
        return container                  #返回container



