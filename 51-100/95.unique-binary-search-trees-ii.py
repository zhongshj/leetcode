# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []

        num_li = [i+1 for i in xrange(n)]
        return self.gen_tree(num_li)
    
    def gen_tree(self, num_li):
        if num_li == []:
            return [None]

        tree_li = []
        for i in xrange(len(num_li)):
            left = self.gen_tree(num_li[:i])
            mid = num_li[i]
            right = self.gen_tree(num_li[i+1:])
            for l in left:
                for r in right:
                    tree = TreeNode(mid)
                    tree.left = l
                    tree.right = r
                    tree_li.append(tree)

        return tree_li
