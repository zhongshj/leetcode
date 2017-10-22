# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []

        left = self.levelOrderBottom(root.left)
        right = self.levelOrderBottom(root.right)

        dif = len(left)-len(right)
        if dif > 0:
            return left[:dif]+[left[i+dif]+right[i] for i in xrange(len(right))]+[[root.val]]
        else:
            return right[:-dif]+[left[i]+right[i-dif] for i in xrange(len(left))]+[[root.val]]
