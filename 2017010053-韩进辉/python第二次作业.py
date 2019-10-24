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

txtReader("D:\\新建文件夹\\txtreader.txt")