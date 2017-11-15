# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        if head.next == None:
            return head

        p = head.next
        head.next = None
        left = ListNode('left')
        right = ListNode('right')
        pl = left
        pr = right
        pm = head
        while p != None:
            if p.val < head.val:
                pl.next = p
                pl = pl.next
            elif p.val > head.val:
                pr.next = p
                pr = pr.next
            else:
                pm.next = p
                pm = pm.next
            p = p.next

        pl.next = None
        pr.next = None

        left = self.sortList(left.next)
        right = self.sortList(right.next)
        pm.next = right
        if left == None:
            return head

        pl = left
        while pl.next != None:
            pl = pl.next
        pl.next = head

        return left
