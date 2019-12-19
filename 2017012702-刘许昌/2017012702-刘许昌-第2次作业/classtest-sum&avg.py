import classtestT
class Stic:
    def sumavg(self, file):
        treader = classtestT.txtReader()
        data = treader.parser(file)
        sum = 0
        i = 0
        for item in data:
            sum += int(item[0])
            i=i+1
        print("sum=",sum)
        print("avg=",sum/i)

sta = Stic()
sta.sumavg('text.txt')
