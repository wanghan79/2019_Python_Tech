import T
class Stic:
    def sum(self,file):
        treader = T.txtReader()
        data = treader.parser(file)
        sum = 0
        for item in data:
            sum += int(item[0])
        print(sum)

sta = Stic()
sta.sum("D:\\zhangyn849\\zhangyn.txt")
from typing import List,Tuple


class txtReader:
    def parser(self,file):
        with open(file) as f:
            row = 0
            container = []
            for line in f:
                words = line.split(" ")
                container.append(words)
        f.close()
        return container

