# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # for a node, add the sums of ancestors with the sums of children
        if root == None:
            return 0

        return self.path_sum(root, 0)

    def path_sum(self, node, val):
        if node.left == None and node.right == None:
            return val*10+node.val

        sums = 0
        if node.left != None:
            sums = sums+self.path_sum(node.left, val*10+node.val)
        if node.right != None:
            sums = sums+self.path_sum(node.right, val*10+node.val)

        return sums

