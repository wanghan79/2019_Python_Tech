seq="why are you So beautiful"
sub="beautiful"

print(seq.capitalize())#将字符串的第一个字母变成大写,其他字母变小写。

print(seq.count(sub)) #用于统计字符串里某个字符出现的次数,选参数为在字符串搜索的开始与结束位置。

print(seq.endswith(sub,1,40))#用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。可选参数"start"与"end"为检索字符串的开始与结束位置。

print(seq.find(sub,0))#检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。

print(seq.index(sub,0))#检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。

print(seq.replace("you","u"))#把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。

print(seq.rfind(sub))#返回字符串最后一次出现的位置(从右向左查询)，如果没有匹配项则返回-1。

print(seq.split(' ',3))#通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串。