import xlwings as excle  ##调用xlwings

excle.App.visible = False
wb = excle.Book(r"2018期刊影响因子及学科平均影响因子列表.xls")  ##选择文件


st = wb.sheets[0]    ##选择工作簿
rownum = st.range('A1').current_region.last_cell.row        ##读取行数
colnum = st.range('A1').current_region.last_cell.column     ##读取列数

name = {}   ##创建字典
for row in range(rownum):
    if row != 0:
        temp = st[row,5].value.split(', ')
        for temp_string in temp:
            if temp_string in name:
                name[temp_string] = name[temp_string] + 1
            else:
                name[temp_string] = 1
for k in name:
    print(k, name[k])   ##输出