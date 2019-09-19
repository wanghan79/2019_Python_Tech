import os


def txtReader(file):
    with open(file) as f:
        for line in f:
            print(line)
    f.close()

txtReader("D:\\yexiaoli\\text.txt")
txtReader("D:\\yexiaoli\\first.docx")
txtReader("D:\\yexiaoli\\first.pptx")
txtReader("D:\\yexiaoli\\first.xlsx")
txtReader("D:\\yexiaoli\\first.html")
