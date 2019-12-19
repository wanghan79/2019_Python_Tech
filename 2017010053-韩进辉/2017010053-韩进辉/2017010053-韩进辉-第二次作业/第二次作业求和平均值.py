import T


class Stic:
    def sum(self, file):
        treader = T.txtReader()
        data = treader.parser(file)
        sum = 0
        line = 0
        for item in data:
            sum += int(item[0])
            line =line+1
        print(sum)
        print(sum/line)
        run=sum/7
        print(run)

sta = Stic()
sta.sum("C:\\Users\\SD\\Documents\GitHub\\2019_Python_Tech\\2017010053-韩进辉\\2017010053-韩进辉\\2017010053-韩进辉-第二次作业\\数据文档.txt")