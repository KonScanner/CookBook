""" Validate Binary Search Tree """
""" Given a tree, determine if it is a valid binary search tree"""
""" Assume a Binary Search Tree is defined as follows:
    - The left subtree of a node containes only nodes with keys less than the node's key.
    - The right subtree of a node contains only nodes with keys greater than the nodes key.
    - Both the left and the right subtrees must also be binary search trees."""

# DEFINITION OF A BINARY TREE NODE:


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isValidBST(root: TreeNode) -> bool:
    def _helper(node, lower, upper):
        """ node, lower bound and upper bound"""
        if not node:
            return True
        val = node.val
        if val <= lower or val >= upper:
            return False
        if not _helper(node.right, val, upper):
            return False
        if not _helper(node.left, lower, val):
            return False
        return True
    return _helper(root, float('-inf'), float('inf'))
