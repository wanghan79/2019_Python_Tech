import xlwings as xw  #导入xlwings库

xw.App.visible = False    #设置excel不可见
wb = xw.Book(r"期刊.xls")

loop=len(wb.sheets)     #读取页数
for sht in range(loop):
    st = wb.sheets[sht]
    print(sht,st.name)     #打印输出每一页名字

rownum = st.range('A1').current_region.last_cell.row     #最后一页行数
colnum = st.range('A1').current_region.last_cell.column  #最后一页列数

print("行数：", rownum)  #打印输出最后一页的行数
print("列数：", colnum)  #打印输出最后一页的列数

for row in range(20):    #打印输出最后一页前20行的数据
    for col in range(colnum):
        print(st[row, col].value)
print(st.range(2, 2).value)
wb.close()     #关闭excel文件




