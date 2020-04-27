# My solution 
# This solution is not optimal as it is not in O(1) extra space and creates two new linked lists and a counter variable 
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
# Two pointers approach 

def oddEvenLinkedLists(head):
    if(head == None):
        return head
    oddHead = head                                  # one pointer to the start of the list (Odd Nodes)
    evenHead = even = head.next                     # Two pointers to the 2nd node (Even Nodes)
    while evenHead and evenHead.next:               # Condition is if hte second node and third node in head is not None
        oddHead.next = oddHead = evenHead.next      # The next odd node is the next node from the even node. Ex: OddNode1 -> EvenNode1 -> OddNode2 ->EvenNode2. The next node of "EvenNode1" is "OddNode2"
        evenHead.next = evenHead = oddHead.next     # The next even node is now the next node of the next odd node. Ex: OddNode1 -> EvenNode1 -> OddNode2 ->EvenNode2. The next even node is the next node of OddNodeTwo, which is EvenNode2
    oddHead.next = even                             # The last OddNodes next pointer should point to the start of the even nodes. (That is why we have two pointers for even node)
    return head                                     # Now that the LL was re-arranged, return the head node (the first node of the LL)
