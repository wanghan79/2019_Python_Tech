import xlrd
import os
f1=open("pip安装方法.txt")
print("pip安装方法:")
line=f1.readline()
while line:
    print(line)
    line = f1.readline()
f1.close()
x1 = xlrd.open_workbook("XLSX-test-01.xlsx")  #打开文件
print("所有sheet名字:",x1.sheet_names())       #获取所有sheet名字
print("sheet数量:",x1.nsheets)                 #获取sheet数量
print("所有sheet对象：",x1.sheets())              #获取所有sheet对象
print("索引查找：",x1.sheet_by_index(0))      #通过索引查找


sheet1 =x1.sheet_by_name("信息表")             #通过sheet名查找
print("表1:",sheet1.name)                      #获取sheet名
print("行数:",sheet1.nrows)                   #获取总行数
print("列数:",sheet1.ncols)                   #获取总列数

for i in range(5):
   #print(sheet1.row_values(i))      #获取第一行所有内容，合并单元格，首行显示值，其它为空
   print(sheet1.row(i))                   #获取单元格值类型和内容
   #print(sheet1.row_values(i))       # 获取单元格数据类型

sheet2 =x1.sheet_by_name("成绩表")
print("表2:",sheet2.name)
#print(sheet2.row_values(0, 2, 3))     # 取第1行，第2~3列
#print(sheet2.col_values(0, 0, 3))     # 取第1列，第0~3行（不含第3行）
#print(sheet2.row_slice(2, 0, 2))      # 获取单元格值类型和内容
#print(sheet2.row_types(1, 0, 2))     # 获取单元格数据类型
for i in range(5):
   print(sheet2.row_values(i))



