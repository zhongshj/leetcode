# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, node):

        # iterate through layers
        # if layer i is connected, we can connect layer i+1 through the list of layer i

        while node != None:
            child = TreeLinkNode(0)
            head = child
            
            # connect through all child in this layer with help of parent-list
            while node != None:
                child.next = node.left
                if child.next != None:
                    child = child.next
                child.next = node.right
                if child.next != None:
                    child = child.next
                node = node.next
            
            # use this child-list as parent-list for next iteration
            node = head.next

