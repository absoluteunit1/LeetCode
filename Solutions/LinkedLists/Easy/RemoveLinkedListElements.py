# First solution

def removeElements(head, val):
    sentinel = cur = ListNode(None)         # Create a reference node (sentinel references the beginning of the LL that has the vals removed)
    while head:
        if head.val != val:
            cur.next = cur = head           # Here we are declaring the next node to be head if head.val is not val and we move to that next node (all in one line. Can be writted as cur.next = head \n cur = cur.next)
        head = head.next
    cur.next = None                         # Finish the LL by adding a None to the next pointer. This ends the LinkedList/
    return sentinel.next                    # Return the pointer that was pointing to the beginning of our new LL (cur)

# Another solution suggested to me. 

def removeElements(self, head, val):
    sentinel = cur = ListNode(None, head)   # ??
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return sentinel.next