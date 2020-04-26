# First Solution

# Create a list, iterate through the linkedList and store each nodes value into the list
# Created a reversed linked list, iterate through the reversed linkedlist and store the values of each node into a new list
# Compare the two lists
def isPalindrome(head):
    order = []
    temp = head
    prev = None
    
    while head:
        order.append(temp.val)
        head = head.next
        temp.next = prev
        prev = temp
        temp = head
    reversedOrder = []
    while prev:
        reversedOrder.append(prev.val) 
        prev = prev.next
    return order == reversedOrder

# Shorter version of the above solution
def isPalindrome2(head):
    vals = []
    while head:
        vals += head.val,  
        head = head.next
    return vals == vals[::-1]

# Using pointers
def isPalindrome3(head):
    pass # Review solution with the pointers

