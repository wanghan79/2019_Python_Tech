import xlwings as xw     #导入xlwing库

xw.App.visible=False     #设置excel不可见
wb=xw.Book(r"期刊.xls")   #以只读模式打开excel文件

loop=len(wb.sheets)      #求excel文件的页数
st=wb.sheets[loop-1]     #取最后一页作为数据

rownum=st.range('A1').current_region.last_cell.row       #求行数
colnum=st.range('A1').current_region.last_cell.column    #求列数

print("行数：",rownum)   #打印输出行数
print("列数：",colnum)   #打印输出列数

sum=0.0   
for row in range(rownum):
    if row!=0:
        sum+=st[row,3].value
print(sum)

sum=sum/rownum  
print(sum)
"""求平均数"""

dic={}                   #建立字典来保存处理结果
for row in range(rownum):   #遍历读取每一行
    if row != 0:            #不考虑第一行
        temp = st[row, 5].value.split(', ')    #分割成新的列表
        for temp_string in temp:               #遍历读取列表
            if temp_string in dic:
                dic[temp_string] = dic[temp_string] + 1
            else:
                dic[temp_string] = 1

for key in dic:             #遍历字典
    print(key,dic[key])     #打印输出
print(len(dic))             #打印字典长度