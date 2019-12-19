from typing import List,Tuple

class txtReader:
    def parser(self,file):
        with open(file) as f:
            row = 0
            container = []
            for line in f:
                words = line.split(" ")
                container.append(words)
        f.close()
        return container





