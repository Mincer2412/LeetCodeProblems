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


def remove_nth_from_end(head: Optional[ListNode], init: int, n: int,) -> Optional[ListNode]:
    node = ListNode.create_nodes(ListNode(), init)
    arr = [node]
    while node.next is not None:
        arr.append(node.next)
        node = node.next

    if len(arr) == 1:
        return None

    if len(arr) == 2:
        arr[n - 1].next = None
        return arr[n - 1]

    if len(arr) - n == 0:
        arr[0].next = None
        return arr[1]
    elif len(arr) - n + 1 == len(arr):
        arr[len(arr) - n - 1].next = None
    else:
        arr[len(arr) - n - 1].next = arr[len(arr) - n + 1]

    for node in arr:
        print(node, node.next)
    print('---')
    return arr[0]


# print(remove_nth_from_end(ListNode(), 5, 1))
# print(remove_nth_from_end(ListNode(), 5, 5))
# print(remove_nth_from_end(ListNode(), 5, 2))
# print(remove_nth_from_end(ListNode(), 3, 1))
print(remove_nth_from_end(ListNode(), 3, 3))
# print(remove_nth_from_end(ListNode(), 2, 1))
# print(remove_nth_from_end(ListNode(), 2, 2))
# print(remove_nth_from_end(None, 1, 1))
