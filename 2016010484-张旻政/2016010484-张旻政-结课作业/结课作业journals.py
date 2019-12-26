import pandas as pd                                                                      # 导入库pandas


file = "2018期刊影响因子及学科平均影响因子列表.xls"                                      # 将文件名赋给变量file
df = pd.read_excel("2018期刊影响因子及学科平均影响因子列表.xls", sheet_name='2018')      # 读取文件file

print(df.columns.values, '\n')                                                           # 打印列名称

print('影响因子平均值', df['影响因子 Impact Factor'].mean(), '\n')                       # 计算并打印各期刊影响因子平均值

rownum = len(df.index)                                                                   # 统计一共有多少行
print("行数共计：", rownum)

dict = {}                                                                                # 创建一个空字典用于存放学科及统计的个数
for row in range(1, rownum):
        subject = df.loc[row-1, "所属学科subject"].split(',')                            # 将学科按“，”分割赋值给subject
        for subject_element in subject:                                                  # 依次对subject中的每个元素进行操作
            if subject_element not in dict:                                              # 判断字典dict里是否已有subject中的元素
                dict[subject_element] = 1                                                # 若无赋值为1
            else:
                dict[subject_element] = dict[subject_element] + 1           # 若有计数加1
for key in dict:                                                            # 依次打印字典中的键值
    print(key, dict[key])

print("学科共计: ", len(dict))                                              # 打印学科统计个数
