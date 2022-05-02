class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


a5 = TreeNode(5)
a2 = TreeNode(2)
a3 = TreeNode(3, a5)
a1 = TreeNode(1, a3, a2)

bx = TreeNode(10)
byy = TreeNode(111)
by = TreeNode(11, left=byy)

b7 = TreeNode(7)
b4 = TreeNode(4)
b3 = TreeNode(3, by, b7)
b1 = TreeNode(1, bx, b4)
b2 = TreeNode(2, b1, b3)


# inorder = left -> root -> right
# preorder = root -> left -> right
# postorder = left -> right -> root


def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val) + '->', end='')
        inorder(root.right)


def preorder(root):
    if root:
        print(str(root.val) + '->', end='')
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val) + '->', end='')


inorder(b2)
print()
preorder(b2)
print()
postorder(b2)
