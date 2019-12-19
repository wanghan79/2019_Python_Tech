import T
class _sum:
    def sum(self, file):
        treader=T.txtReader()
        data=treader.parser(file)
        sum = 0
        for item in data:
            sum+=int(item[0])
        print(sum)

sta = _sum()
sta.sum('11.14.txt')
'''调用T 类求和'''
