from Opentxt import Opentxt                             #调用类Opentxt
class Statistic():
    def __init__(self, file):                           #初始化属性file
        self.file = file

    def statistic_sum(self):                            #定义求和函数
        txt = Opentxt(self.file)
        datas = txt.openfile()                          #调用类Opentxt中的openfile读取文件
        sum = 0
        for data in datas:                              #求和
            sum = sum+int(data[2])
        return sum

    def statistic_average(self):                        #定义求平均值函数
        txt = Opentxt(self.file)
        datas = txt.openfile()                          #调用类Opentxt中的openfile读取文件
        i = 0
        sum = 0
        for data in datas:
            sum = sum + int(data[2])                    #求和
            i = i+1                                     #计数
        average = sum/i                                 #求平均值
        return average



