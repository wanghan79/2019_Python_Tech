class txt_reader:                                        #定义读取txt文件类
    def txt_reading_list(self,file):                 #定义读取txt文件类的读取txt的内置函数
        with open(file) as f:                         #打开文件
            container=[]                               #定义列表
            for line in f:                                #遍历文件
                words=line.split(" ")               #拆分字符串，将一行按照空格拆开
                container.append(words)      #将拆分的字符串的列表加入到预定作为返回值得列表容器中
        f.close()                                        #关闭文件
        return container                          #返回包含字符串列表的列表