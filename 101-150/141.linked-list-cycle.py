# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # go through the list and set each .next to one node
        # if ends with that node, circle exist; else it should ends with None
        terminate = ListNode('#')
        p1 = head
        p2 = head
        while p1 != None:
            p1 = p1.next
            p2.next = terminate
            p2 = p1
            if p1 == terminate:
                return True

        return False
