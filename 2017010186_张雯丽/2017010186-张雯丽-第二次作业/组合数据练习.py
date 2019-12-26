#tuple类型练习
print("tuple类型练习：")
str = ("2017010186","zhangwl","15643114349",20)
print(str)
print("20在str中出现的次数：",str.count(20))
print(hash(str))
print("\n")

#list类型练习
print("list类型练习：")
str1 = ["2017010186","zhangwl"]
print("判断str1是否在str中：",isinstance(str1,list))
str1.append("160")
print(str1)
print("\n")

#set类型练习
print("set类型练习：")
set1 = {'a', 'z', 'b', 4, 6, 1}
set2 = { "2017010186","zhangwl","15643114349",6,"2017010186","zhangwl"}
set3 = {'a', 'z', 'b',2,0}
set1.add(8)
set2.add('keke')
print("将8增加到set1中：",set1)
print("将keke增加到set2中：",set2)
print("set1与set2不同的数量：",set1.difference(set2.difference(set3)))
print("set1与set2不同的字符串：",set2.difference(set1))
print("set1与set2相同的字符串：",set1&set2)
print("取set1与set2的并集：",set1|set2)
print("取set1与set2的差集：",set1-set2)
print("取set2与set1的差集：",set2-set1)
print("\n")

#dict类型练习
print("dict类型练习：")
dic1 = {2017010186:[1,2,3]}
dic2 = {2017010986:[4,5,6]}
dic1.update(b=[2.3])
print(dic1)
dic2.update({2020:[7,8,9]})
dic1.update(dic2)
print(dic1)
print(dic2)
print("\n")

#数据类型之间的关系
print("数据类型之间的关系")
#print(set1.add(str1))  无法互加，因为set是可变值，无法哈希。list顺序结构。
x=-1
for m in str1:
    x+=1
    if m in set2:
       str1.pop(x)
print(str1)