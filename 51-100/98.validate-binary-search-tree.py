# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.valid(root, float('-inf'), float('inf'))


    def valid(self, node, lo, hi):
        if node == None:
            return True

        if node.val <= lo or node.val >= hi:
            return False

        if self.valid(node.left, lo, min(node.val, hi)) == False:
            return False
        if self.valid(node.right, max(node.val, lo), hi) == False:
            return False

        return True