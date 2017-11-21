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
        run=sum/5
        print(run)

sta = Stic()
sta.sum("D:\\hanjh\\text.txt")

from typing import List, Tuple