class Node():
    def __init__(self, data: int = 0):
        self.value = data
        self.next = None


# O(n) 快慢指针，快指针长度每增加二，慢指针（指向待删除节点）长度增加一
def remove_mid_node(head: Node) -> Node:
    if not head or not head.next:
        return head
    if not head.next.next:
        return head.next
    slow, fast = head, head.next.next
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    slow.next = slow.next.next
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
    head = remove_mid_node(node1)
    while head:
        print(head.value)
        head = head.next
