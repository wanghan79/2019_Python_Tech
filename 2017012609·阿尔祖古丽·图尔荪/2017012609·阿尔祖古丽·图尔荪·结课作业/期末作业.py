import xlwings as xw

xw.App.visible=False
wb=xw.Book(r"2018期刊影响因子及学科平均影响因子列表.xls")
loop=len(wb.sheets)
for loop_num in range(loop):
    st=wb.sheets["2018年度"]
    print(loop_num,st.name)

rownum=st.range('A1').current_region.last_cell.row
colnum=st.range('A1').current_region.last_cell.column
print("行数：",rownum)
print("列数：",colnum)

sum=0.0
for row in range(1,200):
    sum+=st[row,3].value
print(sum)
avg=sum/rownum
print(avg)
xue={"0":"0"}
for row in range(1,200):
    if st[row,5].value in xue:
        xue[st[row,5].value]+=xue[st[row,5].value]
    else:
        xue[st[row,5].value] = 1
for key in xue:
    print(key,xue[key])
print(len(xue))