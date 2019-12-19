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
            if element[2]=="one_one":
                print(element)
    f.close()

txtReader('10.24test.txt')