class Node():
    def __init__(self, data: int = 0):
        self.value = data
        self.next = None


def has_cycle(head: Node) -> bool:
    visited = set()
    cur = head
    while cur:
        if id(cur) in visited:
            return True
        else:
            visited.add(id(cur))
            cur = cur.next
    return False


def has_cycle_1(head: Node) -> bool:
    slow = fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(2)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    print(has_cycle(node1))
    print(has_cycle_1(node1))
