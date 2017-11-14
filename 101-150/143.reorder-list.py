# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None:
            return None
        if head.next == None:
            return None

        # 1. find middle
        fast = head
        slow = head
        while True:
            fast = fast.next
            if fast == None:
                break
            fast = fast.next
            if fast == None:
                break
            slow = slow.next

        right = slow.next
        slow.next = None

        # 2. reverse right_half
        right = self.stack_reverse(right)

        # 3. merge left and right

        left = head
        while right != None:
            left_1 = left.next
            right_1 = right.next
            left.next = right
            right.next = left_1
            left = left_1
            right = right_1

        return None

    def reverse(self, head):
        # recursive method exceed maximum depth
        if head == None:
            return None
        if head.next == None:
            return head

        new_head = self.reverse(head.next)
        head.next = None
        pointer = new_head
        while pointer.next != None:
            pointer = pointer.next
        pointer.next = head
        return new_head

    def stack_reverse(self, head):
        # stack approach
        if head == None:
            return None
        li = []
        while head != None:
            li.append(head)
            head = head.next

        new_head = ListNode('#')
        pointer = new_head
        while len(li) > 0:
            pointer.next = li.pop(-1)
            pointer = pointer.next
        pointer.next = None

        return new_head.next
