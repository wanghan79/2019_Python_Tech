stu=("20170116894", "叶筱栗", "叶筱栗", "15568838427", 20)

print(stu[0])
for i in range(4):
    print(stu[i])

print(stu.count("叶筱栗"))

List=["20170116894", "叶筱栗", "叶筱栗", "15568838427", 20]
print(List[0])
print(isinstance(stu,tuple))
print(isinstance(List,list))
List.append("爱吃面")
print(List)

stuSet=(stu, List)
print(stuSet)