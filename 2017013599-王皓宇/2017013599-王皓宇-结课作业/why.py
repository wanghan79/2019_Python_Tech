import xlwings as xw                                            #调用xlwings包

xw.App.visible=False                                            #设置excel不可见
wb=xw.Book(r"200强.xls")                                         #打开excel

loop=len(wb.sheets)                                             #求出excel文件页数
for loop_num in range(loop):
    st=wb.sheets["Sheet1"]                                         #取最后一页作为数据

rownum=st.range('A1').current_region.last_cell.row              #求出行数
colnum=st.range('A1').current_region.last_cell.column           #求出列数

print("行数：",rownum)                                          #输出行数
print("列数：",colnum)                                          #输出列数

print("行数：",rownum)
print("列数：",colnum)
ans_wan=0.0
for row in range(rownum):
    if row!=0:
        ans_wan+=st[row,3].value
print(ans_wan)
ans_wan=ans_wan/rownum
print(ans_wan)

dic={}                                                         #定义用来保存处理结果的字典
for row in range(rownum):                                      #读取每一行
    if row != 0:                                                         #刨除第一行
        temp=st[row,5].value.split(', ')                      
        for temp_string in temp:                               #读取列表
            if temp_string in dic:                          
                dic[temp_string]=dic[temp_string]+1
            else:                                         
                dic[temp_string] = 1

for key in dic:                                               #输出结果
    print(key,dic[key])

print(len(dic))                                                #输出长度