import xlwings as xw

xw.App.visible=False
wb=xw.Book('2018期刊.xlsx')

loop=len(wb.sheets)
for loop_num in range(loop):
    st=wb.sheets["sheet1"]
    print(loop_num,st.name)
rownum=st.range('A1').current_region.last_cell.row
colnum=st.range('A1').current_region.last_cell.column

print("行数：",rownum)
print("列数：",colnum)
ans_wan=0.0
for row in range(rownum):
    if row!=0:
        ans_wan+=st[row,3].value
print(ans_wan)
ans_wan=ans_wan/rownum
print(ans_wan)
dic={ }
for row in range(rownum):
    if row != 0:
        temp=st[row,5].value.split(', ')
        for temp_string in temp:
            if temp_string in dic:
                dic[temp_string]=dic[temp_string]+1
            else:
                dic[temp_string] = 1
for key in dic:
    print(key,dic[key])
print(len(dic))