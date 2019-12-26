import classtestT                                 

class SolvingSumAvg:                                  #定义求和以及求平均值的类
    def SumAvg(self,file):                               #定义求和以及求平均值的函数
        txtreading=classtestT.txt_reader()         
        data=txtreading.txt_reading_list(file)    
        sum=loop_num=0                                
        for item in data:                                   #遍历读取文件之后的列表
            sum+=int(item[0])                            
            loop_num=loop_num+1                   #循环计数
        print("和 ",sum)                                    #输出sum的求和结果
        print("平均值 ",sum/loop_num)             #输出由和以及行数得出来的平均值

sta=SolvingSumAvg()                               
sta.SumAvg('why.txt')                         
