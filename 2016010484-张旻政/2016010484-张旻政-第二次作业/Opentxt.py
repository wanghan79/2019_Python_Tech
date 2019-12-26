container = []
class Opentxt( ):
    def __init__(self, file):                            # 初始化属性file
        self.file = file

    def openfile(self):                                  # 定义读取函数
        with open(self.file) as f:
            for line in f:
                element = line.split(' ')                # 按，分割每一行
                container.append(element)                # 将分割后的元素放入容器container内
        return container
