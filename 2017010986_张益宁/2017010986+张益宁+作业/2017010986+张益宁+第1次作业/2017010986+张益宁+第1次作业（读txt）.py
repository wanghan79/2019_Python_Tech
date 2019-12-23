def reader(file):
    with open(file) as f:
        for line in f:
            print(line)
        f.close()

reader("D:\\2019-2020qiu\\lasthomework\\first\\txtreader.txt")