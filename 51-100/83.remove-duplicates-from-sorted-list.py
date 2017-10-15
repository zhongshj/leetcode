# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        i = head
        while i.next != None:
            if i.val == i.next.val:     # if duplicate, drop that node
                i.next = i.next.next
            else:                       # else, move forward
                i = i.next

        return head
