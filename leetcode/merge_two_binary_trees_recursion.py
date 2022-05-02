from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root2 is None:
            return root1

        if root1 is None and root2:
            return root2

        if root1 and root2:
            print(root1.val, root2.val, root1.val + root2.val)
            root1.val = root1.val + root2.val
            root1.left = Solution.mergeTrees(self, root1.left, root2.left)
            root1.right = Solution.mergeTrees(self, root1.right, root2.right)
        return root1

    # preorder = root -> left -> right
    def preorder(self, root):
        if root:
            print(str(root.val) + '->', end='')
            Solution.preorder(self, root.left)
            Solution.preorder(self, root.right)


a5 = TreeNode(5)
a2 = TreeNode(2)
a3 = TreeNode(3, a5)
a1 = TreeNode(1, a3, a2)

b7 = TreeNode(7)
b4 = TreeNode(4)
b3 = TreeNode(3, None, b7)
b1 = TreeNode(1, None, b4)
b2 = TreeNode(2, b1, b3)

Solution.preorder(Solution(), Solution.mergeTrees(Solution(), a1, b2))
