import T
#调用 T 实现调用包的功能
class Stic:                            #定义求和以及求平均值的类
    def sum(self,file):                #定义求和以及求平均值的函数
        treader = T.txtreader()        #调用T包中的txtreader函数
        data = treader.parser(file)    #调用函数读取测试文本文件
        sum = i = 0                    #初始化变量
        for item in data:              #遍历文件列表中的所有数据
            sum += int(item[0])        #强制将每个字符串中的首个字符强制转化为整型，进行求和计量
            i = i + 1                  #循环计数，每循环一次增加一个单位
        print("sum=",sum)
        print("avg=",sum/i)

sta = Stic()
sta.sum("test2.txt")
