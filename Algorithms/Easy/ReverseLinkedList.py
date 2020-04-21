# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Iteratively

class Solution:
    def reverseList(self, head):
        prev_node = None
        while head:
            temp = head
            head = head.next
            temp.next = prev_node
            prev_node = temp
        return prev_node

