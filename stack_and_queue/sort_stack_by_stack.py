class MStack():
    def __init__(self):
        self.stack = []

    def sort(self):
        tmp_stack = []
        while self.stack:
            if not tmp_stack:
                tmp_stack.append(self.stack.pop())
            else:
                cur = self.stack.pop()
                if cur > tmp_stack[-1]:
                    self.stack.append(tmp_stack.pop())
                    self.stack.append(cur)
                else:
                    tmp_stack.append(cur)

        while tmp_stack:
            self.stack.append(tmp_stack.pop())


if __name__ == '__main__':
    ms = MStack()
    ms.stack.append(5)
    ms.stack.append(2)
    ms.stack.append(1)
    ms.stack.append(3)
    ms.sort()
    print(ms.stack)
