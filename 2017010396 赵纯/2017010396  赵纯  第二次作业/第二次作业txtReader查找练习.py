import os


def reader(file):
    with open(file) as f:
        row = 0
        container = []
        for line in f:
            word = line.split(" ")
            for col, item in enumerate(word):
                element = (row, col, item)
                container.append(element)
            row += 1
        for element in container:
            if element[2] == "wanghan":
                print(element)
            else:
                print("not found")
            f.close()
reader('text.txt')

