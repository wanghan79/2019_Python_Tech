d={"1":"Mao Ze Dong","2":"Deng Xiao Ping","3":"Jiang Ze Min"} #创建字典
print(d["1"])   #打印输出key为"1"的value值
print(d.keys()) #打印输出所有的key
print(d.values())  #打印输出所有的value
print(d.items())  #打印输出key，value元组组成的列表
d.update({"4":"Li Peng"})   #添加一组键值对
print(d)            #打印输出新的字典

