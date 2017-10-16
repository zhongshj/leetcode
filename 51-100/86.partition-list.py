# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # use two pointers i and j, if j meets smaller, remove the node and insert it at i
        if head == None:
            return None

        new_head = ListNode('#')
        new_head.next = head
        i = new_head

        # find the first larger to start
        while i.next.val < x:
            i = i.next
            if i.next == None:
                break
        j = i
        
        # start to pass the list
        while j.next != None:
            if j.next.val >= x:
                j = j.next
            else:
                temp = j.next
                j.next = j.next.next
                temp.next = i.next
                i.next = temp
                i = i.next

        return new_head.next
