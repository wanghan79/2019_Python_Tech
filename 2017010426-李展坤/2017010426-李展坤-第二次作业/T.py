from typing import List, Tuple
#import 特性通常称作模块，此处定义一个新的包
class txtreader:                             #定义读取txt格式文本的类型模块
    def parser(self,file):                   #定义函数
        with open(file) as f:                #打开测试txt文件
            comtainer = []                   #定义列表，用以接受字符串
            for line in f:                   #逐行读取测试文件的每一行
                words = line.split(" ")      #split函数，以空格为标识符拆分字符串，返回结果
                container.append(words)      #append函数
        f.close()
        return container
