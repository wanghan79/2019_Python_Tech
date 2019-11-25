import T
class Stic:
    def sum(self, file):
        treader = T.txtReader()
        data = treader.parser(file)
        sum = 0
        for item in data:
            sum += int(item[0])
        print(sum)

sta = Stic()
sta.sum("D:\\zhaoc\\text.txt")
