import xlrd


from datetime import date,datetime
#file = 'test3.xlsx'
#def read_excel():
wb = xlrd.open_workbook('test3.xlsx')#打开文件
print(wb.sheet_names())#获取所有表格名字
sheet1 = wb.sheet_by_index(0)#通过索引获取表格
sheet2 = wb.sheet_by_name("001")#通过名字获取表格
print(sheet1,sheet2)
print(sheet1.name,sheet1.nrows,sheet1.ncols)
rows = sheet1.row_values(2)#获取行内容
cols = sheet1.col_values(3)#获取列内容
print(rows)
print(cols)
print(sheet1.cell(1,2).ctype)
date_value=xlrd.xldate_as_tuple(sheet1.cell_value(1,2),wb.datemode)
print(date_value)
print(date(*date_value[:3]))
print(date(*date_value[:3]).strftime('%Y/%m%d'))
print(sheet1.merged_cells)
print(sheet1.cell_value(1,3))
print(sheet1.cell_value(4,3))
print(sheet1.cell_value(6,1))
print(sheet1.cell(1,0).value)#获取表格里的内容，三种方式
print(sheet1.cell_value(1,0))
print(sheet1.row(1)[0].value)