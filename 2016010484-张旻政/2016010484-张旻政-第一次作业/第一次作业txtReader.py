def txtreader(file):                         # 定义一个文件读取函数
    with open(file) as f:                    # 打开文件
        for line in f:                       # 依次打印每一行
            print(line)
    f.close()                                # 关闭文件

txtreader('test.txt')                        # 运行函数读取txt文件

