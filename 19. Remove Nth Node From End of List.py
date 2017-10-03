# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # explorer go beyond operator n steps, and delete node when explorer reach end
        explorer = head
        operator = head
        
        for i in range(n):
            explorer = explorer.next
            
        if not explorer:
            return head.next
            
        while explorer.next != None:
            explorer = explorer.next
            operator = operator.next
            
        operator.next = operator.next.next
        return head