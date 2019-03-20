# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if val < root.val:
            if root.left is not None:
                root.left = self.insertIntoBST(root.left, val)
            else:
                root.left = TreeNode(val)
        else:
            if root.right is not None:
                root.right = self.insertIntoBST(root.right, val)
            else:
                root.right = TreeNode(val)
        return root