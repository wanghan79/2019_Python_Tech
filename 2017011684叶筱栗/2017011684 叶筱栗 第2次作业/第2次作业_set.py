
List=["20170116894", "叶筱栗", "15568838427", 20]
List2=["0002", "列表零零二", 20,"12345678910"]
List3=["0003", "列表零零三", 21,"12345678910"]
List4=["0004", "列表零零四", 20,"12345678910"]

stuSet={101, "集合一零一", 20, "00000000001"}
print(stuSet)
#添加不同元素
stuSet.add(102)
print(stuSet)
#添加相同元素
stuSet.add(101)
print(stuSet)
#difrence:差异
stuSet2={102, "集合一零二", 20, "00000000001"}
print(stuSet.difference(stuSet2))
print(stuSet2.difference(stuSet))
#交集
print(stuSet.intersection(stuSet2))
print(stuSet&stuSet2)
#并集
print(stuSet.union(stuSet2))
print(stuSet|stuSet2)

#字典
stuDict={"001":["零零一", 20, "0000001"]}
print(stuDict)
#添加字典的键
stuDict["002"]=["零零二", 20, "0000002"]
print(stuDict)
stuDict.update({"003":["零零三", 20, "0000003"]})
print(stuDict)
#添加字典的值
stuDict["001"]=["零零一", 20, "0000001","春华101"]
print(stuDict)
stuDict.update({"002":["零零三", 20, "0000003", "夏华102"]})
print(stuDict)