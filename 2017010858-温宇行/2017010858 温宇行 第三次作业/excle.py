import xlwings as xw
xw.App.visible=False

wb=xw.Book(r'xinxi.xlsx')   ##确定文件
st=wb.sheets['sheet1']  ##打开指定工作簿

rownum = st.range('A1').current_region.last_cell.row  ##读取行数 整型
colnum = st.range('A1').current_region.last_cell.column  ##读取列数  整型

for row in range(rownum):                        ##按行读取
    for col in range(colnum):                    ##按列读取
        print(st[row,col].value)                 ##输出
print("**********************")
print(st.range(2, 2).value)        ##读取指定行数与列数