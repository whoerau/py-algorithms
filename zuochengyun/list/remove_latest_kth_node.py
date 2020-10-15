class Node():
    def __init__(self, data: int = 0):
        self.value = data
        self.next = None


def remove_latest_kth_node(head: Node, k: int) -> Node:
    n = 0
    cur = head

    while cur:
        n += 1
        cur = cur.next

    if n < k:
        return head
    elif n == k:
        head = head.next
        return head
    else:
        m = n - k - 1
        cur = head
        while cur and m > 0:
            cur = cur.next
            m -= 1
        cur.next = cur.next.next
        return head


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

    head = node1
    head = remove_latest_kth_node(head, 6)
    while head:
        print(head.value)
        head = head.next
