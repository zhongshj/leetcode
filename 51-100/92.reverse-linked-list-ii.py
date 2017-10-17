# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        new_head = ListNode('#')
        new_head.next = head
        pointer = new_head
        
        # locate m, n
        for i in xrange(m-1):
            pointer = pointer.next
        node_m = pointer    # m-1
        for i in xrange(n-m+1):
            pointer = pointer.next
        node_n = pointer    # n
        
        # do reverse between m, n, and reconnect them
        temp = node_n.next
        node_n.next = None
        head = node_m.next
        head, tail = self.reverse(head)
        node_m.next = head
        tail.next = temp

        return new_head.next
    

    def reverse(self, head):    # reverse(s) = reverse(s[1:]).append(s[0])
        if head == None or head.next == None:
            return head, head
        if head.next.next == None:
            new_head = head.next
            new_head.next = head
            head.next = None
            return new_head, new_head.next

        second, tail = self.reverse(head.next)
        head.next = None
        tail.next = head
        return second, head
