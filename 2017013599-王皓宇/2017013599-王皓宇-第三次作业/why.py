import xlwings as xw     #调用xlwings包
                            
              
xw.App.visible=False                                            #设置excel为不可见
wb=xw.Book(r"2018期刊影响因子及学科平均影响因子列表.xls")  #打开excel文件
                                        
for sht in wb.sheets:
    print(sht.name)
st=wb.sheets["2018年度"]

rownum=st.range('A1').current_region.last_cell.row           
colnum=st.range('A1').current_region.last_cell.column          
print("行数：",rownum)                                          #输出最后一页的行数
print("列数：",colnum)                                          #输出最后一页的列数
for row in range(20):                                           #输出最后一页前20行的数据
    for col in range(colnum):
        print(st[row,col].value)
print(st.range(2,2).value)

wb.close                                                        #关闭excel
xw.App.quit                                                     #关闭xlwings的App




