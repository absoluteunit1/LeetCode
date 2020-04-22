def mergeTwoLists(l1, l2):
    head = ListNode(None)
    l3 = head
    while l1 and l2:
        head.next = ListNode(min(l1.val, l2.val))
        if l1.val < l2.val:
            l1 = l1.next
        else:
            l2 = l2.next
        head = head.next
    head.next = l1 if l1 else l2
    return l3.next 