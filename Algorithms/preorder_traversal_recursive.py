# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def preorder(nodes, root):
            if root is None:
                return nodes
            nodes.append(root.val)
            nodes = preorder(nodes, root.left)
            nodes = preorder(nodes, root.right)
            return nodes
        return preorder([],root)
