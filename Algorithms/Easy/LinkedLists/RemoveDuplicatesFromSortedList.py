

def deleteDuplicates(head):
    elements = {}                       # Create a dictionary to keep track of the repeating 
    temp = head                         # Pointer to mark the starting of the LinkedList

    while head:
        if head.val not in elements:    # If the node we are on is a new node, add it to the dict. 
            elements[head.val] = 1
            prev = head                 # Prev variable marks the last non-repeating node in our list
            head = head.next            # Move to the next node
        elif head.val in elements:      # If we are on a repeating node, change the last non_repeating node's (prev node) next pointer to the node next of the current one (explanatioin below)
            prev.next = head.next
            head = prev.next
            
    return temp





#       prev               head        head.next
# NonRepeatingNode -> RepeatingNode -> NextNode

# We came across a repeating node, (head). We have to make the NonRepeatingNode to point to the next node. 
# So we set prev.next = head.next
# Then, to continue our list, we set head to prev.next, and this results in:
#                       head
# NonRepeatingNode -> NextNode -> .....