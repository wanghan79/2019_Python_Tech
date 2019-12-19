import xlwings as xw

xw.App.visible = False
wb=xw.Book(r'text.xlsx')

st=wb.sheets["Sheet1"]

rownum = st.range('A1').current_region.last_cell.row
colnum = st.range('A1').current_region.last_cell.column

for row in range(rownum):
    for col in range(colnum):
        print(st[row,col].value)


