f = open("yll.txt","r")
lines = f.readline( )     #按行读取文件中的内容
for line in lines:     #循环输出读取的内容
    print (line)
f.close( )