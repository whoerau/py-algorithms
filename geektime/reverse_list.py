class Node():
    def __init__(self, data: int = 0):
        self.value = data
        self.next = None


def reverse_list(head: Node) -> Node:
    prev, cur = None, head
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
        # wrong
        # cur.next = prev
        # prev = cur
        # cur = cur.next
    return prev


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    head = reverse_list(node1)
    cur = head
    while cur:
        print(cur.value)
        cur = cur.next
