# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # slow pointer goes 1x, fast 2x 
        # when they first meet, reset two pointer to start node and meet node
        # the node they met is the beginning of circle
        if head == None:
            return None

        fast = head
        slow = head
        count = 0
        while True:
            slow = slow.next
            fast = fast.next
            if fast == None:
                return None
            fast = fast.next
            if fast == None:
                return None
            count += 1
            if fast == slow:
                break

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return fast
        
