# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def middleNode(head):

    # Find length of list
    count = 0
    cur = head
    while cur.next != None:
        count += 1
        cur = cur.next
    
    if count%2 == 0:
        middle = count // 2
    else:
        middle = count//2 + 1

    count = 0
    cur = head
    while count != middle:
        count += 1
        cur = cur.next

    return cur

