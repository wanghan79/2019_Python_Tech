print('元组操作练习：')
students = ('2016010484', 'ZhangMinzheng', '13159562120', 21)
for stu in students:                                                 # 打印元组stu的元素
    print(stu)

print('元素个数为：', students.count('ZhangMinzheng'), '\n')         # 打印元素‘ZhangMinzheng’的个数

print('列表操作练习：')
students = ['2016010484', 'ZhangMinzheng', '13159562120', 21]        # 创建列表

for s in students:                                                   # 打印列表中的元素
    print(s)

print(isinstance(students, list))                                    # 判断stu是否是list
students.append('971018')                                            # stu增加元素'971018'
print(students[-1], '\n')                                            # 打印最后一个元素


print('集合操作练习：')
stuset = set(students)                                               # 将列表stu转化为集合
print(stuset)

stub = {'2016010484', 'ZhangMinzheng', '19971018', 22}
stu3 = ['222', 'ssss']

set2 = {'2016010484', '2016010484', 'ZhangMInzheng', 2000}
print(set2)

stuset.add('2016010484')                                             #加入重复学号
print(stuset, '\n')

stub = {'2016010484', 'ZhangMinzheng', '19971018', 22}
print(stuset.difference(stub))                                       #返回一个集合的差集
print(stuset.intersection(stub))                                     #两个集合取交集
print(stuset.union(stub), '\n')                                      #集合取并集

print('字典操作练习：')
studict = {'学号': students[0], '姓名': students[1], '电话': students[2], '年龄': students[3]}  #创建字典
print(studict)

(studict.update({'name': 'Zhang'}))                                  #增加新的字典键值
print(studict)

studict['ID'] = '370802'                                             #增加新的字典键值
print(studict)

studict2 = {'学生1': students}                                       #字典里的嵌套
print(studict2)



