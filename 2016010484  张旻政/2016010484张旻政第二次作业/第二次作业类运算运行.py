from Statistic import Statistic                                      # 导入Statistic类


a = Statistic('students.txt')
sum = a.statistic_sum()                                              # 求和
print('the sum is ', sum)
ava = a.statistic_average()                                          # 求平均值
print('the average is ', ava)

