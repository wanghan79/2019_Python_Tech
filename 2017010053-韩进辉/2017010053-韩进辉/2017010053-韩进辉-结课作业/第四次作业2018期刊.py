import xlwings as xw

xw.App.visible = False
wb = xw.Book("C:\\Users\SD\Documents\GitHub\\2019_Python_Tech\\2017010053-韩进辉\\2017010053-韩进辉\\2017010053-韩进辉-结课作业\\hanjh001.xls")

loop=len(wb.sheets)
for loop_num in range(loop):
    st=wb.sheets[loop_num]
    print(loop_num,st.name)
#st = wb.sheets["2018年度"]
rownum = st.range('A1').current_region.last_cell.row
colnum = st.range('A1').current_region.last_cell.column
print("学科数：",rownum)
print("列数：",colnum)
ans_wan=0.0
for row in range(rownum):
    if row!=0:
        ans_wan+=st[row,3].value
print(ans_wan)
ans_wan=ans_wan/rownum
print(ans_wan)
#lstCol = []
#for col in range(3,5):
    #for row in range(1,100):
        #lstCol.append(st[row, 3].value)
#print(lstCol)



wb.close
