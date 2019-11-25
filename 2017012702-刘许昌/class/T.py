from typing import List, Tuple


class txtReader:
    def parser(self,file):
        with open(file) as f:

            container = []
            for line in f:
                words = line.split(" ")
                container.append(words)
        f.close()
        return container