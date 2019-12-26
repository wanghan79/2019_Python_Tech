stu=("温","2017010858","123456",19)
print(stu[1])
for stus in stu:
    print(stus)
stu=["温","2017010858","123456",19]
stu.append("照成一之父")                        ##插入
print(stu[1])
for stus in stu:
    print(stus)
print("* * * * * * * * * * * * * * * * * * * * ")
print(isinstance(stu,list))
print("* * * * * * * * * * * * * * * * * * * * ")
s={"温","2017010858","123456",19}
print(s)
s.add("2017010858")
print(s)

print("                  ")
s2={"张","2017011234","123456",20}
z=s.difference(s2)
print(z)

d={"a":"qwe","b":"asd"}
print(d)
d['c'] = "abc"
print(d)
d['a'] = "qwe","102"
print(d)