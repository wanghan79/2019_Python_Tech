import xlwings as xw                                            #调用xlwings包

xw.App.visible=False                                            #设置excel不可见
wb=xw.Book(r"test.xls")                                         #打开excel

loop=len(wb.sheets)                                             #求出excel文件页数
st=wb.sheets[loop-1]                                            #取最后一页作为数据
rownum=st.range('A1').current_region.last_cell.row              #求出行数
colnum=st.range('A1').current_region.last_cell.column           #求出列数

print("行数：",rownum)                                          #输出行数
print("列数：",colnum)                                          #输出列数
dic={}                                                         #定义用来保存处理结果的字典
for row in range(rownum):                                      #读取每一行
    if row != 0:                                               #刨除第一行
        temp=st[row,5].value.split(', ')                       #将字符串用“， ”分隔，得到一个列表
        for temp_string in temp:                               #读取列表
            if temp_string in dic:                             #字典处理，如果这个字符串对应的键在字典里就让键值+1
                dic[temp_string]=dic[temp_string]+1
            else:                                              #如果不在就新建一个键值对，键值为1
                dic[temp_string] = 1
print("发表领域统计：")                                         #输出统计结果
for key in dic:
    print(key,dic[key])