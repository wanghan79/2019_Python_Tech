import os
def TXTreader(file):
    with open(file) as f:
        for line in f:
            print(line)
    f.close()
TXTreader('text.txt')



