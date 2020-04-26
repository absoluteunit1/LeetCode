
# My initial solution
# Using two stacks. 
def addTwoNumbers(l1, l2):
    stack1 = []
    stack2 = []
    # append each linked list element to its correspoding stack
    while l1:
        stack1.append(l1.val)
        l1 = l1.next
    while l2:
        stack2.append(l2.val)
        l2 = l2.next 
    # if the stack are of different lengths, append zeros (placeholder elements) to the stack
    if len(stack1) > len(stack2):
            stack2 = [0]*(len(stack1) - len(stack2)) + stack2
    elif len(stack2) > len(stack1):
        stack1 = [0]*(len(stack2) - len(stack1)) + stack1
    # add the stack together
    finalStack = [sum(i) for i in zip(stack1, stack2)]
    # reverse the final stack
    r = finalStack[::-1]
    # iterate through each element. If the current element is greater than 9, than increment the next element by r[i]//10 and change current element to r[i]%10
    for i in range(len(r)):
        if r[i] > 9:
            if i != len(r) -1:
                r[i+1] += r[i]//10
                r[i] = r[i]%10
            # if we are on the last element and the last element is greater than 9, than we prepend (add the increment to the beginning of the list)
            else:
                r.append(r[len(r)-1]//10)
                r[len(r)-2] = r[len(r)-2]%10
    # reverse the stack to the original order
    finalStack = r[::-1]

    # generate a new LL using the elements in the final stack as the values 
    finalList = dummy_head = ListNode(None)

    for i in finalStack:
        dummy_head.next = dummy_head = ListNode(i)
    dummy_head.next = None
    
    return finalList.next

# Another solution

def addTwoNumbers2(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    # turn the lists in to ints with simple loops. In case you didn't know, you can put
    # multiple statements on the same line if you use semicolons in Python.
    s1 = 0
    s2 = 0
    while l1: s1 *= 10; s1 += l1.val; l1 = l1.next
    while l2: s2 *= 10; s2 += l2.val; l2 = l2.next

    # take the sum and reconstruct the number from tail to head, because it's easier
    # to isolate and chop off the little digits with modulus and division.
    s3 = s1 + s2
    tail = None
    head = None
    while s3 > 0: 
        head = ListNode(s3 % 10); 
        head.next = tail; 
        tail = head; 
        s3 //= 10
    return head if head else ListNode(0)

# Most optimal solution
def addTwoNumbers3(l1, l2):
    num1, num2 = 0, 0
    while l1:
        num1 = num1 * 10 + l1.val
        l1 = l1.next
    while l2:
        num2 = num2 * 10 + l2.val
        l2 = l2.next
    num = num1 + num2
    head = None
    # construct an LL from tail to end by adding nodes to the beginning of the LL. (We are using the integer, and removing its last digit each iteration. )
    while num:
        node = ListNode(num%10)
        node.next = head
        head = node
        num = num//10
    return head if (num1+num2) else ListNode(0)
