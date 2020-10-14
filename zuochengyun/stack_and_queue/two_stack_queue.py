class TwoStackQueue(object):
    def __init__(self):
        self.stack_a = []
        self.stack_b = []

    def push(self, number):
        self.stack_a.append(number)

    def pop(self) -> int:
        if len(self.stack_b) == 0:
            while self.stack_a:
                self.stack_b.append(self.stack_a.pop())
        if self.stack_b:
            return self.stack_b.pop()
        else:
            raise Exception("queue None")

    def get(self) -> int:
        if len(self.stack_b) == 0:
            while self.stack_a:
                self.stack_b.append(self.stack_a.pop())
        if self.stack_b:
            return self.stack_b[-1]
        else:
            raise Exception("stack None")


if __name__ == '__main__':
    queue = TwoStackQueue()
    queue.push(2)
    queue.push(5)
    queue.push(3)
    queue.push(1)
    print("get", queue.get())
    queue.pop()
    print("get", queue.get())
    queue.pop()
    print("get", queue.get())
    queue.pop()
    print("get", queue.get())
    queue.pop()
