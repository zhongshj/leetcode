# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        for i in xrange(len(inorder)):
            if inorder[i] == preorder[0]:
                break

        # left, mid, right: inorder[:i], inorder[i], inorder[i+1:]
        # left, mid, right: preorder[1:i+1], preorder[0], preorder[i+1:]
        node = TreeNode(inorder[i])
        node.left = self.buildTree(preorder[1:i+1], inorder[:i])
        node.right = self.buildTree(preorder[i+1:], inorder[i+1:])

        return node
