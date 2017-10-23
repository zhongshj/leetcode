# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # for each sub-tree, if depths differs >1, return -1 as False, else return depth(larger one)
        if self.depth(root) == -1:
            return False
        return True

    def depth(self, node):
        
        if node == None:
            return 0

        left = self.depth(node.left)
        right = self.depth(node.right)

        if left == -1 or right == -1:
            return -1

        if abs(left-right) > 1:
            return -1

        return max(left, right)+1



        
