# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # for each subtree, merge left and right list, and add node.val at li[0]
        if root == None:
            return []
        
        left = self.levelOrder(root.left)
        right = self.levelOrder(root.right)
       
        if len(left) > len(right):
            return [[root.val]]+[left[i]+right[i] for i in xrange(len(right))]+left[len(right):]
        else:
            return [[root.val]]+[left[i]+right[i] for i in xrange(len(left))]+right[len(left):]
