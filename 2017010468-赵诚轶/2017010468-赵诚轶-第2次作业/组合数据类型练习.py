'''tuple类型练习'''
print("tuple类型练习")
tup1 = ("2017","zhaocy","13837255970",22)
print(tup1)
print(tup1.count(22))
print(hash(tup1))

'''list类型练习'''
print("list类型练习")
lst1 = ["2017","zhaocy","13837255970",22]
print(isinstance(lst1,list))
lst1.append("619")
print(lst1)

'''set类型练习'''
print("set类型练习")
set1 = {'a', 'z', 'b', 4, 6, 1}
set2 = { "2015","zhaocy","17833111872",4,2017,"zhaocy"}
set3 = {'a', 'z', 'b',2,0}
set1.add(8)
set2.add('hi')
set4=set1|set2
print(set1)
print(set2)
print(set4)
print(set1.difference(set2.difference(set3)))
print(set2.difference(set1))
print(set1&set2)
print(set1|set2)
print(set1-set2)
print(set2-set1)

'''dict类型练习'''
print("dict类型练习")
dic1 = {2017010468:[1,2,3]}
dic2 = {2016010468:[4,5,6]}
dic1.update(b=[2.3])
print(dic1)
dic2.update({2020:[7,8,9]})
dic1.update(dic2)
print(dic1)
print(dic2)

'''数据类型之间的关系'''
print("数据类型之间的关系")
print("set1.add(lst1)    无法互加，因为set是可变值，无法哈希。list顺序结构。")
x=-1
for m in lst1:
    x+=1
    if m in set2:
       lst1.pop(x)
print(lst1)