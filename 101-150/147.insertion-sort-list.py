# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        if head.next == None:
            return head

        minimum = head.val
        # get the mimimum order
        i = 0
        min_idx = 0
        p = head
        while p != None:
            if p.val < minimum:
                min_idx = i
                minimum = p.val
            p = p.next
            i += 1
        
        # move it to front
        if min_idx > 0:
            p = head
            for i in xrange(min_idx-1):
                p = p.next
            temp = p.next
            p.next = p.next.next
            temp.next = head
            head = temp

        head.next = self.insertionSortList(head.next)
        return head
