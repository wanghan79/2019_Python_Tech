import xlwings as xw

xw.App.visible = False
wb=xw.Book(r'2018期刊影响因子及学科平均影响因子列表.xls')

for sht in wb.sheets:
    print(sht.name)
st=wb.sheets["2018年度"]

rownum = st.range('A1').current_region.last_cell.row
colnum = st.range('A1').current_region.last_cell.column
print(rownum,colnum)

for col in range(colnum):
    print(st[0,col].value)

lstCol = []
try:
    for row in range(100):
        lstCol.append(st[row, 3].value)
except:
    pass
print("continue")
for item in lstCol:
    print(item)

