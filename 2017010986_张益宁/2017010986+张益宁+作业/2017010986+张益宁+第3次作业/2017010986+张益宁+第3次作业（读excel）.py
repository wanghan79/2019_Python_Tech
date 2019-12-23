import xlrd
def open_excel(file= 'file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))

def excel_table_byname(file= u'F:\\python\\lasthomework\\third\\excelreader.xlsx',colnameindex=0,by_name=u'aa'):#修改自己路径
     data = open_excel(file)
     table = data.sheet_by_name(by_name)
     nrows = table.nrows
     colnames = table.row_values(colnameindex)
     list = []
     for rownum in range(1, nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                 app[colnames[i]] = row[i]
             list.append(app)
     return list

def main():
    tables = excel_table_byname()
    for row in tables:
       print(row)
if __name__ =="__main__":
    main()