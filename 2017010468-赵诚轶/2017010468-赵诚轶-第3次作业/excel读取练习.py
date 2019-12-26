import xlwings as xw

xw.App.visible = False
wb = xw.Book('zcyliebiao-test-01.xlsx')
st = wb.sheets["sheet1"]
rownum = st.range('A1').current_region.last_cell.row
colnum = st.range('A1').current_region.last_cell.column
for row in range(rownum):
    for col in range(colnum):
        print(st[row,col].value)
print(st.range(2,2).value)
cells = st.cells
row, col = cells.shape
print(row,col)

wb.close
xw.App.quit