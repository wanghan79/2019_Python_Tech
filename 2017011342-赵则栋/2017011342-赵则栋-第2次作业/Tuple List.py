stu=("111111","张三","17826376592",22)    #创建一个tuple
print(stu[1])                           #打印第2个元素
for i in stu:                           #遍历这个元组
    print(i)
b=stu.count("张")                       #统计张出现的次数
print(b)
stu1=["111111","张三","17826376592",22]  #创建一个列表
for i in stu1:                           #遍历这个列表
    print(i)
stu1.append("李四")                      #添加"李四"进列表
print(stu1)                             #打印元组
