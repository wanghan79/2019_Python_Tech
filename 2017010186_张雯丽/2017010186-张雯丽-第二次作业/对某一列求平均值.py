import T
class Stic:

    def avg(self,file):
        treader=T.txtReader()
        data=treader.parser(file)
        for item in data:
            sum = 0
            len = 0
            for item in data:
                sum += int(item[2])
                len+=1
                avg=sum/(len)
        print("avg=", avg)
sta=Stic()
sta.avg("txtText.txt")