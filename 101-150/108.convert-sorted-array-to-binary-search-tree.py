# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None

        if len(nums) == 1:
            return TreeNode(nums[0])

        node = TreeNode(nums[len(nums)/2])
        node.left = self.sortedArrayToBST(nums[:len(nums)/2])
        node.right = self.sortedArrayToBST(nums[len(nums)/2+1:])

        return node
