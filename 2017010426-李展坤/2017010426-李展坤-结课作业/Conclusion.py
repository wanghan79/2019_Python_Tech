import xlwings as xw

xw.App.visible = False                                            #设置Excel不可见
wb = xw.Book(r"test4.xls")                                        #即2018期刊影响因子及学科平均影响因子列表
loop = len(wb.sheets)                                             #读取统计表共计有多少张
st = wb.sheets[loop-1]                                            #读取测试文件的最后一页
rownum = st.range('A1').current_region.last_cell.row              #读取测试文件最后一页的行数
colnum = st.range('A1').current_region.last_cell.column           #读取测试文件最后一页的列数
print("rownum：",rownum)                                          #输出对应行数
print("colnum：",colnum)                                          #输出对应列数

dic = {}                                                          #定义一个字典，用来保存处理结果
for row in range(1,200):                                          #读取前200行
    if row != 0:                                                  #判定行数，并剔除第一行题头
        temp = st[row,5].value.split(', ')                        #split函数，拆分字符串，并以“，”分开
        for temp_string in temp:                                  #循环读取列表
            if temp_string in dic:
                dic[temp_string] = dic[temp_string] + 1
            else:
                dic[temp_string] = 1
print("Publishing field statistics：")
for key in dic:
    print(key,dic[key])
