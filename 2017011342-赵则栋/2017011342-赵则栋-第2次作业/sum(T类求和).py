import T  #导入T包

class Sum:   #建立Sum类
    def sum(self, file):       #建立sum函数
        treader=T.txtReader()    #调用T类中的txtReader函数
        data=treader.parser(file)   #调用parser函数
        sum = 0
        for item in data:           #遍历data
            sum+=int(item[0])       #累加item中的第一个整数
        print(sum)

result= Sum()                       #创建result对象
result.sum("a1.txt")                #调用函数打开文件