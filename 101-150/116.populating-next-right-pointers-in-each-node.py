# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None:
            return None
        if root.left == None:
            return None

        self.connect(root.left)
        self.connect(root.right)

        l = root.left
        r = root.right
        l.next = r
        while l != None:
            l.next = r
            l = l.right
            r = r.left
