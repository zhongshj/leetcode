# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # swap the first two nodes, and do recursive on rest of the list
        if not head:
            return
        if head.next == None:
            return head
        
        temp = head.next
        head.next = head.next.next
        temp.next = head
        
        if head.next != None:
            head.next = self.swapPairs(head.next)
        
        return temp