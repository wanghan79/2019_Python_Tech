import xlwings as xw
'''app = xw.App(visible=True,add_book=False)
新建工作簿 (如果不接下一条代码的话，Excel只会一闪而过，卖个萌就走了）
wb = app.books.add()
wb = app.books.open('example.xlsx')'''
wb = xw.Book('2018期刊影响因子及学科平均影响因子列表.xls')
st = wb.sheets["2018年度"]
rownum = st.range('A1').current_region.last_cell.row
colnum = st.range('A1').current_region.last_cell.column
for row in range(rownum):
    for col in range(colnum):
        print(st[row, col].value)
print(st.range(2,2).value)
