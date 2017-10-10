# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        pointer = head
        
        # add list
        while True:
            pointer.val = l1.val + l2.val
            print(pointer.val)
            
            # both done
            if l1.next == None and l2.next == None:
                break
                
            # short list done
            if l1.next == None:
                pointer.next = l2.next
                break
            elif l2.next == None:
                pointer.next = l1.next
                break
                
            pointer.next = ListNode(0)
            pointer = pointer.next
            
            l1 = l1.next
            l2 = l2.next
            
        # carry
        pointer = head
        while True:
            if pointer.val >= 10:
                pointer.val = pointer.val - 10
                if pointer.next != None:
                    pointer.next.val = pointer.next.val + 1
                else:
                    pointer.next = ListNode(1)
            if pointer.next == None:
                break
            pointer = pointer.next
        
        
        return head