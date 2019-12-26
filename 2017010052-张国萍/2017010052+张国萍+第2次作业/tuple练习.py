from typing import Union, Tuple, Set
stuset = {"2017012609","2017012702"}
stulist = ["阿尔祖"]
stuset.add("hello")
stuset.add(9)
stu1 = {"2017012609": ["阿尔祖", "15770184697"]}
print(stu1["2017012609"])
stu2 = {"2017012609": ["阿尔祖", "15770184697"]}
stu1.update(stu2)
print(stu1)

