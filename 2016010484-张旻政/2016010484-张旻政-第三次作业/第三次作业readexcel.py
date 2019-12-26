import xlwings as xw                                              # 导入xlwings库

xw.App.visible = False
wb = xw.Book("newtest.xlsx")                                      # 打开一个Excel文件

num = len(wb.sheets)                                              # 统计工作簿的个数
sheet_name = []
for i in range(num):                                              # 依次打印工作簿名称
    sht = wb.sheets[i]
    print(sht.name)

sht = wb.sheets['家电销售']                                       # 读取工作簿家电销售

rownum = sht.range('A1').current_region.last_cell.row             # 返回行数
colnum = sht.range('A1').current_region.last_cell.column          # 返回列数
print("行数：", rownum)                                           # 打印行数
print("列数：", colnum)                                           # 打印列数

for col in range(colnum):                                         # 打印第一行列名称
    print(sht[0, col].value)

for row in range(5):                                              # 打印前5行数据
    for col in range(colnum):
        print(sht[row, col].value, end=' ')
    print(end='\n')

example = sht.range('a1:a4')                                      # 打印第一列的前4个单元格
print(example.value)

print(sht[2, 3].value)                                            # 打印第3行第4列的值

wb.close()                                                        # 关闭文件

