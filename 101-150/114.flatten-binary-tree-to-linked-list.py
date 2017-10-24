# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # flatten left and right, then append left to right, then append right to the end of left
        if root != None:
        
            self.flatten(root.left)
            self.flatten(root.right)

            temp = root.right
            root.right = root.left
            root.left = None

            i = root
            while i.right != None:
                i = i.right
            i.right = temp

