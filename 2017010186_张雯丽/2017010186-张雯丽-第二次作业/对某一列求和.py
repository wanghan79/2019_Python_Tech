import T
class Stic:
    def sum(self,file):
        treader=T.txtReader()
        data=treader.parser(file)
        sum=0
        for item in data:
            sum+=int(item[2])
        print("sum=", sum)

sta=Stic()
sta.sum("E:\\Pycharm_zhangwl\\2019_Python_Tech\\2017010186_张雯丽\\2017010186-张雯丽-第二次作业\\txtText.txt")