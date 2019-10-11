import xlwt
book = xlwt.Workbook(encoding = 'utf-8')   #创建一个Excel对象
sheet1 = book.add_sheet('sheet1')       #添加一个名为sheet1的sheet
style = xlwt.XFStyle()
for i in range(1,10):              # 其中的i行, j列'指定表中的单元，向该单元写入的i*j的结果
    for j in range(0, 10):
        sheet1.write(i, j, i*j)

sheet2 = book.add_sheet('sheet2')
row1=["12","12","12","12","12"]
column1=["34","34","34","34","34"]
for i in range(0,len(row1)):            #按行次序输入
    sheet2.write(0,i,row1[i])
for i in range(0, len(column1)):         #按列次序输入
    sheet2.write(i+1,0,column1[i])
book.save("work-test.xls")          # 命名保存