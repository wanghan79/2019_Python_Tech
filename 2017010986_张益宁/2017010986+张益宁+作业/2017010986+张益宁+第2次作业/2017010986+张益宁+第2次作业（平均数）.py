from typing import Any

import T
class know:
    def sum(self, file):
        treader = T.txtReader()
        data = treader.parser(file)
        n = 0
        sum = 0
        for item in data:
            sum += int(item[0])
            n += 1
        print(sum/n)
sta = know()

sta.sum('content.txt')