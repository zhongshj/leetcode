# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        i = 1
        node = head
        while node.next != None:
            node = node.next
            i += 1
        node.next = head
    
        k = i - (k % i)
        for i in range(k-1):
            head = head.next
        new_head = head.next
        head.next = None
        return new_head
        