class Node1():
    def __init__(self, data: int = 0):
        self.value = data
        self.next = None


class Node2():
    def __init__(self, data: int = 0):
        self.value = data
        self.next = None
        self.prev = None


def reverse_list1(head: Node1) -> Node1:
    if not head or not head.next:
        return head
    pre, cur = None, head
    while cur and cur.next:
        cur.next, pre, cur = pre, cur, cur.next
    cur.next = pre
    return cur


def reverse_list2(head: Node2) -> Node2:
    if not head or not head.next:
        return head
    pre, cur = None, head
    while cur and cur.next:
        cur.next, cur.prev, pre, cur = pre, cur.next, cur, cur.next
    cur.next = pre
    cur.prev = None
    return cur


if __name__ == '__main__':
    node1 = Node1(1)
    node2 = Node1(2)
    node3 = Node1(3)
    node4 = Node1(4)
    node5 = Node1(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    head1 = reverse_list1(node1)
    cur = head1
    while cur:
        print(cur.value)
        cur = cur.next

    node6 = Node2(6)
    node7 = Node2(7)
    node8 = Node2(8)
    node9 = Node2(9)
    node10 = Node2(10)
    node6.next = node7
    node7.next = node8
    node7.prev = node6
    node8.next = node9
    node8.prev = node7
    node9.next = node10
    node9.prev = node8
    node10.prev = node9
    head2 = reverse_list2(node6)
    cur = head2
    while cur:
        print(cur.value)
        cur = cur.next
