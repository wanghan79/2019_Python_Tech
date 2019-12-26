import xlwings as xw

xw.App.visible=False
wb=xw.Book(r"2018期刊影响因子及学科平均影响因子列表.xls")
loop=len(wb.sheets)
for loop_num in range(loop):
    st=wb.sheets[loop_num]
    print(loop_num,st.name)

rownum=st.range('A1').current_region.last_cell.row
colnum=st.range('A1').current_region.last_cell.column
print("行数：",rownum)
print("列数：",colnum)

sum=0.0
for row in range(1,200):
    sum+=st[row,3].value
print(sum)
avg=sum/200
print(avg)
dic={"0":"0"}
for row in range(1,200):
    if st[row,5].value in dic:
        dic[st[row,5].value]=dic[st[row,5].value]+1
    else:
        dic[st[row,5].value] = 1
for key in dic:
    print(key,dic[key])
print(len(dic))