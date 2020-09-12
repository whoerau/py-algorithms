class MyStack():
    def __init__(self):
        self.v_stack = []
        self.m_stack = []

    def push(self, number: int):
        self.v_stack.append(number)
        if len(self.m_stack) == 0:
            self.m_stack.append(number)
        else:
            if self.m_stack[-1] > number:
                self.m_stack.append(number)
            else:
                self.m_stack.append(self.m_stack[-1])

    def pop(self) -> int:
        if len(self.m_stack) > 0:
            self.m_stack.pop()
            return self.v_stack.pop()
        else:
            raise Exception("Stack None")

    def get_min(self) -> int:
        if len(self.m_stack) > 0:
            return self.m_stack[-1]
        else:
            raise Exception("Stack None")


if __name__ == '__main__':
    s = MyStack()
    s.push(2)
    s.push(5)
    s.push(3)
    s.push(1)
    print("min", s.get_min())
    s.pop()
    print("min", s.get_min())
    s.pop()
    print("min", s.get_min())
    s.pop()
    print("min", s.get_min())
    s.pop()
