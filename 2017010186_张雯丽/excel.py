import xlrd

def open_excel(file= 'excel.xlsx'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))

wb = xlrd.open_workbook("E:\\Pycharm_zhangwl\\excel.xlsx")#打开文件

print(wb.sheet_names())#获取所有的sheet页

身高表 =wb.sheet_by_index(0)#通过索引获取表格页，从o开始

身高表=wb.sheet_by_name(r"身高表")#通过sheet名字获取表格

#输出身高表内容
print(身高表.name,身高表.nrows,身高表.ncols)#获取当前sheet页的名称，行数，列数，都从1开始

rows = 身高表.row_len(0)#获取某一行长度索引为0

print(身高表.row_len(0))#获取某一行长度索引为0

print(rows)

No1 = 身高表.row_values(0)#获取行内容，索引从0开始

hei = 身高表.col_values(1)#获取某一列内容，索引从0开始

print(No1, hei)

#输出分数表内容
分数表 =wb.sheet_by_index(0)#通过索引获取表格页，从o开始

分数表=wb.sheet_by_name(r"分数表")#通过sheet名字获取表格
print(分数表.name,分数表.nrows,分数表.ncols)#获取当前sheet页的名称，行数，列数，都从1开始

rows = 分数表.row_len(0)#获取某一行长度索引为0

print(分数表.row_len(0))#获取某一行长度索引为0

print(rows)

No2 = 分数表.row_values(0)#获取行内容，索引从0开始

sco = 分数表.col_values(1)#获取某一列内容，索引从0开始

print(No2, sco)