import classtestT                                  #调用classtestT，实现调用包的功能

class solving_sum_avg:                             #定义求和以及求平均值的类
    def sum_avg(self,file):                        #定义求和以及求平均值的函数
        txtreading=classtestT.txt_reader()         #调用classtestT包中的txt_reader类，方便读取文件
        data=txtreading.txt_reading_list(file)     #调用txt_reader类中的txt_reading_list函数，读取文件
        sum=loop_num=0                             #初始化用来求和的整形变量和用来求行数的整形变量
        for item in data:                          #遍历读取文件之后的列表
            sum+=int(item[0])                      #将每个字符串列表的第一个字符串强制转化为整形，再加到sum中
            loop_num=loop_num+1                    #循环计数
        print("和 ",sum)                           #输出sum的求和结果
        print("平均值 ",sum/loop_num)              #输出由和以及行数得出来的平均值

sta=solving_sum_avg()                             #创建求和以及求平均值的变量
sta.sum_avg('a_night.txt')                        #调用变量中的内置求和以及求平均值函数