from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"Root: {self.val}, left node: {self.left}, " \
               f"right node: {self.right}"


def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    else:
        return [root.val] + preorder_traversal(root.left) + \
               preorder_traversal(root.right)


if __name__ == "__main__":
    tree = TreeNode(10, TreeNode(5, None, None), TreeNode(6, None, None))
    print(tree)
    print(preorder_traversal(tree))
