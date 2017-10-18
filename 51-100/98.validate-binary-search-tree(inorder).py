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
        li = self.inorder(root)

        for i in range(len(li)-1):
            if li[i] >= li[i+1]:
                return False

        return True
        

    def inorder(self, node):
        if node == None:
            return []

        return self.inorder(node.left)+[node.val]+self.inorder(node.right)
