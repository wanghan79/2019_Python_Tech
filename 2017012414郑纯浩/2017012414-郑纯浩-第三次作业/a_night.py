import xlwings as xw                                            #调用xlwings包
xw.App.visible=False                                            #设置excel为不可见
wb=xw.Book(r"test.xls")                                         #打开excel文件
loop=len(wb.sheets)                                             #读取excel文件有多少页
for loop_num in range(loop):                                    #读取每一页的名字
    st=wb.sheets[loop_num]
    print(loop_num,st.name)
rownum=st.range('A1').current_region.last_cell.row              #最后一页的行数
colnum=st.range('A1').current_region.last_cell.column           #最后一页的列数
print("行数：",rownum)                                          #输出最后一页的行数
print("列数：",colnum)                                          #输出最后一页的列数
for row in range(20):                                           #输出最后一页前20行的数据
    for col in range(colnum):
        print(st[row,col].value)
print(st.range(2,2).value)
wb.close                                                        #关闭excel
xw.App.quit                                                     #关闭xlwings的App




