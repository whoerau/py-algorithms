class MStack(object):
    def __init__(self):
        self.stack = []

    def push(self, number: int):
        self.stack.append(number)

    def _pop_bottom(self) -> int:
        rsp = self.stack.pop()
        if not self.stack:
            return rsp
        else:
            last = self._pop_bottom()
            self.push(rsp)
            return last

    def reverse(self):
        if not self.stack:
            return
        else:
            r = self._pop_bottom()
            self.reverse()
            self.push(r)


if __name__ == '__main__':
    ms = MStack()
    ms.push(2)
    ms.push(5)
    ms.push(3)
    ms.push(1)
    ms.reverse()
    print(ms.stack)
