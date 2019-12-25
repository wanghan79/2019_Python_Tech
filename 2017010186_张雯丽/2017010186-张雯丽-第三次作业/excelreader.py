import xlrd

def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))
wb = xlrd.open_workbook("excel.xlsx")#打开文件
print(wb.sheet_names())#获取所有的sheet页
身高表 =wb.sheet_by_index(0)#通过索引获取表格页，从o开始
身高表=wb.sheet_by_name(r"身高表")#通过sheet名字获取表格
#输出身高表内容
print("表格名：",身高表.name)#获取当前sheet页的名称，都从1开始
print("行数：",身高表.nrows)#获取当前sheet页的行数，都从1开始
print("列数：",身高表.ncols)#获取当前sheet页的列数，都从1开始
rows = 身高表.row_len(0)#获取某一行长度索引为0
print("身高表中第0行的长度：",身高表.row_len(0))#获取某一行长度索引为0
No1 = 身高表.row_values(0)#获取行内容，索引从0开始
hei = 身高表.col_values(1)#获取某一列内容，索引从0开始
print(No1, hei)
print("\n")

#输出分数表内容
分数表 =wb.sheet_by_index(0)#通过索引获取表格页，从o开始
分数表=wb.sheet_by_name("分数表")#通过sheet名字获取表格
print("表格名：",分数表.name)#获取当前sheet页的名称，都从1开始
print("行数：",分数表.nrows)#获取当前sheet页的行数，都从1开始
print("列数：",分数表.ncols)#获取当前sheet页的列数，都从1开始
rows = 分数表.row_len(0)#获取某一行长度索引为0
print("分数表中第0行的长度：",分数表.row_len(0))#获取某一行长度索引为0
No2 = 分数表.row_values(0)#获取行内容，索引从0开始
sco = 分数表.col_values(1)#获取某一列内容，索引从0开始
print(No2, sco)
