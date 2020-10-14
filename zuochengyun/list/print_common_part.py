class Node():
    def __init__(self, data: int = 0):
        self.value = data
        self.next = None


def print_common_part(node1: Node, node2: Node):
    while node1 != None and node2 != None:
        if node1.value < node2.value:
            node1 = node1.next
        elif node1.value > node2.value:
            node2 = node2.next
        else:
            print(node1.value)
            node1 = node1.next
            node2 = node2.next


if __name__ == '__main__':
    pass
