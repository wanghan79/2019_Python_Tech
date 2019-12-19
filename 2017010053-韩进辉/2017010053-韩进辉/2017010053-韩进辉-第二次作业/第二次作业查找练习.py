import os

def txtReader(file):
    with open(file) as f:
        row = 0
        container = []
        for line in f:
            words=line.split(" ")
            for col, item in enumerate(words):
                element = (row,col, item)
                container.append(element)
            row += 1
        for element in container:
            for item in element:
                if item =="han":
                 print(element)
            else:
                print("not found")

    f.close()

txtReader("C:\\Users\SD\Documents\GitHub\\2019_Python_Tech\\2017010053-韩进辉\\2017010053-韩进辉\\2017010053-韩进辉-第二次作业\\txtreader.txt")