seq = "today we are lucky!"
print(seq.capitalize())                    # 大写字符串的首字母
print(seq.count(' '))                      # 空格计数
print(seq.endswith('!'))                   # 判断是否为‘！’结尾
print(seq.find('w'))                       # 查找‘w’出现位置
print(seq.index('w'))                      # 查找‘w’出现位置
seq1 = seq.replace('lucky', 'happy')       # 将‘lucky’替换为‘happy’
print(seq1)                                # 打印seq1
print(seq.rfind('e'))                      # 反向查找‘e’
seq_split = seq.split(" ")                 # 将seq以空格为分隔符分割赋给seq_split
print(seq_split)                           # 打印seq_split
print(seq.upper())                         # 字符串全部大写
print(seq.lower())                         # 字符串全部小写
print(seq.title())                         # 字符串每个单词首字母大写



