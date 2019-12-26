import xlwings as xw

xw.App.visible = False                                     #设置Excel为不可见
wb = xw.Book(r"test3.xlsx")                                #打开测设文件（表格）3
st = wb.sheets["sheet1"]                                   #读取测试文件的表格一（sheet1）
rownum = st.range('A1').current_region.last_cell.row       #读取测试文件最后一页的行数
colnum = st.range('A1').current_region.last_cell.column    #读取测试文件最后一页的列数
print("rownnum：",rownum)                                  #输出对应行数
print("colnum：",colnum)                                   #输出对应列数

for row in range(rownum):                                  #输出最后一页所有行的数据
    for col in range(colnum):
        print(st[row,col].value)
print(st.range(2,2).value)
cells = st.cells
row, col = cells.shape
print(row,col)

wb.close
xw.App.quit                                                #退出xlwings
