from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def create_nodes(self, n: int):
        prev_node = ListNode(n, None)
        for i in range(n, 0, -1):
            prev_node = ListNode(i, prev_node)
        return prev_node


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    node = ListNode.create_nodes(ListNode(), 5)
    arr = [head]
    while node.next is not None:
        arr.append(node.val)
        node = node.next

    return arr[len(arr) // 2]

print(middle_node(None))
