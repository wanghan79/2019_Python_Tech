lst1 = ["2017","祖祖","15770184697",22]
print(isinstance(lst1,list))
lst1.append("619")
print(lst1)
set1 = {'a', 'z', 'b', 4, 6, 1}
set2 = { "2019","祖祖","15770184697",4,2020,"祖祖"}
set3 = {'a', 'z', 'b',2,0}
set1.add(8)
set2.add('hello')
set4=set1|set2
print(set1)
print(set2)
print(set4)
print(set2.difference(set1))
dic1 = {2017012702:[1,2,3]}
dic2 = {2016012702:[4,5,6]}
dic1.update(b=[2.3])
print(dic1)
dic2.update({2020:[7,8,9]})
dic1.update(dic2)
print(dic1)
print(dic2)
print("数据类型之间的关系")
x=-1
for m in lst1:
    x+=1
    if m in set2:
       lst1.pop(x)
print(lst1)