str1="today we are lucky!today we are lucky!"
str2="today"
str3="we"
print(str1.capitalize())                            #首字母大写
print(str1.count(str2))                             #计数
print(str1.endswith(str1))                          #判断是否用str1结尾
print(str1.endswith(str1,1,5))                      #判断从1到4是否用str1结尾
print(str1.find(str2)," ",str1.find(str3))          #查找str2和str3在str1中出现的第一个位置
print(str1.index(str2))                             #查找str2的位置
print(str1.replace("are","was"))                    #将str1中的are替换成was
print(str1.rfind(str2))                             #在str1中反向查找str2
print(str1.split(' ',2))                            #将str1以空格分隔，最大分割为三部分





