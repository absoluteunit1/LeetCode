def splitListToParts(root, k):
    cur, l, result = root, 0, [None]*k

    # Get the length of the linked list first
    while cur:
        l += 1
        cur = cur.next
    extra = l%k
    elems = l//k
    dummy = root
    prev = None
    for i in range(k):
        if dummy:
            result[i] = dummy
            if extra:
                parts = elems + 1
                extra -= 1
            else:
                parts = elems
            # This section is used to iterate through the linked list and break when the the number of elements per that part has been reached
            for k in range(parts):
                prev = dummy
                dummy = dummy.next
            prev.next = None
    return result


    


