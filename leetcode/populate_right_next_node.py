class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    level: int = 0
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        res = []




    def preorder(self, root):
        if root:
            Solution.preorder(self, root.left)
            print(str(root) + '->', end='')
            Solution.preorder(self, root.right)
