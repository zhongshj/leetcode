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
        # add a '#' at the start to make sure no duplicate at the start
        new_head = ListNode('#')
        new_head.next = head

        i = new_head
        if new_head.next == None:   # empty list
            return None

        j = new_head.next
        while j.next != None:
            if j.val != j.next.val:     # if not duplicate, i+1 and j+1
                i = i.next
                j = j.next
            else:                   # if duplicate, go until non-duplicate found
                while True:
                    if j.next == None:
                        break
                    if j.val != j.next.val:
                        break
                    j = j.next
                if j.next == None:  # in case reach tail
                    i.next = None
                    break
                i.next = j.next     # append the non-duplicate
                j = i.next

        return new_head.next
