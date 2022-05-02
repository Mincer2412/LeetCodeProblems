from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def create_nodes(self, n: int):
        prev_node = ListNode(n, None)
        for i in range(n, 1, -1):
            prev_node = ListNode(i, prev_node)
        return prev_node


def remove_nth_from_end(head: Optional[ListNode], init: int, n: int) -> Optional[ListNode]:
    node = ListNode.create_nodes(ListNode(), init)
    pre_head = ListNode(0, head)
    pre_head.next = node
    i, j = pre_head, pre_head

    for _ in range(n):
        j = j.next

    while j.next is not None:
        i = i.next
        j = j.next

    i.next = i.next.next

    return pre_head.next


print(remove_nth_from_end(ListNode(), 5, 1))
print(remove_nth_from_end(ListNode(), 5, 5))
print(remove_nth_from_end(ListNode(), 5, 2))
print(remove_nth_from_end(ListNode(), 3, 1))
print(remove_nth_from_end(ListNode(), 3, 3))
print(remove_nth_from_end(ListNode(), 2, 1))
print(remove_nth_from_end(ListNode(), 2, 2))
print(remove_nth_from_end(None, 1, 1))
