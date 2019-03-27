# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder(nodes, root):
            if root is None:
                return nodes
            nodes = inorder(nodes, root.left)
            nodes.append(root.val)
            nodes = inorder(nodes, root.right)
            return nodes
        return inorder([],root)
