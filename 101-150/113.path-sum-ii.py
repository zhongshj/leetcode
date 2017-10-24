# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root == None:
            return []

        return self.path(root, sum)

    def path(self, root, sum):
        if root.val == sum and root.left == None and root.right == None:
            return [[root.val]]

        li = []
        if root.left != None:
            li = li+self.path(root.left, sum-root.val)
        if root.right != None:
            li = li+self.path(root.right, sum-root.val)

        return  [[root.val]+subli for subli in li]

