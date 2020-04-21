# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Iteratively


def reverseList(head):
    prev_node = None
    while head:
        temp = head
        head = head.next
        temp.next = prev_node
        prev_node = temp
    return prev_node

# Recursively 

def reverseList2(head):
    if head == None or head.next == None:
        return head

    temp = head
    head = reverseList2(head.next)
    temp.next.next = temp
    temp.next = None
    return head

