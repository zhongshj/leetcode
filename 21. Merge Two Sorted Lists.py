# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # empty list
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        
        head = ListNode(0)
        pointer = head
        while True:
            if l1.val < l2.val:
                pointer.next = l1
                pointer = pointer.next
                if l1.next == None:     # l1 done, just append l2
                    pointer.next = l2
                    break
                l1 = l1.next
            else:
                pointer.next = l2
                pointer = pointer.next
                if l2.next == None:     # l2 done, just append l1
                    pointer.next = l1
                    break
                l2 = l2.next
                
        return head.next
        
        