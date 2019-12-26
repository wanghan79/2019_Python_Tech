from typing import Union, Tuple, Set



stu=("2017010986","zhangyn","1783313",40)
for string in stu:
    print('当前内容:',string)
#输出当前内容


stu=("zhangyn","zhangyn","20190101","zhang",18)
print(stu.count("zhangyn"))
#统计字符串里某个字符出现的次数


stu=["zhangyn","zhangyn","20190101","zhang",18]
print(isinstance(stu,list))
#判断一个对象是否是一个已知的类型


stu={"2017","2016","2015","2014"}
stu.add("2014")
print(stu)
#给集合添加元素


stu=["2017","2016","2015","2014"]
stu.append(2019)
print(stu)
#在列表末尾添加新的对象


stu={"zhangyn","201701",18,"ruan"}
stu2={"zhangwl","201702",18,"ying"}
print(stu.difference(stu2))
print(stu2.difference(stu))
#用于返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中


stu={"zhangyn","201701",18,"ruan"}
stu2={"zhangwl","201702",18,"ying"}
print(stu2^stu)
print(stu2-stu)
print(stu2|stu)
print(stu2&stu)
#运算符


stu={"2017010986":["zhangyn",18,1234566]}
stu.update({"201701":["zhang",1,1234]})
print(stu)
stu.update({"2017010986":["zhangyn",1,1234]})
print(stu)
#用于修改当前集合，可以添加新的元素或集合到当前集合中，如果添加的元素在集合中已存在，则该元素只会出现一次，重复的会忽略
