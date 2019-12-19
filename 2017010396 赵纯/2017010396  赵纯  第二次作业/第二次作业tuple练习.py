from typing import Union, Tuple, Set
stuset = {"2017010396","2017010396"}
stulist = ["zhaochun"]
stuset.add("hello")
stuset.add(9)
stu1 = {"2017010396": ["zhaochun", "18743097006"]}
print(stu1["2017010396"])
stu2 = {"2017010397": ["zhaoc", "18823456543"]}
stu1.update(stu2)
print(stu1)

