# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # naive approach: do level order, and reverse odd layers
        li = self.zigzag(root)
        for i in xrange(len(li)):
            if i%2 == 1:
                li[i] = li[i][::-1]

        return li


    def zigzag(self, root):

        if root == None:
            return []

        left = self.zigzag(root.left)
        right = self.zigzag(root.right)        

        if len(left) > len(right):
            return [[root.val]]+[left[i]+right[i] for i in xrange(len(right))]+left[len(right):]
        else:
            return [[root.val]]+[left[i]+right[i] for i in xrange(len(left))]+right[len(left):]

