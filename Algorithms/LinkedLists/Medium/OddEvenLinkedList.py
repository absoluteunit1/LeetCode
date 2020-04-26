# My solution 

def oddEvenLinkedList(head):
    odd = oddHead = ListNode(None)                  # generate two LL nodes. 
    even = evenHead = ListNode(None)
    i = 1                                           # Use a counter that counts the nodes and determines if they are even or odd
    while head:
        if i%2 == 1:
            oddHead.next = oddHead = head           # if a node is odd, then add it to the odd LL
            head = head.next
            i += 1
        else:
            evenHead.next = evenHead = head         # if a node is even, than add it to the even LL
            head = head.next
            i += 1
    
    # since we are grouping the odd nodes first, and then adding the even nodes after. The tail None will be at the end of the even LinkedList.
    # Then we point the end of the odd list to the starting of the even list and return the beginning of the odd list.
    evenHead.next = None
    oddHead.next = even = even.next
    return odd.next

# Another solution 

def oddEvenLinkedLists(head):
   pass

# Add a solution that doesn't use any extra memory 