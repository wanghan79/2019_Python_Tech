from typing import Union, Tuple, Set
stuset = {"2017010053","2017010053"}
stulist = ["hanjinhui"]
stuset.add("hello")
stuset.add(9)
stu1 = {"2017010053": ["hanjinhui", "15543570961"]}
print(stu1["2017010053"])
stu2 = {"2017010051": ["hanjh", "13891224352"]}
stu1.update(stu2)
print(stu1)
