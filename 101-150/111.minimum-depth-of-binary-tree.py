# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return self.depth(root)
        
    def depth(self, node):
        if node.left == None and node.right == None:
            return 1

        if node.left == None:
            return self.depth(node.right)+1
        if node.right == None:
            return self.depth(node.left)+1

        return min(self.depth(node.left), self.depth(node.right))+1
