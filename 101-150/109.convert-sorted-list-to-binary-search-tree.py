# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # get the length first, and divide into [:len/2], [len/2], [:len/2+1]
        if head == None:
            return None

        count = 0
        i = head
        while i != None:
            i = i.next
            count += 1

        return self.bst(head, count)
        
    def bst(self, head, length):
        if length == 0:
            return None
        if length == 1:
            return TreeNode(head.val)

        mid = head
        for i in xrange(length/2-1):
            mid = mid.next
        
        node = TreeNode(mid.next.val)
        node.right = self.bst(mid.next.next, length/2-1+length%2)	# handle odd & even length
        mid.next = None
        node.left = self.bst(head, length/2)

        return node
