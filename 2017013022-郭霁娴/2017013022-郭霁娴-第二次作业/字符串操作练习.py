str1="stu1,2017013022,guojx,20,174,21"
str2="20"
str3="guojx"
str4="0"
print("将字符串首字母大写：", str1.capitalize())
print("计算str1中有多少个str2：", str1.count(str2))
print("判断str1是否用str2结尾：", str1.endswith(str2))
print("查找str2和str3在str1中出现的第一个位置：", str1.find(str2)," ",str1.find(str3))
print("查找str2在str1中的位置：",str1.index(str2))
print("将str1中的are替换成was：",str1.replace("guojx","lisiyu"))
print("在str1中反向查找str2：",str1.rfind(str2))
print("将str1以逗号分隔，最大分割为三部分：",str1.split(',',2))
